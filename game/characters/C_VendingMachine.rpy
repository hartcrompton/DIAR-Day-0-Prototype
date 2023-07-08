#VendingMachine

label conv_VendingMachine:
    p "You're talking to me, the VendingMachine! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_VendingMachine
        "Bye":
            p "See ya"
            jump free_roam