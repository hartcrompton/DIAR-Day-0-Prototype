#day 0
image VelvetRopeOverlay = "Day0/VelvetRope.png"
transform AdminPortrait:
    xalign 0.5
    yalign 0.5
    zoom .75
    yoffset -100
default NameLie = 0
label GameIntroduction:
    scene museumexteriorrain
    #leaving the interview, missed bus, chased by the rain into an empty museum.
    #storm audio
    #play music "<from 5>music/Day0LoopSadBella.wav"
    play audio "<from 10>music/RainLong.mp3" volume .2
    "Hiring Manager" "Dear Applicant,"
    "Hiring Manager" "Every journey begins somewhere."
    $ renpy.music.set_volume(.1, delay=1, channel="audio") 
    "Hiring Manager" "Yours, unfortunately, does not begin with us."
    "So, the interview hadn't gone {i}great{/i}."
    play audio "<from 10>music/RainLong.mp3" volume 1.0 fadein 1
    #"And your day didn't improve when you missed your bus and the rain chased you into this forlorn museum."
    "Then you missed your bus."
    #exterior shot
    
    "Rain soaked, an hour from home, you decide to wait out the storm in the nearby museum."
    #interior transition
    #"With nothing better to do, you wait out the rain in the museum."
    scene foyer bg with fade:
        matrixcolor TintMatrix("#7d91c7")
    "Empty. Not even a receptionist."
    #"Funny, you'd never even thought to visit this museum before."
    "The guest log is {i}very{/i} empty."
    #"It feels wrong not to at least sign it."
    #python:
    #    pc_name = renpy.input("What is your name?", length=32) #length is maximum length of the string
    #    pc_name = pc_name.strip()
    #    if not pc_name:
    #        pc_name = "Player"    

    
    "No job."
    "Wet clothes." 
    "$2.36 in your pocket."
    "Just enough for a vending machine dinner."
    jump VendingMachineIntro

