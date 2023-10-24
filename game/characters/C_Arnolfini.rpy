#Arnolfini
#This one is funky, needs to get overhauled based on Shane's conv design
default beat_Arnolfini = 1
default d_ArnolfiniLabel = "DEFAULT LABEL"
default end_Arnolfini = 0
default ArnolfiniTimeout = 0

label conv_Arnolfini:
    scene fineart_tod:
        blur 5
    show arnolfini at truecenter:
        zoom .7
        yoffset -100
    jump .use_action
    #ar "You're talking to me, the Arnolfini!"
    #menu:
    #    "Beat [beat_Arnolfini]" if actions > 0 and beat_Arnolfini <= 5:
    #        jump .use_action
    #    "Bye":
    #        ar "See ya"
    #        jump FreeRoam
    #    "Reset Beats":
    #        "Beats reset."
    #        $ beat_Arnolfini = 1
    #        jump conv_Arnolfini

label .use_action:
    #menu:
    #    ar "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        call advance_time from _call_advance_time
    #        jump expression "conv_Arnolfini" + "." + "Beat" + "%d" % beat_Arnolfini
    #    "No, not really.":
    #        ar "Understandable."
    #        jump FreeRoam
    #call advance_time from _call_advance_time
    $ ArnolfiniTimeout = 1
    jump expression "conv_Arnolfini" + "." + "Beat" + "%d" % beat_Arnolfini

