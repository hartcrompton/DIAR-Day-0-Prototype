#Arnolfini

default beat_Arnolfini = 1
default d_ArnolfiniLabel = "DEFAULT LABEL"

label conv_Arnolfini:
    scene museumtod with fade
    show arnolfini at right
    ar "You're talking to me, the Arnolfini!"
    menu:
        "[[Chat a little.]":
            ar "We're chatting a little now!"
            pc "We sure are."
            jump conv_Arnolfini
        "[[Use an action.]" if actions > 0 and beat_Arnolfini < 4:
            ar "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            ar "See ya"
            jump free_roam

label .use_action:
    menu:
        ar "Whoa, sure you want to use an action?"
        "Yeah, why not.":
            call advance_time
            jump expression "conv_Arnolfini" + "." + "beat" + "%d" % beat_Arnolfini
        "No, not really.":
            ar "Understandable."
            jump conv_Arnolfini
    return

label .beat1:
    ar "This is the first beat of my story!"
    menu:
        "You rock.":
            ar "That raises my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini < 6: d_Arnolfini + 1
            jump conv_Arnolfini
        "You suck.":
            ar "That lowers my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini > 0: d_Arnolfini - 1
            jump conv_Arnolfini
    return
label .beat2:
    ar "This is the second beat of my story!"
    menu:
        "You rock.":
            ar "That raises my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini < 6: d_Arnolfini + 1
            jump conv_Arnolfini
        "You suck.":
            ar "That lowers my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini > 0: d_Arnolfini - 1
            jump conv_Arnolfini
    return
label .beat3:
    ar "This is the third beat of my story!"
    menu:
        "You rock.":
            ar "That raises my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini < 6: d_Arnolfini + 1
            jump conv_Arnolfini
        "You suck.":
            ar "That lowers my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini > 0: d_Arnolfini - 1
            jump conv_Arnolfini
    return
label .beat4:
    ar "This is the fourth beat of my story!"
    menu:
        "You rock.":
            ar "That raises my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini < 6: d_Arnolfini + 1
            jump conv_Arnolfini
        "You suck.":
            ar "That lowers my disposition."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            $ if d_Arnolfini > 0: d_Arnolfini - 1
            jump conv_Arnolfini
    return