import gym
import numpy as np
from gym import spaces

from os import path

legal_moves = set((-1, 1, 0))


class RobotRobbersEnv(gym.Env):
    def __init__(self) -> None:
        super(RobotRobbersEnv, self).__init__()

        # Game settings
        self.width = 128
        self.height = 128

        self.n_element_types = 5
        self.max_n_elements_per_type = 10
        self.observation_shape = (
            self.n_element_types + 1,
            self.max_n_elements_per_type,
            4
        )

        self.n_robbers = 5
        self.max_n_scrooges = 7
        self.max_n_cashbags = 5
        self.max_n_dropspots = 3
        self.max_n_obstacles = 5
        self._max_obstacle_size = 20
        self._max_carry_capacity = 4
        self._reward_multiplier = 2
        self._scrooge_radius = 15
        self._scrooges_move_interval = 2
        self._robber_cooldown_ticks = 100

        # Observation/action spaces
        self._set_space()
        self._empty_world_state()


        self._reward = 0
        self._total_reward = 0
        self._n_cashbags = 0
        self._n_dropspots = 0
        self._n_scrooges = self.max_n_scrooges
        self._n_obstacles = 0
        self._game_ticks = 0

        # Rendering
        self.scaling = 8
        self.clock = None
        self.screen = None
        self.surface = None
        self.gfxdraw = None
        self.font = None

        self.robot_sprite = None
        self.scrooge_sprite = None
        self.cashbag_sprite = None
        self.dropspot_sprite = None

        self._random_n_obstacles = True

        # Seeding
        self.random = None


    def set_n_robbers(self, amount):
        min_cap = 1
        max_cap = self.max_n_elements_per_type
        assert amount >= min_cap, f'Min amount of robbers is {min_cap}'
        assert amount <= self.max_n_elements_per_type, f'Max amount of robbers is {max_cap}'
        self.n_robbers = amount
        self.reset()


    def set_n_scrooges(self, amount):
        min_cap = 0
        max_cap = min(self.max_n_elements_per_type, self.max_n_scrooges)
        assert amount >= min_cap, f'Min amount of scrooges is {min_cap}'
        assert amount <= max_cap, f'Max amount of scrooges is {max_cap}'
        self._n_scrooges = amount
        self.reset()

    def set_n_cashbags(self, amount):
        min_cap = 1
        max_cap = min(self.max_n_elements_per_type, self.max_n_cashbags)
        assert amount >= min_cap, f'Min amount of cashbags is {min_cap}'
        assert amount <= max_cap, f'Max amount of cashbags is {max_cap}'
        self._n_cashbags = amount
        self.reset()
    
    def set_n_dropspots(self, amount):
        min_cap = 1
        max_cap = min(self.max_n_elements_per_type, self.max_n_dropspots)
        assert amount >= min_cap, f'Min amount of dropspots is {min_cap}'
        assert amount <= max_cap, f'Max amount of dropspots is {max_cap}'
        self._n_dropspots = amount
        self.reset()

    def set_n_obstacles(self, amount):
        min_cap = 0
        max_cap = min(self.max_n_elements_per_type, self.max_n_obstacles)
        assert amount >= min_cap, f'Min amount of obstacles is {min_cap}'
        assert amount <= max_cap, f'Max amount of obstacles is {max_cap}'
        self._n_obstacles = amount
        self._random_n_obstacles = False
        self.reset()

    def reset(self, seed=None) -> tuple:
        self.seed(seed)
        self.random = np.random.RandomState(seed)

        self._set_space()

        if self._random_n_obstacles:
            self._n_obstacles = self.random.randint(2, self.max_n_obstacles)
        
        self._empty_world_state()


        for i in range(self._n_obstacles):
            x, y = self._get_free_cell()
            w, h = self.random.randint(1, self._max_obstacle_size), self.random.randint(
                1, self._max_obstacle_size)
            self._obstacles[i, :] = (x, y, w, h)

        for i in range(self._n_scrooges):
            self._scrooge_positions[i, :] = self._get_free_cell()

        for i in range(self.n_robbers):
            self._robber_positions[i, :] = self._get_free_cell()

        self._generate_cash_bags()
        return self._get_observation()

    def step(self, actions) -> tuple:
        assert self.action_space.contains(
            actions), f'Move instructions must be pairs of {{-1, 0, 1}} but was {actions}'
        self._move_robbers(actions)

        # Check if any robbers are in the same location as cashbags
        for i in range(self.n_robbers):
            rx, ry = self._robber_positions[i]
            for j in range(self.max_n_cashbags):
                cx, cy = self._cashbag_positions[j]

                if rx == cx and ry == cy:
                    self._n_cashbags -= 1
                    self._cashbag_carriers[i] += 1
                    self._cashbag_positions[j] = -1, -1

        # Check if any robbers are in the same location as dropspots
        for dx, dy in self._dropspot_positions:
            for i in range(self.n_robbers):
                rx, ry = self._robber_positions[i]

                if rx == dx and ry == dy:
                    self._reward += self._cashbag_carriers[i] ** self._reward_multiplier
                    self._cashbag_carriers[i] = 0

        # Check if any robbers are in the same location as scrooges
        for sx, sy in self._scrooge_positions:
            for i in range(self.n_robbers):
                rx, ry = self._robber_positions[i]
                has_cashbags = self._cashbag_carriers[i] > 0

                # Give a penalty and take away the cashbag
                if rx == sx and ry == sy and self._robber_cooldown[i] <= 0:
                    self._robber_cooldown[i] = self._robber_cooldown_ticks

                    if has_cashbags:
                        self._reward -= 10
                        self._cashbag_carriers[i] = 0

        # Move scrooges
        self._move_scrooges()

        n_cashbags_on_screen = int(self._n_cashbags + self._cashbag_carriers.sum())

        if n_cashbags_on_screen < self.max_n_cashbags:
            self._generate_cash_bags()

        if self._n_dropspots < self.max_n_dropspots:
            self._dropspot_positions[self._n_dropspots, :] = self._get_free_cell()
            self._n_dropspots += 1

        episode_reward = self._reward
        self._total_reward += episode_reward
        self._reward = 0
        self._game_ticks += 1

        for i in range(self.n_robbers):
            self._robber_cooldown[i] -= 1

        return (
            self._get_observation(),
            episode_reward,
            False,  # Never terminate
            {
                "total_reward": self._total_reward,
                "game_ticks": self._game_ticks
            }
        )

    def render(self, mode=None) -> None:
        try:
            import pygame
            from pygame import gfxdraw
            self.gfxdraw = gfxdraw
            self.pygame = pygame
        except ImportError:
            raise Exception("Please install pygame to use the render method")

        if self.screen is None:
            pygame.init()
            pygame.display.init()
            self.screen = pygame.display.set_mode((
                self.width * self.scaling,
                self.height * self.scaling
            ))

            self.robot_sprite = pygame.transform.scale(
                pygame.image.load(path.join('sprites', 'robot.png')),
                (self.scaling * 2, self.scaling * 2)
            )

            self.scrooge_sprite = pygame.transform.scale(
                pygame.image.load(path.join('sprites', 'scrooge.png')),
                (self.scaling * 2, self.scaling * 2)
            )

            self.cashbag_sprite = pygame.transform.scale(
                pygame.image.load(path.join('sprites', 'cashbag.png')),
                (self.scaling * 1.4, self.scaling * 1.4)
            )

            self.dropspot_sprite = pygame.transform.scale(
                pygame.image.load(path.join('sprites', 'dropspot.png')),
                (self.scaling * 2, self.scaling * 2)
            )

        if self.font is None:
            pygame.font.init()
            # Any PRs to change this will be rejected
            self.font = pygame.font.SysFont('Comic Sans MS', 30)

        if self.clock is None:
            self.clock = pygame.time.Clock()

        self.surface = pygame.Surface(
            (self.width * self.scaling, self.height * self.scaling))
        self.surface.fill((50, 50, 50))

        for i in range(self.max_n_obstacles):
            self._render_obstacle(i)

        for i in range(self.max_n_scrooges):
            self._render_scrooge(i)

        for i in range(self.n_robbers):
            self._render_robber(i)

        for i in range(self.max_n_cashbags):
            self._render_cashbag(i)

        for i in range(self.max_n_dropspots):
            self._render_dropspot(i)

        self.screen.blit(self.surface, (0, 0))

        # Draw the reward and game time in the top left of screen
        reward_txt = self.font.render(
            f'Reward: {self._total_reward}', False, (0, 0, 0))
        time_txt = self.font.render(
            f'Game ticks: {str(self._game_ticks)}', False, (0, 0, 0))

        self.screen.blit(reward_txt, (30, 30))
        self.screen.blit(time_txt, (30, 60))

        pygame.event.pump()
        self.clock.tick(60)
        pygame.display.flip()


    def _set_space(self):
        self._set_action_space()
        self._set_observation_space()

    def _set_action_space(self):
        self.action_space = spaces.Box(low=-1, high=1, shape=(self.n_robbers * 2,), dtype=np.int8)
    
    def _set_observation_space(self):
        self.observation_space = spaces.Box(
            low=-1,
            high=self.height,
            shape=self.observation_shape,
            dtype=np.int16
        )      

    def _empty_world_state(self):
        self._robber_positions = np.ones((self.n_robbers, 2), dtype=np.int16) * -1
        self._scrooge_positions = np.ones((self.max_n_scrooges, 2), dtype=np.int16) * -1
        self._cashbag_positions = np.ones((self.max_n_cashbags, 2), dtype=np.int16) * -1
        self._dropspot_positions = np.ones((self.max_n_dropspots, 2), dtype=np.int16) * -1
        self._obstacles = np.ones((self.max_n_obstacles, 4), dtype=np.int16) * -1
        self._cashbag_carriers = np.zeros((self.n_robbers, ), dtype=np.int16)
        self._robber_cooldown = np.zeros((self.n_robbers, ), dtype=np.int16)

    def _generate_cash_bags(self):
        for ci in range(self.max_n_cashbags):
            cix, _ = self._cashbag_positions[ci]
            if cix == -1:
                self._cashbag_positions[ci, :] = self._get_free_cell()
                self._n_cashbags += 1

    def _is_cell_free(self, cx, cy):
        # Out of bounds
        if cx < 0 or cx >= self.width or cy < 0 or cy >= self.height:
            return False

        # Inside obstacle
        for x, y, w, h in self._obstacles:
            if cx >= x and cx <= x + w and cy >= y and cy <= y + h:
                return False

        return True

    def _get_free_cell(self):
        x = self.random.randint(0, self.width)
        y = self.random.randint(0, self.height)

        while not self._is_cell_free(x, y):
            x = self.random.randint(0, self.width)
            y = self.random.randint(0, self.height)

        return x, y

    def _get_observation(self):
        observation = np.ones(self.observation_shape, dtype=np.int16) * -1

        for i, (x, y) in enumerate(self._robber_positions):
            observation[0, i, :] = [x, y, 1, 1]

        for i, (x, y) in enumerate(self._scrooge_positions):
            observation[1, i, :] = [x, y, 1, 1]

        for i, (x, y) in enumerate(self._cashbag_positions):
            observation[2, i, :] = [x, y, 1, 1]

        for i, (x, y) in enumerate(self._dropspot_positions):
            observation[3, i, :] = [x, y, 1, 1]

        for i, (x, y, w, h) in enumerate(self._obstacles):
            observation[4, i, :] = [x, y, w, h]

        for i, c in enumerate(self._cashbag_carriers):
            observation[5, i, :] = [c, 0, 0, 0]

        return observation

    def _render_obstacle(self, idx):
        x, y, w, h = self._obstacles[idx]
        gx = x * self.scaling
        gy = y * self.scaling
        gw = (w + 1) * self.scaling
        gh = (h + 1) * self.scaling

        self.gfxdraw.filled_polygon(
            self.surface,
            [(gx, gy), (gx + gw, gy), (gx + gw, gy + gh), (gx, gy + gh)],
            (0, 0, 0)
        )

    def _render_scrooge(self, idx):
        x, y = self._scrooge_positions[idx]
        gx = (x * self.scaling) - self.scaling * .5
        gy = (y * self.scaling) - self.scaling * .5

        self.surface.blit(self.scrooge_sprite, (gx, gy))

    def _render_robber(self, idx):
        x, y = self._robber_positions[idx]
        gx = (x * self.scaling) - self.scaling * .5
        gy = (y * self.scaling) - self.scaling * .5

        self.surface.blit(self.robot_sprite, (gx, gy))

        for i in range(self._cashbag_carriers[idx]):
            robber_cx, robber_cy = (
                gx + self.scaling // 2, gy + self.scaling // 2)
            w = i + 1
            self.gfxdraw.filled_polygon(
                self.surface,
                [(robber_cx - w, robber_cy - w), (robber_cx + w, robber_cy - w),
                 (robber_cx + w, robber_cy + w), (robber_cx - w, robber_cy + w)],
                (255, 255, 0)
            )

    def _render_cashbag(self, idx):
        x, y = self._cashbag_positions[idx]
        gx = (x * self.scaling) - self.scaling * .2
        gy = (y * self.scaling) - self.scaling * .2

        self.surface.blit(self.cashbag_sprite, (gx, gy))

    def _render_dropspot(self, idx):
        x, y = self._dropspot_positions[idx]
        gx = (x * self.scaling) - self.scaling * .5
        gy = (y * self.scaling) - self.scaling * .5

        self.surface.blit(self.dropspot_sprite, (gx, gy))

    def _dist(self, x1, y1, x2, y2):
        return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def _move_robbers(self, actions):
        for i in range(self.n_robbers):

            wait_ticks = self._cashbag_carriers[i] + 1
            if not self._game_ticks % wait_ticks == 0:
                continue

            dx, dy = actions[i * 2], actions[i * 2 + 1]
            x, y = self._robber_positions[i]
            x += dx
            y += dy

            if not self._is_cell_free(x, y):
                continue

            self._robber_positions[i] = x, y

    def _move_scrooges(self):
        if not self._game_ticks % self._scrooges_move_interval == 0:
            return

        for i in range(self._n_scrooges):

            x, y = self._scrooge_positions[i]

            distances = [
                self._dist(x, y, *self._robber_positions[idx])
                if self._robber_cooldown[idx] <= 0 else np.inf
                for idx in range(self.n_robbers)
            ]

            if len(distances) == 0:
                # Move randomly
                dx, dy = self.random.randint(-1, 2), self.random.randint(-1, 2)
                x += dx
                y += dy

                self._scrooge_positions[i] = x, y

                continue

            closest_robber = np.argmin(distances)
            if distances[closest_robber] < self._scrooge_radius:
                # Move towards the closest robber if within radius
                rx, ry = self._robber_positions[closest_robber]
                dx, dy = rx - x, ry - y
                x += 1 if dx > 0 else -1 if dx < 0 else 0
                y += 1 if dy > 0 else -1 if dy < 0 else 0

            else:
                # Move randomly
                dx, dy = self.random.randint(-1, 2), self.random.randint(-1, 2)
                x += dx
                y += dy

            if not self._is_cell_free(x, y):
                continue

            self._scrooge_positions[i] = x, y
