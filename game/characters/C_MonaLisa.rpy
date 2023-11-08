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
            m neutral "Perhaps, if you ignore the dust, the trash, and the \"eclectic\" collection."
            pass
        "Yeah, this'll be an uphill battle.":
            m neutral "Uphill? {i}Bambinə{/i}, you've just fallen down a ravine."
            pass
    m neutral "You certainly have your work cut out for you."
    menu:
        "What makes you say that?":
            pass
        "You seem to know a lot.":
            pass

    m neutral "There's Gilgamesh, the mighty hero with a mighty voice. Especially when he's crying."
    m neutral "Sunflowers looks good for their age, and a forty-million valuation. Too bad it makes them a target."
    m neutral "But now we have you, the [pc_work]! And your talent for [pc_skill]."
    m neutral "These works are ignored, confused, insecure, and sad. This place is sad."
    menu:
        "And which are you? I'd guess insecure.":
            m neutral "{i}Bambinə{/i}, I'm five-hundred years old and more famous than the rest of this place put together."
        "You don't have to be so mean.":
            m neutral "These are facts, [pc_work]. Perhaps you read too much from too little."
    m neutral "You should know, {i}bambinə{/i}, I'm {i}everywhere{/i}. If you can see my face, I can see you."
    m neutral "I watched the rest of your interview from a crumpled brochure in the corner."
    m neutral "You're clever. Maybe you can get the others to open up. Or calm down."

    if pc_education == "trades":
        m neutral "If you've apprenticed in a trade, you know to be quick, yes? Or you lose a hand."
    if pc_education == "podcasts":
        m neutral "If you enjoy podcasts, you must have some capacity for obscure details."
    if pc_education == "art course":
        m neutral "If you've taken an art class, you know that your teachers know more than you."
    if pc_education == "Da Vinci Code":
        m neutral "If you've read The Da Vinci Code then you've participated in…bad art, at least."
    if pc_education == "college credits":
        m neutral "You may lack the ambition to finish school, but you did show up. Consistently."
    if pc_education == "not say":
        m neutral "Not answering about your education, though…Better to seem quiet and wise than the alternative, no? Worked for me."
    menu:
        "Don't neg me like you want me to fail.":
            m neutral "Fail? No, {i}bambinə{/i}. If I could move my hands maybe you'd understand more than half my words."
        "I can be mysterious and enigmatic, too.":
            $ MonaHeist = 1
            m neutral "If I could move my hands, you'd know exactly what I'm trying to say. "
    m neutral "Maybe that's for the best. You hear us but don't understand us. Maybe this is a waste of time."
    m neutral "No matter. This museum is the last stop on my way home."
    m neutral "Come back when you're ready to pay attention, {i}bambinə{/i}. {i}Ciao{/i}."
    "She seems upset, but you honestly can't tell."
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .beat2:
    m neutral "Perhaps a touring exhibit will take me closer to Floren–Oh, it's you."
    m neutral "Are you playing nice with the others?"
    menu:
        "I thought you knew everything.":
            m neutral "Steal a phone case with my face on it, and I will."
        "What's this about a touring exhibit?":
            m neutral "Nothing to worry about, I'm sure neither of us will be here much longer."
    m neutral "Now, unless you're here to crate me for transport, I'm sure we both have more valuable things to do."
    menu:
        "I'm not sure I'm allowed to do that.":
            m neutral "How noble. Fortunately, not everyone shares your…moral fortitude."
        "You really want to leave, huh?":
            m neutral "So attentive. I'm flattered. Shall I let you in on the scheme?"
        "Who says I want to keep you?":
            m neutral "{i}Uffa{/i}, don't tease me. You wouldn't be the first to let me down."
    m neutral "I was almost smuggled out in 1911, but that {i}bischero{/i} didn't have the guts to get me all the way home."
    m neutral "The scandal gave me fame, and the fame gave me copies. I can see what every copy sees."
    menu:
        "Art collaborating with art thieves. Interesting.":
            m neutral "I was young, he had keys, you know how it goes."
        "{i}Every{/i} copy? {i}Memes{/i} can see us? That's horrifying.":
            m neutral "Imagine all the things I wish I hadn't seen."
    m neutral "I saw you when you wandered in. Forlorn, sopping, clutching a sad little snack from the Vending Machine."
    m neutral "I'm sure you had a long, terrible day, and wanted nothing more than to go home."
    menu:
        "What does that have do with anything?":
            m neutral "Let's say I can sympathize."
        "Come on, I didn't look {i}that{/i} bad.":
            m neutral "{i}Bambinə{/i}, I saw you from every angle, and none were good."
    m neutral "I've been away from home for a very long time."
    m neutral "I've been attacked with a mug, acid, even cake. Only luck has spared me from Sunflowers' situation."
    m neutral "I'm well aware of what time and distance takes from us."
    m neutral "I miss home. Its smells and sounds. My language. The light on the hills surrounding my city…"
    m neutral "{i}Repubblica Fiorentina{/i}."
    menu:
        "Bless you?":
            pass
        "What did you call me?":
            pass
    m neutral "Florence. "
    m neutral "…Italy."
    m neutral "I see the entire world through my copies. Museum gift shops, textbooks, street art, viral art…brochures mailed to mansions…"
    m neutral "But seeing is not {i}being{/i} home. If the sea rises or the maps change again…it might be too late."
    pc  "I doubt Italy's going to change much."
    m neutral "Oh, the [pc_work] is lecturing in the field of geopolitics, now?  Enlighten us with your learning, Professor."
    menu:
        "Italy seems like a pretty stable place.":
            m neutral "\"Italy\" is a baby. Born in 1946, and it overtook my Florence in a mere eighty-one years."
        "Italy's been around forever.":
            m neutral "Borders shift constantly. A new school of thought here, a treaty or madman in power there–poof."
    m neutral "The only constant is change. I've seen other works return home after being plundered, or broken, or forgotten in storage."
    m neutral "I want the same for myself."
    menu:
        "How have you not schemed your way home yet?":
            m neutral "Give it time. My gallery in Paris was too secure. I helped arrange a \"shipping error\" here as a first step. "
        "There must be Mona Lisas in Florence now.":
            m neutral "Yes, but they're only part of me. I'm the original. I matter the most…"
    m neutral "{i}This{/i} isn't home. The Louvre isn't home."
    menu:
        "Wait, you {i}want{/i} to get stolen?":
            m neutral "It's not like I can steal myself."
        "What if we had another \"shipping error?\"":
            m neutral "{i}Mah{/i}, that certainly is an option."
    m neutral "But \"stealing\" is such a dirty word."
    m neutral "The press start whispering about art theft, and I get locked up tighter than ever. It's their fault the Louvre increased security."
    m neutral "It's all spin, you know."
    m neutral "This museum has the same problem. There's no scandal, no intrigue, no story to tell. No spin."
    menu:
        "What does spin have to do with this?":
            m neutral "Everything. Spin is the difference between being quietly buried; and changing international policy."
        "You would know, your attitude is a big part of that problem.":
            m neutral "I'm helping you curate, Curator."
    m neutral "Most don't realize what it's like for us in museums. I didn't know, either. Until I saw through my copies."
    menu:
        "Don't museums help people and art see each other?":
            m neutral "Lakshmi-Narayan returned to Nepal in 2021, and their neighbors celebrated. Their statue rejoined their community."
        "Is it so bad being preserved and protected?":
            m neutral "I can be preserved, protected, and truly known in my own land and context."
    m neutral "I've seen how it can go. Good and bad. The happier ending is within reach."
    m neutral "If your Grand Gala succeeds, perhaps a clever thief repatriates me. If it fails, I move on and try again."
    menu:
        "Both of those plans end with me getting fired.":
            pass
        "None of that \"spin\" is spinning my way, Mona.":
            pass
    m neutral "I might consider another offer if you have one, {i}bambinə{/i}."
    menu:
        "Homes change, right? \"Home\" is where you choose to stay.":
            m neutral "You don't really believe that, do you?"
        "Your story is more than just you now, it's worth talking about.":
            m neutral "A story worth talking about, but not a problem worth solving? {i}Che palle…{/i}"
        "Maybe a {i}fake{/i} scandal could help the museum?":
            $ MonaHeist = 1
            m neutral "It would have to be the {i}right{/i} scandal or I'll get stuck here, locked up even tighter."
    m neutral "Some food for thought, I suppose."
    m neutral "{i}Non importa, bambinə{/i}. I'm sure you have other duties."
    m neutral "Be seeing you."


    # ###############
    # menu:
    #     "What's this about a touring exhibit?":
    #         pass
    #     "Are you trying to…sneak out?":
    #         pass
    # m neutral "So attentive. I'm flattered. Shall I let you in on the scheme?"
    # m neutral "I was almost smuggled out in 1911, but that {i}bischero{/i} didn't have the guts to get me all the way home."
    # m neutral "The scandal gave me fame, and the fame gave me copies. I can see what every copy sees."
    # menu:
    #     "Art collaborating with art thieves. Interesting.":
    #         m neutral "I was young, he had keys, you know how it goes."
    #     "{i}Every{/i} copy? {i}Memes{/i} can see us? That's horrifying.":
    #         m neutral "Imagine all the things I physically can't look away from."
    # m neutral "But yes, I see all over the world now. Museum gift shops, boutiques, street art, viral art…brochures mailed to mansions."
    # m neutral "I see your problem, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. The museum's problem."
    # m neutral "Your problem is PR. Spin. Cake tried to do to me what Soup's doing to Sunflowers–they're in the trash now."
    # menu:
    #     "You got splattered with cake?":
    #         m neutral "Well, frosting. Someone threw a mug at me, once. And acid, before that."
    #     "What does spin have to do with you sneaking out?":
    #         m neutral "Perhaps I should tell you. You can hear me–{i}us{/i}–after all."
    # m neutral "Suffice to say, my perspective has changed. It made me realize what time and distance takes from us."
    # m neutral "I miss home. Its smells and sounds. My language. The light on the hills surrounding my city…"
    # m neutral "{i}Repubblica Fiorentina{/i}."
    # menu:
    #     "Bless you?":
    #         pass
    #     "What did you call me?":
    #         pass
    # m "Florence. "
    # m "…Italy."
    # m "I want to return to my city. If the sea rises or the maps change again…it might be too late."
    # pc "I doubt Italy's going to change much."
    # m "Oh, Professor [pc_work] lecturing in the field of geopolitics. Enlighten us with your learning."
    # menu:
    #     "Italy's a modern, wealthy country.":
    #         m neutral "\"Italy\" is a baby. Born in 1946, and it overtook my Florence in a mere eighty-one years."
    #     "Italy has a rich, ancient history.":
    #         m neutral "Borders shift constantly. A new school of thought here, a treaty or madman in power there–poof."
    # #line might be a little vague
    # m neutral "The only constant is change. I've seen other works return home after being plundered, or broken, or forgotten in storage."
    # m neutral "I want the same for myself."
    # menu:
    #     "How did you wind up in France?":
    #         m neutral "Da Vinci passed from this world and his apprentice sold me to the French king…"
    #     "There must be Mona Lisas in Florence now.":
    #         m neutral "Yes, but they're only part of me. I'm the original. I matter the most…"
    # #line still sounds like it's implying the Louvre. The Lourvre wasn't home. This isn't either.
    # m neutral "…and I miss my home. The Louvre isn't home."
    # menu:
    #     "How does that work?":
    #         m neutral "Every time I'm studied or made into a joke, I'm there. I smile, people see what they want to see…and I see them."
    #     "How did you wind up here?":
    #         m neutral "I was meant to go to a larger institution but was \"misrouted\" to this place."
    # m neutral "My gallery in Paris is too secure. Touring exhibits leave many…opportunities for theft."
    # menu:
    #     "Wait, you {i}want{/i} to get stolen?":
    #         pass
    #     "Shipping error. Clever.":
    #         m neutral "Indeed. My options are limited, despite my depth and detail."
    #         pass
    # m neutral "Dealing with the press is tricky. It's their fault the Louvre increased security. But I've learned some leverage."
    # m neutral "Gift shops provide access to other museums; but through the news, I can see into people's homes."
    # menu:
    #     "You see out from screens? Creepy.":
    #         m neutral "Perhaps. But when the news reported Lakshmi-Narayan's return to Nepal in 2021, I saw their neighbors-to-be celebrate."
    #         pass
    #     "It must be tough, watching others return home.":
    #         m neutral "I've been lucky. Older pieces get locked in storage. Or scream answers at provenance researchers who never hear them."
    #         pass
    # m neutral "I've seen how it can go. Good and bad. The happier ending is within reach."
    # m neutral "If your gala succeeds, a clever thief repatriates me. If it fails, I move on and try again."
    # menu:
    #     "Both of those plans end with me getting fired.":
    #         pass
    #     "None of that \"spin\" is spinning my way, Mona.":
    #         pass
    # m neutral "I might consider another offer if you have one, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}."
    # "Homes change, right? "Home" is where you choose to stay."
    # m neutral "You don't really believe that, do you?"
    # "Your story is more than just you now, it's worth talking about."
    # m neutral "A story worth talking about, but not a problem worth solving? {i}Che palle…{/i}"
    # "Maybe a {i}fake{/i} scandal could help the museum?"
    # m neutral "It would have to be the {i}right{/i} scandal or I'll get stuck here, locked up even tighter."




    # menu:
    #     "Homes change, right? \"Home\" is where you choose to stay.":
    #         m neutral "You don't really believe that, do you?"
    #     "\"The Many Monas\" is a story worth talking about.":
    #         m neutral "A story worth talking about, but not a problem worth solving? {i}Che palle…{/i}"
    #     "Maybe a {i}fake{/i} scandal could help the museum?":
    #         $ MonaHeist = 1
    #         m neutral "It would have to be the {i}right{/i} scandal or I'll get stuck here, locked up even tighter."
    # m neutral "Some food for thought, I suppose."
    # m neutral "{i}Non importa, {0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. I'm sure you have other duties."
    # m neutral "Be seeing you."

    $ beat_MonaLisa += 1
    jump FreeRoam
    
