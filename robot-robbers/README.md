# Robot Robbers
In this use case, you should develop a system for playing robot robbers.
The Robot Robbers game is an interactive 2D game where you, the player, control 5 robots trying to steal money from angry scrooges.

<p align="center">
  <img src="../images/robot_robbers.png" width=650>
</p>

*A description of the invididual icons will follow...*

The objective of this use case is to reach the highest possible reward in 2 wall-clock minutes. Balance the trade off between time and performance well!

## How to play
Every game runs in a 128x128 grid environment. Every game is initialized with:

1. 5 robots (controlled by the player)
2. 7 scrooges (controlled by the game)
3. Between 2-5 obstacles, the height and width of which range between 1 and 20.
4. 5 cashbags
5. 3 dropspots
All of these are randomly placed at every game start.
You will recive the states at your prediction endpoint for every game tick.

### Controlling robots
<p align="left">
  <img src="../images/robot.png" width=250>
</p>
You'll have to control in total 5 robots for every game tick. Every robot kan only move 1 step at a time in either horizontal, vertical or diagonal direction. Movement instructions has to be provided as delta `x`and `y`.

For example:
```python
action = [
  1, 1,    
  # Move robot 0 one cell to the right, one cell down
  -1, -1,  # Move robot 1 one cell to the left, one cell up
  0, 0     # Make robot 2 stand still
]
```

### Cashbags & Dropspots
<p align="left">
  <img src="../images/cashbag.png" width=50>
  and
  <img src="../images/dropspot.png" width=50>
</p>
When a robot robber intersects with a cashbag, the robot picks it up. When a robot carrying cashbags intersects with a dropspot, the cashbags are deposited and a reward is provided.

The reward of depositing cashbags increases exponentially by the number of cashbags carried, e.g.:

1. Carrying 1 cashbag -> reward of 1
2. Carrying 2 cashbags -> reward of 4
3. Carrying 3 cashbags -> reward of 9
However, robots become burdened by carrying cashbags, and move slower the more they carry:

1. Robot speed (0 cashbags): 1 ticks / move
2. Robot speed (1 cashbag): 2 ticks / move
3. Robot speed (2 cashbags): 3 ticks / move

The number of cashbags on the screen always remains the same; when cashbags are deposited or taken away by scrooges, they will spawn again at random places on the map.

### Scrooges
<p align="left">
  <img src="../images/scrooge.png" width=50>
</p>

The scrooges are the game antagonists. They will try their very best to keep the cashbags from being stolen.

Initially, scrooges will move around randomly on the map.

If a robot carrying cashbags intersects with a scrooge, the cashbags are taken away and the player receives a -10 reward penalty.

If a robot is within 15 units of distance from a robot, the scrooge will chase the robot until:

The scrooge reaches the robot, at which point the robot will not be chased again by any scrooge for 100 game ticks
The robot comes out of range, at which point the scrooge will wander randomly again
Scrooges always move at the speed of 2 ticks / move.

## Rules
* Robots and scrooges cannot move outside of the grid.
* Robots and scrooges can only move one unit in either direction in a single game tick.
* Robots and scrooges cannot move through obstacles.

## Interaction
You'll recive a `RobotRobbersPredictRequestDto` which contain the following:
```python
class RobotRobbersPredictRequestDto(BaseModel):
    state: List[List[List[int]]]
    reward: float
    is_terminal: bool
    total_reward: float
    game_ticks: int
```
Where **state** is composed of the following:
Given an observation matrix $M \in \mathbb{Z}^{6 \times 10 \times 4}$, the contents are as follows:

1. $M_{0}$ is an array of 4-d vectors containing the $x, y, w, h$ of all **robot robbers** ($w, h$ is always $1$).
2. $M_{1}$ is an array of 4-d vectors containing the $x, y, w, h$ of all **scrooges** ($w, h$ is always $1$).
3. $M_{2}$ is an array of 4-d vectors containing the $x, y, w, h$ of all **cashbags** ($w, h$ is always $1$).
4. $M_{3}$ is an array of 4-d vectors containing the $x, y, w, h$ of all **dropspots** ($w, h$ is always $1$).
5. $M_{4}$ is an array of 4-d vectors containing the $x, y, w, h$ of all **obstacles**.
6. $M_{5}$ is an array of 4-d vectors where the first element of the vector is the number of cashbags carried by the robot robber with the same index. The rest of the vector elements are always $0$.
   - For example, given the robber $i$ at $M_{0,i}$, the number of cashbags carried by this robber is $M_{5, i, 0}$.

Each row of the observation matrix contains 10 4-d vectors, but not all vectors represent active game elements.
Inactive game elements (e.g., the last 5 vectors in $M_{0}$) are represented by their position being placed outside the game grid `(-1, -1)`. 
> For example, the vector of an inactive cashbag (cashbags are inactive while being carried by a robot) will always be `(-1, -1, 1, 1)`.

* **Reward** is when you gain points, this will be appearent in the reward.
* **total_reward** is the total score for your current game. 
* **game_ticks** is the number of game tick currently running.

From these information you should be able to predict your next move and return:
```python
class RobotRobbersPredictResponseDto(BaseModel):
    moves: List[int]
```
Which essensially is a list of moves, for example: <br>
moves = [ $Δ_{x,1}$, $Δ_{y,1}$, $Δ_{x,2}$, $Δ_{y,2}$ ... , $Δ_{x,5}$, $Δ_{y,5}$ ] <br>
where, $Δ_{x,n}$ and $Δ_{y,n}$ are the change in x and y direction for robot n.


## Evaluation
During the week of the competition, you will be able to validate your solution against a validation seed. The best score your model achieves on the validation seed will be displayed on the scoreboard. You'll have exactly 2 minutes to play the game for each attempt.

When you think your solution can't get any better, you should evaluate your solution.

After evaluation, your final score will be provided. This score can be seen on the <a href="https://cases.dmiai.dk/">scoreboard</a> shortly after and cannot be changed.

## Getting started using Emily
Once the repository is cloned, navigate to the folder using a terminal and type:
```
emily open robot-robbers
```
A Docker container with a Python environment will be opened. Some content needs to be downloaded the first time a project is opened, this might take a bit of time.

To take full advantage of Emily and the template, your code for prediction should go in api.py:
```python
@app.post('/api/predict', response_model=RobotRobbersPredictResponseDto)
def predict(request: RobotRobbersPredictRequestDto) -> RobotRobbersPredictResponseDto:

    moves = [0, 0,
             0, 0,
             0, 0,
             0, 0,
             0, 0]

    return RobotRobbersPredictResponseDto(moves=moves)
```
You can add new packages to the Python environment by adding the names of the packages to requirements.txt and restarting the project, or by using pip install on a terminal within the container which will result in the package being installed temporarily i.e. it is not installed if the project is restarted. <a href="https://emily.ambolt.io/docs/latest">Click here</a> to visit the Emily documentation.

## Testing the connection to the API
See <a href="https://amboltio.github.io/emily-intro/deploy/test/">this guide</a> for details on how to test your setup before final submission.

## Submission
When you are ready for submission, <a href="https://amboltio.github.io/emily-intro/deploy/">click here</a> for instructions on how to deploy. Then, head over to the <a href="https://cases.dmiai.dk/">Submission Form</a> and submit your model by providing the host address for your API and your UUID obtained during sign up. Make sure that you have tested your connection to the API before you submit!<br>
