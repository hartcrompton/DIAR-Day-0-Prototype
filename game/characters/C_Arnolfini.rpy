#Arnolfini
#This one is funky, needs to get overhauled based on Shane's conv design
default beat_Arnolfini = 1
default d_ArnolfiniLabel = "DEFAULT LABEL"
default end_Arnolfini = 0

label conv_Arnolfini:
    scene arnolfinibackground
    show arnolfini at right
    ar "You're talking to me, the Arnolfini!"
    menu:
        "Beat [beat_Arnolfini]" if actions > 0 and beat_Arnolfini <= 5:
            jump .use_action
        "Bye":
            ar "See ya"
            jump FreeRoam
        "Reset Beats":
            "Beats reset."
            $ beat_Arnolfini = 1
            jump conv_Arnolfini

label .use_action:
    #menu:
    #    ar "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        call advance_time from _call_advance_time
    #        jump expression "conv_Arnolfini" + "." + "Beat" + "%d" % beat_Arnolfini
    #    "No, not really.":
    #        ar "Understandable."
    #        jump FreeRoam
    jump expression "conv_Arnolfini" + "." + "Beat" + "%d" % beat_Arnolfini

label .Beat1:

    arm "Just admit you took it!"
    arw "No! And what about my brooch?"
    pc "Ahem."
    arw "Gio, someone's here! Oh, uh, hello!"
    arm "...hello."
    pc "Hope everything's alright?"
    arw "Everythings totally fine...if he would just admit he took my brooch!"
    arm "And my comb! I've had enough! I don't want to speak to you ever again!"
    arw "But its lovely meeting you though."
    arm "Yes, you seem great."
    arm "Unlike someone."
    arw "Hmph. My name is-"
    arm "I'm Giovanni."
    pc "What if I helped you two out? I can find what you're looking for. Maybe."
    arw "Well...I guess you could try. I'd really appreciate it."
    arm "I'd appreciate it more."
    #minigame go here
    arw "My brooch! Oh, thank you thank you thank you!"
    arm "Yes, thank you!"
    arm "..."
    arw "..."
    arm "Can you stop standing so close to me?"
    arw "I literally can't move. But I can breathe!"
    "She breathed. Very hard."
    arm "Ugh, stop it! Stop it!"
    arm "At least I can see you if you try to snatch something again!"
    arw "I didn't take it!"
    pc "...I'll leave you two alone."
    ard "Psst! Hey! HEY!"
    pc "The dog? You can talk?"
    ard "The dog talking is what's shocking to you?"
    pc "Fair enough."
    ard "It's never ending with these two! It looks like you actually got them to calm down-"
    arm "Is that your hair in my comb!?"
    arw "How would I even do that!?"
    ard "-sort of. Do you think you could help them learn to get along? It would mean the world!"
    pc "I guess I'll see what I can do."
    "As you walk away, you hear the Arnolfinis continue their arguing"
    arw "See, they're leaving! We can't make friends to save our lives!"
    arm "How is that my fault?"
    
    #####
    

    meta "You have [actions] action(s) left."
    $ beat_Arnolfini += 1
    jump FreeRoam

label .Beat2:

    arw "Thanks for coming back, I thought you'd never return! Hahaha..."
    arw "God, I need friends."
    arm "Yes we're both so sorry for all of our quarreling. We just want some space, is all."
    arw "Yes, a private space. Away from each other."
    pc "Aren't you two married? You seem married."
    arw "Actually...are we? We are aren't we?"
    arm "I...I don't know. I never thought about it."
    arw "Oh my god!"
    arm "Oh my god!"
    ard "Oh my god."
    pc "Well if you two are stuck together, what are your common interests?"
    arw "The finer things! Fabrics! Little baubles! Beautiful jewelry!"
    arm "...I like my comb."
    arw "But really, I have more issues with him then he does me! I need friends! Help me, not him!"
    arm "But what about me, I'm suffering more! Help me instead!"
    ard "Hey buddy. Just listen to me. I want them to both get along for their sakes."
    ard "And mine. Mostly mind. But still! Up to you."

    menu:
        "Help Arnolfini's Wife (?)":
            $ ar_b2_c1 = "a"
            arw "Oh, thank you! I knew you'd see reason."
            arm "Really? Hmph! See if I speak to you ever again."
            ard "Good luck. Talk to you later."
        "Help Giovanni":
            $ ar_b2_c1 = "b"
            arm "Ha! Good choice."
            arw "Him? Really? I knew I was right about you."
            ard "Good luck..."
        "Help The Dog":
            $ ar_b2_c1 = "c"
            ard "I judged you right. I have some ideas to make things work here. I'll talk to you later."
            arm "The dog? Really? Hmph!"
            arw "Uh, the dog? I knew I was right about you."

    ####
    $ beat_Arnolfini += 1
    jump FreeRoam
