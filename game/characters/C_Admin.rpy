#Admin

label conv_Admin:
    scene office_bg
    show admin at right
    ad "You're talking to me, the Admin! I'm a side character!"
    menu:
        "[[Chat a little.]":
            ad "We're chatting a little now!"
            pc "We sure are."
            jump conv_Admin
        "Bye":
            ad "See ya"
            jump FreeRoam