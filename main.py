import gym
from gym import spaces
from stable_baselines3 import PPO
import numpy
from own_env import Higher_lower
from gym.envs.registration import register
"""running pre made:
env = gym.make("CartPole-v1",render_mode="human")
model = PPO("MlpPolicy",env,verbose=1)
model.learn(10000)
model.save("test_model")
obs,_ = env.reset()
done = False
while not done:
    action, _states = model.predict(obs)
    obs,reward,done,x,info = env.step(action)
    done = done or x
    env.render()
env.close()"""
#running own:
register(id="testing_env",entry_point="__main__:Higher_lower")
"""env = gym.make("testing_env")
env.reset()
for _ in range(10):
    action = env.action_space.sample()
    state,reward,done,_ = env.step(action)
    print(f"Action{action}  Reward: {reward}")
    if done:
        env.render()
        print("done",state)
        break
env.close()"""

"""model = PPO.load("testedv1")

# Use the model to interact with the environment
env = Envsi()  # Make sure to reinitialize your environment
obs = env.reset()

for i in range(100):
    action, _ = model.predict(obs)  # Predict the best action
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        print("Target reached!",i)
        break"""

import time

env = Higher_lower()
model = PPO("MlpPolicy", env, verbose=1)
#model.learn(total_timesteps=10000) 
#model.save("test_model")

model = PPO.load("test_model", env=env)

# Environment zurücksetzen
obs, _ = env.reset()
done = False

# Simulation des gelernten Modells
while not done:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
    time.sleep(0.1)

env.close()
