#MonaLisa

default beat_MonaLisa = 1
default MonaHeist = 0
default MonaOnly = 0
default MonaOutcome = 0

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
    call advance_time
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
        m "...so clever, and daring -- and broke."
    if pc_work == "layabout":
        m "...with enough blistering drive to spend {i}an entire{/i} day doing nothing."
    m "You realize the enormity of your job, yes? Making something of this rathole?"
    menu:
        "Excuse you, this museum is beautiful.":
            pass
        "Yeah, this'll be an uphill battle.":
            pass
    m "I suppose you have your work cut out for you..."
    pc "Do you have any advice?"
    menu:
        "You're the only piece I recognize.":
            pass
        "What's going on with the others?":
            pass
    m "Hm... Sunflowers looks good for their age. And the forty-million valuation."
    #theo might not make it into the finalversion
    m "Then there's Theodore, one of the most famous faces here, dozens of copies, and he doesn't want to be seen."
    m "And of course Gilgamesh, mighty hero with a mighty voice. Especially when he's crying."
    m "But now we have you, the [pc_work]. And your talent for [pc_skill]."
    menu:
        "How do you know all this?":
            m "I'm over five-hundred years old and famous. That comes with access."
        "You don't have to be so mean.":
            m "These are facts, my friend. Perhaps you read too much from too little."
    m "I'm everywhere, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. If you can see my face, I can see you." 
    m "That crumpled brochure in the corner had my face on it. I saw the rest of your interview from there."
    m "You're clever. Maybe you {i}can{/i} get the others to open up. Or calm down."
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
        m "Not answering about your education, though... Better to seem quiet and wise than the alternative, no? Worked for me."
    menu:
        "Don't neg me like you want me to fail.":
            m "Fail? {i}Ma, no {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. I wish I could move my hands as you can -- maybe I'd be understood, then."
        "I can be mysterious and enigmatic, too.":
            $ MonaHeist = 1
            m "If I could move my hands you'd know exactly what I'm trying to say. "
    m "This museum is the last stop on my way home. But I see you're just like the others."
    m "Come back when you're ready to listen, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}. Ciao.{/i}"
    "She seems upset, but you honestly can't tell."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .beat2:
    m "Perhaps a touring exhibit will take me closer to Floren-- Oh, it's you."
    m "Are you playing nice with the others?"
    menu:
        "I thought you know everything.":
            m "Steal a phone case with my face on it, and I will."
        "How can you leave when you can't move?":
            m "Someone could carry me. It almost worked in 1911."
            m "The more copies there were of me, the more of the world I saw. What happens to art, good and bad."
    m "The problem is PR. Spin. Cake tried to do to me what Soup's doing to Sunflowers -- they're in the trash now."
    menu:
        "You got splattered with cake?":
            m "Well, frosting. Someone threw a mug at me, once. And acid, before that."
        "Your copies are how you see the world?":
            m "Yes. I don't know how it began, but I found myself in museums everywhere. Listening to other works."
            m "Some of us miss the smells and sounds of the place we were created. I had almost forgotten..."
            m "{i}Repubblica Fiorentina.{/i}"
            menu:
                "Bless you?":
                    pass
                "What did you call me?":
                    pass
    m "Florence."
    m "...Italy."
    m "I want to return to my city. If the sea rises or the maps change again... it might be too late."
    pc "I doubt Italy's going to change much."
    m "No? Why do you think that?"
    menu:
        "Italy's a modern, wealthy country.":
            m "\"Italy\" is a baby. Born in 1946, and it overtook my Florence in a mere eighty-one years."
        "Italy has a rich, ancient history.":
            m "Borders shift constantly. A new school of thought here, a treaty or a madmen in power there -- poof."
    #line might be a little vague
    m "Others have made it home despite being plundered, or broken, or forgotten in storage."
    menu:
        "How did you wind up in France?":
            m "Da Vinci passed from this world and his apprentice sold me to the French king."
        "There must be Mona Lisas in Florence now.":
            m "Yes, but they're only part of me. I'm the original. I matter the most."
    m "The more copies, the more I saw. The more I missed my home. That changed everything."
    menu:
        "How does that work?":
            m "Every time I'm studied or made into a joke, I'm there. I smile, people see what they want to see, and I see them."
        "How did you wind up here?":
            m "The first time I was \"stolen\" the press found out and I was sent back to the Louvre."
    m "When I'm on the news I see into people's homes. From gift shops, I hear other artworks."
    m "Shiva Nataraja went back to India in 2014. Skanda returned to Cambodia in 2021. They seemed alive again."
    menu:
        "You see out from the TV? Creepy.":
            pass
        "All the printouts are still you, that's fascinating!":
            pass
    m "I know. You can't know what it's like to smell your own food and hear your own language after so long."
    menu:
        "Home is where you decide to stay.":
            m "Do you really believe that?"
        "\"The Many Monas\" is a story worth telling.":
            m "A story worth telling, but not worth taking action? {i}Che palle...{/i}"
        "Maybe a fake scandal could help the museum?":
            $ MonaHeist = 1
            m "It would have to be the {i}right{/i} scandal or I'll get stuck here. Or locked up even tighter."
    m "{i}Non importa, {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. I'm sure you have other duties."
    m "Be seeing you."

    $ beat_MonaLisa += 1
    jump FreeRoam
    
