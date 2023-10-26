#day 0
#Audio implementation notes for Day 0: 
#Rain is on "sound" channel, so that this loop can continue. 
#Music is on "music" channel so that it will stomp on other music going into Beats 1-4.
#Voice is for one-off sounds that do not loop. (Let's hope this works. :D)
image VelvetRopeOverlay = "Day0/VelvetRope.png"
image VelvetRopeOverlay = "Day0/VelvetRope.png"
transform AdminPortrait:
    xalign 0.5
    yalign 0.5
    zoom .75
    yoffset -100
transform Rumble:
    ease .05 xoffset 15
    ease .05 xoffset -15
    ease .05 xoffset 25
    ease .05 xoffset -25
    ease .05 xoffset 0
default NameLie = 0
label GameIntroduction:
    scene museumexteriorrain
    #leaving the interview, missed bus, chased by the rain into an empty museum.
    #storm audio
    play sound "sfx/Day0Rain.wav" volume 0.5
    hm "{i}Dear Applicant,{/i}"
    hm "{i}Every journey begins somewhere.{/i}"
    #$ renpy.music.set_volume(.1, delay=1, channel="audio") 
    hm "{i}Yours, unfortunately, does not begin with us.{/i}"
    "So, the interview hadn't gone {i}great{/i}."
    #play audio "<from 10>music/RainLong.mp3" volume 1.0 fadein 1
    #"And your day didn't improve when you missed your bus and the rain chased you into this forlorn museum."
    "Then you missed your bus."
    #exterior shot
    
    "Rain-soaked, an hour from home, you decide to wait out the storm in the nearby museum."
    #interior transition
    #"With nothing better to do, you wait out the rain in the museum."
    scene foyer night with fade:
        ##matrixcolor TintMatrix("#7d91c7")
    stop sound fadeout 0.8
    play sfx2 "sfx/rain-on-roof.wav" volume 0.4 loop
    "Deserted. Not even a receptionist."
    #"Funny, you'd never even thought to visit this museum before."
    "The guest log is {i}very{/i} empty."
    #"It feels wrong not to at least sign it."
    #python:
    #    pc_name = renpy.input("What is your name?", length=32) #length is maximum length of the string
    #    pc_name = pc_name.strip()
    #    if not pc_name:
    #        pc_name = "Player"    
    menu:
        "[[Sign your name]":
            "Somehow, a single name seems even sadder."
            pass
        "{i}Almost seems haunted.{/i}":
            pass
        "{i}It doesn't seem like this place is doing well.{/i}":
            pass
    "Just like you."
    "No job."
    "Wet clothes." 
    "$2.36 in your pocket."
    "Just enough for a vending machine dinner."
    jump VendingMachineIntro

