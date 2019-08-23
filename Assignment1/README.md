## Assignment 1 - Intro to Sequential Decision Making and OpenAI Gym

This assignment contains written questions as well as coding assignments.
Particularly, in vi_and_pi.py, implement:
- Policy Evaluation
- Policy Improvement
- Policy Iteration
- Value Iteration

in order to solve the [Deterministic and Stochastic 4x4 Frozen Lake](https://gym.openai.com/envs/FrozenLake-v0/) environments from OpenAI gym.

### Quote from Sutton & Barton's Reinforcement Learning: An Introduction 2nd Edition
I believe this quote from Sutton and Barton's textbook eloquently describes what the value function represents.


**pg. 64**: "The beauty of v_star is that if one uses it to evaluate the short term consequences of actions - 
specifically the one-step consequences - then a greedy policy is actually optimal in the long-term sense in which we are
interested because *v_star already takes into account the reward consequences of all possible future behavior*. By means of
v_star, *the optimal expected long-term return is turned into a quantity that is locally and immediately available for each state*.
Hence, a one-step-ahead search yields the long-term optimal actions."