label .Beat3:
    #choice a
    if ar_b2_c1 == "a":
        arw "There you are! Any ideas on how we can separate? I was thinking what if we ripped the painting in two? Clean in half!"
        pc "Let's maybe try something else."
        arw "Oh...okay."
        pc "I was getting the impression you wanted to make friends outside the painting?"
        arw "I mean...yes! Yes I want that."
        pc "What if we used your husband-"
        arw "Not my husband. I think."
        pc "-your picture companion..."
        arw "Sure."
        pc "as an example. Try being friends with him. You two are stuck together, anyway."
        arw "I guess its worth a shot. Giovanni! I like, uh, your taste in combs!"
        arm "Really? Thats nice of you to say"
        arw "Well I don't talk about it enough. You have dare I say good taste! I mean your hat!"
        arm "I was thinking of adding a feather to it. Or at least imagining a feather."
        arw "Oh that'd be nice!"
        arm "...I think a new necklace would look nice on you as well."
        arw "I was just thinking that! Very kind of you to think that!"
        pc "Look at you two! You haven't yelled in at least one minute!"
        ard "Finally!"
        arw "I have a thought! Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One last favor!"
    if ar_b2_c1 == "b":
        arm "Good to see you! Thank you again for seeing reason and siding with me!"
        arw "Hmph."
        arm "Now about us having our own space. I was thinking of you adding a very thick line between us. VERY thick."
        arm "The thickest line you can think of, but MORE."
        pc "I'm sure I'm not allowed to do that."
        arm "Well why not?"
        pc "I overheard you two wishing you could make friends"
        arm "Well..yes..."
        pc "But you two arguing drives everyone away!"
        arm "Well what am I supposed to do?"
        pc "Well what if you tried being a better friend to your wife-"
        arm "Not my wife. I don't think."
        pc "Your compainion. Just try to make amends. You're stuck with each other, you should at least try to enjoy each other's company."
        arm "I'll try. I guess. ArnolfiniWoman!"
        arw "Yes?"
        arm "I do appreciate your taste. "
        arw "Well thank you!"
        arm "You always look nice and you should take pride in that."
        arw "Same to you! I've always liked your, uh, hat!"
        arm "You think so? I was thinking that it needed a feather in it. I think you'd look lovely with a necklace!"
        arw "Really? That's very kind."
        pc "Look at you two! Getting along!"
        ard "Finally!"
        arw "Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One last favor!"
    if ar_b2_c1 == "c":
        ard "Hey, you finally came by!"
        pc "Did you have any ideas on how to get them to be nicer to each other"
        ard "I thought about that after some ideas to separate them, like separating them with some kind of thick line"
        pc "Can't do that."
        ard "Or just ripping this thin in half"
        pc "Defintiely can't do that."
        ard "But you know? I like it here. The whole painting. And they both have similar qualities."
        pc "Like what."
        ard "Listen its shallow, but have you seen the place we're in? It's beautiful. They like nice things. Get them to compliment there nice things. I can coach you. They don't really notice I talk."
        pc "Okay. Hi you two!"
        arw "What is it?"
        arm "We have nothing to say to you."
        ard "They want to make friends! Mention that!"
        pc "I couldn't help but notice you two wanted to make friends outside of well, yourselves."
        arm "I mean..."
        arw "It's true. It's extremely true."
        ard "Get them to try being friends with each other!"
        pc "What if you started with each other?"
        arm "Pardon?"
        pc "Try being friends with each other. If you can make that work, anyone else should be a cake walk."
        ard "Nice!"
        pc "I mean, you two are already husband and wife."
        arw "Not my husband.  "
        arm "Not my wife.  "
        arw "I don't think..."
        pc "Well your companion. Just try."
        arw "I guess its worth a shot. Giovanni! I like this positive quality."
        arm "Really? Thats nice of you to say"
        arw "Well I don't talk about it enough. It suits you. Your hat does too."
        arm "I was thinking of adding a feather to it. Or at least imagining a feather."
        arw "Oh that'd be nice!"
        arm "I think a new necklace would look nice on you as well."
        arw "I was just thinking that! Very kind of you to think that!"
        pc "Now look at you two, getting along for once!"
        ard "Finally!"
        arw "Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One last favor!"
    ### minigame go here
    arw "Oh thank you, this is just lovely!"
    arm "Yes, thank you!"
    ard "Thank you SO MUCH! Finally! Some peace!"
    arm "You can talk????"
    arw "Well anyway. There's something that's been on my mind."
    arm "Tell me! Anything!"
    arw "What...are we?"
    arm "Like, existentially?"
    pc "Oh no."
    arw "No, no! Like, are we married. Frankly I never thought about it, I just assumed."
    arm "That's a good question. Does the dog know?"
    ard "Don't look at me."
    arw "Now that we've settled, its always been in the back of my mind."
    arm "Me too. Are we married/ Related by blood?"
    arw "Both? Oh no."
    arm "Oh no."
    pc "Oh no."
    ard "I think we're good here for now. We can...figure this out."


