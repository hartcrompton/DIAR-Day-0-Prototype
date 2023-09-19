#MonaLisa

default beat_MonaLisa = 1
default MonaHeist = 0
default MonaOnly = 0

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
    m "The famous [pc_name]! You hear more than most. I should expect no less from someone..."
    if pc_work == "gas station attendant":
        m "...who wears the fragrance of petrol and heat-lamp hot dogs with such panache."
    if pc_work == "gig worker":
        m "...as focused and disciplined as a cat at a laser show. All that energy and no goals."
    if pc_work == "bouncer":
        m "...with the resilience and mental agility of a truck tire."
    if pc_work == "\"painter\"":
        m "...so masterful at applying paint. To a wall. Outside."
    if pc_work == "\"procurer\"":
        m "...with a complexion brighter than their future."
    if pc_work == "layabout":
        m "(placeholder) you think you're good at self care, you're a lazy pos."
    m "You realize the enormity of your job, yes? Making something of this rathole?"
    m "I suppose you have your work cut out for you..."
    m "Sunflowers looks good for their age. And the forty-million valuation."
    m "Then there's Theodore, one of the most famous faces here, dozens of copies, and he doesn't want to be seen."
    m "And of course Gilgamesh, mighty hero with a mighty voice. Especially when he's crying."
    m "But now we have you. And your talent for [pc_skill]."
    menu:
        "How do you know all this?":
            m "Being famous gives me me access. And lots of it."
        "You don't have to be so mean.":
            m "These are facts, my friend. Perhaps you read too much from too little."
    m "I know everything, bambinə. I'm everywhere."
    m "If you can see my face, I can see you. "
    m "I saw your whole interview from the admin's tote bag."
    m "You're a clever one."
    m "Maybe you {i}can{/i} get the others to open up. Or calm down."
    if pc_education == "trades":
        m "If you've apprenticed in a trade, you know to be quick, yes? Or you lose a hand."
    if pc_education == "podcasts":
        m "If you enjoy podcasts you must have some capacity for obscure details."
    if pc_education == "art course":
        m "If you've taken an art class you know your instructors know more than you."
    if pc_education == "Da Vinci Code":
        m "If you've read that book you've participated in bad art, at least. It's a start."
    if pc_education == "college credits":
        m "You may lack the ambition to finish school, but you did show up. Consistently."
    if pc_education == "not say":
        m "Not speaking on your education, though... Better to seem quiet and wise than the alternative, no? Worked for me."
    menu:
        "Don't neg me like you want me to fail.":
            m "Great works rot in foreign basements while empires form, fall and forget. That won't be me. Ever."
        "I can be mysterious and enigmatic, too.":
            m "Is that true? {i}Va bene{/i}. Perhaps we can come up with a plan together."
    m "When you're worth my time, we'll talk more. Ciao, {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}."

    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .beat2:
    m "Perhaps a touring exhibit will take me to Italy... Oh, it's you."
    m "Are you playing nice with the others?"
    menu:
        m "Are you playing nice with the others?"
        "I thought you know everything.":
            m "Steal a phone case with my face on it, and I will."
        "What's your problem?":
            m "I don't have a problem. I have a temporary setback."
    m "This is just a layover. More fame, more copies; the better chance I can go home."
    m "The land you see behind me. The family of the person I'm modeled on. The culture that made me."
    m "{i}Repubblica Fiorentina{/i}."
    menu:
        "Bless you?":
            pass
        "What did you call me?":
            pass
    m "Florence. "
    m "...Italy."
    m "I have to get back while it still exists. If my people are wiped out, or borders redrawn... it might be too late."
    pc "That seems... unlikely for Italy."
    m "No? Why is that?"
    menu:
        "Italy's a modern, stable country.":
            m "\"Italy\" is a baby. Born in 1946, and already overtaking my Florence's name in a mere 81 years."
        "Italy has a rich, ancient history.":
            m "So does Palestine. When the dust settles, who will claim that history?"
    m "We are plundered, lost, and re-written every day. But not me. There are millions of me."
    menu:
        "Is it enough if only one returns?":
            m "No. Every copy increases my fame and influence; but originals are different. Special."
        "I thought there were thousands of you.":
            m "Yes, but they're part of me. I'm the original. I matter most."
    m "The copies exist so that I can go home. All art wants to go home."
    menu:
        "What if this place were your home?":
            pass
        "There might be a way...":
            $ MonaHeist = 1
            pass
    m "{i}Non importa, {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. That's enough for now."
    "She should be upset, but you honestly can't tell."
    m "I'm sure you have other duties."
    m "Be seeing you."

    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    jump FreeRoam
    
label .beat3:
    m "I found a use for you. Have you been to the office yet?"
    menu:
        m "I found a use for you. Have you been to the office yet?"
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
    m "{i}Vai{/i}, {i}vai{/i}, go do as I ask like a good little [pc_work]."
    "Minigame of the admin office, random items like mugs, mousepads, are covered or turned around if you click on them they have a pic of ML. Maybe each one says \"phew,\" \"finally\" \"oh, hey\" \"keep going\""

    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam
    
label .beat4:
    m "That is so much better. You did well, once you finally got around to it."
    pc "I've been thinking about your role here, in the museum."
    m "Really? Enlighten me."
    label StayOrGo:
        menu:
            "Stay here, Mona":
                m "What? No. Absolutely not. Why should I?"
                menu:
                    "You have historic, cultural, and scientific value. You're more than where you came from. This could be your home.":
                        m "Fine. You want to squeeze every last coin out of rich donors? Put me at the center of the exhibit."
                        $ MonaOnly = 1
                        jump MonaStay
                    "Let me reconsider.":
                        jump StayOrGo
            "Let's display you with all the other Monas.":
                m "That's so tacky. What will that achieve?"
                menu:
                    "I think it'll make your story more real. Others should hear what you want, rather than guess, right?":
                        m "Interesting. Put me on the promotional material. I want to see how far the story spreads."
                        $ MonaOnly = 0
                        jump MonaStay
                    "Let me reconsider.":
                        jump StayOrGo
            "Let's send you home. Heist-style." if MonaHeist == 1:
                m "A heist? What does that mean?"
                menu:
                    "Yes. I have all the yous in the office, you don't need to be here to tell your story.":
                        m "Really? You'd give up the jewel of your collection like that?"
                        pc "Of course. A little scandal, a little fame, we all get what we want."
                        m "Heist and scandal. Clever, {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}. I knew I saw a little Peruggia in you. Don't break the deal like he did."
                        jump MonaHeist
                    "Let me reconsider.":
                        jump StayOrGo
    label MonaStay:
        #stay lines go here if there are any
        jump MonaEnd
    label MonaHeist:
        #heist lines go here of there are any
        jump MonaEnd
    label MonaEnd:
        m "This will be easy. Let's make it happen."
        pc "One last question before I set it up..."
        pc "What's the secret behind the enigmatic smile?"
        m "It's not the smile. It's the hands."
        m "No one understands me when I don't move my hands."
        
    ####
   
    meta "You have [actions] action(s) left."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam
