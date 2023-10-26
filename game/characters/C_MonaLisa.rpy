#MonaLisa

default beat_MonaLisa = 1
default MonaHeist = 0
default MonaOnly = 0
default MonaOutcome = 0
default MonaTimeout = 0

label conv_MonaLisa:
    play music "music/B14_W_02.wav" fadein 0.4 volume 0.4
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
    m neutral "The famous [pc_name]! You hear more than most. I should expect no less from someone…"
    if pc_work == "gas station attendant":
        m neutral "…who wears the fragrance of petrol and heat-lamp hot dogs with such style."
    if pc_work == "gig worker":
        m neutral "…as focused and disciplined as a cat at a laser show. All that energy and no goals."
    if pc_work == "bouncer":
        m neutral "…with the resilience and mental agility of a truck tire."
    if pc_work == "\"painter\"":
        m neutral "…so masterful at applying paint. To a wall. Outside."
    if pc_work == "\"procurer\"":
        m neutral "…so clever. And daring. And broke."
    if pc_work == "layabout":
        m neutral "…with enough blistering drive to spend an entire day doing nothing."
    m neutral "You realize the enormity of your job, yes? Making something of this rathole?"
    menu:
        "Excuse you, this museum is beautiful.":
            pass
        "Yeah, this'll be an uphill battle.":
            pass
    m neutral "I suppose you have your work cut out for you."
    menu:
        "I suppose you have more roasts?":
            pass
        "I only recognize you, any insights on the other art?":
            pass

    m neutral "Hm…Let me see…"
    m neutral "There's Gilgamesh, the mighty hero with a mighty voice. Especially when he's crying."
    m neutral "Sunflowers looks good for their age, and a forty-million valuation. Too bad it makes them a target."
    m neutral "The works are ignored, confused, insecure, and sad. This place is sad."
    m neutral "But now we have you, the [pc_work]! And your talent for [pc_skill]."
    m neutral "We're saved."
    menu:
        "How do you know all this?":
            m neutral "I'm over five-hundred years old and famous. I get around."
        "You don't have to be so mean.":
            m neutral "These are facts, my friend. Perhaps you read too much from too little."
    m neutral "You should know, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}, I'm {i}everywhere{/i}. If you can see my face, I can see you."
    m neutral "I watched the rest of your interview from a crumpled brochure in the corner."
    m neutral "You're clever. Maybe you can get the others to open up. Or calm down."
    if pc_education == "trades":
        m neutral "If you've apprenticed in a trade, you know to be quick, yes? Or you lose a hand."
    if pc_education == "podcasts":
        m neutral "If you enjoy podcasts, you must have some capacity for obscure details."
    if pc_education == "art course":
        m neutral "If you've taken an art class, you know that your teachers know more than you."
    if pc_education == "Da Vinci Code":
        #need a stronger reference to "that book"
        m neutral "If you've read that book you've participated in… bad art, at least."
    if pc_education == "college credits":
        mm neutral "You may lack the ambition to finish school, but you did show up. Consistently."
    if pc_education == "not say":
        m neutral "Not answering about your education, though…Better to seem quiet and wise than the alternative, no? Worked for me."
    menu:
        "Don't neg me like you want me to fail.":
            m neutral "Fail? {i}Ma{/i}, no {i}Ma, no {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. If I could move my hands maybe you'd understand more than half my words."
        "I can be mysterious and enigmatic, too.":
            $ MonaHeist = 1
            m neutral "If I could move my hands, you'd know exactly what I'm trying to say. "
    m neutral "Maybe that's for the best. You hear us but don't understand us. Maybe this is a waste of time."
    m neutral "No matter. This museum is the last stop on my way home."
    m neutral "Come back when you're ready to pay attention, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. {i}Ciao{/i}."
    "She seems upset, but you honestly can't tell."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .beat2:
    m neutral "Perhaps a touring exhibit will take me closer to Floren–Oh, it's you."
    m neutral "Are you playing nice with the others?"
    menu:
        "I thought you know everything.":
            m neutral "Steal a phone case with my face on it, and I will."
        "How can you leave when you can't move?":
            m neutral "Someone could carry me."
    menu:
        "What's this about a touring exhibit?":
            pass
        "Are you trying to…sneak out?":
            pass
    m neutral "So attentive. I'm flattered. Shall I let you in on the scheme?"
    m neutral "I was almost smuggled out in 1911, but that {i}bischero{/i} didn't have the guts to get me all the way home."
    m neutral "The scandal gave me fame, and the fame gave me copies. I can see what every copy sees."
    menu:
        "Art collaborating with art thieves. Interesting.":
            m neutral "I was young, he had keys, you know how it goes."
        "{i}Every{/i} copy? {i}Memes{/i} can see us? That's horrifying.":
            m neutral "Imagine all the things I physically can't look away from."
    m neutral "But yes, I see all over the world now. Museum gift shops, boutiques, street art, viral art…brochures mailed to mansions."
    m neutral "I see your problem, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. The museum's problem."
    m neutral "Your problem is PR. Spin. Cake tried to do to me what Soup's doing to Sunflowers–they're in the trash now."
    menu:
        "You got splattered with cake?":
            m neutral "Well, frosting. Someone threw a mug at me, once. And acid, before that."
        "What does spin have to do with you sneaking out?":
            m neutral "Perhaps I should tell you. You can hear me–{i}us{/i}–after all."
    m neutral "Suffice to say, my perspective has changed. It made me realize what time and distance takes from us."
    m neutral "I miss home. Its smells and sounds. My language. The light on the hills surrounding my city…"
    m neutral "{i}Repubblica Fiorentina{/i}."
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
            m neutral "\"Italy\" is a baby. Born in 1946, and it overtook my Florence in a mere eighty-one years."
        "Italy has a rich, ancient history.":
            m neutral "Borders shift constantly. A new school of thought here, a treaty or madman in power there–poof."
    #line might be a little vague
    m neutral "The only constant is change. I've seen other works return home after being plundered, or broken, or forgotten in storage."
    m neutral "I want the same for myself."
    menu:
        "How did you wind up in France?":
            m neutral "Da Vinci passed from this world and his apprentice sold me to the French king…"
        "There must be Mona Lisas in Florence now.":
            m neutral "Yes, but they're only part of me. I'm the original. I matter the most…"
    #line still sounds like it's implying the Louvre. The Lourvre wasn't home. This isn't either.
    m neutral "…and I miss my home. The Louvre isn't home."
    menu:
        "How does that work?":
            m neutral "Every time I'm studied or made into a joke, I'm there. I smile, people see what they want to see…and I see them."
        "How did you wind up here?":
            m neutral "I was meant to go to a larger institution but was \"misrouted\" to this place."
    m neutral "My gallery in Paris is too secure. Touring exhibits leave many…opportunities for theft."
    menu:
        "Wait, you {i}want{/i} to get stolen?":
            pass
        "Shipping error. Clever.":
            m neutral "Indeed. My options are limited, despite my depth and detail."
            pass
    m neutral "Dealing with the press is tricky. It's their fault the Louvre increased security. But I've learned some leverage."
    m neutral "Gift shops provide access to other museums; but through the news, I can see into people's homes."
    menu:
        "You see out from screens? Creepy.":
            m neutral "Perhaps. But when the news reported Lakshmi-Narayan's return to Nepal in 2021, I saw their neighbors-to-be celebrate."
            pass
        "It must be tough, watching others return home.":
            m neutral "I've been lucky. Older pieces get locked in storage. Or scream answers at provenance researchers who never hear them."
            pass
    m neutral "I've seen how it can go. Good and bad. The happier ending is within reach."
    m neutral "If your gala succeeds, a clever thief repatriates me. If it fails, I move on and try again."
    menu:
        "Both of those plans end with me getting fired.":
            pass
        "None of that \"spin\" is spinning my way, Mona.":
            pass
    m neutral "I might consider another offer if you have one, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}."
    menu:
        "Homes change, right? \"Home\" is where you choose to stay.":
            m neutral "You don't really believe that, do you?"
        "\"The Many Monas\" is a story worth talking about.":
            m neutral "A story worth talking about, but not a problem worth solving? {i}Che palle…{/i}"
        "Maybe a {i}fake{/i} scandal could help the museum?":
            $ MonaHeist = 1
            m neutral "It would have to be the {i}right{/i} scandal or I'll get stuck here, locked up even tighter."
    m neutral "Some food for thought, I suppose."
    m neutral "{i}Non importa, {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. I'm sure you have other duties."
    m neutral "Be seeing you."

    $ beat_MonaLisa += 1
    jump FreeRoam
    
