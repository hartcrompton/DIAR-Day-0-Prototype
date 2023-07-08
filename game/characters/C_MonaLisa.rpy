#MonaLisa

default beat_MonaLisa = 1

label conv_MonaLisa:
    p "You're talking to me, the MonaLisa!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_MonaLisa
        "[[Use an action.]" if actions > 0 and beat_MonaLisa < 7:
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
            jump expression "conv_MonaLisa" + "." + "beat" + "%d" % beat_MonaLisa
        "No, not really.":
            p "Understandable."
            jump conv_MonaLisa
    return

label .beat1:
    p "This is the first beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa < 6: d_MonaLisa + 1
            jump conv_MonaLisa
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa > 0: d_MonaLisa - 1
            jump conv_MonaLisa
    return
label .beat2:
    p "This is the second beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa < 6: d_MonaLisa + 1
            jump conv_MonaLisa
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa > 0: d_MonaLisa - 1
            jump conv_MonaLisa
    return
label .beat3:
    p "This is the third beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa < 6: d_MonaLisa + 1
            jump conv_MonaLisa
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa > 0: d_MonaLisa - 1
            jump conv_MonaLisa
    return
label .beat4:
    p "This is the fourth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa < 6: d_MonaLisa + 1
            jump conv_MonaLisa
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa > 0: d_MonaLisa - 1
            jump conv_MonaLisa
    return
label .beat5:
    p "This is the fifth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa < 6: d_MonaLisa + 1
            jump conv_MonaLisa
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa > 0: d_MonaLisa - 1
            jump conv_MonaLisa
    return
label .beat6:
    p "This is the sixth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa < 6: d_MonaLisa + 1
            jump conv_MonaLisa
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa > 0: d_MonaLisa - 1
            jump conv_MonaLisa
    return
label .beat7:
    p "This is the seventh and final beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa < 6: d_MonaLisa + 1
            jump conv_MonaLisa
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_MonaLisa += 1
            $ if d_MonaLisa > 0: d_MonaLisa - 1
            jump conv_MonaLisa
    return