import logic
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # Creates screen to play game
clock = pygame.time.Clock() # makes frame rate control
running=True

while running:
    # check if user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("purple")
    
    print("Type 'start' to start the car. Type 'help' for the menu.")
    while True:
        command = input('> ').lower()
        if command == 'start':
            started = True
            logic.start_car()
        elif command == 'stop':
            logic.stop_car()
            started = False
        elif command == 'forward':
            driving = True
            random_number = random.randint(1,100) #random.randint()
            logic.drive_forward()
        elif command == 'backward':
            driving = True
            random_number = random.randint(1, 100)
            logic.drive_backward()
        elif command == 'left':
            logic.turn_left()
        elif command == 'right':
            logic.turn_right()
        elif command == 'help':
            print('''
                start - to start the car
                stop - to stop the car
                forward - drive forward
                backward - drive backward
                left - turn the car left
                right - turn the car right
                quit - to quit the game
                ''')
        elif command == 'quit':
            print('Game quit!')
            break
        else:
            print('This is not a valid command')
        
        pygame.display.flip()
        clock.tick(60) # sets FPS to 60
    pygame.quit()