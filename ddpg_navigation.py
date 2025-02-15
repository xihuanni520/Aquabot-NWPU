# ddpg_navigation.py
import numpy as np
import tensorflow as tf
from ddpg import DDPG

class UnderwaterNavigator:
    def __init__(self, state_dim=6, action_dim=3):
        self.agent = DDPG(state_dim, action_dim)
        self.agent.load_weights("weights/ddpg_underwater.h5")

    def get_action(self, state):
        # 状态: [x, y, z, vx, vy, vz]
        state = np.reshape(state, [1, state_dim])
        action = self.agent.actor.predict(state)[0]
        return action  # 输出: [胸鳍频率, 转向角, 深度调整]