label DayZero:
    scene foyer night:
        ##matrixcolor TintMatrix("#7d91c7")
    #munch munch SFX
    
    "Your sad little snack doesn't last long."
    #"Outside, the rain still falls."
    #music start here
    scene foyer night with hpunch:
        ##matrixcolor TintMatrix("#7d91c7")
    play music "music/B14_W_02.wav" volume 0.5
    "???" "But do you have to {i}stand{/i} on the head? It's grisly."
    "A voice echoes through the empty hall."

    menu:                                               
        "Hello?":                                
            "Your voice echoes like a ghost with no one to haunt."
        "{i}Where is that coming from?{/i}":                                 
            "You certainly don't see anyone."

    "???" "It's {i}David{/i} and Goliath not {i}Goliath{/i} and Goliath you oversized buffoon."

    #put the velvet rope hre
    scene foyer night:
        blur 5
        ##matrixcolor TintMatrix("#7d91c7")
    show davids
    show VelvetRopeOverlay at truecenter:
        yoffset 450
    "The voices come from somewhere behind a trio of statues."
    #need another arguing line here
    #"They're not... coming from the statues, are they?"
    "All that's stopping you from getting closer is the impenetrable velvet rope."

    menu:                                               
        "[[Step over the velvet rope]":          
            hide VelvetRopeOverlay
            "Cautiously, you raise a leg over the rope."
        "[[Duck under]":          
            hide VelvetRopeOverlay
            "You crouch and prepare to breach the perimeter."

    
    "It feels wrong, like being in a school hallway after hours."
    stop music
    play sound "sfx/PhoneRing.wav" 
    show davids with hpunch
    #phone ring here
    "An alarm blares through the museum."
    play sound "sfx/rain-on-roof.wav" volume 0.4 loop
    menu:                                                
        "I DIDN'T TOUCH ANYTHING!":          
            "You can tell that to the judge. Knowing your luck, you won't even get parole."
        "[[Freeze and act small]":          
            "You're not the first person who tried to get too close to a museum piece."

    play sound "sfx/PhoneRing.mp3"
    show davids with hpunch
    "The alarm sounds again and again."
    "With some relief, you realize it's just the phone."

    play sound "sfx/PhoneRing.mp3"
    show davids with hpunch
    "It's not stopping either."

    #cutesy little phone interaction
    label GetThePhone:
        play sound "sfx/PhoneRing.mp3" 
        scene foyer night with hpunch:
            #matrixcolor TintMatrix("#7d91c7")
        call PhoneWaitResponse from _call_PhoneWaitResponse
        menu:                                               
            "[[Answer the phone.]":      
                "You answer the phone."    
            "[phone_wait]":          
                jump GetThePhone

    show admin at AdminPortrait with vpunch
    play music "music/Admin_ZY_02.wav" volume 0.6 fadein 0.2
    ad panic "Charles! Where were you?"
    menu:
        "Who?":
            pass
        "I think you have the wrong person--":
            pass
    ad neutral "We need to reprint the brochures. It should be \"Michelangelo's David\", {i}not{/i} \"Nickelodeon's\"."
    ad sad "Then I need you to get down in the archives and chase the raccoons out again."
    menu:
        "What do you mean, \"again\"?":
            pass
        "I {i}really{/i} think you have the wrong person.":
            pass
    ad surprise "And start putting some names in the visitor log, it doesn't look good to have it empty."
    ad question "Do you have all that?"
    menu:
        "Uh. Hi.":
            play sound "sfx/AdminScratch.wav" volume 0.8
            stop music fadeout 0.3
            "On the other end, mental gears grind to a halt."
            ad questions "Who is this? Where's Charles?"
        "I'm sorry, who are you?":
            play sound "sfx/AdminScratch.wav"
            stop music fadeout 0.3 
            "On the other end, mental gears grind to a halt."
            ad questions "Who are {i}you{/i}? Where's Charles?"
    show admin at AdminPortrait
    "The voice goes silent again. You hear furious typing."
    ad dots "Oh. He resigned."
    #revise
    ad neutral "That's great, that's fine." 
    ad "I just need to finish the paperwork, start redesigning the brochures now..."
    ad "...send out the press releases and donor letters..."
    #ad "...budgeting a generous half-hour for sleep..."
    #ad "Which would leave... twenty-minutes to prep for the gala."

    menu:                                               
        "I could do it.":          
            ad surprise "You could?"
            "What IT is exactly, you're not sure."
        "Sounds like you're hiring.":          
            #"Hey, worth a shot."
            ad surprise "I... guess we could."

    ad neutral "What's your name?"
    jump PlayerNameInput

