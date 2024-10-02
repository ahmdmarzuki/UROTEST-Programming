class WinScene():
#     def __init__(self, display, winner):
#         self.display = display
    
#     def draw_bg(self):
#         self.display.blit(WHITE, (0, 0))
        
#     def display_text(self):
#         if(winner == 1):
#             self.display.blit(text_player_1_win, 0, 0)
#         elif(winner == 2):
#             self.display.blit(text_player_2_win, 0, 0)
        
#     # def restart_button(self, x, y, width, height, active_color, inactive_color):
#     #     mouse = pygame.mouse.get_pos()  
#     #     click = pygame.mouse.get_pressed()  
#     #     pygame.draw.rect(self.display, inactive_color, (x, y, width, height))
        
#     #     if x + width > mouse[0] > x and y + height > mouse[1] > y:
#     #         pygame.draw.rect(self.display, active_color, (x, y, width, height))
            

#     #         if click[0] == 1 and not self.clicking:
#     #             self.clicking = True
#     #             if self.game.robot_1 is None:
#     #                 self.game.robot_1 = robot(1, 200, 340)
#     #                 print("Player 1: RobotA1 selected")
#     #             elif self.game.robot_2 is None:
#     #                 self.game.robot_2 = robot(2, 700, 340)
#     #                 print("Player 2: RobotA1 selected")
#     #         elif click[0] == 0:
#     #             self.clicking = False
            
#     def run(self):
#         self.draw_bg()
#         self.display_text()