#Sunflowers

default beat_Sunflowers = 1

label conv_Sunflowers:
    scene mixedmedia_bg
    show sunflowers at right
    p "You're talking to me, the Sunflowers!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Sunflowers
        "[[Use an action.]" if actions > 0 and beat_Sunflowers < 7:
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
            jump expression "conv_Sunflowers" + "." + "beat" + "%d" % beat_Sunflowers
        "No, not really.":
            p "Understandable."
            jump conv_Sunflowers
    return

label .beat1:
    p "This is the first beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers < 6: d_Sunflowers + 1
            jump conv_Sunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers > 0: d_Sunflowers - 1
            jump conv_Sunflowers
    return
label .beat2:
    p "This is the second beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers < 6: d_Sunflowers + 1
            jump conv_Sunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers > 0: d_Sunflowers - 1
            jump conv_Sunflowers
    return
label .beat3:
    p "This is the third beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers < 6: d_Sunflowers + 1
            jump conv_Sunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers > 0: d_Sunflowers - 1
            jump conv_Sunflowers
    return
label .beat4:
    p "This is the fourth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers < 6: d_Sunflowers + 1
            jump conv_Sunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers > 0: d_Sunflowers - 1
            jump conv_Sunflowers
    return
label .beat5:
    p "This is the fifth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers < 6: d_Sunflowers + 1
            jump conv_Sunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers > 0: d_Sunflowers - 1
            jump conv_Sunflowers
    return
label .beat6:
    p "This is the sixth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers < 6: d_Sunflowers + 1
            jump conv_Sunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers > 0: d_Sunflowers - 1
            jump conv_Sunflowers
    return
label .beat7:
    p "This is the seventh and final beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers < 6: d_Sunflowers + 1
            jump conv_Sunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Sunflowers += 1
            $ if d_Sunflowers > 0: d_Sunflowers - 1
            jump conv_Sunflowers
    return