label .beat3:
    m "Where have you been? I can't see you anywhere."
    menu:
        "I need to have {i}some{/i} privacy!":
            pass
        "Calm down, I'm right here.":
            pass
    m "I'm not upset. Do I look upset? The office is completely dark. Have you been there yet?"
    menu:
        "Yes.":
            pass
        "No.":
            pass
        "Why?":
            pass
    m "I don't trust the Admin to run the gala. I used to be able to see the calendar, the computer searches, guests."
    m "Now I can't see anything. I think Charles went crazy and covered all my copies."
    menu:
        "What copies?":
            m "Mugs, posters, mousepads, candy wrappers, memes. I told you, I'm everywhere."
        "You read over people's shoulders?":
            m "Of course I do. It's my greatest talent at this point."
    m "{i}Vai, vai,{/i} go fix things in the office like a good little [pc_work] so I can see."

    call minigamestart_office

    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam
    
label .beat4:

    m "I knew it. The admin is ruining the gala. No idea who to invite, where to promote the event, nothing!"
    menu:
        "Why do you care about the gala?":
            pass
        "I thought you wanted to leave this \"rathole.\"":
            pass
    m "If we convince the right people to attend, we all benefit."
    #oh I see, Mona wants to invite someone that will steal her
    m "You keep your job, my fame increases, and then someone will finally walk me out of here."
    pc "That's too risky."
    m "Do you have a better plan?"
    label MonaOutcomeChoice:
    menu:
        "Yes. You should stay here.":
            m "What? No. Absolutely not. Why should I?"
            menu:
                "You have historic, cultural, and scientific value. You're more than where you came from. This could be your home.":
                    $ MonaOutcome = 0
                    m "What's in it for me?"
                    pc "You stay for a season, and if you want to go home, I'll set aside funds to send you."
                    m "Fine. Put me at the center of the exhibit. We'll squeeze every last cent out of these rich donors."
                "Let me reconsider.":
                    jump MonaOutcomeChoice
        "Let's display you with all the other Monas.":
            m "That's so tacky. What will that achieve?"
            menu:
                "It'll make your story more real. Others should hear what you want rather than guess, right?":
                    m "Interesting. Put me on the promotional material. I want to see how far the story spreads."
                    $ MonaOutcome = 1
                "Let me reconsider.":
                    jump MonaOutcomeChoice
        "It's too risky for \"someone\" to walk you out of here. I can do it. Heist-style." if MonaHeist == 1:
            m "Oh, I see! What did you have in mind?"
            menu:
                "Yes. I have all the other Monas from the office, they'll highlight your absence.":
                    $ MonaOutcome = 2
                    m "Really? You'd give up the jewel of your collection like that?"
                    pc "Of course. A little scandal, a little fame, we all get what we want."
                    m "Heist and scandal. Clever, {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}. I knew I saw a little Peruggia in you. Don't break the deal like he did."
                "Let me reconsider.":
                    jump MonaOutcomeChoice
    m "This will be easy. Let's make it happen."
    pc "One last question before I set it up..."
    pc "What's the secret behind the enigmatic smile?"
    m "It's not the smile. It's the hands."
    m "No one understands me when I don't move my hands."
    "Following lines play during the ending:"
    if MonaOutcome == 0:
        "The Mona Lisa brings cultural, historical, and scientific legitimacy to the exhibit; a diminutive diva starring in an underground gala."
        "Nothing to do with the mailers in the invitees's homes, gathering intelligence on what rhey want to see. of course not."
    if MonaOutcome == 1:
        "A dozen enigmatic smiles, a dozen landscapes, the Mona Lisa tells her story..."
        "...Blending high and low art, the past and the present, and a small museum's place in a larger conversation."
        "Visitors leave with new perspective on gaze, surveillance, and what it cost us to get here."
    if MonaOutcome == 2:
        "News outlets light up all over the globe: Miss Mona Missing from Minor Museum!"
        "Not since Peruggia stole the painting in 1911 have crowds swarmed this spot; now taking selfies with the empty space she left behind."
        "In the background, a dozen smiles, distant and satisfied, as though some part of her finally returned home."

    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .Outcome:
    if beat_MonaLisa == 5:
        #alone
        if MonaOutcome == 0:
            "The Mona Lisa brings cultural, historical, and scientific legitimacy to the exhibit; a diminutive diva starring in an underground gala."
            "Nothing to do with the mailers in the invitees's homes, gathering intelligence on what rhey want to see. of course not."
        #kitsch
        if MonaOutcome == 1:
            "A dozen enigmatic smiles, a dozen landscapes, the Mona Lisa tells her story..."
            "...Blending high and low art, the past and the present, and a small museum's place in a larger conversation."
            "Visitors leave with new perspective on gaze, surveillance, and what it cost us to get here."
        #heist
        if MonaOutcome == 2:
            "News outlets light up all over the globe: Miss Mona Missing from Minor Museum!"
            "Not since Peruggia stole the painting in 1911 have crowds swarmed this spot; now taking selfies with the empty space she left behind."
            "In the background, a dozen smiles, distant and satisfied, as though some part of her finally returned home."
        
    elif beat_MonaLisa > 1:
        #alksjdf
        "The Mona Lisa smiles from the painting, from the gift shop, and from the internet; as though her eyes follow you..."
        "Everywhere."
    else:
        "The Mona Lisa was too small to notice. But she seems to notice others."
        "Those who pass by her painting, or mugs, or memes, sense she's laughing at them..."
        "...and all their secret fumbles committed when they thought no one was watching."
        #bad
    return
