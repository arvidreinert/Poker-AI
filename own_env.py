import gym
from gym import spaces
from stable_baselines3 import PPO
import numpy
import random
import math

class Most_Propable(gym.Env):
    def __init__(self):
        super(Most_Propable, self).__init__()
        self.action_space = spaces.Discrete(8) 
        self.observation_space = spaces.MultiDiscrete([10,10])
        #shields, klee,diamonds,hearts
        self.colors = [1,2,3,4]
        self.numbers = list(range(2,15))
        print(self.reset())

    def reset(self):
        fs = [self.get_pair()]
        return random.choice(fs)

    
    def get_co_and_nu(self,n):
        if n < 100:
            return int(str(n/10).split(".")[0]),int(str(n/10).split(".")[1])
        else:
            return int(str(n/100).split(".")[0]),int(str(n/100).split(".")[1])

    def get_pair(self):
        w = random.choice(self.numbers)
        card1 = int(f"{random.choice(self.colors)}{w}")
        card2 = int(f"{random.choice(self.colors)}{w}")
        while card1 == card2:
            card2 = int(f"{random.choice(self.colors)}{w}")
        return card1, card2

    def step(self, action):
        reward = 0
        if action == 0:  # Keine Bewegung
            reward = -2
        elif action == 1:  # Nach oben
            if self.state - 10 >= 0:
                self.state -= 10
            else:
                reward = -2
        elif action == 2:  # Nach rechts
            if self.state + 1 <= 99:
                self.state += 1
            else:
                reward = -2
        elif action == 3:  # Nach unten
            if self.state + 10 <= 99:
                self.state += 10
            else:
                reward = -2
        elif action == 4:  # Nach links
            if self.state - 1 >= 0:
                self.state -= 1
            else:
                reward = -2

        # Belohnung basierend auf Distanz
        if reward == 0:
            xd = abs(self.get_co_f_n(self.target)[0] - self.get_co_f_n(self.state)[0])
            yd = abs(self.get_co_f_n(self.target)[1] - self.get_co_f_n(self.state)[1])
            ndist = math.sqrt(xd * xd + yd * yd)
            if ndist < dist:
                reward = 1
            elif dist == ndist:
                reward = 0
            else:
                reward = -1

        # Prüfen, ob Ziel erreicht wurde
        done = self.state == self.target
        if done:
            reward = 10

        # Update der Karte
        self.map = [0] * 100
        self.map[self.state] = 2
        self.map[self.target] = 1

        return numpy.array(self.map), reward, done, {}


    def render(self):
        t = ""
        c = 0
        for i in self.map:
            if i == 0:
                t += "⬜"
            if i == 1:
                t += "🟥"
            if i == 2:
                t += "🟩"
            if c%10==0:
                c = 0
                t += "\n"
        print(t)

t = Most_Propable()