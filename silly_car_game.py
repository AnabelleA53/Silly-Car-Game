import random

#variables
command = ''
started = False
driving = False
random_number = 0
end_reached = False

#define functions
def start_car(): #start the car
    print('Car started... Ready to go!')
    
def stop_car(): #stop the car
    if started:
        print('Car stopped...')
    else:
        print("You can't stop a car that isn't driving! Start the car first!")
        
def drive_forward(): #drive forward
    if started: 
        print('You drove forward!')
        check()
    else: 
        print("You can't drive a car that hasn't started! Start the car first!")

def drive_backward():
    if started:
        print("You drove backward!")
        check()
    else:
        print("You can't drive a car that hasn't started! Start the car first!")

def turn_left():
    if driving:
        print('You turned left!')
    else:
        print("You can't turn a car that isn't driving! Start driving the car first!")

def turn_right():
    if driving:
        print('You turned right!')
    else:
        print("You can't turn a car that isn't driving! Start driving the car first!")
        
def check():
    if random_number == 23:
        end_1()
    if random_number == 48:
        end_2()
    if random_number == 52:
        end_3()
    if random_number == 81:
        end_4()
        
def end_1():
    print("""
          You got pulled over by the cop for speeding.
          They asked for your license, but you are under 18!!!
          You should not be driving!!!!!!!
          You're sent to juvie on the spot!
          
          Game over.
          """)

def end_2():
    print("""
          You crashed into a light post! Those darned things!
          Unfortunately you're stuck here now. Luckily, someone called the cops for you!
          Unluckily, when they ask for your license, you can't give it to them!
          You're under 18!!! Why are you driving on the road??? You don't even have a permit!!!
          You're sent to juvie on the spot!
          
          Game over.
          """)

def end_3():
    print("""
          You burn a red light and a 16 wheeler comes hurtling your way!!! 
          Your Honda Civic is way too small compared to that!!!
          You see the impact before you can register the pain. It was a quick death.
          
          Game over.
          """)
    
def end_4():
    print("""
          Miraculously, you make it to school right when the 7:30 bell rings.
          Phew! You speed walk to the entrance to get to your first class. 
          A teacher standing at the door gives you a look, almost as if he knew what you were doing, but he doesn't comment.
          Despite the odds being stacked against you, you made it to class on time.
          
          Success! Game over :)
          """)


print("Type 'start' to start the car. Type 'help' for the menu.")
while True:
    command = input('> ').lower()
    if command == 'start':
        started = True
        start_car()
    elif command == 'stop':
        stop_car()
        started = False
    elif command == 'forward':
        driving = True
        random_number = random.randint(1,100) #random.randint()
        drive_forward()
    elif command == 'backward':
        driving = True
        random_number = random.randint(1, 100)
        drive_backward()
    elif command == 'left':
        turn_left()
    elif command == 'right':
        turn_right()
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
        

