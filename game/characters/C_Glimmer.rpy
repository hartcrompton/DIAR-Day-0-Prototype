#Glimmer

default beat_Glimmer = 1

label conv_Glimmer:
    scene mixedmedia_bg
    show glimmer at right
    p "You're talking to me, the Glimmer!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Glimmer
        "[[Use an action.]" if actions > 0 and beat_Glimmer < 7:
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
            jump expression "conv_Glimmer" + "." + "beat" + "%d" % beat_Glimmer
        "No, not really.":
            p "Understandable."
            jump conv_Glimmer
    return

label .beat1:
    p "This is the first beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer < 6: d_Glimmer + 1
            jump conv_Glimmer
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer > 0: d_Glimmer - 1
            jump conv_Glimmer
    return
label .beat2:
    p "This is the second beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer < 6: d_Glimmer + 1
            jump conv_Glimmer
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer > 0: d_Glimmer - 1
            jump conv_Glimmer
    return
label .beat3:
    p "This is the third beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer < 6: d_Glimmer + 1
            jump conv_Glimmer
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer > 0: d_Glimmer - 1
            jump conv_Glimmer
    return
label .beat4:
    p "This is the fourth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer < 6: d_Glimmer + 1
            jump conv_Glimmer
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer > 0: d_Glimmer - 1
            jump conv_Glimmer
    return
label .beat5:
    p "This is the fifth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer < 6: d_Glimmer + 1
            jump conv_Glimmer
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer > 0: d_Glimmer - 1
            jump conv_Glimmer
    return
label .beat6:
    p "This is the sixth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer < 6: d_Glimmer + 1
            jump conv_Glimmer
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer > 0: d_Glimmer - 1
            jump conv_Glimmer
    return
label .beat7:
    p "This is the seventh and final beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer < 6: d_Glimmer + 1
            jump conv_Glimmer
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Glimmer += 1
            $ if d_Glimmer > 0: d_Glimmer - 1
            jump conv_Glimmer
    return