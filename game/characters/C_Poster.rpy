#Poster

default beat_Poster = 1
default p_b3_c1 = 0
default CorgiPortraitStage = "base"
image corgiportrait = "/Characters/Poster/corgi base.png"
default PosterTimeout = 0

label conv_Poster:
    play music "music/B14_W_02.wav" fadein 0.4 volume 0.4
    scene office bg:
        blur 2
    if CorgiPortraitStage == "base":
        show corgi base at truecenter:
            yoffset -125
            zoom .8
    if CorgiPortraitStage == "flag":
        show corgi flag at truecenter:
            yoffset -125
            xoffset -115
            zoom .8
    if CorgiPortraitStage == "final":
        show corgi final at truecenter:
            yoffset -125
            xoffset -115
            zoom .8
    jump .use_action
    #menu:
    #    #"[[Chat a little.]":
        #    p "We're chatting a little now!"
        #    pc "We sure are."
        #    jump conv_Poster
    #    "Beat [beat_Poster]" if actions > 0 and beat_Poster < 5:
            #p "Whoa, sure you want to use an action?"
    #        jump .use_action
    #    "Bye":
    #        p "See ya"
    #        jump FreeRoam
    #    "Reset Beats":
    #        "Beats reset."
    #        $ CorgiPortraitStage = "base"
    #        $ beat_Poster = 1
    #        jump conv_Poster

label .use_action:
    #menu:
    #    p "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_Poster" + "." + "beat" + "%d" % beat_Poster
    #    "No, not really.":
    #        p "Understandable."
    #        jump conv_Poster
    #call advance_time from _call_advance_time_4
    $ PosterTimeout = 1
    jump expression "conv_Poster" + "." + "beat" + "%d" % beat_Poster

label .beat1:
    p neutral "Did I help yesterday?"
    menu:
        "I have to say, I didn't expect a poster to also be able to talk.":
            p neutral "How else could I help motivate you without talking?"
            pc  "I mean…fair enough."
            pass
        "Aah! A talking dog!":
            p surprise "Oh, I'm sorry for scaring you!"
            pass
        "Uh...woof?":
            p question "Woof? I don't know what you mean?"
            pc "I...uh...never mind."
            pass
    p neutral "So did I help? Was your day better?"
    menu:
        "Yes, you definitely helped!":
            p sigh "Oh that's good, thank you! Maybe that means I can help even more people in this place."
        "Nah, not really.":
            p panic "Oh…oh no. Then how could I ever hope to help everyone in this place?"
    pc "Why do you even want to do that?"
    p neutral "I just need to! I feel like I'm missing something, something that will help me do better."
    menu:
        "What do you need?":
            p neutral "I'm sure there's something in this room."
        "How would that even work?":
            p neutral "There's probably something in this room. You can tape it onto me!"
        "Nah, you don't need anything.":
            p neutral "No, I'm sure there's something I'm missing. I bet there's something in this room!"
    p neutral "Can you look around for me? It'd mean the world!"
    p neutral "There's a lot of things lying around here, I'm sure you can find something!"
    pc  "Sure, I can look around."

    call minigamestart_corgi("1") from _call_minigamestart_corgi
    $ CorgiPortraitStage = "flag"
    #hide corgi
    scene office bg with fade:
        blur 2
    show corgi base at truecenter:
            yoffset -125
            zoom .8
    p happy "That's perfect!"
    p neutral "Now there's some tape nearby…can you help me out?"
    show corgi flag at truecenter:
        xoffset -115
        yoffset -125
        zoom .8
    p happy "This will help me so much, I mean look at it!"
    "The corgi poster makes a grunting noise, seemingly as an attempt to wave the little flag."
    "Wow, look at me! I hope me and my little flag here helps make your day the best it can be! Good luck!"
    #####
    $ beat_Poster += 1
    jump FreeRoam
    
