import numpy as np
import gym
import random
import time
from IPython.display import clear_output
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Create the environment
env = gym.make("FrozenLake-v1")

# Initialize Q-table with zeros
possible_actions = env.action_space.n
possible_states = env.observation_space.n
qtable = np.zeros((possible_states, possible_actions))

# Set parameters
num_episodes = 10000
max_steps_per_episode = 250

learning_rate = 0.09
discount_rate = 0.99

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.0009

# Initialize rewards array
rewards_all_episodes = []

# Q-learning algorithm
for episode in range(num_episodes):
    state, prob = env.reset()
    done = False
    rewards_current_episode = 0

    for step in range(max_steps_per_episode):
        exploration_rate_threshold = random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(qtable[state, :])
        else:
            action = env.action_space.sample()

        new_state, reward, done, truncated, info = env.step(action)
        max_new_state = np.max(qtable[new_state, :])
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + discount_rate * max_new_state - qtable[state, action])

        state = new_state
        rewards_current_episode += reward

        if done or truncated:
            break

    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate * episode)
    rewards_all_episodes.append(rewards_current_episode)

# Calculate and print the average reward per thousand episodes
reward_per_thousand_episodes = np.split(np.array(rewards_all_episodes), num_episodes / 1000)
count = 1000
print("Average reward per thousand episodes:")
for r in reward_per_thousand_episodes:
    print(count, ":", str(np.sum(r) / 1000))
    count += 1000

# Print the final Q-table
#print("\nQ-table:")
#print(qtable)
"""
import time
env = gym.make("FrozenLake-v1", render_mode="human")
for episodes in range(3):
    state, info = env.reset()
    done = False
    time.sleep(1)

    for step in range(max_steps_per_episode):
        print("Episode", episodes + 1)
        clear_output(wait = True)
        env.render()
        time.sleep(0.3)

        action = np.argmax(qtable[state, :])
        new_state, reward, done, trucated, info = env.step(action)

        if done:
            if reward == 1:
                print("You reached the goal")
                time.sleep(3)
            else:
                print("You fell in hole")
                time.sleep(3)
            break

        if done:
            break
        state = new_state
env.close()
"""
