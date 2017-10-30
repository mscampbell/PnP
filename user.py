#!/usr/bin/env python3

#================================================
# Define main user charactrer class and methods
#================================================

import random, time
import creatures
import combatResponses
from textFormat import print_s, input_s, printHealthBar, combatStatus
class Prisoner(object):
	
	def __init__(self, name = 'Unknown', hp = 20, hpmax = 20 ,level = 1, difficulty = 'medium', attack = 6, intelligence = 2, location = 'Prison', mana = 3):
		self.name = name
		if difficulty.upper() == 'easy'.upper():
			hp = 40
			hpmax = 40
			intelligence = 3
		elif difficulty.upper() == 'medium'.upper():
			hp = 20
			hpmax = 20
			intelligence = 2
		elif difficulty.upper() == 'hard'.upper():
			hp = 10
			hpmax = 10
			intelligence = 1
		else:
			hp = 20
			hpmax = 20
			intelligence = 2
			difficulty = 'medium'
		self._intelligence = intelligence
		self._level = level
		self._hp = hp
		self._hpmax = hpmax
		self.difficulty = difficulty
		self._attack = attack
		self.location = location
		self._mana = mana

#Properties to check self variables that should not equal 0 and return hidden attr and pass to unhidden versions

	@property	
	def hp(self):
		if self._hp  < 0:
			self._hp = 0
		return self._hp

	@hp.setter
	def hp(self, value):
		self._hp = value

	@property
	def hpmax(self):
		if self._hpmax < 10:
			self._hpmax = 10
		return self._hpmax

	@hpmax.setter
	def hpmax(self,value):
		self._hpmax = value

	@property
	def intelligence(self):
		if self._intelligence < 0:
			self._intelligence
		return self._intelligence

	@intelligence.setter
	def intelligence(self, value):
		self._intelligence = value

	@property
	def level(self):
		if self._level < 1:
			self._level = 1
		return self._level

	@level.setter
	def level(self, value):
		self._level = value

	@property
	def attack(self):
		if self._attack < 0:
			self._attack = 0
		return self._attack

	@attack.setter
	def attack(self, value):
		self._attack = value

	@property
	def mana(self):
		if self._mana < 0:
			self.mana = 0
		return self._mana

	@mana.setter
	def mana(self, value):
		self._mana = value

# Combat function for creature encounters --- calls combatResponses for sassy comments during battle

	def combat(self,  monster = None):
		while monster.hp > 0:
			if self.hp <= 0:
				input_s('You have died to a ' + monster.name, self, color = 'red')
				break
			elif monster.hp > 0:
				combat_query=input_s('[a]ttack, [r]isky attack, or [m]agic?\n', self)
				
				if combat_query == 'a':
					new_user_attack = random.randint(1,self.attack)
					new_mon_attack = random.randint(1,monster.attack)
					input_s(combatResponses.combatResponse_player(self.attack, new_user_attack) + ' ' + 'You deal ' + str(new_user_attack) + ' damage to ' + monster.name, self, color = 'red')
					monster.hp -= new_user_attack
					if monster.hp > 0:
						input_s('The ' + monster.name + ' has ' + str(monster.hp) + ' health remaining.', self)
						self.hp -= new_mon_attack
						input_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' + monster.name + ' does ' + str(new_mon_attack) + ' damage. Your health is now ' + str(self.hp), self, color = 'red')
					else:
						input_s('The ' + monster.name + ' is dead.\n', self)
						break


				if combat_query == 'r':
					chance = random.randint(1,20)
					min_damage = int(0.5*self.attack)
					max_damage = 2*self.attack
					new_user_attack = random.randint(min_damage,max_damage)
					new_mon_attack = random.randint(1,monster.attack)
					if chance > 10:
						input_s(combatResponses.combatResponse_player(self.attack, new_user_attack) + ' '+ 'You deal ' + str(new_user_attack) + ' damage to ' + monster.name, self, color = 'red')
						monster.hp -= new_user_attack
						if monster.hp > 0:
							input_s('The ' + monster.name + ' has ' + str(monster.hp) + ' health remaining.', self)
							self.hp -= new_mon_attack
							input_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' + monster.name + ' does ' + str(new_mon_attack) + ' damage. Your health is now ' + str(self.hp), self, color = 'red')
						else:
							input_s('The ' + monster.name + ' is dead.\n', self)
							break
					else:
						input_s(combatResponses.missResponse(), self, color = 'purple')
						self.hp -= new_mon_attack
						input_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' +  monster.name + ' does ' + str(new_mon_attack) + ' damage. Your health is now ' + str(self.hp), self, color = 'red')	

				if combat_query == 'm':
					if self.mana > 0:
						new_user_attack = self.attack
						new_mon_attack = random.randint(1,monster.attack)
						input_s(combatResponses.magicResponse() + str(new_user_attack) + ' damage.', self, color = 'red')
						monster.hp -= new_user_attack
						self.mana -= 1
						input_s('You have ' + str(self.mana) + ' mana left.', self)
						if monster.hp > 0:
							input_s('The ' + monster.name + ' has ' + str(monster.hp) + ' health remaining.', self)
							self.hp -=new_mon_attack
							input_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' + monster.name + ' does ' + str(new_mon_attack) + ' damage. Your health is now ' + str(self.hp), self, color = 'red')							
						else:
							input_s('The ' + monster.name + ' is dead.\n', self)
							break
					else:
						input_s('You have no mana left!', self, color = 'blue')
			else:
				break
		combatStatus(self)
# Methods to set self variables

	def setHP(self, new_hp = None):
		self.hp = new_hp

	def setescapeStatus(self, escapeStatus = False):
		self.escapeStatus = escapeStatus

	def setAttack(self, attack_inc = 0):
		self.attack += attack_inc
		print('Your attack damage has increased to ',self.attack,'.\n', sep = '')