label DayZero:
    scene foyer bg:
        matrixcolor TintMatrix("#7d91c7")
    #munch munch SFX
    
    "Your sad little snack doesn't last long."
    #"Outside, the rain still falls."
    #music start here
    scene foyer bg with hpunch:
        matrixcolor TintMatrix("#7d91c7")
    "???" "But do you have to {i}stand{/i} on the head? It's grisly."
    "A voice echoes through the empty hall."

    menu:                                               
        "Hello?":                                
            "Your voice echoes like a ghost with no one to haunt."
        "{i}Where is that coming from?{/i}":                                 
            "You certainly don't see anyone."

    "???" "It's {i}David{/i} and Goliath not {i}Goliath{/i} and Goliath you oversized buffoon."

    #put the velvet rope hre
    scene foyer bg:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
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
    play sound "sfx/PhoneRing.mp3"
    show davids with hpunch
    #phone ring here
    "An alarm blares through the museum."
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
        scene antiquities bg with hpunch:
            matrixcolor TintMatrix("#7d91c7")
        call PhoneWaitResponse from _call_PhoneWaitResponse
        menu:                                               
            "[[Answer the phone.]":      
                "You answer the phone."    
            "[phone_wait]":          
                jump GetThePhone

    show admin at AdminPortrait with vpunch
    #play music "music/Day0AdminCallBella.wav"
    ad "Charles! Where were you?"
    menu:
        "Who?":
            pass
        "I think you have the wrong person--":
            pass
    ad "We need to reprint the brochures. It should be \"Michelangelo's David\", {i}not{/i} \"Nickelodeon's\"."
    ad "Then I need you to get down in the archives and chase the raccoons out again."
    menu:
        "What do you mean, \"again\"?":
            pass
        "I {i}really{/i} think you have the wrong person.":
            pass
    ad "And start putting some names in the visitor log, it doesn't look good to have it empty."
    ad "Do you have all that?"
    menu:
        "Uh. Hi.":
            "On the other end, mental gears grind to a halt."
            ad "Who is this? Where's Charles?"
        "I'm sorry, who are you?":
            "On the other end, mental gears grind to a halt."
            ad "Who are {i}you{/i}? Where's Charles?"
    show admin at AdminPortrait
    "The voice goes silent again. You hear furious typing."
    ad "Oh. He resigned."
    #revise
    ad "That's great, that's fine." 
    ad "I just need to finish the paperwork, start redesigning the brochures now..."
    ad "...send out the press releases and donor letters..."
    #ad "...budgeting a generous half-hour for sleep..."
    #ad "Which would leave... twenty-minutes to prep for the gala."

    menu:                                               
        "I could do it.":          
            ad "You could?"
            "What IT is exactly, you're not sure."
        "Sounds like you're hiring.":          
            #"Hey, worth a shot."
            ad "I... guess we could."

    ad "What's your name?"
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
    ad "Are you {i}the{/i} Dr. [pc_name]?"
    ad "We spoke after your last visit."
    ad "Your paper on the deontological ramifications of popularized historicity was..."
    ad "Well, I didn't understand much of it, but wow!"

    #revise
    menu:                                               
        "[[Lie] Yes.":     
            "In this economy, the truth has to be a little flexible."
            $ NameLie = 1     
            ad "Wonderful, I'm just going to connect you to the hiring manager now."
            #ad "You'll be happy to know we're getting that racoon problem sorted out."
        "Yes?":       
            $ NameLie = 0   
            "Well, it isn't {i}NOT{/i} your name."
            ad "Oh, it's just that it's a very rare name."
            ad "I'll connect you to the hiring manager now."
        "No.":     
            $ NameLie = 0        
            "Smart to wait until you have the job to start lying."
            ad "Oh, it's just that it's a very rare name."
            ad "I'll connect you to the hiring manager now."

    show admin at AdminPortrait
    hide admin
    "There is a clunk as the receiver is set down."
    show admin at AdminPortrait
    ad "Retention and Recruitment, am I speaking with {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [pc_name]?"
    "It is {i}clearly{/i} the same person as before."
    menu:
        "Who else?":
            ad "Wonderful, I've heard great things from the head office so I'm going to fast track you."
        "Yes.":
            ad "Wonderful, I've heard great things from the head office so I'm going to fast track you."
        "We were just speaking.":
            ad "No, that was Head Office, this is Retention and Recruitment."
            ad "I've heard great things though, so I'll fast track you."

    ad "We can skip most of the fluff."
    ad "Do you have any relevant work experience?"
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
        "I um, I've {i}procured{/i} art from private clients.":     
            $ pc_work = "\"procurer\"" 
            ad "Do you mean 'for'?"
            pc "No."
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
    ad "Wonderful, I've heard back from Retention and Recruitment. They've approved!"
    ad "You are officially our new Curator."
    pc "Curator?"
    ad "Now I'm sure you're eager to get started so take the handset and follow along."