label .beat3:
    m neutral "Where have you been? I can't see you anywhere."
    menu:
        "I need to have {i}some{/i} privacy!":
            pass
        "Calm down, I'm right here.":
            pass
    m neutral "I'm not upset. Do I look upset?"
    menu:
        "No, of course not!":
            pass
        "I…honestly can't tell.":
            pass
        "Yes. You seem constantly upset.":
            pass
    m neutral "You would think, given Da Vinci's predilection for science, anatomy, and optical illusions…"
    m neutral "…that he would give me hands that moved and danced and let me {i}express{/i} myself!"
    m neutral "Is that so much to ask? Rather than thrusting me into the endless barrage of inane questions and spectral analysis?"
    m neutral "Is {i}this{/i} what you want?"
    "The gaze of a hundred million Mona Lisas concentrates to a single point; no longer the viewed, but the {i}viewer{/i}."
    m sparkles "…"
    "Nothing has changed. Everything has changed."
    menu:
        "I just wanted you to smile!":
            pass
        "I'm in trouble no matter what I say, aren't I?":
            pass
    #is this the right tag?
    "Her eyes follow you; silent. Perfect. Like so many others, named and nameless."
    "And then, in an instant, it's gone."
    m neutral "…"
    m neutral "{i}Basta{/i}. Clipped wings still have their beauty, yes? The details are there for those who–Wait…"
    m neutral "…Something important is happening in the Geneva Museum of Ethnography."
    menu:
        "A crime? A robbery?":
            pass
        "Is your copy all right?":
            pass
    m neutral "A repatriation. A Haudenosaunee medicine mask is returning home! Wonderful news."
    m neutral "We must focus, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. That tantrum cleared my mind, but some of my copies feel off…"
    m neutral "The museum's office, have you been there, yet? I need your help."
    menu:
        "Yes.":
            pass
        "No.":
            pass
        "Why?":
            pass
    m neutral "I don't trust the Admin to run the gala. I used to be able to see the calendar, the computer searches, guest lists…"
    m neutral "Now I can't see anything. Perhaps Charles went crazy and covered my copies when I wasn't paying attention."
    menu:
        "Where should I look?":
            m neutral "Mugs, posters, mouse pads, candy wrappers, memes. I told you, I'm everywhere."
        "You read over people's shoulders?":
            m neutral "Naturally. It's my greatest talent at this point."
    m neutral "With my network of informants, and your general ability to move, we can guarantee the gala's success."
    m neutral "Remember what I said about PR and spin? The right promotion at the right time. That's what we need."
    m neutral "{i}Vai, vai{/i}, go uncover my eyes in the office like a good little [pc_work] so I can see what's happening in there."
    call minigamestart_office from _call_minigamestart_office
    scene fineart_tod:
        blur 5
    show monalisa at truecenter:
        zoom .8
        yoffset -75
    pc  "It's done, I found all of them. You. Er, the copies."
    menu:
        "Is there anything we need to change?":
            pass
        "How can I be sure this isn't a scheme?":
            pass
    m neutral "You need to trust me, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. Now, hush. I need a moment to review everything."
    m neutral "Come back later."

    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam
    
