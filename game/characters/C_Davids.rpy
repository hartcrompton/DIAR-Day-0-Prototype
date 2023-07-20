#Davids

default beat_Davids = 1

label conv_Davids:
    scene foyer_bg
    show davids at right
    p "You're talking to me, the Davids!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Davids
        "[[Use an action.]" if actions > 0 and beat_Davids < 4:
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
            jump expression "conv_Davids" + "." + "beat" + "%d" % beat_Davids
        "No, not really.":
            p "Understandable."
            jump conv_Davids
    return

label .beat1:
    p "This is the first beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids < 6: d_Davids + 1
            jump conv_Davids
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids > 0: d_Davids - 1
            jump conv_Davids
    return
label .beat2:
    p "This is the second beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids < 6: d_Davids + 1
            jump conv_Davids
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids > 0: d_Davids - 1
            jump conv_Davids
    return
label .beat3:
    p "This is the third beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids < 6: d_Davids + 1
            jump conv_Davids
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids > 0: d_Davids - 1
            jump conv_Davids
    return
label .beat4:
    p "This is the fourth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids < 6: d_Davids + 1
            jump conv_Davids
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Davids += 1
            $ if d_Davids > 0: d_Davids - 1
            jump conv_Davids
    return