#Arnolfini
#This one is funky, needs to get overhauled based on Shane's conv design
default beat_Arnolfini = 1
default d_ArnolfiniLabel = "DEFAULT LABEL"
default end_Arnolfini = 0
default ArnolfiniTimeout = 0
default ArnolfiniDecoration = 0
image arnolfiniportrait = ConditionSwitch(
    "ArnolfiniDecoration == 0", "images/Characters/Arnolfini/Arnolfini.jpg",
    "ArnolfiniDecoration == 1", "images/Characters/Arnolfini/Arnolfini_Decorated.jpg"
)

label conv_Arnolfini:
    play music "music/B14_W_02.wav" fadein 0.4 volume 0.4
    scene fineart_tod:
        blur 5
    show arnolfiniportrait at truecenter:
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
    arm neutral "Just admit you took it!"
    arw neutral "No! And what about my brooch?"
    pc  "Ahem."
    arw panic "Gio, someone's here! Oh, uh, hello!"
    arm neutral "…Hello."
    menu:
        "Hope everything's alright?":
            pass
        "You two are really loud, what's wrong?":
            pass
        "Can we please bring it down a few notches?":
            pass
    arw neutral "Everything's totally fine…{i}if{/i} he would just admit he took my brooch!"
    arm angry "And my comb! I've had enough! I don't want to speak to you ever again!"
    arw neutral "Do you even have hair under there that you need to comb?"
    arw neutral "But anyway, hello. It's {i}so{/i} nice to meet you."
    arm neutral "Yes, you seem great."
    arm dots "…"
    arm angry "Unlike someone."
    arw angry "Hmph."
    menu:
        "Well, can I help with anything?":
            arw neutral "Only if you can tell {i}someone{/i} where they hid my most treasured brooch!"
            arm neutral "I'm telling you I didn't take it! {i}You{/i} took something of {i}mine{/i}!"
        "You two are being very loud, just so you know.":
            arw surprise "Loud? Us!?"
            arw neutral "Gio, I told you this is why no one wants to talk to us!"
            arm neutral "Who cares what everyone else thinks? I just want my comb back."
    arm neutral "Anyway, I'm Giovanni."
    arw confused "I'm…actually do I even have a name?"
    menu:
        "You don't have a name?":
            arw confused "I…I don't think I do. Why haven't I thought about that?"
            arm neutral "Maybe you were too busy stealing things that don't belong to you!"
            arw neutral "Again, I didn't do anything!"
        "Who needs a name?":
            arw neutral "Well, I think I'd like to have one. His name is Giovanni, why can't I have one?"
            arm neutral "Like you could have a better name than mine, anyway."
            arw confused "Ugh!"
        "You seem like an \"Ethel\" to me.":
            $ arwName = "Ethel?"
            arw question "Ethel? I don't know…"
            arm neutral "I knew an Ethel, once. Just awful."
            arw neutral "Please, I'm the only woman you've ever talked to."
            arm panic "That's not true! There's… there's…"
            arw neutral "You're going to say you talked to an \"Ethel,\" aren't you?"
            arm panic "I wasn't… NO!"
    arm neutral "Anyway, you've caught us at an impasse. For you see, {i}she{/i} has stolen something most precious to me!"
    menu:
        "Well didn't you take something of hers?":
            arm neutral "I did no such thing!"
            arm neutral "I'm very careful with all of my possessions. Note my beautiful hat, my wardrobe, that chandelier!"
            arm neutral "I could go on but everything is just where it needs to be. As it should!"
            arm neutral "Now when something is misplaced I notice! And my comb is GONE!"
            pc  "Do you remember where it was?"
            arm dots "…"
            arm neutral  "No."
            arw neutral "See? You don't even know where you had it in the first place. How do you know you didn't lose it yourself?"
        "Maybe if you asked {i}nicely{/i} for it back, she'd give it to you?":
            arm neutral "Ha! You must be new here."
            arw neutral "Gio, [they] {i}{0}is{/0}{1}is{/1}{2}are{/2}{/i} new here. This is the first time we've met."
            arm neutral "I… "
            arm angry "See what I mean!? She's impossible! A thief with a boorish tongue!"
            arw neutral "Oh, please."
            arm neutral "See? See!?"
            pc  "She didn't say much."
            arm neutral "Ah, but what she was thinking? We'll never know. It's probably just awful."
            "You get the sense the woman is rolling her eyes. Somehow."
        "Can you two even move? How could you steal from each other?":
            arm surprise "Well I! I…"
            arw neutral "Gio.[they!c] [are] right."
            arm angry "Argh, you must've taken my comb! You must've!"
            arw angry "You're impossible!"
            arm neutral "You're… you're…"
            arm neutral "Incorrigible!"
            arw neutral "Ugh, enough with the vocabulary! We get it! You like big words!"
    
    pc  "Want me to find the comb and brooch for you two? They're probably somewhere in the painting with you."
    arw bulb "Oh, yes, please! Let's put an end to this, I'd really appreciate it."
    arm neutral "I'd appreciate it more."
    #minigame go here
    call minigamestart_arnolfini(1) from _call_minigamestart_arnolfini
    scene fineart_tod:
        blur 5
    show arnolfiniportrait at truecenter:
        zoom .7
        yoffset -100
    arw happy "My brooch! Oh, thank you, thank you, thank you!"
    arm happy "Yes, thank you!"
    arm dots "…"
    arw dots "…"
    arm neutral "You have your brooch back, now can you stop standing so close to me? I can't breathe!"
    arw neutral "I literally can't move. But I can breathe!"
    "She breathes."
    "Very hard."
    "In his face."
    arm panic "Ugh, stop it! Stop it!"
    arm neutral "At least I can see you if you try to snatch something again!"
    arw neutral "I didn't take it!"
    menu:
        "…I'll leave you two alone.":
            pass
        "[[Just silently try to leave]":
            pass
    ard bulb "Psst! Hey! HEY!"
    "Was that the dog whispering at you?"
    menu:
        "You can talk too!?":
            ard neutral "The dog talking is what's shocking to you?"
            pc  "Fair enough."
        "[[Bark at the dog]":
            ard sad "Don't patronize me."
            ard neutral "Now listen up!"    
    ard neutral "It's never ending with these two! It looks like you actually got them to calm down–"
    arm neutral "Is that your hair in my comb!?"
    arw neutral "How would I even do that!?"
    ard neutral "–sort of. Do you think you could help them learn to get along? It would mean the world!"  
    menu:
        "I guess I'll see what I can do.":
            ard sparkle "You'd be a life saver for little old me!"
        "Are you sure they're worth it?":
            ard neutral "Listen, I ask that sometimes too; but I'd do anything for some peace at this point."
        "Of course I'll help!":
            ard sparkle "Glad to hear it, thank you!"
    "As you walk away, you hear the Arnolfinis continue their arguing"
    arw neutral "See, they're leaving! We can't make friends to save our lives!"
    arm neutral "How is that my fault?"
    
    #####
    
    $ beat_Arnolfini += 1
    jump FreeRoam

