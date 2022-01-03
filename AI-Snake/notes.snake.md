# AI Snake challenge 

## 1. Rules of the competition

* Board size: 30x30 / 10x10 / nxn 
* Starting snake length: 3 / 1 
* Starting position: center / random
* Starting direction: random
* Game over rate < 0.01% / ..%

Nokia original game:
* https://playsnake.org
* Board size: ?? W x 15H
* Starting snake length: 3 
* Starting position: center: Top Center 
* Starting direction: Down

  

# AI Snake Project

## Current Development

Features:  
- [x] Basic POC with manual input
- [x] Create GIU using pygame
- [x] Refactor code using OOP
- [x] Separate Engine and Agent logic

Pathfinding Algorithms:
- [x] Add Greedy algo / agent
- [x] Add A* algo / agent
- [x] Add Modes: Play and Benchmark
- [-] Logging history
- [-] Create snapshot of game configuration/situation/..
- [-] Replay of snapshots
- [-] Rewind steps (manual)

Evolution/Genetic algorithm selecting NN:
- [-] 

Supervised Learning: Deep Learning:
- [-] Training data generation

Reinforcement Learning: 1. Q-Learning

Reinforcement Learning: 2. Deep Q-Learning



# 2. References

## 2.0 Problem definition

Graph:
- Pathfinding problem
- Shortest path (over all iterations)
- Deterministic Time-dependant graph (the snake tail changes graph)
- Stochastic next objective (Next apple location is random) 
- ..

### 2.0.2 Objects  definition

> UML Graph of objects

* Game
    - GameParams (mode, ..)
    * UI [1]
    * Engine [1]
    * Session [1-*]
        - SessionParams (steps, points)
        * Agent [1][Abstract]
        * Board
        * Snake
        * Apple
        * History

The board:
* x: columns From 1, Axe: Horizontal, from Left to right
* y: rows From 1, Axe: vertical, from bottom to top


#### Design patterns

#### 


#### 

## 2.1. Pathfinding Algorithmic  

### 2.1.1 Pathfinding
1. Greedy
1. Shortest path problems
    - https://en.wikipedia.org/wiki/Shortest_path_problem
1. A* Pathfinding Algorithm
    - http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
