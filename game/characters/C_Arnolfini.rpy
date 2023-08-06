#Arnolfini
#This one is funky, needs to get overhauled based on Shane's conv design
default beat_Arnolfini = 1
default d_ArnolfiniLabel = "DEFAULT LABEL"
default end_Arnolfini = 0

label conv_Arnolfini:
    scene museumtod with fade
    show arnolfini at right
    ar "You're talking to me, the Arnolfini!"
    menu:
        "[[Chat a little.]":
            ar "We're chatting a little now!"
            pc "We sure are."
            jump conv_Arnolfini
        "[[Use an action.]" if actions > 0 and beat_Arnolfini <= 4:
            ar "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            ar "See ya"
            jump FreeRoam

label .use_action:
    menu:
        ar "Whoa, sure you want to use an action?"
        "Yeah, why not.":
            call advance_time
            jump expression "conv_Arnolfini" + "." + "Beat" + "%d" % beat_Arnolfini
        "No, not really.":
            ar "Understandable."
            jump conv_Arnolfini
    return

label .Beat1:
    ar "This is the first beat of my story!"
    menu:
        "Path A":
            ar "This is a path A dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
        "Path B":
            ar "This is a path B dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
    return
label .Beat2:
    ar "This is the second beat of my story!"
    menu:
        "Path A":
            ar "This is a path A dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
        "Path B":
            ar "This is a path B dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
    return
label .Beat3:
    ar "This is the third beat of my story!"
    menu:
        "Path A":
            ar "This is a path A dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
        "Path B":
            ar "This is a path B dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
    return
label .Beat4:
    ar "This is the fourth beat of my story!"
    $ end_Arnolfini = 1
    menu:
        "Path A":
            ar "This is a path A dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
        "Path B":
            ar "This is a path B dialogue string."
            ar "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Arnolfini += 1
            jump conv_Arnolfini
    return

label .OutcomeA:
    ar "This is outcome A."
    return

label .OutcomeB:
    ar "This is outcome B."
    return

label .OutcomeU:
    ar "This is the unresolved outcome."
    return