label .Beat1:
    arm "Just admit you took it!"
    arw "No! And what about my brooch?"
    pc "Ahem."
    arw "Gio, someone's here! Oh, uh, hello!"
    arm "...hello."
    menu:
        "Hope everything's alright?":
            pass
        "You two are really loud, what's wrong?":
            pass
        "Can we please bring it down a few notches?":
            pass
    arw "Everythings totally fine...{i}if{/i} he would just admit he took my brooch!"
    arm "And my comb! I've had enough! I don't want to speak to you ever again!"
    arw "Do you even have hair under there that you need to comb?"
    arw "But anyway, hello. It's {i}so{/i} nice to meet you."
    arm "Yes, you seem great."
    arm "…"
    arm "Unlike someone."
    arw "Hmph."
    menu:
        "Well, can I help with anything?":
            arw "Only if you can tell {i}someone{/i} where they hid my most treasured brooch!"
            arm "I'm telling you I didn't take it! {i}You{/i} took something of {i}mine{/i}!"
        "You two are being very loud, just so you know.":
            arw "Loud? Us!?"
            arw "Gio, I told you this is why no one wants to talk to us!"
            arm "Who cares what everyone else thinks? I just want my comb back."
    arm "Anyway, I'm Giovanni."
    arw "I'm...actually do I even have a name?"
    menu:
        "You don't have a name?":
            arw "I...I don't think I do. Why haven't I thought about that?"
            arm "Maybe you were too busy stealing things that don't belong to you!"
            arw "Again, I didn't do anything!"
        "Who needs a name?":
            arw "Well I think I'd like to have one. His name is Giovanni, why can't I have one?"
            arm "Like you could have a better name than mine, anyway."
            arw "Ugh!"
        "You seem like an \"Ethel\" to me.":
            $ arwName = "Ethel?"
            arw "Ethel? I don't know..."
            arm "I knew an Ethel once. Just awful."
            arw "Please, I'm the only woman you've ever talked to."
            arm "That's not true! There's...there's..."
            #mis spelled?
            arw "You're going to say you talked to an \"Etel,\" aren't you?"
            arm "I wasn't...NO!"
    arm "Anyway you've caught us at an impasse. For you see, {i}she{/} has stolen something most precious to me!"
    menu:
        "Well didn't you take something of hers?":
            arm "I did no such thing!"
            arm "I'm very careful with all of my possessions. Note my beautiful hat, my wardrobe, that chandelier!"
            arm "I could go on but everything is just where it needs to be. As it should!"
            arm "Now when something is misplaced I notice! And my comb is GONE!"
            pc "Do you remember where it was?"
            arm "…"
            arm "No."
            arw "See? You don't even know where you had it in the first place. How do you know you didn't lose it yourself?"
        "Maybe if you {i}nicely{/i} asked for it back she'd give it to you?":
            arm "Ha! You must be new here."
            arw "Gio, they {i}are{/i} new here this is the first time we've met."
            arm "I... "
            arm "See what I mean!? She's impossible! A thief with a boorish tongue!"
            arw "Oh, please."
            arm "See? See!?"
            pc "She didn't say much."
            arm "Ah, but what she was thinking? We'll never know. It's probably just awful."
            "You get the sense the woman is rolling her eyes. Somehow."
        "Can you two even move? How could you steal from each other?":
            arm "Well I! I..."
            arw "Gio. {0}He's{/0}{1}She's{/1}{2}They're{/2} right."
            arm "Argh, you must've taken my comb! You must've!"
            arw "You're impossible!"
            arm "You're...you're..."
            arm "Incorrigible!"
            arw "Ugh, enough with the vocabulary! We get it! You like big words!"
    
    pc "Want me to just find the comb and brooch for you two? They're probably somewhere in the painting with you."
    arw "Oh, yes please! Lets put an end to this, I'd really appreciate it."
    arm "I'd appreciate it more."
    #minigame go here
    call minigamestart_arnolfini(1) from _call_minigamestart_arnolfini
    scene fineart_tod:
        blur 5
    show arnolfini at truecenter:
        zoom .7
        yoffset -100
    arw "My brooch! Oh, thank you, thank you, thank you!"
    arm "Yes, thank you!"
    arm "…"
    arw "…"
    arm "You have your brooch back, now can you stop standing so close to me? I can't breathe!"
    arw "I literally can't move. But I can breathe!"
    "She breathed."
    "Very hard."
    "In his face."
    arm "Ugh, stop it! Stop it!"
    arm "At least I can see you if you try to snatch something again!"
    arw "I didn't take it!"
    menu:
        "...I'll leave you two alone.":
            pass
        "[[Just silently try to leave]":
            pass
    ard "Psst! Hey! HEY!"
    "Was that the dog whispering at you?"
    menu:
        "You can talk too!?":
            ard "The dog talking is what's shocking to you?"
            pc "Fair enough."
        "[[Bark at the dog]":
            ard "Don't patronize me."
            ard "Now listen up!"    
    ard "It's never ending with these two! It looks like you actually got them to calm down-"
    arm "Is that your hair in my comb!?"
    arw "How would I even do that!?"
    ard "-sort of. Do you think you could help them learn to get along? It would mean the world!"   
    menu:
        "I guess I'll see what I can do.":
            ard "You'd be a life saver for little old me!"
        "Are you sure they're worth it?":
            ard "Listen I ask that sometimes too, but I'd do anything for some peace at this point."
        "Of course I'll help!":
            ard "Glad to hear it, thank you!"
    "As you walk away, you hear the Arnolfinis continue their arguing"
    arw "See, they're leaving! We can't make friends to save our lives!"
    arm "How is that my fault?"
    
    #####
    
    $ beat_Arnolfini += 1
    jump FreeRoam

