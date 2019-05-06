import pygame
pygame.init()

win = pygame.display.set_mode((500,500)) #delimita o tamanho da janela aberta

pygame.display.set_caption("Fist Game") #caption da um título ao programa

#load images on Pygame

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.load.image('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.pndg')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 50
y = 450
width = 40
height = 60
vel = 5
red = (255,0,0)
isJump = False
jumpCount = 10
#What frame we are puting on our screen, What direction is our character moving
#A gente tem que saber qual a direção em que o nosso character está movendo
#Ele está movendo?
#Se sim, quantos passos ele está movendo?
left = False
right = False
walkCount = 0

run = True  
while run: #inicia o looping do jogo
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #se clicar no 'xzinho', fecha a aplicação
            run = False #invalida o looping
            
    keys = pygame.key.get_pressed()
    #top left would be (0,0) rigt corner would be (0,500)
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    #it will be a plataform game, so it won't move up and down
    if not(isJump):
        #if keys[pygame.K_UP] and y > vel: 
            #y -= vel
        #cuidado com a inversão de sinais, "<" e ">"
        #if keys[pygame.K_DOWN] and y < 500 - height - vel:
            #y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1 #double jump?

        else:
            isJump = False
            jumpCount = 10
        
    #se deixar sem o fill, eu estarei desenhando um retângulo vermelho pela tela, em vez de criar um movimento     
    win.fill((0,0,0)) #agora isso realmente torna-se um movimento
    pygame.draw.rect(win, red, (x,y,width,height)) #definindo um novo character
    pygame.display.update()

pygame.quit() #fecha o aplicativo
quit() #dá certeza que vai fechar o aplicativo

