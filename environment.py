'''
Authors: Lei Wang, Casey Sader
Project: Reinforcement Learning
Date: 05/15/19
@ALl rights reserved
'''
import numpy as np
import random
import sys

class Map(object):
	"""docstring for Map"""
	def __init__(self, dim):
		self.dim = dim

	def initMap(self):
		self.map = np.zeros((self.dim, self.dim))

	def makeTreasure(self):
		while True:
			x = random.randint(0, self.dim-1)
			y = random.randint(0 ,self.dim-1)
			if x != 0 or y != 0:
				break
		self.map[x][y] = 1
		self.treasure_pos = (x, y)
		print self.treasure_pos

	def makeOpponents(self):
		self.oppo_pos = []
		self.num_of_oppo = random.randint(1, self.dim//2)
		for i in range(self.num_of_oppo):
			x = random.randint(1, self.dim-1)
			y = random.randint(1 ,self.dim-1)
			self.map[x][y] = 3
			self.oppo_pos.append((x, y))

	def makeObsticles(self):
		self.obs_pos = []
		self.num_of_oppo = random.randint(1, self.dim)
		for i in range(self.num_of_oppo):
			x = random.randint(1, self.dim-1)
			y = random.randint(1 ,self.dim-1)
			self.map[x][y] = 2
			self.obs_pos.append((x, y))

	def makePlayer(self):
		self.map[0][0] = -1
		self.play_pos = (0, 0)

	def movePlayer(self, direction):
		done = False
		x = self.play_pos[0]
		y = self.play_pos[1]
		if direction == 0 and y-1 >= 0:
			self.map[x][y] = 0
			self.map[x][y-1] = -1
			self.play_pos = (x, y-1)
		elif direction == 1 and y+1 <= self.dim-1:
			self.map[x][y] = 0
			self.map[x][y+1] = -1
			self.play_pos = (x, y+1)
		elif direction == 2 and x-1 >= 0:
			self.map[x][y] = 0
			self.map[x-1][y] = -1
			self.play_pos = (x-1, y)
		elif direction == 3 and x+1 <= self.dim-1:
			self.map[x][y] = 0
			self.map[x+1][y] = -1
			self.play_pos = (x+1, y)

		if self.play_pos in self.oppo_pos:
			reward = -10
		elif self.play_pos in self.obs_pos:
			reward = -5
		elif self.play_pos == self.treasure_pos:
			reward = 100
			print 'treasure is found'
			done = True
		else:
			reward = -1

		new_s = self.dim*self.play_pos[0] + self.play_pos[1]
		return new_s, reward, done

	def makeMap(self):
		self.initMap()
		self.makeOpponents()
		self.makeObsticles()
		self.makeTreasure()
		self.makePlayer()
		return 0

	def render(self):
		for (x,y) in self.obs_pos:
			if (x,y) != self.play_pos:
				self.map[x][y] = 3
		for (x,y) in self.oppo_pos:
			if (x,y) != self.play_pos:
				self.map[x][y] = 3
		if self.play_pos != self.treasure_pos:
			self.map[self.treasure_pos[0]][self.treasure_pos[1]] = 1
		print self.map


if __name__ == '__main__':
	map = Map(5)

	for i in range(10):
		map.makeMap()
		map.render()



