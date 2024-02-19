import time

def intro():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious house...")
    time.sleep(2)
    print("You need to find your way out before it's too late!\n")
    time.sleep(2)

def choose_path():
    print("You stand at a crossroads.")
    print("There are two paths in front of you: left or right.")
    choice = input("Which path will you choose? (left/right): ").lower()
    if choice == "left":
        print("\nYou chose the left path.")
        left_path()
    elif choice == "right":
        print("\nYou chose the right path.")
        right_path()
    else:
        print("\nInvalid choice! Please enter 'left' or 'right'.")
        choose_path()

def left_path():
    print("\nYou follow the left path and arrive in a dark room.")
    print("You see a table with a candle and a key on it.")
    time.sleep(2)
    print("What will you do?")
    choice = input("1. Light the candle\n2. Take the key\nChoose 1 or 2: ")
    if choice == "1":
        print("\nYou light the candle and see a door at the other end of the room.")
        time.sleep(2)
        print("You move towards the door...")
        time.sleep(2)
        print("Congratulations! You escaped the house!")
    elif choice == "2":
        print("\nYou take the key and suddenly the room starts shaking.")
        time.sleep(2)
        print("The ceiling collapses and you're trapped!")
        time.sleep(2)
        print("Game Over!")
    else:
        print("\nInvalid choice! Please enter '1' or '2'.")
        left_path()
def right_path():
    print("\nYou follow the right path and arrive in a dusty library.")
    print("You see a bookshelf and a staircase leading upwards.")
    time.sleep(2)
    print("What will you do?")
    choice = input("1. Search the bookshelf\n2. Climb the staircase\nChoose 1 or 2: ")
    if choice == "1":
        print("\nYou search the bookshelf and find a secret passage behind it.")
        time.sleep(2)
        print("You enter the passage and find yourself outside the house.")
        time.sleep(2)
        print("Congratulations! You escaped the house!")
    elif choice == "2":
        print("\nYou climb the staircase and hear a loud noise above.")
        time.sleep(2)
        print("Suddenly, the staircase collapses and you fall into darkness.")
        time.sleep(2)
        print("Game Over!")
    else:
        print("\nInvalid choice! Please enter '1' or '2'.")
        right_path()

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
