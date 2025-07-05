# Echoes in The Silence -- A simple story game
def intro():
    print("\n-- Echoes In The Silence --\n")
    print("You wake up in a quiet, dimly lit room.")
    print("The air feels still. Your head is heavy, But your heart in calm. ")
    print("What will you do ?")
    print("1. Call out for someone.")
    print("2. Stay silent and Look around")

    choice = input("\nEnter 1 or 2: " )

    if choice == "1":
        path_voice()
    elif choice == "2":
        path_silent()
    else:
        print("Hmm, That's not a valid choice. Try again.. ")
        intro()

def path_voice():
    print("\nYour voice breaks the silence like a glass.")
    print("A shadow stirs. Footsteps... slow , deliberate.")
    print("You feel like someone was waiting for you.")
    print("Do you want to:")
    print("1. Wait for the footsteps to reach you.")
    print("2. Move away from the sound.")

    choice = input("\nEnter 1 or 2:" )

    if choice == "1":
        print("\nA soft voice says, 'I knew you'd speak first.'")
        print("The presence is strangely familiar. You are not alone.")
        #Add more scenes here.
    elif choice =="2":
        print("\nYou slip into the shadows, heart racing. Silence follows.")
        print("\nBut something tells you... It noticed.")
        #Add more scenes here.
    else:
        print("Not quite. Try again.")
        path_voice()

def path_silent():
    print("\nYou stay quiet. Your breathing slows. The walls seem to listen.")
    print("A soft breeze brushes your cheeks-- but the windows are closed.")
    print("You feel like someone was waiting for you.")
    print("Do you:")
    print("1. Follow the breeze.")
    print("2. Sit down and try to remember.")

    choice = input("\nEnter 1 or 2: " )

    if choice == "1":
        print("\nYou walk towards the unknown. Something in you knows the way.")
        #Add more scenes here.
    elif choice =="2":
        print("\nYou sit. Flashes of memory -- Someone smiling. Your hands are shaking.")
        #Add more scenes here.
    else:
        print("Try again.")
        path_silent()

intro()


    