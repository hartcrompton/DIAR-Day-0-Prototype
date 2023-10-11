#Arnolfini
#This one is funky, needs to get overhauled based on Shane's conv design
default beat_Arnolfini = 1
default d_ArnolfiniLabel = "DEFAULT LABEL"
default end_Arnolfini = 0

label conv_Arnolfini:
    scene arnolfinibackground
    show arnolfini at truecenter:
        zoom .7
        yoffset -100
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
    call advance_time
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
    arw "Well...I guess you could try. I'd really appreciate it. Also do I even have a name...?"
    arm "I'd appreciate it more."
    #minigame go here
    call minigamestart_arnolfini(1)
    arw "My brooch! Oh, thank you thank you thank you!"
    arm "Yes, thank you!"
    arm "..."
    arw "..."
    arm "Can you stop standing so close to me?"
    arw "I literally can't move. But I can breathe!"
    "She breathed. Very hard. In his face."
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
    
    $ beat_Arnolfini += 1
    jump FreeRoam

label .Beat2:

    arw "Thanks for coming back, I thought you'd never return! Hahaha..."
    arw "God, I need friends."
    #change ARW name here
    $ arwName = "Alessandra"
    arw "Also I didn't introduce myself. I'm Alessandra."
    arm "Alessandra? A bit flowery for a name, don't you think?"
    arw "Thats rich coming from a Giovanni."
    arm "..."
    arm "Anyway, we're both so sorry for all of our quarreling. We just want some space, is all."
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
    ard "And mine. Mostly mine. But still! Up to you."

    menu:
        "Help Arnolfini's...Wife? Sister? Cousin?":
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
        arw "There you are! I'm trying a new name today. Alessandra was passé, you know?"
        #change ARW name here
        $ arwName = "Gertrude"
        arw "Now how about this: Gertrude. Beautiful, no?"
        pc "I think whatever you want works best."
        arw "Thank you! Nice to see some approval around here."
        arw "Now then, any ideas on how we can separate? I was thinking what if we ripped the painting in two? Clean in half!"
        pc "Let's maybe try something else."
        arw "Oh...okay."
        pc "I was getting the impression you wanted to make friends outside the painting?"
        arw "I mean...yes! Yes I want that."
        pc "What if we used your husband-"
        arw "Not my husband."
        arw "I think."
        pc "-your picture companion..."
        arw "...sure."
        pc "as an example. Try being friends with him. You two are stuck together, anyway."
        arw "I guess its worth a shot. Giovanni! I like this positive quality."
        arw "I like, uh, your taste in combs?"
        arm "Really? Thats nice of you to say"
        arw "Well I don't talk about it enough. You have, dare I say, good taste! I mean your hat!"
        arm "Ooh, I was thinking of adding a feather to it. Or at least imagining a feather."
        arw "That'd be nice! Don't you agree, [pc_name]?"
        pc "I agree!"
        arm "...I think a new necklace would look nice on you as well."
        arw "Oh wouldn't it?"
        pc "Look at you two! You haven't yelled in at least a minute!"
        ard "Finally!"
        arw "I have a thought! Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One final favor! We'll be the talk of the room!"
    if ar_b2_c1 == "b":
        arm "Welcome back! Thank you for listening to me. The reasonable one!"
        arw "Hmph."
        arm "Now about us having our own space. I was thinking of you adding a very thick line between us"
        arm "VERY thick."
        pc "I'm sure I'm not allowed to do that."
        arm "Well why not?"
        pc "What if you tried to look outside of your frame a bit? Don't you want to make some friends?"
        arm "Well...yes..."
        pc "But you two bicker so much how could anyone else ever get a word in?"
        ard "Preach."
        arm "What am I supposed to do about that!"
        pc "Well what if you started off being friends with your wife—"
        arm "Not my wife."
        arm "I think."
        pc "-your picture companion..."
        arm "I'll accept that."
        pc "Just try to make amends. You're stuck with each other, you should at least try to enjoy each other's company."
        arm "I'll try. I guess. Ahem!"
        arw "Yes?"
        arm "You...whats your name again?"
        #change ARW name
        $ arwName = "Gertrude"
        arw "It's Gertrude today."
        arm "You look quite...nice today...Gertrude. I like your taste. I don't say that enough."
        arw "Well thank you!"
        arm "You always look quitenice and you should take pride in that."
        arw "Same to you! I've always liked your, uh, hat!"
        arm "You think so? I was thinking that it needed a feather in it. I think you'd look lovely with a necklace!"
        arw "Really? I think so too!"
        pc "Look at you two! You haven't yelled in at least a minute!"
        ard "Finally!"
        arw "I have a thought! Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One final favor! We'll be the talk of the room!"
    if ar_b2_c1 == "c":
        ard "Hey, you finally came by!"
        pc "Yeah! It seemed like you had some ideas, or an idea, of how to get thes two to get along? At least a little bit?"
        ard "Well I mean we could just separate them. Draw like a BIG line between them."
        pc "Can't do that."
        ard "Or just ripping this thing in half"
        pc "Defintiely can't do that."
        ard "But you know? I like it here. The whole painting. And they both have similar interests, they just have to communicate!"
        pc "Interests?"
        ard "Listen its shallow, but have you seen the place we're in? It's beautiful. They like nice things."
        ard "Get them to compliment each others things. Their taste. I can coach you. If you haven't noticed they don't really pay attention to me."
        pc "Alright, I'll try."
        pc "Hi you two!"
        arw "What is it?"
        arm "We have nothing to say to you."
        ard "They want to make friends! Mention that!"
        pc "I couldn't help but notice you two wanted to make friends outside of well, yourselves."
        arm "I mean..."
        arw "It's true! It's extremely true."
        ard "Remember: they should really befriend each other first!"
        pc "What if you started with each other?"
        arm "Pardon?"
        pc "Try being friends with each other. If you can make that work, anyone else should be a cake walk."
        ard "Perfect!"
        pc "I mean, you two are already husband and wife."
        arw "Not my husband.  "
        arm "Not my wife.  "
        arw "I don't think..."
        pc "Your photo companion?"
        arm "Meh."
        arw "Sure."
        pc "Just try?"
        arw "Fine. If he won't try first I guess I will."
        arw "Giovanni. That comb you found. It's...nice. You have good taste."
        arm "Really? Thats nice of you to say. Should I be suspicious?"
        arw "No! I don't talk about it enough. It suits you. Your hat does too."
        arm "You know, I was thinking of adding a feather to it. Or at least imagining a feather."
        arw "Oh that'd be nice!"
        arm "I think a new necklace would look nice on you as well...whats your name again?"
        #change ARW name here
        $ arwName = "Gertrude"
        arw "It's Gertrude today."
        arm "It looks good...Gertrude. I like your taste. I don't say that enough."
        arw "Really? Well thank you!"
        pc "Look at you two! You haven't yelled in at least a minute!"
        ard "Finally!"
        arw "I have a thought! Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One final favor! We'll be the talk of the room!"
    "Placeholder minigame: Waiting on final objects"
    call minigamestart_arnolfini(2)
    arw "Oh thank you, this is just lovely!"
    arm "Yes, thank you!"
    ard "Thank you SO MUCH! Finally! Some peace!"
    arm "The dog can talk?"
    ard "If I could move my eyes they'd be rolling right now."
    arw "Well anyway. There's something that's been on my mind, lately."
    arm "Tell me! Anything!"
    arw "What...are we?"
    arm "Like, existentially?"
    pc "Oh boy."
    arw "No, no! Like, are we married. Frankly I never thought about it, I just assumed."
    arm "That's a good question. Does the dog know?"
    ard "Don't look at me. I tuned you two out ages ago."
    arw "Now that we've settled, its always been in the back of my mind."
    arm "Well could we be blood relatives? Or is it marraige?"
    arw "Or may be both..?"
    arw "...oh no."
    arm "Oh no."
    pc "Oh no."
    arm "..."
    arw "..."
    ard "...I think we're good for now. They need some time to process...whatever this is. Talk to you later."