####
    $ beat_Arnolfini += 1
    jump conv_Arnolfini

label .Beat4:
    ####
    ard "Welcome back! These two have been...eerily silent."
    arw "We just dont know what to think!"
    arm "Agreement"
    ard "Well lets look at what you have argued about"
    arw "I prefer forceful discussion"
    ard "I've seen the PC doing a lot of cleaning, lets see if it can jog you two's memories."
    ### minigame go here
    meta "Clean up various objects that each of the Arnolfini's finds relatable to their interests. Don't know if we have design implementation for specific objects in the minigmae, but I can tailor the writing to what is available if not."
    ard "Well anything?"
    arw "Let me think..."
    arm "...I've got nothing."
    arw "No, not a clue. I really don't know."
    ard "PC, can you maybe talk to them one-on-one?"
    menu:
        "ArnolfiniMan":
            $ ar_b4_c1 = a
            arm "History about what he knows of ArnolfiniWoman leading to conclusion: They're married"
        "ArnolfiniWoman":
            $ ar_b4_c1 = b
            arw "History about what she knows of ArnolfiniMan leading to conclusion: They're cousins. Just blood related."
        "Dog":
            $ ar_b4_c1 = c
            ard "History about what the dog knows of the two Arnolfinis leading to conclusion: They're related AND married. It was the 1400s."
    ard "Alright what do you think?"
    arm "Well?"
    arw "What is it?"
    menu:
        "They're married":
            $ ar_b4_c2 = "a"
        "They're just related":
            $ ar_b4_c2 = "b"
        "They're married AND related":
            $ ar_b4_c2 = "c"
    if ar_b4_c2 == "a":
        arm "We're married! That makes sense."
        arw "Definitely. You know what? I love you."
        arm "I love you too."
        arw "Though I think we should try a different feather."
        arm "You gave this to me!"
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    if ar_b4_c2 == "b":
        arw "We're cousins! Oh, that makes sense."
        arm "I knew it!"
        arw "Sure you did."
        arm "Do you think our family is even bigger than just us?"
        arw "Oh no where do you think they are? Should we look for them?"
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    if ar_b4_c2 == "c":
        arw "Oh..."
        arm "Oh no..."
        pc "Well it was the 1400s?"
        arm "I don't know what you mean by that, but I guess this is fine?"
        arw "The family must've had a good reason"
        arm "Do you think our family is even bigger than just us?"
        arw "Oh no where do you think they are? Should we look for them?"
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    pc "Well no matter what, it looks like you two"
    ard "Ahem"
    pc "You three seem to be pretty alright"
    arw "Maybe we can finally make other friends? Like that Mona Lisa!"
    arm "Ooh, are those statues I've heard a bit about. They all have the same name!"
    ard "What if you two paid attention to me a bit for a change?"
    arw "Well I don't see why not!"
    arm "Who are you again"
    ard "We'll work on it."

    meta "You have [actions] action(s) left."
    $ beat_Arnolfini += 1
    jump FreeRoam

label .OutcomeA:
    ar "This is outcome A."
    return

label .OutcomeB:
    ar "This is outcome B."
    return

label .OutcomeU:
    ar "This is the unresolved outcome."
    return