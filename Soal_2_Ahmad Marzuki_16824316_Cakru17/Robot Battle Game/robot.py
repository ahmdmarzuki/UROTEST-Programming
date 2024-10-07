import pygame # type: ignore


current_time = pygame.time.get_ticks()

# ROBOT 1
class RobotA1():
    def __init__(self, player, x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 130 , 130))
        
        self.image = pygame.image.load("assets/Character/robot_1.png")  # Load sprite
        self.scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))  # Rescale sprite
        
        self.vel_y = 0
        self.attacking = False
        self.attack_type = 0
        self.current_health = 80
        self.total_health = 80
        self.damage = 8
        self.player = player
        self.last_attack_time = 0
        self.attack_delay = 200
        
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        JUMP_HEIGHT = 30
        dx = 0
        dy = 0
        
        # get key pressed
        key = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()
        
        current_time = pygame.time.get_ticks()
    
        # movement
        if key[pygame. K_a]:
            dx = -SPEED
        if key[pygame. K_d]:
            dx = SPEED
        
        # biar bisa loncat loncat aeokaka
        if self.rect.bottom + dy >= screen_height - 80:
            if key[pygame. K_w]:
                self.vel_y = -JUMP_HEIGHT
        # attack
        if click[0] == 1 and current_time - self.last_attack_time >= self.attack_delay:
            self.last_attack_time = current_time
            self.attack(surface, target)
            print("attacking")
        else:
            self.attacking = False
        
        # pastikan player berhadapan
        if target.rect > self.rect:
            self.flip = False
        else:
            self.flip = True
        
        self.vel_y += GRAVITY
        dy += self.vel_y
            
            
        # biar player ga keluar frame
        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.bottom + dy > screen_height - 80:
            self.vel_y = 0
            dy = screen_height - 80 - self.rect.bottom
            
            
        # update posisi robot
        self.rect.x += dx
        self.rect.y += dy
        
        
    def move_p2(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        JUMP_HEIGHT = 30
        dx = 0
        dy = 0
        
        # get key pressed
        key = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()
        
        current_time = pygame.time.get_ticks()
    
        # movement
        if key[pygame. K_LEFT]:
            dx = -SPEED
        if key[pygame. K_RIGHT]:
            dx = SPEED
        
        # biar bisa loncat loncat aeokaka
        if self.rect.bottom + dy >= screen_height - 80:
            if key[pygame. K_UP]:
                self.vel_y = -JUMP_HEIGHT
        # attack
        if key[pygame. K_DOWN] and current_time - self.last_attack_time >= self.attack_delay:
            self.last_attack_time = current_time
            self.attack(surface, target)
            print("attacking")
        else:
            self.attacking = False
        
        # pastikan player berhadapan
        if target.rect > self.rect:
            self.flip = False
        else:
            self.flip = True
        
        self.vel_y += GRAVITY
        dy += self.vel_y
            
            
        # biar player ga keluar frame
        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.bottom + dy > screen_height - 80:
            self.vel_y = 0
            dy = screen_height - 80 - self.rect.bottom
            
            
        # update posisi robot
        self.rect.x += dx
        self.rect.y += dy
    
    
    def attack(self, surface, target):
        # self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)

            
        if attacking_rect.colliderect(target.rect):
            print(target.current_health)
            target.current_health -= 10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            

    def draw(self, surface):
        # pygame.draw.rect(surface, (255, 225, 0), self.rect)
        surface.blit(pygame.transform.flip(self.scaled_image, self.flip, False), (self.rect.x, self.rect.y))

        
        
# ROBOT 2  
class RobotA2():
    def __init__(self, player, x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 130 , 130))
        
        self.image = pygame.image.load("assets/Character/robot_1.png")  # Load sprite
        self.scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))  # Rescale sprite

        self.vel_y = 0
        self.attacking = False
        self.attack_type = 0
        self.current_health = 100
        self.total_health = 100
        self.damage = 6
        self.player = player
        self.last_attack_time = 0
        self.attack_delay = 200
        
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        JUMP_HEIGHT = 30
        dx = 0
        dy = 0
        
        # get key pressed
        key = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()
        
        current_time = pygame.time.get_ticks()
    
        # movement
        if key[pygame. K_a]:
            dx = -SPEED
        if key[pygame. K_d]:
            dx = SPEED
        
        # biar bisa loncat loncat aeokaka
        if self.rect.bottom + dy >= screen_height - 80:
            if key[pygame. K_w]:
                self.vel_y = -JUMP_HEIGHT
        # attack
        if click[0] == 1 and current_time - self.last_attack_time >= self.attack_delay:
            self.last_attack_time = current_time
            self.attack(surface, target)
            print("attacking")
        else:
            self.attacking = False
        
        # pastikan player berhadapan
        if target.rect > self.rect:
            self.flip = False
        else:
            self.flip = True
        
        self.vel_y += GRAVITY
        dy += self.vel_y
            
            
        # biar player ga keluar frame
        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.bottom + dy > screen_height - 80:
            self.vel_y = 0
            dy = screen_height - 80 - self.rect.bottom
            
            
        # update posisi robot
        self.rect.x += dx
        self.rect.y += dy
        
    def move_p2(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        JUMP_HEIGHT = 30
        dx = 0
        dy = 0
        
        # get key pressed
        key = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()
        
        current_time = pygame.time.get_ticks()
    
        # movement
        if key[pygame. K_LEFT]:
            dx = -SPEED
        if key[pygame. K_RIGHT]:
            dx = SPEED
        
        # biar bisa loncat loncat aeokaka
        if self.rect.bottom + dy >= screen_height - 80:
            if key[pygame. K_UP]:
                self.vel_y = -JUMP_HEIGHT
        # attack
        if key[pygame. K_DOWN] and current_time - self.last_attack_time >= self.attack_delay:
            self.last_attack_time = current_time
            self.attack(surface, target)
            print("attacking")
        else:
            self.attacking = False
        
        # pastikan player berhadapan
        if target.rect > self.rect:
            self.flip = False
        else:
            self.flip = True
        
        self.vel_y += GRAVITY
        dy += self.vel_y
            
            
        # biar player ga keluar frame
        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.bottom + dy > screen_height - 80:
            self.vel_y = 0
            dy = screen_height - 80 - self.rect.bottom
            
            
        # update posisi robot
        self.rect.x += dx
        self.rect.y += dy
    
    
    def attack(self, surface, target):
        # self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)

            
        if attacking_rect.colliderect(target.rect):
            print(target.current_health)
            target.current_health -= 10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            

    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.scaled_image, self.flip, False), (self.rect.x, self.rect.y))

        
        