label .Beat2:

    arw neutral "Thanks for coming back, I thought you'd never return! Haha…"
    arw sigh "{i}God, I need friends.{/i}"
    $ arwName = "Alessandra"
    arw neutral "Also, I never really introduced myself properly: I'm Alessandra."
    arm neutral "Alessandra? A bit flowery for a name, don't you think?"
    arw neutral "That's rich coming from a Giovanni."
    arm dots "…"
    arm neutral "Anyway, we're both so sorry for all of our quarreling. We just want some space, is all."
    arw neutral "Yes, a private space. Away from each other."
    pc  "Aren't you two married? You seem married."
    arw question "Actually…are we? We are, aren't we?"
    arm questions "I…I don't know. I've never thought about it."
    arw panic "Oh my God!"
    arm panic "Oh my God!"
    ard sigh "Oh my God."
    menu:
        "You really never considered if you were married?":
            arw neutral "Listen, I just was dealt the hand I got. Gio's here and…I don't know how we ended up together."
            arm neutral "I mean it does look like I'm vowing something to you. And we're touching hands!"
            arw neutral "Ugh, don't remind me. I wish I had gloves."
        "Well, I mean, maybe you aren't. I don't know.":
            arm neutral "Right! It's not like we {i}chose{/i} to be stuck together like this, touching hands and everything!"
            arw neutral "You have very clammy hands, by the way."
            arm angry "See, if I were your husband you'd {i}never{/i} say anything like that to me. You'd listen!"
            arw neutral "Well, good thing we probably aren't. I'd never agree to you being the head of any kind of household!"
            arw neutral "The dog would be better at handling our affairs!"
            ard neutral "Well, she's got a point."
            arm neutral "Did you hear something?"
        "Alessandra, aren't you pregnant? It has to be Giovanni's!":
            arw panic "I…you can't just ask someone that!"
            arm laugh "{0}Sir{/0}{1}Ma'am{/1}{2}Friend{/2}, even {i}I{/i} know not to ask something like that and I can't stand her!"
            arw neutral "And I'll have you know I have a very large pillow under here."
            arm dots "…"
            arm neutral "Why do you have a pillow under your clothes?"
            arw happy "I have a hand sitting here and it keeps it comfy. Simple!"
    pc  "Well, if you two are stuck together, let's find some similar ground. What are your common interests?"
    arw sparkles "The finer things! Fabrics! Little baubles! Beautiful jewelry!"
    arm dots "… I like my comb."
    arw neutral "But really, I have more issues with him then he does me! I need friends! Help me, not him!"
    arm neutral "She has no respect for me! I'm suffering more! Help me instead!"
    ard neutral "Hey, buddy! Hey! Just listen to me. I want them both to get along for their sakes."
    ard neutral "And mine. Mostly mine. But still! Up to you."
    menu:
        "[[Help Arnolfini's…Wife? Sister? Cousin?]":
            $ ar_b2_c1 = "a"
            arw happy "Oh, thank you! I knew you'd see reason."
            arm angry "Really? Hmph! See if I speak to you ever again."
            ard neutral "Good luck."
            arw neutral "Come back in just a bit, won't you? I'm going to come up with some conversation starters for when I make all my new besties!"
        "[[Help Giovanni]":
            $ ar_b2_c1 = "b"
            arm happy "Ha! Good choice."
            arw angry "Him? Really? I knew I was right about you."
            ard neutral "Good luck…"
            arm neutral "Let me get back to you in a bit. I think I have a way to finally get some respect around here!"
        "[[Help The Dog]":
            $ ar_b2_c1 = "c"
            ard happy "I judged you right. I have some ideas to make things work, here. I'll talk to you later."
            arm angry "The dog? Really? Hmph!"
            arw angry "Uh, the dog? I knew I was right about you."
            ard neutral "I can talk!"
            arw neutral "Gio, did you hear something?"
            arm neutral "Nothing."
            ard confused "Ugh, they're oblivious."

    ####
    $ beat_Arnolfini += 1
    jump FreeRoam
