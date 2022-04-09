import pygame
from oop.bullet import Arrow, Fire, Water
from oop.control import GameController
from oop.scene import Scene
from oop.level.level1 import Level1
from oop.level.level2 import Level2
from oop.level.level3 import Level3
from oop.player import Player

pygame.init()

#Pilih 3 Weapon ! dengan menghapus (#)
scene = Scene((640, 480))
scene.setup_level(
  Level1(),
  Level2(),
  Level3()
)
#Pilih 3 Weapon ! dengan menghapus (#)
player = Player(scene.screen)
#player.set_weapon(Arrow())
#player.set_weapon(Fire())
player.set_weapon(Water())
game_controller = GameController(player)

scene.next_level();
scene.next_level();
running = True
while(running):
  scene.fill()
  game_controller.keyboard_event()
  game_controller.mouse_position_event()
  player.draw()
  pygame.display.flip()