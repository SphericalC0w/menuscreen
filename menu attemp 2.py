import pygame

pygame.init()
running = True
screen = pygame.display.set_mode((1280, 720))
surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Menu screen')
object1 = pygame.Rect((426, 100), (754, 133))
object2 = pygame.Rect((426, 293), (754, 133))
object3 = pygame.Rect((426, 486), (754, 133))
menu_photo = pygame.image.load(r'C:\Users\SphericalCow\Desktop\coding\menu\menu.png')
red = pygame.image.load(r'C:\Users\SphericalCow\Desktop\coding\menu\red.png')
green = pygame.image.load(r'C:\Users\SphericalCow\Desktop\coding\menu\green.png')
blue = pygame.image.load(r'C:\Users\SphericalCow\Desktop\coding\menu\blue.png')
menu1 = False
menu2 = False
menu3 = False
	
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(426, 100, 754, 133))
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(426, 293, 754, 133))
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(426, 486, 754, 133))
screen.blit(menu_photo, (100, 0))
screen.blit(red, (426, 100))
screen.blit(green, (426, 293))
screen.blit(blue, (426, 486))
pygame.display.flip()

while running:
    if pygame.mouse.get_pressed()[0] and object1.collidepoint(pygame.mouse.get_pos()):
        menu1 = True
    if pygame.mouse.get_pressed()[0] and object2.collidepoint(pygame.mouse.get_pos()):
        menu2 = True    
    if pygame.mouse.get_pressed()[0] and object3.collidepoint(pygame.mouse.get_pos()):
        menu3 = True    
   
    if menu1 == True:
        screen.fill((255, 0, 0))
        pygame.display.update()
        break
    if menu2 == True:
        screen.fill((0, 255, 0))
        pygame.display.update()
        break
    if menu3 == True:
        screen.fill((0, 0, 255))
        pygame.display.update()
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
