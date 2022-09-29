import pygame
from game.environment import RobotRobbersEnv

env = RobotRobbersEnv()
env.reset(42)
env.set_n_cashbags(5)
env.render()
sample = env.observation_space.sample()


current_key = None


def get_move_from_keyboard():
    global current_key

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            current_key = event.key
        elif event.type == pygame.KEYUP:
            current_key = None

    if current_key == pygame.K_LEFT:
        return (-1, 0)
    elif current_key == pygame.K_RIGHT:
        return (1, 0)
    elif current_key == pygame.K_UP:
        return (0, -1)
    elif current_key == pygame.K_DOWN:
        return (0, 1)
    else:
        return (0, 0)


while True:
    move = get_move_from_keyboard()

    state, reward, is_done, info = env.step([
        *move,  # Robot 1 moves according to arrow keys
        0, 0,   # All other robots stand still
        0, 0,
        0, 0,
        0, 0
    ])

    # If you want to render the game as it runs, it's recommended to
    # run this script locally:
    #
    # ```bash
    # python3 -m venv .venv
    # source .venv/bin/activate
    # pip install -r requirements.txt
    # python run_game.py
    # ```
    #
    env.render()
