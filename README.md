## Treasure Hunters Inc.
### Authors:
* Lei Wang
* Casey Sader

### To compile:
```python
python RL.py <dimensionality> <episode>
e.x. python RL.py 10 10
```
***dimensionality: the dimensionality of the environment***

***episode: the amount of episode, each episode generates a new map***

### Approach: Q learning with ϵ-greedy action selection
In this work, we used Q learning with ϵ-greedy action selection as the reinforcement learning algorithm. The policy is based on the maximum Q value in any given state and it gives a certain possibility to randomly pick an action to take for each state to prevent "lock in".

### Map attributes:
we use a 2d array to represent the environment, and there are 4 types of states:
* "-1" represents a player, and it always spawns at the top left corner.
* "0" represents a free state where it has the potential to be the part of the path.
* "1" denotes the treasure which randomly spawns within the environment but never overlaps with the player.
* "2" denotes the obstacle which the player tries to avoid and they are randomly spawned in the environment.
* "3" is the opponent that the player tries to avoid and they are also randomly spawned in the environment.

### Policy:
#### Reward
* The default reward for a move is -1, this way, it encourages the player to find the treature as soon as possible.
* The reward for encounting the obstacle is -5.
* The reward for encounting the opponent is -10.
* The reward for finding the treasure is 100, which is highly rewarding to encourage the player to find treasure.

#### Q-table
In the end of all episodes, a Q table is printed in the console to display all the rewards for taking an action based on the state the player is at. Each row represents a state and each column represents an action. The states are read from left to right and top to bottom. The first column is move_left, second column is move_right, third one is move_up, and the last column is move_down.

### Reference
[reinforment learning tutorial](https://adventuresinmachinelearning.com/reinforcement-learning-tutorial-python-keras/)

[Standford RL lecture](https://www.youtube.com/watch?v=FgzM3zpZ55o&t=3383s&frags=pl%2Cwn)

