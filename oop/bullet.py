import pygame
import math


class Bullet:
	def __init__(self, max_bullet):
		self.max_bullet = max_bullet
		self.bullets = []

	def tiles(self):
		pass

	def shoot_sound(self):
		pass

	def hit_enemy_sound(self):
		pass

	def hit_enemy(self):
		pass

	def set_screen(self, screen):
		self.screen = screen
	
	def add_bullet(self, cordinate):
		if len(self.bullets) <= self.max_bullet:
			self.bullets.append(cordinate)

	def draw(self):
		for bullet in self.bullets:
			arrow_index = 0
			velx = math.cos(bullet[0])*10
			vely = math.sin(bullet[0])*10
			bullet[1] += velx
			bullet[2] += vely
			if bullet[1] < -64 or bullet[1] > pygame.display.Info().current_w or bullet[2] < -64 or bullet[2] > pygame.display.Info().current_h:
				self.bullets.pop(arrow_index)

			arrow_index += 1
		# draw the arrow of list bullets
		for projectile in self.bullets:
			new_arrow = pygame.transform.rotate(
				self.tiles(), 360-projectile[0]*57.29)
			self.screen.blit(new_arrow, (projectile[1], projectile[2]))
	def draw(self):
		for bullet in self.bullets:
			fire_index = 0
			velx = math.cos(bullet[0])*10
			vely = math.sin(bullet[0])*10
			bullet[1] += velx
			bullet[2] += vely
			if bullet[1] < -64 or bullet[1] > pygame.display.Info().current_w or bullet[2] < -64 or bullet[2] > pygame.display.Info().current_h:
				self.bullets.pop(fire_index)
			fire_index += 1
		# draw the fire of list bullets
		for projectile in self.bullets:
			new_fire = pygame.transform.rotate(
				self.tiles(), 360-projectile[0]*57.29)
			self.screen.blit(new_fire, (projectile[1], projectile[2]))
class Fire(Bullet):
	max_fire = 5

	def __init__(self):
		Bullet.__init__(self, Fire.max_fire)

	def tiles(self):
		return pygame.image.load('resources\images\._fire.png')

	def shoot_sound(self):
		tmp = pygame.mixer.Sound("resources/audio/shoot.wav")
		tmp.set_volume(0.05)
		return tmp

	def hit_enemy_sound(self):
		pass

	def hit_enemy(self, enemies):
		pass



class Arrow(Bullet):
	max_bullet = 5

	def __init__(self):
		Bullet.__init__(self, Arrow.max_bullet)

	def tiles(self):
		return pygame.image.load('resources/images/bullet.png')

	def shoot_sound(self):
		tmp = pygame.mixer.Sound("resources/audio/shoot.wav")
		tmp.set_volume(0.05)
		return tmp

	def hit_enemy_sound(self):
		pass

	def hit_enemy(self, enemies):
		pass




	def draw(self):
		for bullet in self.bullets:
			water_index = 0
			velx = math.cos(bullet[0])*10
			vely = math.sin(bullet[0])*10
			bullet[1] += velx
			bullet[2] += vely
			if bullet[1] < -64 or bullet[1] > pygame.display.Info().current_w or bullet[2] < -64 or bullet[2] > pygame.display.Info().current_h:
				self.bullets.pop(water_index)
			water_index += 1
		# draw the water of list bullets
		for projectile in self.bullets:
			new_water = pygame.transform.rotate(
				self.tiles(), 360-projectile[0]*57.29)
			self.screen.blit(new_water, (projectile[1], projectile[2]))
class Water(Bullet):
	max_water = 5

	def __init__(self):
		Bullet.__init__(self, Water.max_water)

	def tiles(self):
		return pygame.image.load('resources\images\._water.png')

	def shoot_sound(self):
		tmp = pygame.mixer.Sound("resources/audio/shoot.wav")
		tmp.set_volume(0.05)
		return tmp

	def hit_enemy_sound(self):
		pass

	def hit_enemy(self, enemies):
		pass







