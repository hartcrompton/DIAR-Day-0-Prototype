#Poster

label conv_Poster:
    p "You're talking to me, the Poster! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Poster
        "Bye":
            p "See ya"
            jump free_roam