####
    $ beat_Arnolfini += 1
    jump conv_Arnolfini

label .Beat4:
    ####
    ard "Good morning! These two have been...eerily silent."
    arw "We just dont know what to think!"
    arm "What ARE we!?"
    pc "Does it really matter if you're getting along?"
    arm "Of course it does!"
    arw "What would the other pieces of art think if we didn't know? How would we even introduce ourselves!?"
    pc "Well lets look at what you have argued about and maybe we can figure this out."
    arw "I prefer \"discussion with force.\""
    ard "I've seen the PC doing a lot of cleaning, lets see if it can jog you two's memories."
    pc "Hey, it's worth a shot!"
    call minigamestart_cleaning_arnolfini
    ### minigame go here
    #meta "Clean up various objects that each of the Arnolfini's finds relatable to their interests. Don't know if we have design implementation for specific objects in the minigmae, but I can tailor the writing to what is available if not."
    ard "Well anything? Some kind of memory jogged."
    arw "Let me think..."
    arm "...I've got nothing."
    arw "No, not a clue. I really don't know. Great job cleaning though!"
    pc "Oh, thanks!"
    arw "Look, Gio, I complimented them!"
    arm "Ooh, so that's how it works with other pepole."
    ard "PC, can you maybe talk to them one-on-one?"
    ard "I don't think we're getting anywhere with this. Maybe talk to them one-on-one and see if there's any kind of clue?"
    pc "Think that'd work?"
    ard "Yeah, just go with your intution. Come talk to me too, I may remember something."
    $ SpeakGiovanni = 0
    $ SpeakWoman = 0
    $ SpeakDog = 0
    label ArnolfiniInvestigate:
        menu:
            "Speak to Giovanni" if SpeakGiovanni == 0:
                $ SpeakGiovanni = 1
                $ ar_b4_c1 = "a"
                pc "Do you remember anything from your past that might help define you two's relationship?"
                arm "History about what he knows of ArnolfiniWoman leading to conclusion: They're married"
                jump ArnolfiniInvestigate
            "Speak to Gertrude" if SpeakWoman == 0:
                $ SpeakWoman = 1
                $ ar_b4_c1 = "b"
                pc "What can you tell me about your history with Giovanni? Maybe there's something we're missing."
                arw "History about what she knows of ArnolfiniMan leading to conclusion: They're cousins. Just blood related."
                jump ArnolfiniInvestigate
            "Speak to the Dog" if SpeakDog == 0:
                $ SpeakDog = 1
                $ ar_b4_c1 = "c"
                pc "So you said you remembered something?"
                ard "History about what the dog knows of the two Arnolfinis leading to conclusion: They're related AND married. It was the 1400s."
                jump ArnolfiniInvestigate
    ard "Alright what do you think?"
    arm "Well?"
    arw "What is it? What are we?"
    menu:
        "They're married":
            $ ar_b4_c2 = "a"
        "They're just related":
            $ ar_b4_c2 = "b"
        "They're married AND related":
            $ ar_b4_c2 = "c"
    if ar_b4_c2 == "a":
        pc "You two are married. Simple as that."
        arm "We're married! That makes sense."
        arw "Completely. You know, we're here together. We're married. We must've loved each other at some point?"
        arm "Absolutely, we can work toward that!"
        arw "Though I think we should try a different feather in your hat. That might help."
        arm "But...but you gave this to me!"
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    if ar_b4_c2 == "b":
        pc "You two are related. I'd guess cousins?"
        arw "We're cousins! Oh, that makes sense."
        arm "Of course, I knew it!"
        arw "Sure you did."
        arm "Do you think our family is even bigger than just us?"
        arw "Oh no where do you think they are? Should we look for them? You! [player]! Can you get us out of this painting too?"
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    if ar_b4_c2 == "c":
        pc "I think you too are married...and related."
        arw "Oh..."
        arm "Oh no..."
        pc "Well it was the 1400s? If that helps? It wasn't that weird."
        arm "I don't know what you mean by that, but I guess this is fine?"
        arw "The family must've had a good reason, even if I don't like you like that."
        arm "What of my own parents? Were they too...related?"
        arw "Oh no, I don't like where this is going. I'm just not going to think about it. At least its settled."
        arm "Ugh, more or less."
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    pc "Well no matter what, it looks like you two— Giovanni and-"
    #change ARW name here
    $ arwName = "Carlotta"
    arw "It's Carlotta now. I'm workshopping it. Ethel's also a contender."
    pc "Giovanni and Carlotta-"
    ard "*Ahem*"
    pc "—you THREE seem to be pretty okay now."
    arw "Maybe we can finally make other friends? Ooh, like that Mona Lisa!"
    arm "Ooh, are those statues I've heard a bit about. They all have the same name!"
    pc "Well I think you've already made a friend outside of yourselves!"
    arm "...Who?"
    arw "Yes, who are you talking about?"
    pc "...Me. It's me. I'm your friend."
    arw "Oh...oh you! Yes, that's true. I'm sorry. Thank you so much again!"
    arm "Yes, thank you! You are really a friend. Well now what do we do?"
    ard "What if you two paid attention to me a bit for a change?"
    arw "Well I don't see why not!"
    arm "Who are you again?"
    ard "...we'll work on it."
    $ StoryCompletedTotal += 1
    $ beat_Arnolfini += 1
    jump FreeRoam

#complete
label .Outcome:
    if beat_Arnolfini == 5:
        "The Arnolfinis were a lot happier together. Sure, they still fought a bit, but they started making friends with nearby paintings and actually - finally - enjoyed each other's presence. The dog too!"
    elif beat_Arnolfini > 1:
        "The Arnolfinis were getting a long a bit better, but there arguments never ended, annoying all the surrounding pieces of art. If only you could've helped them reconcile..."
    else:
        "The Arnolfinis arguments grew more and more irate and every piece of art around them suffered for it, including the dog."
        "Eventually, the piece tore in two, separating them forever and leaving them all alone. Sure, they weren't arguing anymore, but now they had no one else to talk to."
    return