label .Beat2:

    arw "{i}God, I need friends.{/i}"
    $ arwName = "Alessandra"
    arw "Also I never really introduced myself properly: I'm Alessandra."
    arm "Alessandra? A bit flowery for a name, don't you think?"
    arw "Thats rich coming from a Giovanni."
    arm "…"
    arm "Anyway, we're both so sorry for all of our quarreling. We just want some space, is all."
    arw "Yes, a private space. Away from each other."
    pc "Aren't you two married? You seem married."
    arw "Actually...are we? We are aren't we?"
    arm "I...I don't know. I've never thought about it."
    arw "Oh my god!"
    arm "Oh my god!"
    ard "Oh my god."
    menu:
        "You really never thought if you were married?":
            arw "Listen, I just was dealt the hand I got. Gio's here and...I don't know how we ended up togehter."
            arm "I mean it does look I'm vowing something to you. And we're touching hands!"
            arw "Ugh don't remind me. I wish I had gloves."
        "Well I mean maybe you aren't. I don't know.":
            arm "Right! It's not like we {i}chose{/i} to be stuck together like this, touching hands and everything!"
            arw "You have very clammy hands, by the way."
            arm "See, if I was your husband you'd {i}never{/i} say anything like that to me. You'd listen!"
            arw "Well good thing we probably aren't, I'd never agree to you being the head of any kind of household!"
            arw "The dog would be better at handling our affairs!"
            ard "Well, she's got a point."
            arm "Did you hear something?"
        "Alessandra, aren't you pregnant? It has to be Giovanni's!":
            arw "I...you can't just ask someone that!"
            arm "Sir, even {i}I{/i} know not to ask something like that and I can't stand her!"
            arw "And I'll have you know I have a very large pillow under here."
            arm "…"
            arm "Why do you have a pillow under your clothes?"
            arw "I have a hand sitting here and it keeps it comfy. Simple!"
    pc "Well if you two are stuck together, lets find some similary ground. What are your common interests?"
    arw "The finer things! Fabrics! Little baubles! Beautiful jewelry!"
    arm "...I like my comb."
    arw "But really, I have more issues with him then he does me! I need friends! Help me, not him!"
    arm "She has no respect for me! I'm suffering more! Help me instead!"
    ard "Hey, buddy! Hey! Just listen to me. I want them to both get along for their sakes."
    ard "And mine. Mostly mine. But still! Up to you."
    menu:
        "[[Help Arnolfini's...Wife? Sister? Cousin?]":
            $ ar_b2_c1 = "a"
            arw "Oh, thank you! I knew you'd see reason."
            arm "Really? Hmph! See if I speak to you ever again."
            ard "Good luck."
            arw "Come back in just a bit, won't you? I'm going to come up with some converstaion starters for when I make all my new besties!"
        "[[Help Giovanni]":
            $ ar_b2_c1 = "b"
            arm "Ha! Good choice."
            arw "Him? Really? I knew I was right about you."
            ard "Good luck..."
            arm "Let me get back to you in a bit. I think I have a way to finally get some respect around here!"
        "[[Help The Dog]":
            $ ar_b2_c1 = "c"
            ard "I judged you right. I have some ideas to make things work here. I'll talk to you later."
            arm "The dog? Really? Hmph!"
            arw "Uh, the dog? I knew I was right about you."
            ard "I can talk!"
            arw "Gio, you hear something?"
            arm "Nothing."
            ard "Ugh, they're oblivious."

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
        menu:
            "Let's maybe try something else.":
                arw "Oh...okay."
            "That could be painful with you two holding hands.":
                arw "Ah, good point. I do like this hand more than the other. I don't fancy losing it to {i}his{/i} side of the painting."
            "Sure, let be go grab a {i}BIG{/i} pair of scissors real quick!":
                arw "Oh, uh, on second thought, maybe not. Scissors sound a bit...barbaric."
        pc "I was getting the impression you wanted to make friends outside the painting?"
        arw "I mean...yes! Yes I want that."
        pc "What if we used your husband-"
        arw "Not my husband."
        arw "I think."
        pc "-your picture companion..."
        arw "...sure."
        pc "...as an example. Try being friends with him. You two are stuck together, anyway."
        arw "I guess its worth a shot. Giovanni!"
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
        menu:
            "I'm sure I'm not allowed to do that.":
                arm "Well why not!? Be like me and take charge!"
                arw "Ha! You? Taking charge? That'd be the day."
                arm "Hmph."
            "Would that even accomplish anything?":
                arm "Well...I guess not. We wouldn't be separated. Just a big line between us."
                arm "That wouldn't be fun to look at, would it?"
            "Sure, let me go get a big ol' permanent marker!":
                arm "Oh, a marker you say?"
                arm "…"
                arm "Well that wouldn't look good with my hat, would it? Forget I mentioned that."
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
        $ arwName = "Gertrude"
        arw "It's Gertrude today."
        arm "You look quite...nice today...Gertrude. I like your taste. I don't say that enough."
        arw "Well thank you!"
        arm "You always look lovely and you should take pride in that."
        arw "Same to you! I've always liked your, uh, hat!"
        arm "You think so? I was thinking that it needed a feather in it. I think you'd look lovely with a necklace!"
        arw "Really? I think so too!"
        pc "Look at you two! You haven't yelled in at least a minute!"
        ard "Finally!"
        arw "I have a thought! Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One final favor! We'll be the talk of the room!"
        

    if ar_b2_c1 == "c":
        $ CantDoThat = 0
        $ ABadIdea = 0
        $ MaybeSomethingElse = 0
        ard "Hey, you finally came by!"
        pc "Yeah! It seemed like you had some ideas, or an idea, of how to get thes two to get along? At least a little bit?"
        ard "Well I mean we could just separate them. Draw like a BIG line between them."
        menu:
            "Can't do that." if CantDoThat == 0:
                $ CantDoThat = 1
                pass
            "Oh that's a bad idea." if ABadIdea == 0:
                $ ABadIdea = 1
                pass
            "Maybe something else?" if MaybeSomethingElse == 0:
                $ MaybeSomethingElse = 1
                pass
        ard "What about ripping the whole thing in two? Dodging around me, of course."
        menu:
            "Can't do that." if CantDoThat == 0:
                $ CantDoThat = 1
                pass
            "Oh that's a bad idea." if ABadIdea == 0:
                $ ABadIdea = 1
                pass
            "Maybe something else?" if MaybeSomethingElse == 0:
                $ MaybeSomethingElse = 1
                pass
        ard "Ooh, I know! A strategic fire, just burn the painting in half! Easy!"
        menu:
            "Can't do that." if CantDoThat == 0:
                $ CantDoThat = 1
                pass
            "Oh that's a bad idea." if ABadIdea == 0:
                $ ABadIdea = 1
                pass
            "Maybe something else?" if MaybeSomethingElse == 0:
                $ MaybeSomethingElse = 1
                pass
        "The dog lets out a long, somewhat adorable sigh."
        ard "But you know? I actually like it here. The whole painting. I don't expect them to get along perfectly."
        ard "And they both have similar interests.They just have to communicate!"
        menu:
            "They actually have interests?":
                pass
            "Do they like anything beyond themselves?":
                pass
        ard "Listen its shallow, but have you seen the place we're in? It's beautiful. They like nice things."
        ard "Get them to compliment each others things. Their taste. I can coach you. If you haven't noticed they don't really pay attention to me. Watch."
        "You hear what sounds like the dog passing gas."
        arm "Ugh, did you do that!?"
        arw "Wasn't me! Gross, it had to have been you!"
        ard "See? I don't exist to them."
        menu:
            "Alright, I'll try.":
                pass
            "I guess I'll give it a go.":
                pass
            "Let's go, marriage counseling!":
                pass
        pc "Hi, you two!"
        arw "What is it?"
        arm "We have nothing to say to you."
        ard "They want to make friends! Mention that!"
        menu:
            "I couldn't help but notice you two wanted to make friends outside of well, yourselves.":
                arm "I mean..."
                arw "It's true! It's extremely true."
            "It seems like you two wish the other respected you more?":
                arw "Well..."
                arm "Yes! More than anything!"
        ard "Remember: they should really befriend each other first!"
        pc "What if you started with each other?"
        arm "Pardon?"
        pc "Try being friends. Respecting each other. If you can make that work, anything else should be a cake walk."
        ard "Perfect!"
        pc "I mean, you two are already husband and wife."
        arw "Not my husband.  "
        arm "Not my wife.  "
        arw "I don't think..."
        pc "Your photo companion?"
        arm "Meh."
        arw "Sure."
        pc "Just...try?"
        arw "Fine. If he won't try first I guess I will."
        arw "Giovanni. That comb you found. It's...nice. You have good taste."
        arm "Really? Thats nice of you to say. Should I be suspicious?"
        arw "No! I don't talk about it enough. It suits you. Your hat does too."
        arm "You know, I was thinking of adding a feather to it. Or at least imagining a feather."
        arw "Oh, that'd be nice!"
        arm "I think a new necklace would look nice on you as well...whats your name again?"
        $ arwName = "Gertrude"
        arw "It's Gertrude today."
        arm "It looks good...Gertrude. I like your taste. I don't say that enough."
        arw "Really? Well thank you!"
        menu:
            "Look at you two! You haven't yelled in at least a minute!":
                ard "I'll take a minute of peace!"
            "See? You can be friends! Or at least friendly!":
                ard "Friendly's good! The bare minimum!"
            "Look, you can exist together! Sort of!":
                ard "One moment's peace is something. I can take that."
        arw "I have a thought! Do you think you could help us find these things for each other?"
        arm "Yes that'd be so nice of you! One final favor! We'll be the talk of the room!"
    arw "Ooh, I'd love a beautiful necklace, it'd go so nicely with my brooch!"
    arm "...Can I have another comb?"
    arw "Gio! Really?"
    arm "Fine. What about a feature for my hat? Can you find these things for us?"
    arw "I'm sure they can! They have to be around here somewhere."
    call minigamestart_arnolfini(2) from _call_minigamestart_arnolfini_1
    scene fineart_tod:
        blur 5
    show arnolfini at truecenter:
        zoom .7
        yoffset -100
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
    pc "Oh no."
    pc "Oh shit."
    arw "No, no! Like, are we married? Frankly I never thought about it, I just assumed."
    arm "That's a good question. I know we mentioned it recently, but I'm still not sure. Does the dog know?"
    ard "Don't look at me. I tuned you two out ages ago."
    arw "Now that we can agree on some things, I'd really love to know. It's always been in the back of my mind."
    arm "Well could we be blood relatives? Or is it really marriage?"
    arw "…"
    menu:
        "What are you thinking?":
            pass
        "Did you remember something?":
            pass
        "Should I be concerned?":
            pass
    arw "…"
    arw "...what if we're both?"
    arm "Oh no."
    arw "Oh no."
    menu:
        "Oh no.":
            pass
        "Oh shit.":
            pass
        "Oh fuck.":
            pass
    arm "…"
    arw "…"
    ard "I think they need some time to process...whatever this is. Talk to you later, okay?"

