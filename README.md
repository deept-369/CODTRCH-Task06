# Task Six: Reinforcement Learning for Game Playing

## 1. Details

**Name:** TANWAR DEEP DINESHBHAI  
**Company:** CODTECH IT SOLUTIONS  
**ID:** CT08DS408  
**Domain:** ARTIFICIAL INTELLIGENCE  
**Duration:** DECEMBER 5th, 2024 to JANUARY 5th, 2025  
**Mentor:** Muzammil Ahmed  

---

## 2. Overview of the Project

Reinforcement Learning (RL) is a core branch of Artificial Intelligence designed to train agents to make optimal decisions in an environment by maximizing cumulative rewards over time. This project involves developing an RL agent capable of playing the **FrozenLake** game, a well-known environment in the OpenAI Gym library. The primary objective is to train the agent to navigate the grid world efficiently and reach the goal while avoiding obstacles.

### Objectives:
- Implement a **Q-learning** algorithm.
- Train the RL agent over multiple episodes.
- Evaluate the performance of the trained agent using the learned Q-table.

---

## 3. Key Activities

### Environment Initialization:
- Set up the FrozenLake environment with deterministic behavior (`is_slippery=False`) for easier debugging and training.

### Q-table Initialization:
- Create a Q-table to store the value of state-action pairs.

### Q-learning Implementation:
- Implement the Q-learning algorithm, which uses the **Bellman equation** to iteratively update the Q-values.
- Employ an **epsilon-greedy** approach to balance exploration and exploitation.

### Training:
- Train the agent over **1000 episodes**.
- Gradually decrease the exploration rate to shift from exploration to exploitation as the agent learns the environment.

### Evaluation and Testing:
- Evaluate the agent's performance using average rewards over the last **100 episodes**.
- Test the trained policy by running the agent in the environment and rendering its actions.

---

## 4. Technologies Used

### Programming Language:
- **Python**

### Libraries:
- **NumPy**: For efficient numerical computations and array manipulations.
- **Gym**: To provide the FrozenLake environment for RL training.

---

## 5. Output
![image](https://github.com/user-attachments/assets/512da419-9350-446d-aaab-918bb407af53)