label PlayerNameInput:
    #player name input
    python:
        pc_name = renpy.input("What is your name?", length=32) #length is maximum length of the string
        pc_name = pc_name.strip()
        if not pc_name:
            pc_name = "Player"

    pc "I'm [pc_name]."
    show admin at AdminPortrait
    "A gasp crackles over the line."
    play music "music/Admin_ZY_02.wav" volume 0.6
    ad sparkles "Are you {i}the{/i} Dr. [pc_name]?"
    ad neutral "We spoke after your last visit."
    ad "Your paper on the deontological ramifications of popularized historicity was..."
    ad "Well, I didn't understand much of it, but wow!"

    #revise
    menu:                                               
        "[[Lie] Yes.":     
            "In this economy, the truth has to be a little flexible."
            $ NameLie = 1     
            ad neutral "Wonderful, I'm just going to connect you to the hiring manager now."
            #ad "You'll be happy to know we're getting that racoon problem sorted out."
        "Yes?":       
            $ NameLie = 0   
            "Well, it isn't {i}NOT{/i} your name."
            ad neutral "Oh, it's just that it's a very rare name."
            ad neutral "I'll connect you to the hiring manager now."
        "No.":     
            $ NameLie = 0        
            "Smart to wait until you have the job to start lying."
            ad neutral "Oh, it's just that it's a very rare name."
            ad neutral "I'll connect you to the hiring manager now."

    show admin at AdminPortrait
    hide admin
    "There is a clunk as the receiver is set down."
    show admin at AdminPortrait
    if NameLie == 0:
        ad "Retention and Recruitment, am I speaking with {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [pc_name]?"
    if NameLie == 1:
        ad "Retention and Recruitment, am I speaking with Dr. [pc_name]?"
    "It is {i}clearly{/i} the same person as before."
    menu:
        "Who else?":
            ad sparkle "Wonderful, I've heard great things from the head office so I'm going to fast track you."
        "Yes.":
            ad sparkle "Wonderful, I've heard great things from the head office so I'm going to fast track you."
        "We were just speaking.":
            ad "No, that was Head Office, this is Retention and Recruitment."
            ad sparkle "I've heard great things though, so I'll fast track you."

    ad neutral "We can skip most of the fluff."
    ad neutral "Do you have any relevant work experience?"
    #work experience choices
    menu:               
        ad "Do you have any relevant work experience?"                             
        "I was a gas station attendant.": 
            $ pc_work = "gas station attendant"
            ad "That's... OK, great!"
        "Mostly gig work.":       
            $ pc_work = "gig worker"
            ad "Good, you'll be wearing plenty of hats here."
            #ad "Metaphorically. The raccoons started off in the gift shop."
        "Bouncer.":       
            $ pc_work = "bouncer"
            ad "That's... OK, great!"
        "I've done some painting.":      
            $ pc_work = "\"painter\""
            ad "Wonderful! Portraits, landscapes?"
            pc "Mostly houses. A few boats, some propane tanks."
            ad "That's... OK, great!"
        "I, um, I've {i}procured{/i} art from private clients.":     
            $ pc_work = "\"procurer\"" 
            ad "You mean you procured art {i}for{/i} clients?"
            pc "No, mostly {i}from{/i}."
        "I mean, not really?":     
            $ pc_work = "layabout" 
            ad "That's... well it's not too important."
    
    #update variables
    menu:              
        ad "Next: Any relevant skills?"                                 
        "I can really dissociate at work.":
            $ pc_skill = "dissociating"
            ad "Oh my, that must be nice."
        "My friends all treat me like their therapist.":   
            $ pc_skill = "therapy" 
            ad "Friends? Wow, I'll put, 'great social skills.'"
        "I know how to throw a KILLER party.":   
            $ pc_skill = "partying"
            pc "Ragers, keggers, raves, I'm flexible."
        "Just some light breaking and entering.":      
            $ pc_skill = "burglary"
            ad "Hmm, let's put: 'discretion and experience with tools.'" #logistics import export #asset acquisition
        "I've listened to a lot of people complain.":      
            $ pc_skill = "listening"
            ad "Ah, we do get a lot of those here."
        "Afraid not.":      
            $ pc_skill = "nothing"
            ad "I'm not sure... oh, it's fine."

    #update variables
    menu:             
        ad "Lastly: What's your education background?"                                  
        "I've apprenticed in the trades.":
            $ pc_education = "trades"
            ad "Wonderful! Our maintenance budget has really tanked."
        "I listen to like, A LOT of podcasts.":   
            $ pc_education = "podcastas" 
            ad "Me too! I have three going right now."
        "I think I took an art course?":   
            $ pc_education = "art course"
            ad "You think?"
            pc "I mean, I didn't go."
            ad "Well, that's better than nothing!"
        "I've seen The Da Vinci Code":      
            $ pc_education = "Da Vinci Code"
            ad "Oh, that is my favorite documentary!"
            ad "I never would have guessed Tom Hanks was a historian."
        "I have over three-hundred college credits.":      
            $ pc_education = "college credits"
            ad "Oh! What did you major in?"
            pc "I didn't. Never quite graduated."
        "I'd rather not say.":      
            $ pc_education = "not say"
            ad "Well, it's not that important."

    ad "Ok, great! Let me look this over while I transfer you back."
    hide admin
    "Once again, they set down the receiver."
    show admin at AdminPortrait
    ad sparkles "Wonderful, I've heard back from Retention and Recruitment. They've approved!"
    ad neutral "You are officially our new Curator."
    pc "Curator?"
    ad "Now I'm sure you're eager to get started so take the handset and follow along."

