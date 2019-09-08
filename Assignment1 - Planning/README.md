## Assignment 1 - Intro to Sequential Decision Making and OpenAI Gym

This assignment contains written questions as well as coding assignments. We use dynamic programming methods to compute optimal policies given a perfect model of the environment as a Markov decision process.

Particularly, in vi_and_pi.py, we implement:
- Policy Evaluation
- Policy Improvement
- Policy Iteration
- Value Iteration

in order to solve the [Deterministic and Stochastic 4x4 Frozen Lake](https://gym.openai.com/envs/FrozenLake-v0/) environments from OpenAI gym.

### Quotes from Sutton & Barton's Reinforcement Learning: An Introduction 2nd Edition
__I believe this quote from Sutton and Barton's textbook eloquently describes what the value function represents:__

**pg. 64**: "The beauty of v_star is that if one uses it to evaluate the short term consequences of actions - 
specifically the one-step consequences - then a greedy policy is actually optimal in the long-term sense in which we are
interested because *v_star already takes into account the reward consequences of all possible future behavior*. By means of
v_star, *the optimal expected long-term return is turned into a quantity that is locally and immediately available for each state*.
Hence, a one-step-ahead search yields the long-term optimal actions."

__Also, this quote states the limitations to this assignment's approach to solving reinforcement learning problems:__

**pg. 73**: "Classical DP (Dynamic Programming) algorithms are of limited utility in reinforcement learning both
because of their assumption of a perfect model and because of their great computational expense, but they are still
important theoretically."
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
converges for a suboptimal policy. The policy is updated by computing the values of
choosing an action and **then** following the current policy for all possible actions. If any of these values
are greater than the current value for a certain state, then the policy is updated accordingly to the new action.
This is repeated until either the policy or value function converges.

**Both methods when implemented correctly will converge to the same value function
as there is only one unique optimal value function in a Markov Decision Process.
Optimal policies on the other hand may be non-unique and thus be different.**
The pros/cons of each method pertain to computational efficiency.

Regardless of which iteration method is used, both dynamic programming algorithms work
due to **bootstrapping** in which we update our current estimate of the value function by using our
previous estimate. This works because each iteration of the value function is the k-horizon value of the states under 
a policy. In other words, it is the expected discounted sum of returns if we were to start from each state and have
k time steps following a given policy. Due to this, we can bootstrap and update our value function by adding the expected immediate reward with the expected (k-1) value for all possible future states.
Using this method, there is no need to compute any more steps past the first one giving the immediate reward for each update because we have already technically computed the rest of the (k-1) steps for all states under a given policy as given by our (k-1) value function. Therefore, we can **bootstrap** the rest of the value arising from future possibilities with our (k-1) value function. As k --> infinity, the value function will become an accurate estimate of the infinite horizon value of states under the policy.