label .beat2:
    p sparkle "Hope you do your best today! And thank you for helping yesterday, it really helps me emphasize my words! Watch!"
    "Again, the poster seems to indicate its waving the flag. Again, nothing actually happens."
    p laugh "I feel so free!"
    p neutral "…Who said that!?"
    p sigh "…Unlike the last person who was here."
    menu:
        "What happened with them?":
            p neutral "I'm not sure. At least not completely."
        "Could the last person hear you too?":
            p neutral "I don't think so, but that didn't stop me from doing my job to motivate them!"
        "Maybe they were a cat person.":
            p sad "I don't see how that's relevant."
    #p "The last employee here seemed really happy and I thought I was helping."
    #p "Cheering them on, words of encouragement, everything! Even though I don't think they could actually hear me."
    menu:
        "Well that's good, right?":
            p neutral "I thought so. Whenever they looked at me they usually gave me a little smile!"
        "I'm sure you did your best.":
            p confused "I could've tried harder, though! I wasn't enough."
        "Well you didn't have a flag then!":
            p dots "I guess that's true…"
    p neutral "But eventually they started to ignore me. They were barely in here at all."
    p neutral "I tried to yell as loud as I could to see if maybe I could actually be heard, but nothing."
    p sigh "They didn't even so much as glance at me. It was like they were sleepwalking."
    p neutral "Then, one day, they stopped coming here completely. I never saw them again."
    menu:
        "I'm sorry.":
            p sweat "{i}Sniff{/i} …thanks."
        "[[Pet the dog's head]":
            "The Corgi Poster lets out a content, yet still sad sigh."
    p  "It's all my fault! I should've tried harder to help them, but I wasn't enough."
    p neutral "So I really gotta help you so you don't leave too!"
    p neutral "You are staying, right?"
    menu:
        "Yes, I'm staying.":
            p happy "Yay! Great!"
            p neutral "Have a great day today! Do your best!"
            $ p_b2_c1 = "a"
        "I'm not sure.":
            p panic "Oh no, I'm messing it up again! Was the flag not enough? Can you still hear me?"
            p neutral "Well regardless, I hope today is a great one. Do your best…"
            $ p_b2_c1 = "b"
    ####
    $ beat_Poster += 1
    jump FreeRoam
label .beat3:
    pc  "Got anything to help me stay confident today?"
    if p_b2_c1 == "b":
        p neutral "If you're just going to leave like the last person did, why even try?"
        pc "I might stay!"
    if p_b2_c1 == "a":
        p neutral "I don't know. You said you'd stay but how do I do if you really won't leave like the last one?"
        pc "I really thing I'm going to stay!"
    p confused "Sure…"
    pc  "Well what if I have something to help cheer you up?"
    p question "…What is it?"
    $ AnotherFlag = 0
    $ AnotherPat = 0
    label CheerYouUp:
        menu:
            "Do you want another flag?" if AnotherFlag == 0:
                $ AnotherFlag = 1
                p neutral "I don't think another one's going to help."
                jump CheerYouUp
            "Uh...there, there. [[Pet the dogs head]" if AnotherPat == 0:
                $ AnotherPat = 1
                "The corgi sadly whines a bit. Pets are nice but clearly that's not the solution here."
                jump CheerYouUp
            "What if I got you out of this room for a little bit?":
                p sigh "I mean okay, I guess."
    pc "I need to do some cleaning and I really think you could motivate me to do my best!"
    p "Oh! I think I can help with that!"   
    call minigamestart_cleaning_corgi from _call_minigamestart_cleaning_corgi
    scene office bg with fade:
        blur 2
    if CorgiPortraitStage == "base":
        show corgi base at truecenter:
            yoffset -125
            zoom .85
    if CorgiPortraitStage == "flag":
        show corgi flag at truecenter:
            yoffset -125
            xoffset -115
            zoom .85
    if CorgiPortraitStage == "final":
        show corgi final at truecenter:
            yoffset -125
            xoffset -115
            zoom .85
    p sparkles "Thank you, that really helped! And you did an amazing job with the cleaning!"
    pc  "Good to hear!"
    p neutral "I was thinking, remember when I said I wanted to motivate this entire place? The art place? This artsy building place?"
    menu:
        "You mean museum?":
            p neutral "Museum, yes! Thank you!"
        "That's right. Artsy Building Place.":
            p neutral "Yes! That!"
    pc "Well what if I moved you somewhere outside this room where more people could see you?"
    p surprise "Ooh, really? Where do you think would be best? Somewhere clean, I'm sure!"
    menu:
        "The Entrance.":
            $ p_b3_c1 = "Museum Entrance"
            p sparkles "That's exciting! Right at the front!"
        "The Ticket Counter.":
            $ p_b3_c1 = "Ticket Counter"
            p sparkles "Ooh, that's' probably a busy area. That so exciting, I love that!"
        "By the Restrooms.":
            $ p_b3_c1 = "Restroom"
            p sparkle "That should work! Wow, this is so exciting I feel like I could burst! And I hear that's a good place for bursting!"
    p neutral "But I feel like I'm still missing something. Can you help?"
    pc  "Again?"
    p neutral "Yeah, just one more thing. The flag is great but if I'm going to be out amongst the people, I think I need a little more flair!"
    call minigamestart_corgi("2") from _call_minigamestart_corgi_1
    scene office bg:
        blur 5
    #Ooh still not sure that'll work. Did you clean it yet? I feel like the fuzzy things are getting bigger.
    #The wire on that looks busted. Not exactly inspiring. More flammable than anything.
    #I really dont like that thing. Those teeth? They'd hurt my little paws!
    #The teeth's weapon of choice.
    #{i}shudder{/i} Keep that away from me, please!
    #I saw that thing crawling out of there earlier today. I'm naming it Geoffrey.
    #Oh those will be perfect! Yes! Let's get the tape!
    hide corgi
    show corgi final at truecenter:
        xoffset -115
        yoffset -125
        zoom .9
    $ CorgiPortraitStage = "final"
    p sparkles "This is perfect, thank you! I'm rooting for you!"
    p neutral "You mentioned the [p_b3_c1]–I think I'm ready to be moved out there!"
    "Of course, they don't move, but it's the thought that counts: They generate the necessary good vibes."
    p laugh "Gooooo you!"

    $ beat_Poster += 1
    jump FreeRoam
