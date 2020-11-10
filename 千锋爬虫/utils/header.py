import random

from . import user_agents

def get_ua():
    # 随即提取一个user_agent
    return random.choice(user_agents)