label .Beat3:
    #choice a
    if ar_b2_c1 == "a":
        arw neutral "There you are! I'm trying a new name today. Alessandra was passé, you know?"
        #change ARW name here
        $ arwName = "Gertrude"
        arw sparkles "Now, how about this: Gertrude. Beautiful, no?"
        pc  "I think whatever you want works best."
        arw happy "Thank you! Nice to see some approval around here."
        arw neutral "Now then, any ideas on how we can separate? What if we ripped the painting in two? Clean in half!"
        menu:
            "Let's maybe try something else.":
                arw sigh "Oh…okay."
            "That could be painful with you two holding hands.":
                arw panic "Ah, good point. I do like this hand more than the other. I don't fancy losing it to {i}his{/i} side of the painting."
            "Sure, let me go grab a {i}BIG{/i} pair of scissors real quick!":
                arw sweat "Oh, uh, on second thought, maybe not. Scissors sound a bit…barbaric."
        pc  "I was getting the impression you wanted to make friends outside the painting?"
        arw sparkle "I mean…yes! Yes, I want that."
        pc  "What if we used your husband–"
        arw neutral "Not my husband."
        arw sweat "I think."
        pc  "–your picture companion…"
        arw neutral "… Sure."
        pc  "… as an example. Try being friends with him. You two are stuck together, anyway."
        arw neutral "I guess it's worth a shot. Giovanni!"
        arw question "I like, uh, your taste in combs?"
        arm sparkle "Really? That's nice of you to say"
        arw neutral "Well, I don't talk about it enough. You have, dare I say, good taste! I mean, your hat–"
        arm happy "Ooh, I was thinking of adding a feather to it. Or at least imagining a feather."
        arw happy "That'd be nice! Don't you agree, [pc_name]?"
        pc  "I agree!"
        arm neutral "…I think a new necklace would look nice on you as well."
        arw surprise "Oh, wouldn't it?"
        pc  "Look at you two! You haven't yelled in at least a minute!"
        ard neutral "Finally!"
        arw neutral "I have a thought! Do you think you could help us find these things for each other?"
        arm sparkle "Yes that'd be so nice of you! One final favor! We'll be the talk of the room!"
    if ar_b2_c1 == "b":
        arm sparkle "Welcome back! Thank you for listening to me, the reasonable one!"
        arw neutral "Hmph."
        arm neutral "Now about us having our own space. How about you add a very thick line between us."
        arm sparkles "VERY thick."
        menu:
            "I'm sure I'm not allowed to do that.":
                arm neutral "Well, why not!? Be like me and take charge!"
                arw laugh "Ha! You? Taking charge? That'd be the day."
                arm neutral "Hmph."
            "Would that even accomplish anything?":
                arm neutral "Well…I guess not. We wouldn't be separated. Just a big line between us."
                arm neutral "That wouldn't be fun to look at, would it?"
            "Sure, let me go get a big ol' permanent marker!":
                arm neutral "Oh, a marker you say?"
                arm dots "…"
                arm neutral "Well that wouldn't look good with my hat, would it? Forget I mentioned that."
        pc  "What if you tried to look outside of your frame a bit? Don't you want to make some friends?"
        arm neutral "Well…yes…"
        pc  "But you two bicker so much, how could anyone else ever get a word in?"
        ard sigh "Preach."
        arm neutral "What am I supposed to do about that!"
        pc  "Well, what if you started off being friends with your wife—"
        arm neutral "Not my wife."
        arm sweat "I think."
        pc  "–your picture companion…"
        arm neutral "I'll accept that."
        pc  "Just try to make amends. You're stuck with each other, you should at least try to enjoy each other's company."
        arm neutral "I'll try. I guess. Ahem!"
        arw neutral "Yes?"
        arm neutral "You… what's your name again?"
        $ arwName = "Gertrude"
        arw neutral "It's Gertrude today."
        arm neutral "You look quite…nice today…Gertrude. I like your taste. I don't say that enough."
        arw happy "Well, thank you!"
        arm neutral "You always look lovely, and you should take pride in that."
        arw neutral "Same to you! I've always liked your, uh, hat!"
        arm sparkle "You think so? I was thinking that it needed a feather in it. I think you'd look lovely with a necklace!"
        arw sparkles "Really? I think so, too!"
        pc  "Look at you two! You haven't yelled in at least a minute!"
        ard sigh "Finally!"
        arw neutral "I have a thought! Do you think you could help us find these things for each other?"
        arm neutral "Yes that'd be so nice of you! One final favor! We'll be the talk of the room!"
        

    if ar_b2_c1 == "c":
        $ CantDoThat = 0
        $ ABadIdea = 0
        $ MaybeSomethingElse = 0
        ard happy "Hey, you finally came by!"
        pc  "Yeah! It seemed like you had some ideas, or an idea, of how to get these two to get along? At least a little bit?"
        ard neutral "Well, I mean we could just separate them. Draw like a BIG line between them."
        menu:
            "Can't do that." if CantDoThat == 0:
                $ CantDoThat = 1
                pass
            "Oh, that's a bad idea." if ABadIdea == 0:
                $ ABadIdea = 1
                pass
            "Maybe something else?" if MaybeSomethingElse == 0:
                $ MaybeSomethingElse = 1
                pass
        ard neutral "What about ripping the whole thing in two? Dodging around me, of course."
        menu:
            "Can't do that." if CantDoThat == 0:
                $ CantDoThat = 1
                pass
            "Oh, that's a bad idea." if ABadIdea == 0:
                $ ABadIdea = 1
                pass
            "Maybe something else?" if MaybeSomethingElse == 0:
                $ MaybeSomethingElse = 1
                pass
        ard bulb "Ooh, I know! A strategic fire, just burn the painting in half! Easy!"
        menu:
            "Can't do that." if CantDoThat == 0:
                $ CantDoThat = 1
                pass
            "Oh, that's a bad idea." if ABadIdea == 0:
                $ ABadIdea = 1
                pass
            "Maybe something else?" if MaybeSomethingElse == 0:
                $ MaybeSomethingElse = 1
                pass
        "The dog lets out a long, somewhat adorable sigh."
        ard neutral "But you know? I actually like it here. The whole painting. I don't expect them to get along perfectly."
        ard neutral "They both have similar interests. They just have to communicate!"
        menu:
            "They actually have interests?":
                pass
            "Do they like anything beyond themselves?":
                pass
        ard neutral "Listen, it's shallow, but have you seen the place we're in? It's beautiful. They like nice things."
        ard neutral "Get them to compliment each others' things. Their taste. I can coach you. If you haven't noticed, they don't really pay attention to me. Watch."
        "You hear what sounds like the dog passing gas."
        arm sad "Ugh, did you do that!?"
        arw sad "Wasn't me! Gross, it had to have been you!"
        ard neutral "See? I don't exist to them."
        menu:
            "Alright, I'll try.":
                pass
            "I guess I'll give it a go.":
                pass
            "Let's go, marriage counseling!":
                pass
        pc  "Hi, you two!"
        arw neutral "What is it?"
        arm neutral "We have nothing to say to you."
        ard neutral "They want to make friends! Mention that!"
        menu:
            "I couldn't help but notice you two wanted to make friends outside of, well, yourselves.":
                arm neutral "I mean…"
                arw panic "It's true! It's extremely true."
            "It seems like you two wish the others respected you more?":
                arw neutral "Well…"
                arm panic "Yes! More than anything!"
        ard neutral "Remember: they should really befriend each other first!"
        pc  "What if you started with each other?"
        arm question "Pardon?"
        pc  "Try being friends. Respecting each other. If you can make that work, anything else should be a cake walk."
        ard sparkle "Perfect!"
        pc  "I mean, you two are already husband and wife."
        arw neutral "Not my husband.  "
        arm neutral "Not my wife.  "
        arw neutral "I don't think…"
        pc  "Your painting companion?"
        arm neutral "Meh."
        arw neutral "Sure."
        pc  "Just…try?"
        arw neutral "Fine. If he won't try first, I guess I will.."
        arw neutral "Giovanni. That comb you found. It's…nice. You have good taste."
        arm neutral "Really? That's nice of you to say. Should I be suspicious?"
        arw neutral "No! I don't talk about it enough. It suits you. Your hat does, too."
        arm sparkle "You know, I was thinking of adding a feather to it. Or at least imagining a feather."
        arw happy "Oh, that'd be nice!"
        arm neutral "I think a new necklace would look nice on you as well…what's your name again?"
        $ arwName = "Gertrude"
        arw neutral "It's Gertrude today."
        arm neutral "It looks good…Gertrude. I like your taste. I don't say that enough."
        arw sparkle "Really? Well, thank you!"
        menu:
            "Look at you two! You haven't yelled in at least a minute!":
                ard sigh "I'll take a minute of peace!"
            "See? You can be friends! Or at least friendly!":
                ard happy "Friendly's good! The bare minimum!"
            "Look, you can exist together! Sort of!":
                ard sigh "One moment's peace is something. I can take that."
        arw neutral "I have a thought! Do you think you could help us find these things for each other?"
        arm neutral "Yes, that'd be so nice of you! One final favor! We'll be the talk of the room!"
    arw sparkles "Ooh, I'd love a beautiful necklace, it'd go so nicely with my brooch!"
    arm neutral "… Can I have another comb?"
    arw neutral "Gio! Really?"
    arm neutral "Fine. What about a feather for my hat? Can you find these things for us?"
    arw neutral "I'm sure [they] can! They have to be around here somewhere."
    call minigamestart_arnolfini(2) from _call_minigamestart_arnolfini_1
    $ ArnolfiniDecoration = 1
    scene fineart_tod:
        blur 5
    show arnolfiniportrait at truecenter:
        zoom .7
        yoffset -100
    arw happy "Oh, thank you, this is just lovely!"
    arm happy "Yes, thank you!"
    ard happy "Thank you SO MUCH! Finally! Some peace!"
    arm neutral "The dog can talk?"
    ard sad "If I could move my eyes they'd be rolling right now."
    arw neutral "Well, anyway. There's something that's been on my mind, lately."
    arm neutral "Tell me! Anything!"
    arw neutral "What…are we?"
    arm neutral "Like, existentially?"
    pc  "Oh boy."
    pc  "Oh no."
    pc  "Oh shit."
    arw neutral "No, no! Like, are we married? Frankly, I've never thought about it, I just assumed."
    arm neutral "That's a good question. I know we mentioned it recently, but I'm still not sure. Does the dog know?"
    ard neutral "Don't look at me. I tuned you two out ages ago."
    arw neutral "Now that we can agree on some things, I'd really love to know. It's always been in the back of my mind."
    arm neutral "Well, could we be blood relatives? Or is it really marriage?"
    arw neutral "…"
    menu:
        "What are you thinking?":
            pass
        "Did you remember something?":
            pass
        "Should I be concerned?":
            pass
    arw dots "…"
    arw neutral "…What if we're both?"
    arm sweat "Oh no."
    arw sweat "Oh no."
    menu:
        "Oh no.":
            pass
        "Oh shit.":
            pass
        "Oh fuck.":
            pass
    arm dots "…"
    arw dots "…"
    ard neutral "I think they need some time to process…whatever this is. Talk to you later, okay?"