label MuseumTour:
    scene foyer night with fade:
        blur 5
        #matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad "I left the cordless phone in the Grand Foyer, so you're probably there right now!"
    ad "And these… are our Davids."
    "At first, you think you hear an echo:"
    #fix up the echo
    hide admin
    $ renpy.music.set_volume(0.1, delay=0.5, channel="music")
    show davidm at truecenter
    d "I'm David."
    hide davidm
    show davidm at truecenter:
        matrixcolor TintMatrix("#787878")
    show davidd at truecenter:
        xoffset 400
        yoffset 200
    d "I'm David."
    hide davidd
    show davidd at truecenter:
        xoffset 400
        yoffset 200
        matrixcolor TintMatrix("#787878")
    show davidb at truecenter:
        xoffset -300
        yoffset 200
    d "I'm David."
    hide davidm
    hide davidd
    hide davidb
    show davidm at truecenter
    show davidd at truecenter:
        xoffset 400
        yoffset 200
    show davidb at truecenter:
        xoffset -300
        yoffset 200
    "But as you approach, the echo fractures into three different voices, each one placing more emphasis on claiming identity for the one true David."
    dm sparkles "It's preposterous that either of you could be the David. It's clearly me."
    dd angry "No way, {i}I'm{/i} the David. You're just a couple of posers!"
    db neutral "Neither of you weaklings could possibly be {i}the{/i} David. I am!"
    
    menu:
        "They're... talking?":
            $ renpy.music.set_volume(0.6, delay=0.2, channel="music")
            pass
        "There's three of them? Don't we only need one?":
            $ renpy.music.set_volume(0.6, delay=0.2, channel="music")
            show admin at AdminPortrait
            ad sparkle "What an insightful question! Can't wait to hear how you solve this problem."
            pass
    hide admin
    #pc "They sure seem to be talking a lot. Why do we have three of them?"
    show admin at AdminPortrait
    ad neutral "Moving on!"

    scene antiquities night with fade:
        blur 5
        #matrixcolor TintMatrix("#7d91c7")
    ad "This is the Antiquities wing."
    ad "We're lucky to have a small collection of Sumerian artifacts."
    show gilgamesh at truecenter:
        zoom .8
    $ renpy.music.set_volume(0.1, delay=0.5, channel="music")
    gi sparkles "Nasir, look sharp! Another of the common-folk has come to bask in my glory. Ah to have such an opportunity."
    gi neutral "I'd envy [them] if I didn't pity [them]."
    show gilgamesh at left with move:
        xoffset 300
        zoom .8
    show eanasir at right:
        xoffset -300
        zoom .75
    e sad "Ugh..."
    hide gilgamesh
    hide eanasir
    #show sue at truecenter with hpunch
    #sue "Roar."
    #pc "Did you just {i}say{/i}, \"Roar\"?"
    #revise
    show admin at AdminPortrait
    $ renpy.music.set_volume(0.6, delay=0.1, channel="music")
    pc "Can't you hear that?"
    ad "Try not to fall behind, I have 57 calls waiting!"

    scene fineart night with fade:
        blur 5
        #matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad "This is the Fine Art wing."
    hide admin
    show arnolfini at truecenter:
        zoom 0.8
        yoffset -50
    $ renpy.music.set_volume(0.1, delay=0.5, channel="music")
    arw "I didn't take it, Giovanni! What makes you think I did!?"
    ad "This is the Arnolfini Portrait, note the lovely detail and its depiction of serene, marital bliss!"
    arm angry "I know you have it! Who else took it? The dog!?"
    ard neutral "You two can't even move, how could either of you take anything?"
    arw angry "Did you say that, Gio!?"
    arm neutral "I said no such thing!"
    hide arnolfini
    show admin at AdminPortrait
    ad "Often imitated and duplicated, our French collection includes the Mona Lisa!"
    hide admin
    show monalisa at truecenter:
        zoom .8
        yoffset -50
    m neutral "This {i}bischerə{/i}. I'm Florentine, not French."
    m neutral "And what do we have here? A [pc_work]. How prestigious. And rain-soaked."
    m neutral "Water remains the driving force of all nature. When it drives this place into the ground we can all go home."
    #revise
    hide monalisa
    menu:
        "I didn't sign up for {i}talking{/i} art.":
            pass
        "What is her problem?":
            pass
    show admin at AdminPortrait
    $ renpy.music.set_volume(0.6, delay=0.2, channel="music")
    ad "Please don't interrupt the tour!"

    scene mixedmedia night with fade:
        blur 5
        #matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad "This is the Mixed Media wing."
    hide admin
    show soupandsunflowers at truecenter:
        zoom .8
        yoffset -50
    #ad "Sunflowers was in the Fine Art wing with the other Van Gogh, until..."
    ad "We've got a couple of Van Goghs in our collection. This one was purchased at a generous discount!"
    $ renpy.music.set_volume(0.1, delay=0.4, channel="music")
    su neutral "Say, there’s a new face!"
    so neutral "Why [are] [they] wasting time wandering around a stupid museum? THE PLANET IS ON FIRE!"
    su sigh "I hope they know a good cleaning service…"
    hide soupandsunflowers
    scene day0 saint bg:
        matrixcolor TintMatrix("#7d91c7")
    #show saintblondebroken at truecenter
    ad "This is where our stained glass of Saint Catherine of Alexandria used to hang. It's French. Or Roman? Either way, it's broken."
    st neutral "It’s so dark. Where am I?"
    st neutral "Who am I?"
    st confused "Please…I know you can't hear me, but I'm here."
    menu:
        "Is she alright?":
            $ renpy.music.set_volume(0.6, delay=0.2, channel="music")
            ad question "Who? Pay attention, one more stop."
            pass
        "Where are you?":
            $ renpy.music.set_volume(0.6, delay=0.2, channel="music")
            ad question "What? Pay attention, one more stop."
            pass

    scene office bg with fade:
        blur 5
        #matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad neutral "Lastly, this is the Office."
    hide admin
    "Surely there's nothing in here that can talk."
    $ renpy.music.set_volume(0.1, delay=0.4, channel="music")
    p neutral "Um... uh... good luck!"
    menu:
        "...Who said that?":
            pass
        "Of course.":
            pass
    hide admin
    show corgiposter at truecenter:
        zoom .8
        yoffset -110
    "You turn to see an inspirational poster hanging on the wall featuring a cute corgi leaping into the air."
    p sweat "I... I hope you do your best today! I'm rooting for you!"
    
    scene foyer night with fade:
        blur 5
        #matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    $ renpy.music.set_volume(0.7, delay=0.4, channel="music")
    ad "And that's the tour! As you can see, it's all very straightforward. Really, all you need to do is clean."
    menu:
        "Uh huh. Totally.":
            pass
        "Hold on, they were {i}talking{/i}.":
            pass
    #pc "No, hold on, they were {i}talking{/i}--"
    ad surprise "Is there anything else...? Oh, I nearly forgot! "
    ad panic "We might be closing permanently after our Grand Gala in four days."
    menu:
        #ad "We might be closing permanently after our Grand Gala in four days."
        "Closing?":
            ad neutral "The donors aren't pleased with our current number of visitors."
        "In four days?":
            ad neutral "Yes! You can imagine my relief that you're here now."
    ad sparkle "But don't worry!"
    ad neutral "I'm sure you have a plan."
    pc "I don't even have the keys!"
    ad "Sorry! Call on the other line! Talk tomorrow!"
    play sound "sfx/AdminHangupLONG.wav" noloop
    stop music
    hide admin
    menu:
        "Hello?":
            stop sound fadeout 2.0
            "The dial tone does not respond."
    "???" "Psst."
    "No, the vending machine did not just, 'psst' you."
    show vendingmachine
    play music "music/Vending_ZV_01.wav" fadein 0.9 volume 0.2
    v "{i}Pssst.{/i} Hey!"
    "Its lights flicker conspiratorially."
    v "You the new{0} guy{/0}{1} gal{/1}{2}bie{/2}?"
    v "Right on. Let me get you the keys."
    hide vendingmachine
    show vendingmachine at Rumble:
        xalign 0.5
    "The machine {i}kachunks{/i} and {i}grinds{/i}. A heavy key ring flies out of the change door."
    v "Congrats on the curator gig, [pc_name]! Really diving into the deep end."
    menu:
    #    "Thanks?":
    #        v "De nada, {0}bro{/0}{1}sis{/1}{2}friendo{/2}."
    #    "Why do you have these?":
    #        v "Gotta stay prepped."
        "Am I really on my own?":
            v "Nah, don't be silly."
            v "You've got me!"
        "Why is this place so... crappy?":
            v "Whoa, throwin' shade!" 
            v "A little scrubbing, a little sweeping, this place could be as beautiful as the day it opened."
            v "It's the art that's the real mess."
    v "And it looks like you've got a busy week coming up."
    #pc "Yeah, the Admin mentioned that. Why is the museum closing?"
    $ WhyClosing = 0
    $ WhyHear = 0
    label WhyAndArt:
        menu:
            "Why is the museum closing?" if WhyClosing == 0:
                $ WhyClosing = 1
                v "You met the reasons. The whole vibe here is rancid."
                v "Back in the day, we'd have lines out the door. I'd get restocked three, maybe four times a day."
                v "Now, anybody with a feel for art is gonna run screaming. No offense."
                jump WhyAndArt
        #v "They've been twisted up inside themselves so long, even they don't know what they're about."
            "Why can I hear the art? The Admin couldn't." if WhyHear == 0:
                $ WhyHear = 1
                v "{i}All{/i} art can speak, most people just can't {i}listen.{/i}"
                v "They got all these {i}ideas{/i} and {i}thoughts{/i}. What art IS, what it ISN'T."
                v "But art speaks so quiet, they can't hear it over their own thoughts."
                pc "So why can {i}I{/i} hear it?"
                "The Vending Machine pauses with an electric hum."
                v "I guess you know how to keep your head clear."
                jump WhyAndArt

    #v "You got it twisted, {0}buddy{/0}{1}girl{/1}{2}buckaroo{/2}."
    
    #"Or empty."
    menu:
        "Are you saying I'm stupid?":
            v "Whoa, {0}bro{/0}{1}sis{/1}{2}champ{/2}! No aggro; I'm saying you're {i}zen{/i}."
        "So I've got a superpower.":
            v "Heck yes, {0}bro{/0}{1}sis{/1}{2}champ{/2}!"
    v "Now I like to think I'm something of a cu-ra-tor myself. Anything you need, ask away."
    $ VendingGala = 0
    $ VendingCurator = 0
    $ VendingAdmin = 0
    label VendingQuestions:
        menu:   
            "What is the \"Grand Gala\"?" if VendingGala != 1:
                v "Just a little shindig."
                v "All the major press outlets, art critics, the big donors too."
                v "You didn't hear this from me, but last year they threatened to pull the funding if this one doesn't go well."
                v "No pressure though."
                $ VendingGala = 1
                jump VendingQuestions
            "What happened to the last curator?" if VendingCurator != 1:
                v "Charles?"
                v "Dude tried, but was a bit high-strung TBH."
                v "Had all these ideas about lighting, layout, merch."
                v "No {i}soul{/i}. Couldn't {i}listen{/i} to the art."
                v "One too many glares from Mona and he called it quits."
                $ VendingCurator = 1
                jump VendingQuestions
            "Why can you talk? Are {i}you{/i} art?" if VendingAdmin != 1:
                #v "Beats me. Keep too many plates spinning too long, maybe your head starts to spin too."
                v "I've learned a trick or two."
                v "But sometimes, you just {i}become{/i}."
                v "Someone sees you in a new light, a new angle."
                v "The world changes, and you're the same, but different."
                v "But I'm sure you know all about that, {i}curator{/i}."
                menu:
                    "Whoa, that's awesome.":
                        v "Right?"
                    "That doesn't make any sense.":
                        "Somehow, the Vending Machine shrugs."
                    "Okay, but {i}are{/i} you art?":
                        v "I'm not sure it's up to me."
                $ VendingAdmin = 1
                jump VendingQuestions
    v "I've seen a lot of curators come through here."
    v "They all thought a few lights and some marketing could save this place."
    v "But you can {i}listen{/i}, feel the current. You're the first one I think has a chance."
    menu:
        "What if I don't?":
            pass
        "I hope you're right.":
            pass
    v "Listen, these jokers weren't always this miserable."
    v "Most of them just spent too much time being looked at, not enough time being heard."
    v "I mean, you think Saint Cathy {i}likes{/i} being in a cupboard?"
    v "Even the Arnolfinis used to play nice."
    v "But going into storage or getting auctioned off won't help anything."
    menu: 
        "What happens to you if the museum closes?":
            v "Straight to the dump."
            v "Crushed."
            v "Cubed."
            v "{i}Recycled.{/i}"
            "The Vending Machine shivers."
            v "But try not to worry about that."
        "How can I help?":
            v "Just talk to 'em, {0}bro{/0}{1}sis{/1}{2}champ{/2}!"
            v "Won't matter how clean this place is if the art's still a mess."
            v "Just don't get spread thin."
    #v "But don't worry, it's all the great circle of life."
    v "They've probably got more problems than you have time."
    v "Sometimes, the best way to help everyone is to {i}not{/i} help everyone. Feel me?"
    v "Now go lock up and get some rest, busy day tomorrow!"
    stop music fadeout 2

    scene foyer night with fade:
        #matrixcolor TintMatrix("#7d91c7")
    "Four days."
    "Just four days to save a dysfunctional gallery of art from itself. And maybe save your job with it."
    #"But that can wait for tomorrow."
    #"As you leave, someone whispers behind you, unnoticed. (Or is that somebodies, plural?)"
    "After you leave, a new voice echoes through the Foyer."
    scene foyer night:
        blur 5
        #matrixcolor TintMatrix("#7d91c7")
    play music "music/Nighthawks_ZU_01.wav" volume 0.3
    show nighthawks at truecenter:
        zoom .65
        yoffset -125
    n1 "Think our new curator is going to make it?"
    n2 "After THAT first day? Doubtful."
    if NameLie == 1:
        n3 "Like watching a slow-moving car crash. I mean, everyone knows the REAL Dr. [pc_name] is summering in the Hamptons with Banksy."
    if NameLie == 0:
        n3 "Like watching a slow-moving car crash. I mean, choosing {i}honesty{/i}? Everyone knows lying in interviews is a sacred and time-honored practice."
    n4 "I'd be shocked if [they] even come[s] back tomorrow."
    stop music fadeout 1.0
    stop sfx2 fadeout 0.8
    jump DayStart
    #menu:
    #    "Daily Loop - VERY Work-In-Progress":
    #        jump DayStart
    #    "Restart Tour":
    #        jump MuseumTour
    #    "Main Menu":
    #        return

    return
    #jump DayStart

#generates random responses for the phone
label PhoneWaitResponse:
    if phone_wait_count == 0:
        $ phone_wait = "Someone will get it."
        $ phone_wait_count += 1
    elif phone_wait_count > 0:
        $ phone_wait = renpy.random.choice(["Any minute now.", "Must be on their break.", "Really not my business.", "Wow, just keeps going.", "Isn't it going to go to voicemail?", "Whistle nonchalantly."])
        $ phone_wait_count += 1
    #else:
    #    $ phone_wait = renpy.random.choice(["Wow, that could drive you nuts.", "Must be a LONG break.", "Someone must be coming.", "Whistle nonchalantlier."])
    #    $ phone_wait_count += 1
    return

label VendingMachineIntro:
        python:
            button_press_count = 0
            selection = 0
        call screen vendingmachineselection          
