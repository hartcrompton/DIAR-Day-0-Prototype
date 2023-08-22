#MonaLisa

default beat_MonaLisa = 1

label conv_MonaLisa:
    scene monalisabackground
    show monalisa at right
    menu:
        "Beat [beat_MonaLisa]" if actions > 0 and beat_MonaLisa < 5:
            #m "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            m "See ya"
            jump FreeRoam
        "Reset Beats":
            "Beats reset."
            $ beat_MonaLisa = 1
            jump conv_MonaLisa

label .use_action:
    #menu:
    #    m "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_MonaLisa" + "." + "beat" + "%d" % beat_MonaLisa
    #    "No, not really.":
    #        m "Understandable."
    #        jump conv_MonaLisa
    jump expression "conv_MonaLisa" + "." + "beat" + "%d" % beat_MonaLisa

label .beat1:
    m "Hey [pc_name],"
    if pc_work == "gas station attendant":
        m "(placeholder) you're reliable and low class."
    if pc_work == "gig worker":
        m "(placeholder) you're adventurous and have no goals."
    if pc_work == "bouncer":
        m "(placeholder) you're strong and stupid."
    if pc_work == "\"painter\"":
        m "(placeholder) you're adept and don't belong here."
    if pc_work == "\"procurer\"":
        m "(placeholder) you're clever and broke."
    if pc_work == "layabout":
        m "(placeholder) you think you're good at self care, you're a lazy pos."
    m "You realize the enormity of your job, right?"
    m "Sunflowers looks good for their age, and a forty-million valuation."
    m "And Theodore, one of the most famous faces here and he doesn't want to be seen."
    m "Or Gilgamesh, a great hero of mighty voice; especially when he's crying."
    m "But we have you now. And your talent for [pc_skill]."
    menu:
        "You don't know me.":
            pass
        "You don't have to be so mean.":
            pass
    m "Darling, I know everything. I'm everywhere."
    m "If you can see my face, I can see you."
    m "Maybe you can get the others to open up. Or calm down."
    m "You've got a way with words, at least."
    if pc_education == "trades":
        m "(placeholder) an apprentice might have potential"
    if pc_education == "podcasts":
        m "(placeholder) a podcast fan can collect lots of little tidbits"
    if pc_education == "art course":
        m "(placeholder) you've seen a paintbrush before"
    if pc_education == "Da Vinci Code":
        m "(placeholder) you participate in bad art, at least"
    if pc_education == "college credits":
        m "(placeholder) you show up, but have no ambition"
    if pc_education == "not say":
        m "(placeholder) you know when to shut up"
    m "When you're worth my time, we'll talk more."

    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .beat2:
    m "Perhaps a touring exhibit will take me to Italy... Oh, it's you."
    menu:
        m "Are you playing nice with the others?"
        "I thought you know everything.":
            m "Steal a phone case with my face on it, and I will."
        "What's your problem?":
            m "I don't have a problem. I have a temporary setback."
    m "This is just a layover. More fame, more copies; the better chance I can go home."
    m "All art wants to go home."
    menu:
        "What is home, for you?":
            m "The land you see behind me. The family of the person I'm modeled on. The culture that made me."
        "Where are you trying to go?":
            m "Florence, Italy."
    m "I have to get back while it still exists. If my people are wiped out, or borders redrawn... it might be too late."
    m "This discussion is truly riveting, but I'm sure you have other duties."
    m "Be seeing you."
    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam
    
label .beat3:
    m "Ciao, [pc_name]."
    meta "Player asks how Mona got to be so famous, setting up 3 possible endings."
    m "I found a use for you. Have you been to the office yet?"
    menu:
        "Yes.":
            pass
        "No.":
            pass
        "Why?":
            pass
    m "I used to be able to see the calendar, the computer searches, guests."
    m "Now I can't see anything. I think Charles went crazy and covered all my copies."
    menu:
        "What copies?":
            m "Mugs, posters, mousepads, candy wrappers, memes. I told you, I'm everywhere."
        "You read over people's shoulders?":
            m "Of course I do. Don't you?"
    m "Vai, vai, go do as I ask like a good little [pc_work]."
    meta "Minigame of the admin office, random items like mugs, mousepads, are covered or turned around if you click on them they have a pic of ML. Maybe each one says \"phew,\" \"finally\" \"oh, hey\" \"keep going\""
    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam
label .beat4:
    m "That is so much better. You did well, once you finally got around to it."
    pc "You can't keep talking to people this way and expect them to like you."
    m "No? I have historic and scientific value in addition to cultural cache."
    m "I could make you famous, too. Or the museum. Whichever."
    menu:
        "Make me famous for partying.":
            m "Here's what wat we're gonna do..."
        "Make me rich.":
            m "You want to squeeze every last coin out of rich donors? Put me at the center of the exhibit."
        "Let's send you home.":
            m "Really? Wow. You might have what it takes after all, [pc_name]."
    m "This will be easy. Let's make it happen."
    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam
