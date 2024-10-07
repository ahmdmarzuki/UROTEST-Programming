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
        
        self.winner = None
        self.winner_sprite = None
        
        # robot attribute
        self.robot_1 = None
        self.robot_2 = None

        self.gameStateManager = GameStateManager('start')

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
        self.clock = pygame.time.Clock()
        
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.start_bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display.blit(scaled_bg, (0, 0))

    # tombol start
    def draw_fight_button(self, x, y, width, height):
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()          

        fight_button = pygame.image.load("assets/UI/fight_button.png")
        fight_button_hovered = pygame.image.load("assets/UI/fight_button_hovered.png")
        
        scaled_fight_button = pygame.transform.scale(fight_button, (width, height))
        scaled_fight_button_hovered = pygame.transform.scale(fight_button_hovered, (width, height))
        
        # buat nampilin fight button
        self.display.blit(scaled_fight_button, (x, y))
        
        key = pygame.key.get_pressed()

        # memeriksa apakah mouse udah di area rect
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            
            # fight button pas di hover
            self.display.blit(scaled_fight_button_hovered, (x, y))
            
            if click[0] == 1: 
                if self.game.robot_1 is not None and self.game.robot_2 is not None:
                    self.gameStateManager.set_state('arena')
                else:
                    print("Select both robots")

    # ROBOT GUI
    def draw_robot_gui(self, x, y, width, height, hovered_img, unselected_img, robot):
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()  
        self.selected = False
        
        self.unselected_gui = pygame.image.load(unselected_img).convert_alpha()
        self.hovered_gui = pygame.image.load(hovered_img).convert_alpha()
        
        scaled_unselected_gui = pygame.transform.scale(self.unselected_gui, (width, height))
        scaled_hovered_gui = pygame.transform.scale(self.hovered_gui, (width, height))
        
        
        self.display.blit(scaled_unselected_gui, (x, y))
            
            
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            
            self.display.blit(scaled_hovered_gui, (x, y)) 
            
            if click[0] == 1 and not self.clicking:
                self.clicking = True
                self.selected = True
                self.display.blit(scaled_hovered_gui, (x, y)) 
                print(self.selected)
                if self.game.robot_1 is None:
                    self.game.robot_1 = robot(1, 200, 340)
                    print("Player 1: RobotA1 selected")
                    print(game.robot_1)
                    
                elif self.game.robot_2 is None:
                    self.game.robot_2 = robot(2, 700, 340)
                    print("Player 2: RobotA1 selected")
                    print(game.robot_2)
                     
            elif click[0] == 0:
                self.clicking = False
        

    def run(self):
        self.draw_bg()
        self.draw_robot_gui(50, 90, 250, 320, "assets/UI/robot_1_gui_hovered.png", "assets/UI/robot_1_gui_unselected.png", RobotA1)
        self.draw_robot_gui(380, 90, 250, 320, "assets/UI/robot_2_gui_hovered.png", "assets/UI/robot_2_gui_unselected.png", RobotA2)
        self.draw_robot_gui(700, 90, 250, 320, "assets/UI/robot_3_gui_hovered.png", "assets/UI/robot_3_gui_unselected.png", RobotA3)
        
        if self.game.robot_1 is None:
            screen.blit(text_select_p1, (380, 20))
        elif self.game.robot_1 is not None and self.game.robot_2 is None:
            screen.blit(text_select_p2, (380, 20))
        elif self.game.robot_1 is not None and self.game.robot_2 is not None:
            screen.blit(text_start_game, (380, 20))
            self.draw_fight_button(350, 470, 300, 80)
            
        pygame.display.update()
        self.clock.tick(FPS)
            
            


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
            self.game.robot_2.move_p2(SCREEN_WIDTH, SCREEN_HEIGHT, self.display, self.game.robot_1)
            self.game.robot_2.draw(self.display)
        else:
            print("Robots are not set")
            
        if (self.game.robot_1.current_health <= 0 or self.game.robot_2.current_health <= 0):

            self.gameStateManager.set_state('win_scene')
    
            if (self.game.robot_1.current_health <= 0):
                self.game.winner = 2
                self.game.winner_sprite = self.game.robot_2.image
            
            elif (self.game.robot_2.current_health <= 0):
                self.game.winner = 1
                self.game.winner_sprite = self.game.robot_1.image
                
            # print(self.game.winner_sprite)
            
            


class WinScene():
    def __init__(self, display, gameStateManager, game):
        self.display = display
        self.bg_image = pygame.image.load("assets/images/winscene_bg.jpeg").convert_alpha()
        self.game = game
        self.gameStateManager = gameStateManager
    
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display.blit(scaled_bg, (0, 0))
        
    def display_text(self):
        if(self.game.winner == 1):
            self.display.blit(text_player_1_win, (420, 50))
            print(winner)
        elif(self.game.winner == 2):
            self.display.blit(text_player_2_win, (420, 50))
            print(winner)
            
    def display_winner_sprite(self):
        scaled_sprite = pygame.transform.scale(self.game.winner_sprite, (150, 150))
        self.display.blit(scaled_sprite, (425, 110))
        
    def rematch_button(self, x, y, width, height):
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()  
        
        rematch_button = pygame.image.load("assets/UI/rematch_button.png")
        rematch_button_hovered = pygame.image.load("assets/UI/rematch_button_hovered.png")
        
        scaled_rematch_button = pygame.transform.scale(rematch_button, (width, height))
        scaled_rematch_button_hovered = pygame.transform.scale(rematch_button_hovered, (width, height))
        
        self.display.blit(scaled_rematch_button, (x, y))
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            self.display.blit(scaled_rematch_button_hovered, (x, y))
            
            if click[0] == 1:
                self.game.robot_1.current_health =  self.game.robot_1.total_health
                self.game.robot_2.current_health =  self.game.robot_2.total_health
                self.game.robot_1.rect.x = 200
                self.game.robot_2.rect.x = 700
                self.game.robot_1.rect.y = 340
                self.game.robot_2.rect.y = 340
                self.gameStateManager.set_state('arena')
                
                # if self.game.robot_1 is not None and self.game.robot_2 is not None:
                # else:
                #     print("Select both robots")
        
        
    
        
    def restart_button(self, x, y, width, height, active_color, inactive_color):
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed() 
        clicking = False
        
        restart_button = pygame.image.load("assets/UI/restart_button.png")
        restart_button_hovered = pygame.image.load("assets/UI/restart_button_hovered.png")
        
        scaled_restart_button = pygame.transform.scale(restart_button, (width, height))
        scaled_restart_button_hovered = pygame.transform.scale(restart_button_hovered, (width, height))
        
        self.display.blit(scaled_restart_button, (x, y))
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            self.display.blit(scaled_restart_button_hovered, (x, y))
            
            if click[0] == 1:
                self.gameStateManager.set_state('start')
                self.game.robot_1 = None
                self.game.robot_2 = None
                self.game.winner = None
                self.game.winner_sprite = None
            
    def run(self):
        self.draw_bg()
        self.display_text()
        self.display_winner_sprite()
        self.rematch_button(350, 350, 300, 80)
        self.restart_button(350, 450, 300, 80, WHITE, RED)
    
        
    


if __name__ == '__main__':
    game = Game()
    game.run()
