### MDP Value Iteration and Policy Iteration

import numpy as np
import gym
import time
from lake_envs import *

np.set_printoptions(precision=3)

"""
For policy_evaluation, policy_improvement, policy_iteration and value_iteration,
the parameters P, nS, nA, gamma are defined as follows:

    P: nested dictionary
        From gym.core.Environment
        For each pair of states in [1, nS] and actions in [1, nA], P[state][action] is a
        tuple of the form (probability, nextstate, reward, terminal) where
            - probability: float
                the probability of transitioning from "state" to "nextstate" with "action"
            - nextstate: int
                denotes the state we transition to (in range [0, nS - 1])
            - reward: int
                either 0 or 1, the reward for transitioning from "state" to
                "nextstate" with "action"
            - terminal: bool
              True when "nextstate" is a terminal state (hole or goal), False otherwise
    nS: int
        number of states in the environment
    nA: int
        number of actions in the environment
    gamma: float
        Discount factor. Number in range [0, 1)
"""

def policy_evaluation(P, nS, nA, policy, gamma=0.9, tol=1e-3):
    """Evaluate the value function from a given policy.

    Parameters
    ----------
    P, nS, nA, gamma:
        defined at beginning of file
    policy: np.array[nS]
        The policy to evaluate. Maps states to actions.
    tol: float
        Terminate policy evaluation when
            max |value_function(s) - prev_value_function(s)| < tol
    Returns
    -------
    V: np.ndarray[nS]
        The value function of the given policy, where value_function[s] is
        the value of state s
    """

    ############################
    # YOUR IMPLEMENTATION HERE #

    newV = np.zeros(nS, dtype=float)

    while True:
        # Each iteration is a Bellman Backup
        V = newV.copy()
        newV = np.zeros(nS, dtype=float)
        for state in range(nS):
            action = policy[state]
            # store a value for each state as the sum of the weighted rewards
            # for all possible outcomes given by the action chosen by the policy
            for probability, nextState, reward, terminal in P[state][action]:
                newV[state] += probability * (reward + gamma*V[nextState])

        # Output the value function upon convergence
        if np.all(np.abs(newV - V) < tol): break

    return newV
    ############################


def policy_improvement(P, nS, nA, value_from_policy, policy, gamma=0.9):
    """Given the value function from policy improve the policy.

    Parameters
    ----------
    P, nS, nA, gamma:
        defined at beginning of file
    value_from_policy: np.ndarray
        The value calculated from the policy
    policy: np.array
        The previous policy.

    Returns
    -------
    newPolicy: np.ndarray[nS]
        An array of integers. Each integer is the optimal action to take
        in that state according to the environment dynamics and the
        given value function.
    """

    ############################
    # YOUR IMPLEMENTATION HERE #

    newPolicy = policy.copy()

    for state in range(nS):
        # overwrite each Q vector for each state as there is no need to
        # store previous state Q values
        Q = np.zeros(nA)
        for action in range(nA):
            for probability, nextState, reward, terminal in P[state][action]:
                # store each (state, action) pair's value as a sum of the
                # weighted rewards for all possible outcomes of the chosen action
                Q[action] += probability * (reward + gamma*value_from_policy[nextState])

        # np.argmax does not randomly tie break, so implement this method
        # where the new most optimal action for each state is randomly chosen
        maxPos = np.argwhere(Q == np.amax(Q)).ravel()
        newPolicy[state] = np.random.choice(maxPos)

    return newPolicy
    ############################


def policy_iteration(P, nS, nA, gamma=0.9, tol=1e-3):
    """Runs policy iteration.

    You should call the policy_evaluation() and policy_improvement() methods to
    implement this method.

    Parameters
    ----------
    P, nS, nA, gamma:
        defined at beginning of file
    tol: float
        tol parameter used in policy_evaluation()
    Returns:
    ----------
    V: np.ndarray[nS]
    policy: np.ndarray[nS]
    """

    ############################
    # YOUR IMPLEMENTATION HERE #

    newV = np.zeros(nS)
    iterations = 0
    firstIter = True
    newPolicy = np.random.randint(0, nA, nS)
    start = time.time()

    while True:
        iterations += 1
        V = newV.copy()
        policy = newPolicy.copy()

        # Calculate the value function for the given policy
        newV = policy_evaluation(P, nS, nA, policy, gamma, tol)

        # Using the new value function, create a new improved policy
        newPolicy = policy_improvement(P, nS, nA, newV, policy, gamma)

        # Repeat until convergence of the policy
        if np.linalg.norm(newPolicy - policy, ord=1) < tol: break
        # often times value function has converged but there are many tie
        # policies; this cancels unproductive continuous policy switching
        if not firstIter and np.all(np.abs(newV - V) < tol): break
        firstIter = False

    end = time.time()

    print("NOTE - Policy iteration does not count iterations of value function " + \
          "converging for each new policy.\nTherefore, time elapsed would be a " + \
          "better indicator of performance.\n")
    print('Policy - Iterations: ' + str(iterations))
    print("Policy iteration took " + str(end - start) + " seconds to converge.")

    return V, policy
    ############################


