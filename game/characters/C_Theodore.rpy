#Theodore

label conv_Theodore:
    scene fineart_bg
    show theodore at right
    p "You're talking to me, the Theodore! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Theodore
        "Bye":
            p "See ya"
            jump FreeRoam