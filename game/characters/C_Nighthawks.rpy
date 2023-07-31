#Nighthawks

label conv_Nighthawks:
    scene foyer_bg
    show nighthawks at right
    p "You're talking to me, the Nighthawks! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Nighthawks
        "Bye":
            p "See ya"
            jump FreeRoam