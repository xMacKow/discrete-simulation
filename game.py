import init_screen
import initial_battles
import logic
from troops import *

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((init_screen.WIDTH, init_screen.HEIGHT))
        self.image = pygame.image.load('bg.jpg').convert()
        self.screen = init_screen.init_screen(self.screen, self.image)
        self.pattern = 1
        self.setHusar = True
        self.setCossacsThirdBattle = True
        self.setInfantryThirdBattle = True
        self.myFont = pygame.font.SysFont("monospace", 20)
        self.firstLabel = self.myFont.render("Bitwa pod Chocimiem 1509", 1, (0, 0, 0))
        self.secondLabel = self.myFont.render("Bitwa pod Chocimiem 1621", 1, (0, 0, 0))
        self.thirdLabel = self.myFont.render("Bitwa pod Chocimiem 1673", 1, (0, 0, 0))

    def update_troops(self, polish_moving, osman_moving):
        if not self.polish_troops or not self.osman_troops:
            return

        for squad in self.polish_troops:
            closest = logic.find_closest_object(squad.x, squad.y, self.osman_troops)

            if self.setCossacsThirdBattle and self.pattern == 3 and type(squad) == Cossack:
                speed = squad.speed / 10
                if squad.x < 985:
                    squad.x += speed / 4
                    squad.y -= speed
                elif squad.x >= 985:
                    self.setCossacsThirdBattle = False
                continue

            if logic.does_overlap(closest, squad):
                squad.stop()
                closest.stop()
                closest.damage(squad.attack * 0.01)
            elif polish_moving:
                squad.move(closest)

        for squad in self.osman_troops:
            closest = logic.find_closest_object(squad.x, squad.y, self.polish_troops)

            if self.setInfantryThirdBattle and self.pattern == 3 and type(squad) == Infantry:
                if squad.x < 825:
                    speed2 = squad.speed / 10
                    squad.x += speed2 / 4
                    squad.y -= speed2 / 5
                elif squad.x >= 825:
                    self.setInfantryThirdBattle = False
                continue

            if logic.does_overlap(closest, squad):
                squad.stop()
                closest.stop()
                closest.damage(squad.attack * 0.01)
            elif osman_moving:
                squad.move(closest)

    def draw_troops(self):
        if not self.polish_troops or not self.osman_troops:
            return

        for squad in self.osman_troops:
            pygame.display.update(squad.draw(self.screen, False))
        for squad in self.polish_troops:
            pygame.display.update(squad.draw(self.screen, True))

    def first_battle(self):
        if not self.osman_troops or not self.polish_troops:
            self.running = False
        for squad in self.osman_troops:
            if squad.number == 0:
                self.osman_troops.remove(squad)

        for squad in self.polish_troops:
            if squad.number == 0:
                self.polish_troops.remove(squad)

        if not self.polish_troops or not self.osman_troops:
            return

        for squad in self.polish_troops:
            closest = logic.find_closest_object(squad.x, squad.y, self.osman_troops)

            if type(squad) == Hussar and self.setHusar:
                speed = squad.speed / 10

                if squad.x > 770:
                    squad.x -= speed
                elif 770 >= squad.x > 430:
                    squad.x -= speed
                    squad.y += speed
                    if squad.y >= 500:
                        squad.y -= speed
                        squad.x -= speed
                elif 430 >= squad.x > 360:
                    squad.y -= speed
                    squad.x -= speed / 4
                if squad.x <= 360:
                    self.setHusar = False

                continue

            if logic.does_overlap(closest, squad):
                squad.stop()
                closest.stop()
                closest.damage(squad.attack * 0.01)
            else:
                squad.move(closest)

        for squad in self.osman_troops:
            closest = logic.find_closest_object(squad.x, squad.y, self.polish_troops)

            if logic.does_overlap(closest, squad):
                squad.stop()
                closest.stop()
                closest.damage(squad.attack * 0.01)
            else:
                squad.move(closest)

        self.draw_troops()

    def default_battle(self, polish_moving, osman_moving):
        if not self.osman_troops or not self.polish_troops:
            self.running = False
        for squad in self.osman_troops:
            if squad.number == 0:
                self.osman_troops.remove(squad)

        for squad in self.polish_troops:
            if squad.number == 0:
                self.polish_troops.remove(squad)

        if self.polish_troops and self.osman_troops:
            self.update_troops(polish_moving, osman_moving)
        self.draw_troops()

    def battle(self):
        if self.pattern == 1:
            self.first_battle()
        elif 2 <= self.pattern <= 3:
            self.default_battle(True, True)
        else:
            self.running = False

    def run(self):
        can_continue = True
        while can_continue:
            self.running = True
            TROOPS = initial_battles.load_battle(self.pattern)
            if not TROOPS:
                self.running = False
                can_continue = False
                break

            self.polish_troops = TROOPS[0]
            self.osman_troops = TROOPS[1]

            paused = False
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        can_continue = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            paused = not paused
                        # Wciśnięcie 'q' spowoduje wypisanie w konsoli wszystkich oddziałów aktualnej bitwy
                        if event.key == pygame.K_q:
                            print('-----------------------------------')
                            for enemy in self.osman_troops:
                                print("Oddział tatarski: " + enemy.name + ", Units left = " + str(int(enemy.number)))
                            for troop in self.polish_troops:
                                print("Oddział polski: " + troop.name + ", Units left = " + str(int(troop.number)))
                        if event.key == pygame.K_RIGHT:
                            self.pattern += 1
                            if self.pattern == 1:
                                self.setHusar = True
                            if self.pattern == 3:
                                self.setCossacsThirdBattle = True
                                self.setInfantryThirdBattle = True
                            self.running = False
                            break

                        if event.key == pygame.K_LEFT:
                            self.pattern -= 1
                            if self.pattern == 1:
                                self.setHusar = True
                            if self.pattern == 3:
                                self.setCossacsThirdBattle = True
                                self.setInfantryThirdBattle = True
                            self.running = False
                            break

                if paused:
                    continue

                pygame.display.flip()
                self.screen.blit(self.image, (0, 0))
                if self.pattern == 1:
                    self.screen.blit(self.firstLabel, (400, 20))
                elif self.pattern == 2:
                    self.screen.blit(self.secondLabel, (400, 20))
                elif self.pattern == 3:
                    self.screen.blit(self.thirdLabel, (400, 20))
                pygame.time.delay(30)
                self.battle()

            if not self.polish_troops:
                print("ENEMY WINS")
                for enemy in self.osman_troops:
                    print("Left: " + enemy.name + ", Units left = " + str(int(enemy.number)))
                self.pattern += 1
            elif not self.osman_troops:
                print("POLAND WINS")
                for troop in self.polish_troops:
                    print("Left: " + troop.name + ", Units left = " + str(int(troop.number)))
                self.pattern += 1

    def start(self):
        self.run()
