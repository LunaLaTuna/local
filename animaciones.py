import pygame, sys
pygame.init()


#Definir colores
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = (0, 0, 255)

size = (800, 500)

#Crear ventana
screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock() #Controlar los frame por segundo
screen.fill(WHITE)  

tiempo_actual = 0
boton_presionado = 0


#Anchp
largo = 80


#Velocidad
speed_x = 50


rojo = 6
azul = 3
verde = 8




while True:
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    
        if event.type == pygame.KEYDOWN:
            boton_presionado = pygame.time.get_ticks()
           
    tiempo_actual = pygame.time.get_ticks()

    pygame.draw.rect(screen, RED, (100, 100, largo, 80))


    

    if tiempo_actual - boton_presionado > 1000:
        
        pygame.draw.rect(screen, BLUE, (100, 200, largo, 80))
       

    if tiempo_actual - boton_presionado > 2000:

        pygame.draw.rect(screen, GREEN, (100, 300, largo, 80))


    if (largo < 400 ):
        largo += speed_x

    else:
        speed_x = 0

    
    
    

##Cuadrado

    #pygame.draw.rect(screen, RED, (100, 100, largo, 80))
    #pygame.draw.rect(screen, BLUE, (200, 200, largo, 80))
    
    print(f"Tiempo actual:{tiempo_actual} Boton presionado: {boton_presionado}")
    pygame.display.flip()
    clock.tick(1)