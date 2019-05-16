'''
Authors: Lei Wang, Casey Sader
Project: Reinforcement Learning
Date: 05/15/19
@ALl rights reserved
'''
import numpy as np
import environment
import sys

def eps_greedy_q_learning_with_table(dim, num_episodes=50):
    q_table = np.zeros((dim*dim, 4))
    y = 0.95
    eps = 0.5
    lr = 0.8
    decay_factor = 0.999
    for i in range(num_episodes):
        print '\r episode %i' % i
        s = map.makeMap()
        eps *= decay_factor
        done = False
        counter = 0
        while not done:
            print 'counter', counter
            counter += 1
            # select the action with highest cummulative reward
            if np.random.random() < eps or np.sum(q_table[s, :]) == 0:
                a = np.random.randint(0, 4)
            else:
                a = np.argmax(q_table[s, :])
            new_s, r, done = map.movePlayer(a)
            map.render()
            q_table[s, a] += r + lr * (y * np.max(q_table[new_s, :]) - q_table[s, a])
            s = new_s
            if counter == 500:
                done = True

    print '\r\rQ table'
    print q_table


if __name__ == '__main__':
    dim, episodes = int(sys.argv[1]),int(sys.argv[2])
    map = environment.Map(dim)

    m2_table = eps_greedy_q_learning_with_table(dim, episodes)
