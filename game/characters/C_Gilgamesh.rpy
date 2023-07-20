#Gilgamesh

default beat_Gilgamesh = 1

label conv_Gilgamesh:
    scene antiquities_bg
    show gilgamesh at right
    p "You're talking to me, the Gilgamesh!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Gilgamesh
        "[[Use an action.]" if actions > 0 and beat_Gilgamesh < 4:
            p "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            p "See ya"
            jump free_roam

label .use_action:
    menu:
        p "Whoa, sure you want to use an action?"
        "Yeah, why not.":
            $ actions = actions - 1
            jump expression "conv_Gilgamesh" + "." + "beat" + "%d" % beat_Gilgamesh
        "No, not really.":
            p "Understandable."
            jump conv_Gilgamesh
    return

label .beat1:
    p "This is the first beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh < 6: d_Gilgamesh + 1
            jump conv_Gilgamesh
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh > 0: d_Gilgamesh - 1
            jump conv_Gilgamesh
    return
label .beat2:
    p "This is the second beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh < 6: d_Gilgamesh + 1
            jump conv_Gilgamesh
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh > 0: d_Gilgamesh - 1
            jump conv_Gilgamesh
    return
label .beat3:
    p "This is the third beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh < 6: d_Gilgamesh + 1
            jump conv_Gilgamesh
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh > 0: d_Gilgamesh - 1
            jump conv_Gilgamesh
    return
label .beat4:
    p "This is the fourth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh < 6: d_Gilgamesh + 1
            jump conv_Gilgamesh
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Gilgamesh += 1
            $ if d_Gilgamesh > 0: d_Gilgamesh - 1
            jump conv_Gilgamesh
    return