1. Hamiltonian loop/cycle
1. K-shortest paths  
    [Alternative Routing: k-Shortest Paths with Limited Overlap](https://www.informatik.hu-berlin.de/de/forschung/gebiete/wbi/research/publications/2015/sigspatial_kshortest.pdf)

Source: Dijkstras Algorithm, A*
  * [..](https://www.youtube.com/watch?v=-L-WgKMFuhE&ab_channel=SebastianLague)
  * [..](https://www.researchgate.net/publication/237197542_Shortest_Path_Finding_Problem_in_Stochastic_Time-Dependent_Road_Networks_With_Stochastic_First-In-First-Out_Property)
  * [..](https://neo4j.com/developer/graph-data-science/path-finding-graph-algorithms/)

1. Graph
    1. Data structures for Graph-Network representations
        * Adjacent Matrix
        * Adjacent List / Set 
    1. Graph libraries  
        1. NetworkX
    1. Graph algorithms
        * Branch & Bound > Dynamic Prgramming > A* > Dijkstra
    1. Graph and Time
        * "Time-dependant", "Time variaing", "Temporal network", "evolving network", ..
    1. Graph concepts
        * Hamiltonian (hamiltonicity)
        * vs. Eulerian
        * path and cycles/ loop
        * Connectivity
        * 


## 2.2. Genetic algorithm with NN selection

## 2.3. Supervised Learning
Neural Network, trained by Gradient Descent  
NN type: deep FFNN, 

Feature engineering:

Point of view | "Bird view" | "Snake vision"
------------- | -------------- | -----------
.. | .. | From the pixel<br> global view (whole board) or local view (NxN matrix around head)
Actions | The 4 directions (N,S,E,W) | 3 actions (turn right, turn left, go straight) relative to snake body
.. | .. | - Distance head to Danger (R,L,S)<br> - Direction (NSEW)<br>  - Food (NSEW)

## 2.4. Re-inforcement Learning
- Q Learning
- Deep Q Learning

---
Q-Learning:
* States S
* Actions A
* Transition proba T(s, a, s')
* Rewards R(s, a, s')

Reward: Keep in the range [-1;+1]


MODEL

FFNN (feed forward NN): 
- input layer size = State dim (one hot)
- output layer size = Actions dim (3)





# References: Open Projects

* Code Bullet  
    * Video 1: [A.I. Learns to play Snake using Deep Q Learning](https://www.youtube.com/watch?v=3bhP7zulFfY&ab_channel=CodeBullet)
    * Video 2: [I Created a PERFECT SNAKE A.I.](https://www.youtube.com/watch?v=tjQIO1rqTBE)
    * GitHub: [Code-Bullet/SnakeFusion](https://github.com/Code-Bullet/SnakeFusion) - 
* AlphaPhoenix
    * [Video](https://www.youtube.com/watch?v=TOpBcfbAgPg&ab_channel=AlphaPhoenix)
* Jack of Some
    * Video: [Neural Network Learns to Play Snake using Deep Reinforcement Learning](https://www.youtube.com/watch?v=i0Pkgtbh1xw) - March 2020
    * GitHub: ??
>>  
    www.wandb.com ?
    NN Learning need learning data  
    exploration strategy:
    - epsilon greedy (exploration: random move / explotation: NN output)
    64 snakes games running in parallel, 16 steps, >> train
    RL Improvements:
    - Advantage Actor-Critic (A2C)
    - Proximal Policy Optimization (PPO) OpenAI
    - Monte Carlo Tree Search
    Use a model (model-free vs. ..)  
    Calculate the next few frames


* V.Gedace  
    * [Generic solution for the Snake game via Hamiltonian Cycle and additional abbreviation logic.](https://www.youtube.com/watch?v=UI_I6sJXaJw&t=45s&ab_channel=V.Gedace) - Video - Oct 2020  
    * GitHub: [Hamiltonian-Cylce-Snake](https://github.com/UweR70/Hamiltonian-Cylce-Snake) - C# - Algo / Hamiltonian-Cycle
* Pyhton Engineer
    * [Teach AI To Play Snake - Reinforcement Learning Tutorial With PyTorch And Pygame (Part 1)](https://www.youtube.com/watch?v=PJl4iabBEz0&ab_channel=PythonEngineer) - Dec 2020
    * GitHub [snake-ai-pytorch](https://github.com/python-engineer/snake-ai-pytorch)
* Alex Patrenko
    * [Advantage Actor-Critic solves 6x6 Snake (Reinforcement Learning)](https://www.youtube.com/watch?v=bh_5aIqVTUY) - Apr 2018
    * GitHub: [snake-rl](https://github.com/alex-petrenko/snake-rl) - Python - RL Reinforcement Learning, "Monte-Carlo rollout into the future predicted by DNN"
    * GitHub: [sample-factory](https://github.com/alex-petrenko/sample-factory) - Python - Asynchronous reinforcement learning, samples
* Paweł Kamiński
    * Blog: [Training an AI bot to play Snake](https://www.codeer.dev/blog/2020/05/03/ai-snake.html)
    * Video: [AI learns to play Snake - Deep Q Learning - Neural Network](https://www.youtube.com/watch?v=ozFDavKIvpk&ab_channel=Pawe%C5%82Kami%C5%84ski)
    * GitHub: [AI-Snake](https://github.com/pawelkami/AI-Snake) - Python - Deep Reinforcement Learning algorithm, Deep Q Neural Network


* Others:
    * GreerViau [GreerViau](https://www.youtube.com/watch?v=zIkBYwdkuTk&ab_channel=GreerViau)

* To watch:
    * Square Robot [Square Robot](https://www.youtube.com/watch?v=8cdUree20j4&ab_channel=SquareRobots)
    * Ludius0 [..](https://www.youtube.com/watch?v=7Vh77YytDgg&ab_channel=ludius0)


* https://www.researchgate.net/publication/254184076_Neural_Networks_for_Real-time_Pathfinding_in_Computer_Games



## 2. link

[Link to reference](#2-link)


---
 


