#SoupAndSunflowers

default beat_SoupAndSunflowers = 1

label conv_SoupAndSunflowers:
    scene mixedmedia_bg
    show SoupAndSunflowers at right
    p "You're talking to me, the SoupAndSunflowers!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_SoupAndSunflowers
        "[[Use an action.]" if actions > 0 and beat_SoupAndSunflowers < 4:
            p "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            p "See ya"
            jump FreeRoam

label .use_action:
    menu:
        p "Whoa, sure you want to use an action?"
        "Yeah, why not.":
            $ actions = actions - 1
            jump expression "conv_SoupAndSunflowers" + "." + "beat" + "%d" % beat_SoupAndSunflowers
        "No, not really.":
            p "Understandable."
            jump conv_SoupAndSunflowers
    return

label .beat1:
    p "This is the first beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers < 6: d_SoupAndSunflowers + 1
            jump conv_SoupAndSunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers > 0: d_SoupAndSunflowers - 1
            jump conv_SoupAndSunflowers
    return
label .beat2:
    p "This is the second beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers < 6: d_SoupAndSunflowers + 1
            jump conv_SoupAndSunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers > 0: d_SoupAndSunflowers - 1
            jump conv_SoupAndSunflowers
    return
label .beat3:
    p "This is the third beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers < 6: d_SoupAndSunflowers + 1
            jump conv_SoupAndSunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers > 0: d_SoupAndSunflowers - 1
            jump conv_SoupAndSunflowers
    return
label .beat4:
    p "This is the fourth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers < 6: d_SoupAndSunflowers + 1
            jump conv_SoupAndSunflowers
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_SoupAndSunflowers += 1
            $ if d_SoupAndSunflowers > 0: d_SoupAndSunflowers - 1
            jump conv_SoupAndSunflowers
    return