label .beat4:
    ####
    p sigh "{i}Sigh{/i} Hi again."
    menu:
        "What's bothering you?":
            pass
        "Did the pom-poms not help?":
            pass
        "Need another knick-knack to help?":
            pass
    p neutral "You found these things for me to help out more, but what if it's not enough? What if you still leave?"
    p neutral "What if this was all for nothing?"
    p surprise "{i}GASP!{/i}"
    p panic "What if EVERYONE leaves???"
    $ OtherThanMe = 0
    label WhatIfEveryoneLeaves:
        menu:
            "You know, it doesn't matter if I stay or leave.":
                p question "It doesn't?"
            "That one employee leaving wasn't your fault.":
                p question "It wasn't?"
            "Everyone? Do you know someone other than me?" if OtherThanMe == 0:
                $ OtherThanMe = 1
                p neutral "Well, you and Geoffrey. The creature in the chip bag."
                jump WhatIfEveryoneLeaves
    pc "I don't know, maybe you motivated the last person here {i}so{/i} well they moved on to bigger and better things!"
    p neutral "Wait–"
    p questions "What you do ISN'T the most important job in the world?"
    menu:
        "No, it's not that important.":
            p sigh "Oh, okay…"
        "Yes, sorry, you're right. Nothing is more important than what I do!":
            p happy "Good! I thought so."
    pc  "Either way it doesn't matter what I do. You help people no matter what, trying to give them the confidence to keep going each day."
    pc  "It's not your fault how they take that. They might have more going on than you know!"
    p neutral "I guess that's true. I can only motivate the best I can and just decide that's enough."
    pc  "Exactly.  All you can do is try to be encouraging and be satisfied that you're doing your best."
    p sparkle "Yeah, you're right! As long as I'm happy and doing my best to help, that's enough."
    menu:
        "That's the spirit!":
            "The corgi smiles proudly."
        "Go you!":
            p happy "Yay! Go me!"
        "[[Proudly pet the corgis head]":
            "The corgi squeaks happily as you pat its head. This time the pets are enough."
    p bulb "You know what? I think I'm ready to move out of this room."
    p neutral "I love helping you, but I think I'm ready to support more people with my cheering!"
    pc  "You sure?"
    p neutral "Positive!"
    p neutral "You mentioned the [p_b3_c1]–I think I'm ready to be moved out there!"
    p question "Do you think I'm ready?"
    pc  "One-hundred percent!"
    p sparkle "Good! I know I am, I just wanted you to confirm it! I've helped you be more confident in yourself too, you know!"
    if p_b3_c1 == "Museum Entrance":
        p neutral "Now I'm ready to motivate the people as they walk into this place!"
        p surprise "TO THE ENTRANCE!!!"
    if p_b3_c1 == "Ticket Counter":
        p neutral "Now I'm ready to motivate the people as they buy their tickets to this place!"
        p surprise "TO THE TICKET COUNTER!!!"
    if p_b3_c1 == "Restroom":
        p neutral "Now I'm ready to motivate the people as they do their…uh…business."
        p surprise "TO THE RESTROOMS!!!"
    "You take the poster out to the [p_b3_c1]"
    if p_b3_c1 == "Museum Entrance":
        scene foyer bg:
            blur 5
        show corgi final at truecenter:
            xoffset -115
            yoffset -125
            zoom .9
        p happy "I love it here! Ooh I can see outside too!"
        p neutral "Now do your best! I'll be seeing you everyday first thing as you walk in!"
    if p_b3_c1 == "Ticket Counter":
        scene foyer bg:
            blur 5
        show corgi final at truecenter:
            xoffset -115
            yoffset -125
            zoom .9
        p happy "Ooh this is perfect! I'm sure there'll be lots of hustle and bustle!"
        p neutral "It might get busy, but I'll always keep an eye out for you, so do your best!"
    if p_b3_c1 == "Restroom":
        scene foyer bg:
            blur 5
        show corgi final at truecenter:
            xoffset -115
            yoffset -125
            zoom .9
        p happy "Oh, this is a fun spot! That's an interesting smell, what is that?"
        p neutral "No matter! People will be coming in and out of here and I'm sure they'll really need the motivation to get their business done!"
        p neutral "Now do your best! I'm sure I'll see you around here too. I see the things you eat when you're not doing much."
    p neutral "Haha, I can say to so many people now! Do your best! You do your best too! Yes, especially you over there!"
    menu:
        "Thank you for pushing me too, you really helped!":
            pass
        "I really think you're going to thrive out here, you really helped me!":
            pass
        "I'm glad you're so happy. Now {i}you{/i} do your best!":
            pass
    "Even though the poster still is static and unmoving, you feel like its smiler has somehow, someway, gotten bigger."
    p happy "Hooray!"
    $ StoryCompletedTotal += 1
    $ beat_Poster += 1
    jump FreeRoam

label .Outcome:
    if beat_Poster == 5:
        scene foyer bg:
            blur 5
        show corgi final at truecenter:
            xoffset -115
            yoffset -125
            zoom .9
        "The corgi poster enjoyed its new placement out in the museum."
        "They constantly and joyfully kept shouting words of encouragement to all who passed by, even though people couldn't hear them."
    elif beat_Poster > 1:
        scene office bg:
            blur 2
        if CorgiPortraitStage == "base":
            show corgi base at truecenter:
                yoffset -125
                zoom .8
        if CorgiPortraitStage == "flag":
            show corgi flag at truecenter:
                yoffset -125
                xoffset -115
                zoom .8
        "The corgi poster was happy to have a new employee to encourage."
        "However, they were left feeling they could be helping more people if they could've just gotten out of the office."
    else:
        scene office bg:
            blur 2
        if CorgiPortraitStage == "base":
            show corgi base at truecenter:
                yoffset -125
                zoom .8
        if CorgiPortraitStage == "flag":
            show corgi flag at truecenter:
                yoffset -125
                xoffset -115
                zoom .8
        "The corgi poster sat lonely in the office, wondering why there words of encouragement never reached [pc_name]."
        "Were they just not helpful enough? Could they really not be heard. I guess they'll never know."
    return