label MuseumTour:
    scene foyer bg with fade:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad happy "This is the Grand Foyer."
    ad "And these… are our Davids."
    "At first, you think you hear an echo:"
    #fix up the echo
    hide admin
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
    dm "It's preposterous that either of you could be the David. It's clearly me."
    dd "No way, {i}I'm{/i} the David. You're just a couple of posers!"
    db "Neither of you weaklings could possibly be {i}the{/i} David. I am!."
    
    menu:
        "They're... talking?":
            pass
        "There's three of them? Don't we only need one?":
            ad "What an insightful question! Can't wait to hear how you solve this problem."
            pass
    #pc "They sure seem to be talking a lot. Why do we have three of them?"
    show admin at AdminPortrait
    ad "Moving on!"

    scene antiquities bg with fade:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
    ad "This is the Antiquities wing."
    ad "We're lucky to have a small collection of Sumerian artifacts."
    show gilgamesh at truecenter:
        zoom .8
    gi "Nasir, look sharp! Another of the common-folk has come to bask in my glory. Ah to have such an opportunity."
    gi "I'd envy [them] if I didn't pity [them]."
    show gilgamesh at left with move:
        xoffset 300
        zoom .8
    show eanasir at right:
        xoffset -300
        zoom .75
    e "Ugh..."
    hide gilgamesh
    hide eanasir
    #show sue at truecenter with hpunch
    #sue "Roar."
    #pc "Did you just {i}say{/i}, \"Roar\"?"
    #revise
    show admin at AdminPortrait
    pc "Can't you hear that?"
    ad "Try not to fall behind, I have 57 calls waiting!"

    scene fineart bg with fade:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad "This is the Fine Art wing."
    hide admin
    show arnolfini at truecenter:
        zoom 0.8
        yoffset -50
    arw "I didn't take it, Giovanni! What makes you think I did!?"
    ad "This is the Arnolfini Portrait, note the lovely detail and its depiction of serene, marital bliss!"
    arm "I know you have it! Who else took it? The dog!?"
    ard "You two can't even move, how could either of you take anything?"
    arw "Shush!"
    arm "Stay out of it!"
    hide arnolfini
    show admin at AdminPortrait
    ad "Often imitated and duplicated, our French collection includes the Mona Lisa!"
    hide admin
    show monalisa at truecenter:
        zoom .8
        yoffset -50
    m "This {i}bischero{/i}. I'm Florentine, not French."
    m "And what do we have here? A [pc_work]. How prestigious. And rain-soaked."
    m "Water remains the driving force of all nature. When it drives this place into the ground we can all go home."
    #revise
    hide monalisa
    menu:
        "I didn't sign up for {i}talking{/i} art.":
            pass
        "What is her problem?":
            pass
    ad "Please don't interrupt the tour!"

    scene mixedmedia bg with fade:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad "This is the Mixed Media wing."
    hide admin
    show soupandsunflowers at truecenter:
        zoom .8
        yoffset -50
    #ad "Sunflowers was in the Fine Art wing with the other Van Gogh, until..."
    ad "We've got a couple of Van Goghs in our collection. This one was purchased at a generous discount!"
    su "Say, there’s a new face!"
    so "Why {0}is{/0}{1}is{/1}{2}are{2} [they] wasting time wandering around a stupid museum? THE PLANET IS ON FIRE!"
    su "I hope they know a good cleaning service…"
    hide soupandsunflowers
    scene day0 saint bg:
        matrixcolor TintMatrix("#7d91c7")
    #show saintblondebroken at truecenter
    ad "This is where our stained glass of Saint Catherine of Alexandria used to hang. It's French. Or Roman? Either way, it's broken."
    st dark "It's so dark. Where am I?"
    st "Who am I?"
    st "Please... I know you can't hear me, but I'm here."
    menu:
        "Is she alright?":
            ad "Who? Pay attention, one more stop."
            pass
        "Where are you?":
            ad "What? Pay attention, one more stop."
            pass

    scene office bg with fade:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad "Lastly, this is the Office."
    hide admin
    "Surely there's nothing in here that can talk."
    p "Um... uh... good luck!"
    menu:
        "...Who said that?":
            pass
        "Of course.":
            pass
    hide admin
    show corgiposter at truecenter:
        zoom .8
        yoffset -110
    "You turn to see an inspirational poster hanging on the wall featuring a cute corgi leaping into the air"
    p "I... I hope you do your best today! I'm rooting for you!"
    
    scene foyer bg with fade:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
    show admin at AdminPortrait
    ad "And that's the tour! As you can see, it's all very straightforward."
    menu:
        "Uh huh. Totally.":
            pass
        "Hold on, they were {i}talking{/i}.":
            pass
    #pc "No, hold on, they were {i}talking{/i}--"
    ad "Is there anything else...? Oh, I nearly forgot! "
    ad "We might be closing permanently after our Grand Gala in four days."
    menu:
        ad "We might be closing permanently after our Grand Gala in four days."
        "Closing?":
            ad "The donors aren't pleased with our current number of visitors."
        "In four days?":
            ad "Yes! You can imagine my relief that you're here now."
    ad "But don't worry!"
    ad "I'm sure you have a plan."
    pc "I don't even have the keys!"
    ad "Sorry! Call on the other line! Talk tomorrow!"
    hide admin
    menu:
        "Hello?":
            "The dial tone does not respond."
    "???" "Psst."
    "No, the vending machine did not just, 'psst' you."
    show vendingmachine
    v "{i}Pssst.{/i} Hey!"
    "Its lights flicker conspiratorially."
    v "You the new{0} guy{/0}{1} gal{/1}{2}bie{/2}?"
    v "Right on. Let me get you the keys."
    "The machine {i}kachunks{/i} and {i}grinds{/i}. A heavy key ring flies out of the change door."
    menu:
        "Thanks?":
            v "De nada, {0}bro{/0}{1}sis{/1}{2}friendo{/2}."
        "Why do you have these?":
            v "Gotta stay prepped."
    v "So you're the new curator? Really diving into the deep end."
    v "Worst case, you only need to last a week."
    #pc "Yeah, the Admin mentioned that. Why is the museum closing?"
    $ WhyClosing = 0
    $ WhyHear = 0
    label WhyAndArt:
        menu:
            "Why is the museum closing?" if WhyClosing == 0:
                $ WhyClosing = 1
                v "You met the reasons."
                v "Anybody with a feel for art is gonna run screaming. No offense."
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
                v "Dude was a bit high-strung, TBH."
                v "Had all these ideas about lighting, layout, merch."
                v "No {i}soul{/i}. Couldn't {i}listen{/i} to the art."
                v "One too many glares from Mona and he called it quits."
                $ VendingCurator = 1
                jump VendingQuestions
            "About the Admin..." if VendingAdmin != 1:
                v "Sure."
                pc "What's wrong with them?"
                v "Beats me. Keep too many plates spinning too long, maybe your head starts to spin too."
                $ VendingAdmin = 1
                jump VendingQuestions
    v "I'll be honest. I've seen a lot of curators come through here."
    v "They all thought a few lights and some marketing could save this place."
    v "But you can {i}listen{/i}, feel the current. You're the first one I think who has a chance."
    pc "What if I don't?"
    v "No stress. All these jokers are on loan. If the museum closes, they just get shipped back."
    pc "What about you?"
    show vendingmachine
    v "Straight to the dump."
    v "Crushed."
    v "Cubed."
    "The Vending Machine shivers."
    v "Re-cycled. But don't worry, it's all the great circle of life."
    v "Now go lock up and get some rest, busy day tomorrow!"

    scene foyer bg with fade:
        matrixcolor TintMatrix("#7d91c7")
    "Four days."
    "Four days to save a dysfunctional gallery of art from itself. And maybe save your job with it."
    "But that can wait for tomorrow."
    "As you leave, someone whispers behind you, unnoticed. (Or is that somebodies, plural?)"
    scene foyer bg:
        blur 5
        matrixcolor TintMatrix("#7d91c7")
    show nighthawks at truecenter:
        zoom .65
        yoffset -125
    n1 "Think our new curator is going to make it?"
    n2 "After THAT first day? Doubtful."
    if NameLie == 1:
        n3 "Like watching a slow-moving car crash. I mean, everyone knows the REAL Dr. [pc_name] is currently summering in the Hamptons with Banksy."
    if NameLie == 0:
        n3 "Like watching a slow-moving car crash. I mean, choosing {i}honesty{/i}? Everyone knows lying in interviews is a sacred and time-honored practice."
    n4 "I'd be shocked if [they] even come[s] back tomorrow."
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