label .beat4:

    m neutral "I knew it. The Admin is ruining the gala. No idea who to invite, where to promote the event, nothing!"
    menu:
        "Why do you care about the gala?":
            pass
        "I thought you wanted to leave this \"rathole.\"":
            pass
    m neutral "If we convince the right people to attend, we'll all benefit."
    m neutral "You keep your job, my fame increases, and then someone will finally walk me out of here."
    menu:
        "That's too risky.":
            m neutral "The institution is the problem, not you. You won't be implicated."
        "I don't want you to go!":
            m neutral "I thought you could hear me, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. Was I wrong about you?"

    m neutral "What's the alternative?"
    label MonaOutcomeChoice:
    menu:
        "You should stay here.":
            m neutral "What? No. Absolutely not. Why should I?"
            menu:
                "You have historic, cultural, and scientific value beyond your origins. This could be your home.":
                    $ MonaOutcome = 0
                    m neutral "What's in it for me?"
                    pc  "You stay for a season, and if you want to go home, I'll set aside funds to send you."
                    m neutral "Fine. Put me at the center of the exhibit. We'll squeeze every last cent out of these rich donors."
                #need summer to write these
                "Let me reconsider.":
                    jump MonaOutcomeChoice
        "Let's display you with all the other Mona Lisas.":
            m neutral "That's so tacky. What will that achieve?"
            menu:
                "It'll make your story more real. Do you want to be perfect and silent, or tell the world what you've told me?":
                    m neutral "Interesting. Put me on the promotional material. I want to see how far this story spreads."
                    $ MonaOutcome = 1
                "Let me reconsider.":
                    jump MonaOutcomeChoice
        "It's too risky for \"someone\" to walk you out of here. I can do it. Heist-style." if MonaHeist == 1:
            m neutral "Oh, I see! What did you have in mind?"
            menu:
                "I have all the other Monas from the office, they'll highlight your absence.":
                    $ MonaOutcome = 2
                    m neutral "Really? You'd give up the jewel of your collection like that?"
                    pc  "Of course. A little scandal, a little fame, we all get what we want."
                    m neutral "Heist and scandal. Clever, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. I knew I saw a little Peruggia in you. Don't break the deal like he did."
                "Let me reconsider.":
                    jump MonaOutcomeChoice
    m neutral "We actually did it. We have a plan."
    m neutral "Let's make it happen."
    pc  "One last question before I set it up…"
    pc  "How did you avoid taking the fall after the theft?"
    m neutral "[pc_name]…Isn't it obvious?"
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
            "The curator, [pc_name], received all due credit for the evening's uncanny success."
            "And nothing further was said about mailers in the invitees’ homes, gathering intelligence on what they wanted to see."
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
        "The Mona Lisa smiles from the painting, from the gift shop, and from the internet; cold and unreadable."
        "You forgot something, and she knows. Her eyes seem to follow you…"
        "…everywhere."
    else:
        scene mona end alone with fade
        "The Mona Lisa was too small to notice. But she notices."
        "Those who pass by her image on posters, totes, and mugs feel her gaze flit across their soul…"
        "…and find nothing worthwhile."
        #bad
    return
