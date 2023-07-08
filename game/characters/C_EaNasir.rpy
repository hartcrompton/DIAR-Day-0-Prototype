#EaNasir

label conv_EaNasir:
    scene antiquities_bg
    show eanasir at right
    p "You're talking to me, the EaNasir! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_EaNasir
        "Bye":
            p "See ya"
            jump free_roam