# ROBOT 3
class RobotA3():
    def __init__(self, player, x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 130 , 130))
        
        self.image = pygame.image.load("assets/Character/robot_1.png")  # Load sprite
        self.scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))  # Rescale sprite

        self.vel_y = 0
        self.attacking = False
        self.current_health = 120
        self.total_health = 120
        self.player = player
        self.damage = 4
        self.last_attack_time = 0
        self.attack_delay = 200  
        
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        JUMP_HEIGHT = 30
        dx = 0
        dy = 0
        
        # get key pressed
        key = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()
        
        
        
        current_time = pygame.time.get_ticks()
        
        
    
        # movement
        if key[pygame. K_a]:
            dx = -SPEED
        if key[pygame. K_d]:
            dx = SPEED
        
        # biar bisa loncat loncat aeokaka
        if self.rect.bottom + dy >= screen_height - 80:
            if key[pygame. K_w]:
                self.vel_y = -JUMP_HEIGHT
        # attack
        if click[0] == 1 and current_time - self.last_attack_time >= self.attack_delay:
            self.last_attack_time = current_time
            self.attack(surface, target)
            print("attacking")
        
        # pastikan player berhadapan
        if target.rect > self.rect:
            self.flip = False
        else:
            self.flip = True
        
        self.vel_y += GRAVITY
        dy += self.vel_y
            
            
        # biar player ga keluar frame
        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.bottom + dy > screen_height - 80:
            self.vel_y = 0
            dy = screen_height - 80 - self.rect.bottom
            
            
        # update posisi robot
        self.rect.x += dx
        self.rect.y += dy
        
    def move_p2(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        JUMP_HEIGHT = 30
        dx = 0
        dy = 0
        
        # get key pressed
        key = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()
        
        current_time = pygame.time.get_ticks()
    
        # movement
        if key[pygame. K_LEFT]:
            dx = -SPEED
        if key[pygame. K_RIGHT]:
            dx = SPEED
        
        # biar bisa loncat loncat aeokaka
        if self.rect.bottom + dy >= screen_height - 80:
            if key[pygame. K_UP]:
                self.vel_y = -JUMP_HEIGHT
        # attack
        if key[pygame. K_DOWN] and current_time - self.last_attack_time >= self.attack_delay:
            self.last_attack_time = current_time
            self.attack(surface, target)
            print("attacking")
        else:
            self.attacking = False
        
        # pastikan player berhadapan
        if target.rect > self.rect:
            self.flip = False
        else:
            self.flip = True
        
        self.vel_y += GRAVITY
        dy += self.vel_y
            
            
        # biar player ga keluar frame
        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.bottom + dy > screen_height - 80:
            self.vel_y = 0
            dy = screen_height - 80 - self.rect.bottom
            
            
        # update posisi robot
        self.rect.x += dx
        self.rect.y += dy
    
    
    def attack(self, surface, target):
        # self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)

            
        if attacking_rect.colliderect(target.rect):
            print(target.current_health)
            target.current_health -= self.damage
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            

    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.scaled_image, self.flip, False), (self.rect.x, self.rect.y))