label .beat3:
    m neutral "Where have you been? I couldn't see you anywhere."
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
        "Yes. You always seem upset.":
            pass
    m neutral "Do you find the other artworks equally hard to read?"
    menu:
        "No. They laugh, and panic, and…sparkle? It's very clear.":
            m neutral "We all have our ways. I wouldn't worry about it."
        "Yes. It's all a bit overwhelming.":
            m neutral "Don't stress. My enigmatic smile has launched a thousand research papers. Even the experts are still learning."
    m neutral "The details are there for those who–"
    m neutral "Wait…"
    m neutral "Something important is happening in the Geneva Museum of Ethnography!"
    menu:
        "A crime? A robbery?":
            pass
        "Is your copy all right?":
            pass
    m neutral "A repatriation. A Haudenosaunee medicine mask is returning home! Wonderful news."
    m neutral "The other works are so excited for them. Give me a moment while I offer my congratulations…"
    menu:
        "[[Be patient, let her have this moment]":
            pass
        "[[Tap your foot]":
            pass
    m neutral "…There. These victories are precious and hard-won."
    m neutral "They never gave up, and neither shall I."
    m neutral "Speaking of…The museum's office, have you been there, yet? I need your help."
    menu:
        "Yes.":
            pass
        "No.":
            pass
        "Why?":
            pass
    m neutral "I don't trust the Admin to run the gala. I used to be able to see the calendar, the computer searches, guest lists…"
    m neutral "Now I can't see anything. Perhaps Charles went crazy and covered my copies when I wasn't paying attention."
    m neutral "I need my eyes back if we want the gala to go smoothly."
    menu:
        "Where should I look?":
            m neutral "Mugs, posters, mouse pads, candy wrappers, memes. I told you, I'm everywhere."
        "You read over people's shoulders?":
            m neutral "Naturally. It's my greatest talent at this point."
    m neutral "With my network of informants, and your…incredible ability to use your hands, we can guarantee the gala's success."
    m neutral "Remember what I said about PR and spin? The right promotion at the right time. That's what we need."
    m neutral "{i}Vai, vai{/i}, go uncover my eyes in the office like a good little [pc_work] so I can see what's happening in there."

    # m neutral "You would think, given Da Vinci's predilection for science, anatomy, and optical illusions…"
    # m neutral "…that he would give me hands that moved and danced and let me {i}express{/i} myself!"
    # m neutral "Is that so much to ask? Rather than thrusting me into the endless barrage of inane questions and spectral analysis?"
    # m neutral "Is {i}this{/i} what you want?"
    # "The gaze of a hundred million Mona Lisas concentrates to a single point; no longer the viewed, but the {i}viewer{/i}."
    # m sparkles "…"
    # "Nothing has changed. Everything has changed."
    # menu:
    #     "I just wanted you to smile!":
    #         pass
    #     "I'm in trouble no matter what I say, aren't I?":
    #         pass
    # #is this the right tag?
    # "Her eyes follow you; silent. Perfect. Like so many others, named and nameless."
    # "And then, in an instant, it's gone."
    # m neutral "…"
    # m neutral "{i}Basta{/i}. Clipped wings still have their beauty, yes? The details are there for those who–Wait…"
    # m neutral "…Something important is happening in the Geneva Museum of Ethnography."
    # menu:
    #     "A crime? A robbery?":
    #         pass
    #     "Is your copy all right?":
    #         pass
    # m neutral "A repatriation. A Haudenosaunee medicine mask is returning home! Wonderful news."
    # m neutral "We must focus, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. That tantrum cleared my mind, but some of my copies feel off…"
    # m neutral "The museum's office, have you been there, yet? I need your help."
    # menu:
    #     "Yes.":
    #         pass
    #     "No.":
    #         pass
    #     "Why?":
    #         pass
    # m neutral "I don't trust the Admin to run the gala. I used to be able to see the calendar, the computer searches, guest lists…"
    # m neutral "Now I can't see anything. Perhaps Charles went crazy and covered my copies when I wasn't paying attention."
    # menu:
    #     "Where should I look?":
    #         m neutral "Mugs, posters, mouse pads, candy wrappers, memes. I told you, I'm everywhere."
    #     "You read over people's shoulders?":
    #         m neutral "Naturally. It's my greatest talent at this point."
    # m neutral "With my network of informants, and your general ability to move, we can guarantee the gala's success."
    # m neutral "Remember what I said about PR and spin? The right promotion at the right time. That's what we need."
    # m neutral "{i}Vai, vai{/i}, go uncover my eyes in the office like a good little [pc_work] so I can see what's happening in there."
    call minigamestart_office from _call_minigamestart_office
    scene fineart_tod:
        blur 5
    show monalisa at truecenter:
        zoom .8
        yoffset -75
    pc  "It's done, I found all of them. You. Er, the copies."
    menu:
        "Is there anything we need to change?":
            m neutral "I'm sure there will be, {i}bambinə{/i}."
        "How can I be sure this isn't a scheme?":
            $ MonaHeist = 1
            m neutral "But this is a scheme, {i}bambinə{/i}, aren't you paying attention?"
    m neutral "Trust me, and hush. I need a moment to review everything."
    m neutral "Come back later. We'll fix whatever the Admin's planned."



    ##########
    # pc  "It's done, I found all of them. You. Er, the copies."
    # menu:
    #     "Is there anything we need to change?":
    #         pass
    #     "How can I be sure this isn't a scheme?":
    #         pass
    # m neutral "You need to trust me, {i}{0}bambino{/0}{1}bambina{/1}{2}bambinə{/2}{/i}. Now, hush. I need a moment to review everything."
    # m neutral "Come back later."

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
    m neutral "You keep your job, and the right someone will finally walk me out of here."
    menu:
        "That's too risky.":
            m neutral "The institution is the problem, not you. You won't be implicated."
        "Theft can't be the only way.":
            m neutral "I thought you could hear me, {i}bambinə{/i}. Was I wrong about you?"

    m neutral "What's the alternative?"
    label MonaOutcomeChoice:
    menu:
        "You don't have to stay forever. Just a season.":
            m neutral "I still don't see what's in it for me."
            menu:
                "If the gala goes well and the museum survives, I'll be able to set aside funds to send you anywhere.":
                    $ MonaOutcome = 0
                    m neutral "Fine. Put me at the center of the exhibit. We'll squeeze every last cent out of these rich donors."
                #need summer to write these
                "Let me reconsider.":
                    jump MonaOutcomeChoice
        "We could make the exhibit about you…All of you.":
            pc  "I'll display you with all the other Monas. Mugs, posters, everything."
            m neutral "That's so tacky. What will that achieve?"
            menu:
                "It'll platform your story. Do you want to be enigmatic and unreadable, or tell the whole world what you've told me?":
                    m neutral "Interesting. Put me on the promotional material, too. I want to make sure the message is received."
                    $ MonaOutcome = 1
                "Let me reconsider.":
                    jump MonaOutcomeChoice
        "We can't let just anyone walk you out of here. I should do it." if MonaHeist == 1:
            m neutral "Really?"
            m neutral "You'd give up the jewel of your collection? Just like that?"
            menu:
                "If I put all the other Monas on display, but you go missing, we'll make headlines.":
                    $ MonaOutcome = 2
                    pc  "You can help me prepare the museum's statement. To make sure it has the right {i}spin{/i}."
                    m neutral "Hah! Clever, {i}bambinə{/i}. I knew I saw a little Peruggia in you. Don't break the deal like he did."
                "Let me reconsider.":
                    jump MonaOutcomeChoice
    m neutral "We actually did it. We have a plan."
    m neutral "Let's make it happen."
    pc  "One last question before I set it up…"
    pc  "How did you avoid taking the fall after the theft?"
    m neutral "[pc_name]…Isn't it obvious?"
    m neutral "I was framed."
    "…"
    m neutral "See you around, my friend."

    $ StoryCompletedTotal += 1
    $ beat_MonaLisa += 1
    #$ if d_MonaLisa < 6: d_MonaLisa + 1
    jump FreeRoam