####
    $ beat_Arnolfini += 1
    jump FreeRoam

label .Beat4:
    ard "Hi again! These two have been...eerily silent."
    arm "…"
    arw "…"
    arw "...we just dont know what to think!"
    arm "...what ARE we!?"
    menu:
        "Does it really matter if you're getting along?":
            arm "Of course it does!"
        "Who cares if you're maybe married and/or related?":
            arm "Well {i}we{/i} care!"
        "[[Lie] I really don't think it's that big of a deal!":
            arm "You've got to be kidding."
    arw "What would the other pieces of art think if we didn't know? How would we even introduce ourselves!?"
    pc "Well lets look at what you have argued about and maybe we can figure this out."
    arw "I prefer \"discussion with force.\""
    ard "I've seen the PC doing a lot of cleaning, lets see if it can jog you two's memories."
    ard "Maybe there's an answer outside of the painting?"
    pc "Hey, it's worth a shot!"
    call minigamestart_cleaning_arnolfini from _call_minigamestart_cleaning_arnolfini
    scene fineart_tod:
        blur 5
    show arnolfini at truecenter:
        zoom .7
        yoffset -100
    #Dialogue	ArnolfiniMan	Ah, food! I've always wanted to try it! That reminds me of the time we had some at...I want to say a party?				Bag of Chips
    #Dialogue	ArnolfiniWoman	What were we celebrating, i wonder?				Bag of Chips
    #Dialogue	ArnolfiniWoman	A drink vessel! Rather plain, isn't it?				Bottle
    #Dialogue	ArnolfiniMan	A drink must always be in the finest glass! You know, like when we visited family that one time!				Bottle
    #Dialogue	ArnolfiniWoman	My family? Your family? Both of ours? I don't remember...				Bottle
    #Dialogue	ArnolfiniMan	I think I killed a man once.				Red Stain
    #Dialogue	ArnolfiniWoman	I...don't know how to respond to that.				Red Stain
    #Dialogue	ArnolfiniWoman	Oh, I love the color green! I remember a previous outfit I had that was that color. It came with a veil!				Green Stain
    #Dialogue	ArnolfiniMan	A veil? Like a wedding?				Green Stain
    #Dialogue	ArnolfiniWoman	Ugh, if only I could recall!				Green Stain
    #Dialogue	ArnolfiniMan	Now those are nowhere near as fancy as what we wear.				Socks
    #Dialogue	ArnolfiniWoman	Didn't we get those as children one Christmas? Together?				Socks
    #Dialogue	ArnolfiniMan	Yes, we grew up together! But were we family or betrothed? Or both?				Socks
    #Dialogue	ArnolfiniDog	I have this really intense desire to chew on those socks right now. Can you put them away before I lose any restraint?				Socks
    ### minigame go here
    #meta "Clean up various objects that each of the Arnolfini's finds relatable to their interests. Don't know if we have design implementation for specific objects in the minigmae, but I can tailor the writing to what is available if not."
    ard "Well anything? Some kind of memory jogged?"
    arw "Let me think..."
    arm "...I've got nothing."
    arw "No, not a clue. I really don't know. Great job cleaning though!"
    menu:
        "Gee. Thanks.":
            pass
        "It's all in the wrist.":
            pass
        "I really wish I knew how half of stains showed up.":
            pass
    "She doesn't really notice you respond."
    arw "Look, Gio, I complimented them!"
    arm "Ooh, so that's how it works with other people."
    ard "PC, can you maybe talk to them one-on-one?"
    ard "I don't think we're getting anywhere with this. Maybe talk to them one-on-one and see if there's any kind of clue?"
    pc "Think that'd work?"
    ard "Yeah, just go with your intution. Come talk to me too, I may remember something."
    $ SpeakGiovanni = 0
    $ SpeakWoman = 0
    $ SpeakDog = 0
    label ArnolfiniInvestigate:
        menu:
            "[[Speak to Giovanni]" if SpeakGiovanni == 0:
                $ SpeakGiovanni = 1
                $ ar_b4_c1 = "a"
                pc "Do you remember anything from your past that might help define you two's relationship?"
                arm "Now she mentioned a previous green dress with a veil...I remember that. I'm not one hundred percent sure but..."
                arm "...I really think it was at a wedding. Our wedding. I could be wrong, though."
                jump ArnolfiniInvestigate
            "[[Speak to Gertrude]" if SpeakWoman == 0:
                $ SpeakWoman = 1
                $ ar_b4_c1 = "b"
                pc "What can you tell me about your history with Giovanni? Maybe there's something we're missing."
                arw "Now about those socks – I really do remember getting them as a gift. And Gio was there!"
                arw "I can't speak with total authority, but I feel like we're just cousins. We're related, not married."
                jump ArnolfiniInvestigate
            "[[Speak to the Dog]" if SpeakDog == 0:
                $ SpeakDog = 1
                $ ar_b4_c1 = "c"
                ard "So you said you remembered something?"
                ard "All that crud you cleaned up? I think they're both right with what they remember."
                ard "The green veil? That was their wedding. And the socks at Christmas? I think they're cousins. They grew up together."
                ard "I can't be sure, but I think they're married {i}and{/} related."
                jump ArnolfiniInvestigate
    pc "Alright, I guess that's all the information I'm going to get."
    ard "Alright what do you think?"
    arm "Well?"
    arw "What is it? What are we?"
    menu:
        "You're married.":
            $ ar_b4_c2 = "a"
        "You're just related. Cousins, probably.":
            $ ar_b4_c2 = "b"
        "You're married {i}and{/i} you're related.":
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
        arw "Oh no where do you think they are? Should we look for them? You! [pc_name]! Can you get us out of this painting too?"
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    if ar_b4_c2 == "c":
        pc "I think you too are married...and related."
        arw "Oh..."
        arm "Oh no..."
        pc "Well it was the 1400s? If that helps? It wasn't {i}that{/i} weird...I think."
        arm "I don't really know what you mean by that, but I guess this is fine?"
        arw "The family must've had a good reason, even if I don't like you like that."
        arm "What of my own parents? Were they too...related?"
        arw "…"
        arm "…"
        arw "I don't like where this is going. I'm just not going to think about it. At least its settled."
        arm "Ugh, more or less."
        ard "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm "Yes, thank you!"
        arw "We won't forget this!"
    pc "Well no matter what, it looks like you two— Giovanni and-"
    $ arwName = "Carlotta"
    arw "It's Carlotta now. I'm workshopping it. I'm actually circling back on Ethel, maybe."
    pc "Giovanni and Carlotta-"
    ard "*Ahem*"
    pc "—you THREE seem to be pretty okay now. More or less."
    arw "Maybe we can finally make other friends? Ooh, like that Mona Lisa!"
    arm "Ooh, there are those statues I've heard a bit about. They all have the same name!"
    pc "Well I think you've already made a friend outside of yourselves!"
    arm "...Who?"
    arw "Yes, who are you talking about?"
    menu:
        "...Me. It's me. I'm your friend.":
            arw "Oh...oh you! Yes, that's true. I'm sorry. Thank you so much again!"
            arm "Yes, thank you! You are really a friend. Well now what do we do?"
        "...never mind.":
            arw "Well, whatever you say!"
            arm "Yes, yes. Well now what do we do?"
        "Forget I said anything. Look! You aren't arguing as much!":
            arw "Yes, its nice not to be so aggrieved all the time for once."
            arm "Ooh, I like that word! Well now what do we do?"






    ard "What if you two paid attention to me a bit for a change?"
    arw "I don't see why not!"
    arm "Who are you again?"
    ard "…"
    ard "We'll work on it."
    $ StoryCompletedTotal += 1
    $ beat_Arnolfini += 1
    jump FreeRoam

#complete
label .Outcome:
    if beat_Arnolfini == 5:
        scene fineart_tod:
            blur 5
        show arnolfini at truecenter:
            zoom .7
            yoffset -100
        "The Arnolfinis were a lot happier together."
        "Sure, they still fought a bit, but they started making friends with nearby paintings and actually - finally - enjoyed each other's presence."
        "The dog too!"
    elif beat_Arnolfini > 1:
        scene fineart_tod:
            blur 5
        show arnolfini at truecenter:
            zoom .7
            yoffset -100
        "The Arnolfinis were getting a long a bit better, but there arguments never ended, annoying all the surrounding pieces of art."
        "If only you could've helped them reconcile..."
    else:
        scene fineart_tod:
            blur 5
        show arnolfini at truecenter:
            zoom .7
            yoffset -100
        "The Arnolfinis arguments grew more and more irate and every piece of art around them suffered for it, including the dog."
        "Eventually, the piece tore in two, separating them forever and leaving them all alone."
        "Sure, they weren't arguing anymore, but now they had no one else to talk to."
    return