####
    $ beat_Arnolfini += 1
    jump FreeRoam

label .Beat4:
    ard neutral "Hi, again! These two have been…eerily silent."
    arm dots "…"
    arw dots "…"
    arw panic "… We just don't know what to think!"
    arm panic "… What ARE we!?"
    menu:
        "Does it really matter if you're getting along?":
            arm angry "Of course it does!"
        "Who cares if you're maybe married and/or related?":
            arm angry "Well {i}we{/i} care!"
        "[[Lie] I really don't think it's that big of a deal!":
            arm sweat "You've got to be kidding."
    arw panic "What would the other pieces of art think if we didn't know? How would we even introduce ourselves!?"
    pc  "Well, let's look at what you've argued about and maybe we can figure this out."
    arw neutral "I prefer \"discussed with force.\""
    ard neutral "I've seen the PC doing a lot of cleaning, lets see if it can jog you two's memories."
    ard neutral "Maybe there's an answer outside of the painting?"
    pc  "Hey, it's worth a shot!"
    call minigamestart_cleaning_arnolfini from _call_minigamestart_cleaning_arnolfini
    scene fineart_tod:
        blur 5
    show arnolfiniportrait at truecenter:
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
    ard neutral "Well, anything? Some kind of memory jogged?"
    arw neutral "Let me think…"
    arm neutral "…I've got nothing."
    arw neutral "No, not a clue. I really don't know. Great job cleaning though!"
    menu:
        "Gee. Thanks.":
            pass
        "It's all in the wrist.":
            pass
        "I really wish I knew how half of the stains showed up.":
            pass
    "She doesn't really notice you respond."
    arw happy "Look, Gio, I complimented them!"
    arm bulb "Ooh, so that's how it works with other people."
    ard neutral "[pc_name], can you maybe talk to them one-on-one?"
    ard neutral "I don't think we're getting anywhere with this. Maybe talk to them one-on-one and see if there's any kind of clue?"
    pc  "Think that'd work?"
    ard neutral "Yeah, just go with your intuition. Come talk to me too, I may remember something."
    $ SpeakGiovanni = 0
    $ SpeakWoman = 0
    $ SpeakDog = 0
    label ArnolfiniInvestigate:
        menu:
            "[[Speak to Giovanni]" if SpeakGiovanni == 0:
                $ SpeakGiovanni = 1
                $ ar_b4_c1 = "a"
                pc  "Do you remember anything from your past that might help define you two's relationship?"
                arm neutral "She mentioned a previous green dress with a veil…I remember that. I'm not one-hundred percent sure, but…"
                arm neutral "…I really think it was at a wedding. Our wedding. I could be wrong, though."
                jump ArnolfiniInvestigate
            "[[Speak to Gertrude]" if SpeakWoman == 0:
                $ SpeakWoman = 1
                $ ar_b4_c1 = "b"
                pc  "What can you tell me about your history with Giovanni? Maybe there's something we're missing."
                arw neutral "About those socks–I really do remember getting them as a gift. And Gio was there!"
                arw neutral "I can't speak with total authority, but I feel like we're just cousins. We're related, not married."
                jump ArnolfiniInvestigate
            "[[Speak to the Dog]" if SpeakDog == 0:
                $ SpeakDog = 1
                $ ar_b4_c1 = "c"
                ard neutral "You said you remembered something?"
                ard neutral "All that crud you cleaned up? I think they're both right with what they remember."
                ard neutral "The green veil? That was their wedding. And the socks at Christmas? I think they're cousins. They grew up together."
                ard neutral "I can't be sure, but I think they're married {i}and{/} related."
                jump ArnolfiniInvestigate
    pc  "Alright, I guess that's all the information I'm going to get."
    ard neutral "Alright what do you think?"
    arm neutral "Well?"
    arw neutral "What is it? What are we?"
    menu:
        "You're married.":
            $ ar_b4_c2 = "a"
        "You're just related. Cousins, probably.":
            $ ar_b4_c2 = "b"
        "You're married {i}and{/i} you're related.":
            $ ar_b4_c2 = "c"
    if ar_b4_c2 == "a":
        pc  "You two are married. Simple as that."
        arm sparkle "We're married! That makes sense."
        arw sparkle "Completely. You know, we're here together. We're married. We must've loved each other at some point?"
        arm neutral "Absolutely, we can work toward that!"
        arw neutral "Though I think we should try a different feather in your hat. That might help."
        arm panic "But…but you gave this to me!"
        ard sigh "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm neutral "Yes, thank you!"
        arw neutral "We won't forget this!"
    if ar_b4_c2 == "b":
        pc  "You two are related. I'd guess cousins?"
        arw happy "We're cousins! Oh, that makes sense."
        arm happy "Of course, I knew it!"
        arw laugh "Sure you did."
        arm neutral "Do you think our family is even bigger than just us?"
        arw neutral "Oh no, where do you think they are? Should we look for them? You! [pc_name]! Can you get us out of this painting too?"
        ard neutral "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm neutral "Yes, thank you!"
        arw neutral "We won't forget this!"
    if ar_b4_c2 == "c":
        pc  "I think you two are married…and related."
        arw sad "Oh…"
        arm sad "Oh no…"
        pc  "Well it was the 1400s, if that helps. It wasn't {i}that{/i} weird…I think."
        arm neutral "I don't really know what you mean by that, but I guess this is fine?"
        arw neutral "The family must've had a good reason, even if I don't like you like that."
        arm confused "What of my own parents? Were they, too…related?"
        arw dots "…"
        arm dots "…"
        arw panic "I don't like where this is going. I'm just not going to think about it. At least it's settled."
        arm neutral "Ugh, more or less."
        ard neutral "Oh, brother. Well, at least they're doing better. Thanks again for your help."
        arm neutral "Yes, thank you!"
        arw neutral "We won't forget this!"
    pc  "Well no matter what, it looks like you two–Giovanni and–"
    $ arwName = "Carlotta"
    arw neutral "It's Carlotta, now. I'm workshopping it. I'm actually circling back on Ethel, maybe."
    pc  "Well no matter what, it looks like you two–Giovanni and–"
    ard neutral "Ahem."
    pc  "—you THREE seem to be pretty okay now. More or less."
    arw neutral "Maybe we can finally make other friends? Ooh, like that Mona Lisa!"
    arm bulb "Ooh, there are those statues I've heard a bit about. They all have the same name!"
    pc  "Well I think you've already made a friend outside of yourselves!"
    arm questions "…Who?"
    arw questions "Yes, who are you talking about?"
    menu:
        "…Me. It's me. I'm your friend.":
            arw neutral "Oh…Oh you! Yes, that's true. I'm sorry. Thank you so much again!"
            arm neutral "Yes, thank you! You are really a friend. Well now what do we do?"
        "…Never mind.":
            arw neutral "Well, whatever you say!"
            arm neutral "Yes, yes. Well now what do we do?"
        "Forget I said anything. Look! You aren't arguing as much!":
            arw neutral "Yes, it's nice not to be so aggrieved all the time."
            arm neutral "Ooh, I like that word! Well, now what do we do?"

    ard neutral "What if you two paid attention to me a bit for a change?"
    arw neutral "I don't see why not!"
    arm question "Who are you again?"
    ard dots "…"
    ard neutral "We'll work on it."
    $ StoryCompletedTotal += 1
    $ beat_Arnolfini += 1
    jump FreeRoam

#complete
label .Outcome:
    if beat_Arnolfini == 5:
        scene fineart_tod:
            blur 5
        show arnolfiniportrait at truecenter:
            zoom .7
            yoffset -100
        "The Arnolfinis were a lot happier together."
        "While they still fought now and then, they eventually made friends with nearby paintings and–finally–enjoyed each other's presence."
        "The dog too!"
    elif beat_Arnolfini > 1:
        scene fineart_tod:
            blur 5
        show arnolfiniportrait at truecenter:
            zoom .7
            yoffset -100
        "The Arnolfinis got along a bit better, but their arguments never ended; annoying all of the surrounding pieces of art."
        "If only you had helped them reconcile…"
    else:
        scene fineart_tod:
            blur 5
        show arnolfiniportrait at truecenter:
            zoom .7
            yoffset -100
        "The Arnolfinis' arguments grew more and more dire and every piece of art around them suffered for it, including the dog."
        "Eventually, the piece tore in two, separating them forever and leaving them all alone."
        "Their arguing ended, along with all other contact and conversation."
    return