def value_iteration(P, nS, nA, gamma=0.9, tol=1e-3):
    """
    Learn value function and policy by using value iteration method for a given
    gamma and environment.

    Parameters:
    ----------
    P, nS, nA, gamma:
        defined at beginning of file
    tol: float
        Terminate value iteration when
            max |value_function(s) - prev_value_function(s)| < tol
    Returns:
    ----------
    V: np.ndarray[nS]
    policy: np.ndarray[nS]
    """

    ############################
    # YOUR IMPLEMENTATION HERE #

    V = np.zeros(nS)
    newV = V.copy()
    policy = np.zeros(nS, dtype=int)
    iterations = 0
    start = time.time()

    while True:
        # Each iteration is a Bellman Backup
        iterations += 1

        for state in range(nS):
            # overwrite each B vector for each state as there is no need to
            # store previous state B values
            B = np.zeros(nA)
            for action in range(nA):
                # store each (state, action) pair's value as a sum of the
                # weighted rewards for all possible outcomes of the chosen action
                for probability, nextState, reward, terminal in P[state][action]:
                    B[action] += probability * (reward + gamma*V[nextState])

            # Assign the max of vector B to the value function for a particular state
            # Notice that in value iteration, we do not update the policy and therefore
            # do not necessarily care about recording which actions were taken.
            # Although we iterate through the actions, we do not record them; only the
            # max value from the optimal action is recorded. This is in direct contrast
            # to policy iteration where the optimal actions ARE recorded and used to
            # determine the next chosen actions during policy evaluation (Bellman Backup).
            newV[state] = np.amax(B)

        # Repeat until convergence
        if np.all(np.abs(V - newV) < tol): break
        V = newV.copy()

    # Update the policy only once, once the value function has converged
    # Any policy that employs greedy selection with an optimal value function
    # is an optimal policy.
    policy = policy_improvement(P, nS, nA, newV, policy, gamma)
    end = time.time()

    print("Value - Iterations: " + str(iterations))
    print("Value iteration took " + str(end-start) + " seconds to converge.")

    return newV, policy
    # ############################


def render_single(env, policy, max_steps=100):
  """
    This function does not need to be modified
    Renders policy once on environment. Watch your agent play!

    Parameters
    ----------
    env: gym.core.Environment
      Environment to play on. Must have nS, nA, and P as
      attributes.
    Policy: np.array of shape [env.nS]
      The action to take at a given state
  """

  episode_reward = 0
  ob = env.reset()
  for t in range(max_steps):
    env.render()
    time.sleep(0.20)
    a = policy[ob]
    ob, rew, done, _ = env.step(a)
    episode_reward += rew
    if done:
      break
  env.render();
  if not done:
    print("The agent didn't reach a terminal state in {} steps.".format(max_steps))
  else:
    print("Episode reward: %f" % episode_reward)


# Edit below to run policy and value iteration on different environments and
# visualize the resulting policies in action!
# You may change the parameters in the functions below
if __name__ == "__main__":

    # comment/uncomment these lines to switch between deterministic/stochastic environments
    #env = gym.make("Deterministic-4x4-FrozenLake-v0")
    env = gym.make("Stochastic-4x4-FrozenLake-v0")

    V_pi, p_pi = policy_iteration(env.P, env.nS, env.nA, gamma=0.9, tol=1e-3)
    V_vi, p_vi = value_iteration(env.P, env.nS, env.nA, gamma=0.9, tol=1e-3)
    print("\n" + "-" * 25 + "\nPolicy Iteration\n" + "-" * 25)
    print('  Optimal Value Function: %r' % V_pi)
    print('  Optimal Policy:         %r' % p_pi)
    print("\n" + "-" * 25 + "\nValue Iteration\n" + "-" * 25)
    print('  Optimal Value Function: %r' % V_vi)
    print('  Optimal Policy:         %r' % p_vi)
    print("\n" + "-" * 25 + "\nBeginning Policy Iteration\n" + "-" * 25)
    render_single(env, p_pi, 100)
    print("\n" + "-" * 25 + "\nBeginning Value Iteration\n" + "-" * 25)
    render_single(env, p_vi, 100)
