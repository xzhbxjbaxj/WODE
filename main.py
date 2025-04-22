from agents.dqn_agent import DQNAgent
from envs.multi_task_env import MultiTaskEnv
import torch

def train():
    env = MultiTaskEnv()
    agent = DQNAgent(env.observation_space.shape[0], env.action_space.n)

    episodes = 1000
    for episode in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.select_action(state)
            next_state, reward, done, info = env.step(action)
            agent.store_transition(state, action, reward, next_state, done)
            agent.learn()
            state = next_state
            total_reward += reward

        print(f"Episode {episode}, Total Reward: {total_reward}")

if __name__ == "__main__":
    train()
