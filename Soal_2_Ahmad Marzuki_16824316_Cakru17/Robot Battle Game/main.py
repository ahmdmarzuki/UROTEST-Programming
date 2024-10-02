import pygame
import sys
from robot import RobotA1, RobotA2, RobotA3

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Robot Battle")

# framerate
clock = pygame.time.Clock()
FPS = 60

# color
YELLOW = (225, 225, 0)
RED = (225, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 0, 200)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Arial', 40)
text_color = (0, 0, 0)
text_select_p1 = font.render("Select player 1!", True, text_color)
text_select_p2 = font.render("Select player 2!", True, text_color)
text_start_game = font.render("Let's start fighting!", True, text_color)
text_player_1_win = font.render("Player 1 Win", True, text_color)
text_player_2_win = font.render("Player 2 Win", True, text_color)


# image bg
bg_image = pygame.image.load("assets/images/bg.jpeg").convert_alpha()

winner = None

# GameStateManager
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        # robot attribute
        self.robot_1 = None
        self.robot_2 = None

        self.gameStateManager = GameStateManager('win_scene')

        # sceneee
        self.start = Start(self.screen, self.gameStateManager, self)
        self.arena = Battle(self.screen, self.gameStateManager, self)
        self.winScene = WinScene(self.screen, self.gameStateManager, self)

        # dict scene
        self.states = {'start': self.start, 'arena': self.arena, 'win_scene': self.winScene}
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Run the current state
            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)


# scene buat milih milih robot
class Start:
    def __init__(self, display, gameStateManager, game):
        self.display = display
        self.gameStateManager = gameStateManager
        self.game = game
        self.start_bg_image = pygame.image.load("assets/images/start_bg.jpeg").convert_alpha()
        self.clicking = False
        
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.start_bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display.blit(scaled_bg, (0, 0))

    # tombol start
    def draw_clickable_rectangle(self, x, y, width, height, active_color, inactive_color):
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()  
        pygame.draw.rect(self.display, inactive_color, (x, y, width, height))
        
        key = pygame.key.get_pressed()

        # memeriksa apakah mouse udah di area rect
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.display, active_color, (x, y, width, height))
            
            if click[0] == 1: 
                if self.game.robot_1 is not None and self.game.robot_2 is not None:
                    self.gameStateManager.set_state('arena')
                else:
                    print("Select both robots")

    # UI ROBOT 1
    def draw_robot_gui(self, x, y, width, height, active_color, inactive_color, robot):
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()  
        pygame.draw.rect(self.display, inactive_color, (x, y, width, height))
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.display, active_color, (x, y, width, height))
            

            if click[0] == 1 and not self.clicking:
                self.clicking = True
                if self.game.robot_1 is None:
                    self.game.robot_1 = robot(1, 200, 340)
                    print("Player 1: RobotA1 selected")
                elif self.game.robot_2 is None:
                    self.game.robot_2 = robot(2, 700, 340)
                    print("Player 2: RobotA1 selected")
            elif click[0] == 0:
                self.clicking = False
        

    def run(self):
        self.draw_bg()
        self.draw_robot_gui(50, 90, 250, 320, RED, WHITE, RobotA1)
        self.draw_robot_gui(380, 90, 250, 320, RED, WHITE, RobotA2)
        self.draw_robot_gui(700, 90, 250, 320, RED, WHITE, RobotA3)
        self.draw_clickable_rectangle(350, 500, 300, 50, LIGHT_BLUE, RED)
        if self.game.robot_1 is None:
            screen.blit(text_select_p1, (380, 20))
        elif self.game.robot_1 is not None and self.game.robot_2 is None:
            screen.blit(text_select_p2, (380, 20))
        elif self.game.robot_1 is not None and self.game.robot_2 is not None:
            screen.blit(text_start_game, (380, 20))
            
            


# scene buatt tempurrrr
class Battle:
    def __init__(self, display, gameStateManager, game):
        self.display = display
        self.gameStateManager = gameStateManager
        self.game = game
        self.bg_image = pygame.image.load("assets/images/bg.jpeg").convert_alpha()

    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display.blit(scaled_bg, (0, 0))

    def draw_health_bar(self, health, total_health, x, y):
        ratio = health / total_health
        pygame.draw.rect(self.display, RED, (x, y, 400, 30))
        pygame.draw.rect(self.display, YELLOW, (x, y, ratio * 400, 30))

    def run(self):
        self.draw_bg()
        if self.game.robot_1 and self.game.robot_2:
            self.draw_health_bar(self.game.robot_1.current_health, game.robot_1.total_health,20, 20)
            self.draw_health_bar(self.game.robot_2.current_health, game.robot_2.total_health, 580, 20)

            self.game.robot_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, self.display, self.game.robot_2)
            self.game.robot_1.draw(self.display)
            self.game.robot_2.draw(self.display)
        else:
            print("Robots are not set")


class WinScene():
    def __init__(self, display, gameStateManager, winner):
        self.display = display
    
    def draw_bg(self):
        self.display.blit(WHITE, (0, 0))
        
    def display_text(self):
        if(winner == 1):
            self.display.blit(text_player_1_win, 0, 0)
        elif(winner == 2):
            self.display.blit(text_player_2_win, 0, 0)
        
    # def restart_button(self, x, y, width, height, active_color, inactive_color):
    #     mouse = pygame.mouse.get_pos()  
    #     click = pygame.mouse.get_pressed()  
    #     pygame.draw.rect(self.display, inactive_color, (x, y, width, height))
        
    #     if x + width > mouse[0] > x and y + height > mouse[1] > y:
    #         pygame.draw.rect(self.display, active_color, (x, y, width, height))
            

    #         if click[0] == 1 and not self.clicking:
    #             self.clicking = True
    #             if self.game.robot_1 is None:
    #                 self.game.robot_1 = robot(1, 200, 340)
    #                 print("Player 1: RobotA1 selected")
    #             elif self.game.robot_2 is None:
    #                 self.game.robot_2 = robot(2, 700, 340)
    #                 print("Player 2: RobotA1 selected")
    #         elif click[0] == 0:
    #             self.clicking = False
            
    def run(self):
        self.draw_bg()
        self.display_text()
        
    
        
        
        


if __name__ == '__main__':
    game = Game()
    game.run()
