# Import the required libraries
import numpy as np
import gym

# Initialize the environment: FrozenLake with render_mode specified
env = gym.make('FrozenLake-v1', is_slippery=False, render_mode='human')

# Initialize Q-table with zeros
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Set hyperparameters
learning_rate = 0.8
discount_factor = 0.95
episodes = 1000
max_steps = 100  # Max steps per episode
exploration_rate = 1.0  # Exploration rate (epsilon)
max_exploration_rate = 1.0
min_exploration_rate = 0.01
decay_rate = 0.001

# List to store total rewards per episode
rewards_all_episodes = []

# Q-learning algorithm
for episode in range(episodes):
    state = env.reset()[0]  # Reset the environment and get initial state
    total_rewards = 0
    
    for step in range(max_steps):
        # Choose action using epsilon-greedy approach
        if np.random.rand() < exploration_rate:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(Q[state, :])  # Exploit

        # Take the action and observe the new state and reward
        new_state, reward, done, _, _ = env.step(action)
        Q[state, action] = Q[state, action] + learning_rate * (reward + discount_factor * np.max(Q[new_state, :]) - Q[state, action])

        state = new_state  # Update the state
        total_rewards += reward
        
        if done:  # If the episode is over, break the loop
            break

    # Decrease exploration rate (epsilon) to reduce exploration over time
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-decay_rate * episode)

    rewards_all_episodes.append(total_rewards)

# Evaluate the learned policy
print(f"Average reward per 100 episodes: {np.mean(rewards_all_episodes[-100:])}")

# Test the learned policy
state = env.reset()[0]
done = False
while not done:
    action = np.argmax(Q[state, :])  # Take the best action according to Q-table
    state, reward, done, _, _ = env.step(action)
    env.render()  # Render the environment (show the grid)
