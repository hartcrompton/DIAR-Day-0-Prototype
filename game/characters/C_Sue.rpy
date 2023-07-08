#Sue

label conv_Sue:
    p "You're talking to me, the Sue! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Sue
        "Bye":
            p "See ya"
            jump free_roam