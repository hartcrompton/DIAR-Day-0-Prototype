#Admin

label conv_Admin:
    p "You're talking to me, the Admin! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Admin
        "Bye":
            p "See ya"
            jump free_roam