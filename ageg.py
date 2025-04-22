import random
import torch
import torch.nn as nn
import torch.optim as optim
from utils.replay_buffer import ReplayBuffer
import numpy as np

class Net(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(Net, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
        )

    def forward(self, x):
        return self.fc(x)

class DQNAgent:
    def __init__(self, state_dim, action_dim):
        self.model = Net(state_dim, action_dim)
        self.target = Net(state_dim, action_dim)
        self.optimizer = optim.Adam(self.model.parameters(), lr=1e-3)
        self.buffer = ReplayBuffer(10000)
        self.gamma = 0.99
        self.epsilon = 0.1
        self.action_dim = action_dim

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_dim - 1)
        state = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
        with torch.no_grad():
            return self.model(state).argmax().item()

    def store_transition(self, s, a, r, s_, d):
        self.buffer.push(s, a, r, s_, d)

    def learn(self):
        if len(self.buffer) < 32:
            return
        states, actions, rewards, next_states, dones = self.buffer.sample(32)

        q_values = self.model(states).gather(1, actions)
        with torch.no_grad():
            next_q = self.target(next_states).max(1)[0].unsqueeze(1)
            target = rewards + self.gamma * next_q * (1 - dones)

        loss = nn.MSELoss()(q_values, target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
