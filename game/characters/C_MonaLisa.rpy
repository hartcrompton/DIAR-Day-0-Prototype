#MonaLisa

default beat_MonaLisa = 1
default MonaHeist = 0
default MonaOnly = 0
default MonaOutcome = 0
default MonaTimeout = 0

label conv_MonaLisa:
    scene fineart_tod:
        blur 5
    show monalisa at truecenter:
        zoom .8
        yoffset -75
    jump .use_action
    #menu:
    #    "Beat [beat_MonaLisa]" if actions > 0 and beat_MonaLisa < 5:
    #        #m "Whoa, sure you want to use an action?"
    #        jump .use_action
    #    "Bye":
    #        m "See ya"
    #        jump FreeRoam
    #    "Reset Beats":
    #        "Beats reset."
    #        $ beat_MonaLisa = 1
    #        jump conv_MonaLisa

label .use_action:
    #menu:
    #    m "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_MonaLisa" + "." + "beat" + "%d" % beat_MonaLisa
    #    "No, not really.":
    #        m "Understandable."
    #        jump conv_MonaLisa
    #call advance_time from _call_advance_time_3
    $ MonaTimeout = 1
    jump expression "conv_MonaLisa" + "." + "beat" + "%d" % beat_MonaLisa

label .beat1:
    m "The famous [pc_name]! You hear more than most. I should expect no less from someone…"
    if pc_work == "gas station attendant":
        m "…who wears the fragrance of petrol and heat-lamp hot dogs with such panache."
    if pc_work == "gig worker":
        m "…as focused and disciplined as a cat at a laser show. All that energy and no goals."
    if pc_work == "bouncer":
        m "…with the resilience and mental agility of a truck tire."
    if pc_work == "\"painter\"":
        m "…so masterful at applying paint. To a wall. Outside."
    if pc_work == "\"procurer\"":
        m "…so clever, and daring–and broke."
    if pc_work == "layabout":
        m "…with enough blistering drive to spend an entire day doing nothing."
    m "You realize the enormity of your job, yes? Making something of this rathole?"
    menu:
        "Excuse you, this museum is beautiful.":
            pass
        "Yeah, this'll be an uphill battle.":
            pass
    m "I suppose you have your work cut out for you."
    pc "Do you have any advice?"
    menu:
        "You're the only piece I recognize.":
            pass
        "What's going on with the others?":
            pass

    m "There's Gilgamesh, the mighty hero with a mighty voice. Especially when he's crying."
    #confirm gender on sunflowers
    m "And Sunflowers looks good for her age. The forty-million valuation helps, but it also makes her a target."
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
        m "If you enjoy podcasts, you must have some capacity for obscure details."
    if pc_education == "art course":
        m "If you've taken an art class, you know that your teachers know more than you."
    if pc_education == "Da Vinci Code":
        #need a stronger reference to "that book"
        m "If you've read that book you've participated in bad art, at least. It's a start."
    if pc_education == "college credits":
        m "You may lack the ambition to finish school, but you did show up. Consistently."
    if pc_education == "not say":
        m "Not answering about your education, though…Better to seem quiet and wise than the alternative, no? Worked for me."
    menu:
        "Don't neg me like you want me to fail.":
            m "Fail? {i}Ma, no {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. If I could move my hands maybe you'd understand more than half my words."
        "I can be mysterious and enigmatic, too.":
            $ MonaHeist = 1
            m "If I could move my hands, you'd know exactly what I'm trying to say. "
    m "But maybe that's for the best. You hear us but you don't see us. Maybe this is a waste of time."
    m "No matter. This museum is the last stop on my way home."
    m "Come back when you're ready to pay attention, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}. Ciao.{/i}"
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
            m "Someone could carry me."
    m "I was almost smuggled out in 1911, but he didn't have the guts to get me all the way home."
    m "The scandal was good for me. It gave me fame, and gave me copies. I can see what every copy sees."
    menu:
        "Art collaborating with art thieves. Interesting.":
            pass
        "Mona Lisa memes can see us? That's horrifying.":
            pass
    m "My copies saw all over the world through museum gift shops, and then boutiques. Then street art. Viral art. Brochures mailed to mansions."
    m "I see your problem, {i}bambinə{/i}."
    m "Your problem is PR. Spin. Cake tried to do to me what Soup's doing to Sunflowers–they're in the trash now."
    menu:
        "You got splattered with cake?":
            m "Well, frosting. Someone threw a mug at me, once. And acid, before that."
        "You see the whole world through the eyes of your copies?":
            m "Yes. I don't know how it began, but I see all of it. Good and bad."
    m "I didn't understand what it all meant when I was younger. Things changed."
    m "My perspective changed. It made me realize how far time and distance can stretch."
    m "I miss the smells and sounds of my home. My language. The light on the hills surrounding my city…"
    m "{i}Repubblica Fiorentina{/i}."
    menu:
        "Bless you?":
            pass
        "What did you call me?":
            pass
    m "Florence. "
    m "…Italy."
    m "I want to return to my city. If the sea rises or the maps change again…it might be too late."
    pc "I doubt Italy's going to change much."
    m "Oh, Professor [pc_work] lecturing in the field of geopolitics. Enlighten us with your learning."
    menu:
        "Italy's a modern, wealthy country.":
            m "\"Italy\" is a baby. Born in 1946, and it overtook my Florence in a mere eighty-one years."
        "Italy has a rich, ancient history.":
            m "Borders shift constantly. A new school of thought here, a treaty or madmen in power there–poof."
    #line might be a little vague
    m "The only constant is change. I've seen other works return home after being plundered, or broken, or forgotten in storage."
    m "I want the same for myself."
    menu:
        "How did you wind up in France?":
            m "Da Vinci passed from this world and his apprentice sold me to the French king…"
        "There must be Mona Lisas in Florence now.":
            m "Yes, but they're only part of me. I'm the original. I matter the most…"
    #line still sounds like it's implying the Louvre. The Lourvre wasn't home. This isn't either.
    m "…and I miss my home. The Louvre isn't home."
    menu:
        "How does that work?":
            m "Every time I'm studied or made into a joke, I'm there. I smile, people see what they want to see, and I see them."
        "How did you wind up here?":
            m "I was meant to go to a larger institution but was \"misrouted\" to this place."
    m "My gallery in Paris is too secure. Touring exhibits leave many…opportunities for theft.."
    menu:
        "Wait, you {i}want{/i} to get stolen?":
            pass
        "Shipping error. Clever.":
            m "My options are limited when I can't move."
            pass
    m "The first time I was \"stolen\" the press found out and I was sent back to the Louvre. "
    m "From gift shops, I hear other artworks; but from the news, I can see into people's homes."
    menu:
        "You see out from the TV? Creepy.":
            m "Perhaps. I don't regret seeing a Nepalese woman nod at the screen when the news reported Lakshmi-Narayan's return in 2021."
            pass
        "It must be tough, watching others return home.":
            m "I've been very lucky. The older ones forget they're mute and yell HOT or COLD while provenance researchers guess their origins."
            pass
    m "I just want to hear my own language and smell the air in my own land. It's been too long."
    m "So you see my position. If your gala succeeds, I'm a more tempting target. If it fails, I move on and try again."
    menu:
        "Even homes change. \"Home\" is where you choose to stay.":
            m "Do you really believe that?"
        "\"The Many Monas\" is a story worth telling.":
            m "A story worth telling, but not worth taking action? {i}Che palle…{/i}"
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
    m "I'm not upset. Do I look upset?"
    menu:
        "No, of course not!":
            pass
        "I…honestly can't tell.":
            pass
    m "You would think, given Da Vinci's predilection for science, anatomy, and optical illusions…"
    m "…that he would give me hands that moved and danced and let me {i}express{/i} myself!"
    m "Is that so much to ask? Rather than thrusting me into the endless barrage of inane questions and spectral analysis?"
    m "Is {i}this{/i} what you want?"
    "The gaze of a hundred million Mona Lisas concentrates to a single point; no longer the viewed, but the viewer."
    m "…"
    "Nothing has changed. Everything has changed." 
    menu:
        "I just wanted you to smile!":
            pass
        "I'm in trouble no matter what I say, aren't I?":
            pass
    #is this the right tag?
    "Her eyes follow you; silent. Perfect. Like so many others, named and nameless."
    "And then, in an instant, it's gone."
    m "…"
    m "{i}Basta{/i}. Clipped wings still have their beauty, yes? The details are there for those who–Wait…"
    m "…Something important is happening in the Geneva Museum of Ethnography."
    menu:
        "A crime? A robbery?":
            pass
        "Is your copy all right?":
            pass
    m "A repatriation. A Haudenosaunee medicine mask is returning home! Wonderful news."
    m "We must focus, {i}bambinə{/i}. That tantrum cleared my mind, but some of my copies…"
    m "The museum's office, have you been there, yet? I need your help."
    menu:
        "Yes.":
            pass
        "No.":
            pass
        "Why?":
            pass
    m "I don't trust the Admin to run the gala. I used to be able to see the calendar, the computer searches, guest lists…"
    m "Now I can't see anything. Perhaps Charles went crazy and covered my copies when I wasn't paying attention."
    menu:
        "Where should I look?":
            m "Mugs, posters, mouse pads, candy wrappers, memes. I told you, I'm everywhere."
        "You read over people's shoulders?":
            m "Naturally. It's my greatest talent at this point."
    m "With my network of informants, and your general ability to move, we can guarantee the gala's success."
    m "Remember what I said about PR and spin? The right promotion at the right time. That's what we need."
    m "{i}Vai, vai{/i}, go uncover my eyes in the office like a good little [pc_work] so I can see what's happening in there."
    call minigamestart_office from _call_minigamestart_office
    scene fineart_tod:
        blur 5
    show monalisa at truecenter:
        zoom .8
        yoffset -75
    pc "It's done, I found all of them. You. Er, the copies."
    menu:
        "Is there anything we need to change?":
            pass
        "Why do you suddenly care about the gala's success?":
            pass
    m "Hush, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}, I need a moment to review everything."
    m "Come back later."

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
    m "If we convince the right people to attend, we'll all benefit."
    m "You keep your job, my fame increases, and then someone will finally walk me out of here."
    menu:
        "That's too risky.":
            m "The institution is the problem, not you. You won't be implicated."
        "I don't want you to go!":
            m "I thought you could hear me, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. Was I wrong about you?"
    

    m "What's the alternative?"
    label MonaOutcomeChoice:
    menu:
        "You should stay here.":
            m "What? No. Absolutely not. Why should I?"
            menu:
                "You have historic, cultural, and scientific value beyond your origins. This could be your home.":
                    $ MonaOutcome = 0
                    m "What's in it for me?"
                    pc "You stay for a season, and if you want to go home, I'll set aside funds to send you."
                    m "Fine. Put me at the center of the exhibit. We'll squeeze every last cent out of these rich donors."
                #need summer to write these
                "Let me reconsider.":
                    jump MonaOutcomeChoice
        "Let's display you with all the other Monas.":
            m "That's so tacky. What will that achieve?"
            menu:
                "It'll make your story more real. Do you want to be perfect and silent, or tell the world what you've told me?":
                    m "Interesting. Put me on the promotional material. I want to see how far this story spreads."
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
                    m "Heist and scandal. Clever, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. I knew I saw a little Peruggia in you. Don't break the deal like he did."
                "Let me reconsider.":
                    jump MonaOutcomeChoice
    m "This will be easy. Let's make it happen."
    pc "One last question before I set it up…"
    pc "How did you avoid getting in trouble after the theft?"
    m "{i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}…Isn't it obvious?"
    m "I was framed."
    "…"
    m "See you around, my friend."

    $ StoryCompletedTotal += 1
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .Outcome:
    if beat_MonaLisa == 5:
        #alone
        if MonaOutcome == 0:
            scene mona end alone with fade
            "The Mona Lisa brings cultural, historical, and scientific legitimacy to the exhibit; a diminutive diva starring in an underground gala."
            "It had nothing to do with the mailers in the invitees’ homes, gathering intelligence on what they wanted to see."
        #kitsch
        if MonaOutcome == 1:
            scene mona end kitsch with fade
            "A dozen enigmatic smiles, a dozen landscapes, the Mona Lisa tells her story…"
            "…Blending high and low art, the past and the present, and a small museum's place in a larger conversation."
            "Visitors leave with new perspectives on gaze, surveillance, and what it cost us to get here."
        #heist
        if MonaOutcome == 2:
            scene mona end heist with fade
            "News outlets light up all over the globe: Miss Mona Missing from Minor Museum!"
            "Not since Peruggia stole the painting in 1911 have crowds swarmed this spot; now taking selfies with the empty space she left behind."
            "In the background, a dozen smiles, distant and satisfied, as though some part of her finally returned home."
        
    elif beat_MonaLisa > 1:
        #alksjdf
        scene mona end alone with fade
        "The Mona Lisa smiles from the painting, from the gift shop, and from the internet; as though her eyes follow you…"
        "Everywhere."
    else:
        scene mona end alone with fade
        "The Mona Lisa was too small to notice. But she seems to notice others."
        "Those who pass by her painting, or mugs, or memes, sense she's laughing at them…"
        "…and all their secret fumbles committed when they thought no one was watching."
        #bad
    return