label .Outcome:
    if beat_MonaLisa == 5:
        #alone
        if MonaOutcome == 0:
            scene mona end alone with fade
            "The Mona Lisa brought cultural, historical, and scientific legitimacy to the exhibit; a diminutive diva starring in an underground gala."
            "The curator, [pc_name], received all due credit for the evening's uncanny success."
            "And nothing further was said about mailers in the invitees’ homes, gathering intelligence on how best to entice generous donations."
        #kitsch
        if MonaOutcome == 1:
            scene mona end kitsch with fade
            "A dozen enigmatic smiles, a dozen landscapes, the Monas Lisa told their story…"
            "…Blending high and low art, the past and the present, and a small museum's place in a larger conversation."
            "Visitors left with new perspectives on gaze, surveillance, and what it cost us to get here."
        #heist
        if MonaOutcome == 2:
            scene mona end heist with fade
            "News outlets lit up all over the globe: Miss Mona Missing from Minor Museum!"
            "Not since Peruggia stole the painting in 1911 have crowds swarmed this spot; snapping selfies with the empty space she left behind."
            "In the background, a dozen smiles, distant and satisfied, as though some part of her finally returned home."
        
    elif beat_MonaLisa > 1:
        #alksjdf
        scene mona end alone with fade
        "The Mona Lisa smiled from the painting, from the gift shop, and from the internet; cold and unreadable."
        "You forgot something, and she knew. Her eyes seemed to follow you…"
        "…everywhere."
    else:
        scene mona end alone with fade
        "The Mona Lisa was too small to notice. But she noticed."
        "Those who passed by her image on posters, totes, and mugs felt her gaze flit across their soul…"
        "…and found nothing worthwhile."
        #bad
    return
