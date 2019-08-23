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
***
### My Own Intuition
Notice that in value iteration, we do not use or update a policy and
therefore do not necessarily care about recording which actions were taken.
In each Bellman backup for value iteration, we iterate through every possible 
action for every state with only the max values from the best actions for each
state being recorded into the value function. This is repeated until the value
function converges. Only then is a policy formed. This policy is optimal as any
policy derived from an optimal value function is itself optimal.

In contrast, policy iteration performs Bellman backups for the value function
following a given policy where the policy is updated whenever the value function
converges for a suboptimal policy. This is repeated until either the policy or
value function converges.

Both methods when implemented correctly will converge to the same value function
as there is only one unique optimal value function in a Markov Decision Process.
Optimal policies on the other hand may be non-unique and thus be different.
The pros/cons of each method pertain to computational efficiency.
