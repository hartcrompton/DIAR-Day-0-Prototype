#day 0

label GameIntroduction:
    scene intro bg1
    #this is too long
    #leaving the interview, missed bus, chased by the rain into an empty museum.
    "Hiring Manager" "Every journey begins somewhere."
    "Hiring Manager" "Yours, unfortunately, does not begin with us."
    "So, the interview hadn't gone great."
    "And your day didn't improve when you missed your bus and the rain chased you into an empty museum."

    scene museum bg1
    
    "The rain isn't stopping, and your dinner is waiting for you at home."
    "You have just enough cash for something from the vending machine."
    jump VendingMachineIntro

#I am using WAY too few labels in this prototype
label DayZero:
    scene museum bg1
    d "But do you have to {i}stand{/i} on the head? It's grisly."
    "A voice echoes through the empty hall. Looking around, you can't see anyone."

    menu:                                               
        "Hello?":                                
            "Your voice echoes like a ghost with no one to haunt."
        "Where is that coming from?":                                 
            "You look for the sound."

    d "It's {i}David{/i} and Goliath not {i}Goliath{/i} and Goliath you oversized freak."

    scene museum bg1
    show davids
    "The voices come from somewhere behind a trio of statues."
    "They're not... coming from the statues, are they?"
    "All that's stopping you from getting closer is the velvet rope."

    menu:                                               
        "Step over the velvet rope.":          
            "Cautiously, you raise a leg over the rope."

    "It feels wrong, like being in a school hallway after hours."
    scene museum bg1 with hpunch:
    show davids
    "An alarm blares through the museum."
    "You hastily pull your leg back."

    menu:                                               
        "I DIDN'T TOUCH ANYTHING!":          
            "You can tell that to the judge. Knowing your luck, you won't even get parole."
        "[[Freeze and act small.]":          
            "You're not the first person who tried to get too close to a museum piece."

    scene museum bg1 with hpunch:
    show davids
    "The alarm blares again and again."
    "With some relief, you realize it's just the phone."

    scene museum bg1 with hpunch:
    "It's not stopping either."

    #cutesy little phone interaction
    label GetThePhone:
        scene museum bg1 with hpunch:
        call PhoneWaitResponse
        menu:                                               
            "[[Answer the phone.]":      
                "You answer the phone."    
            "[phone_wait]":          
                jump GetThePhone

    show admin excited at right
    ad "Charles! Where were you?"
    ad "We need to reprint the brochures. They should not say \"Nickelodeon's\" David."
    pc "Hold on-"
    ad "Then I need you to get down in the archives and chase the raccoons out again."
    pc "I don't think-"
    ad "And start putting some names in the visitor log, it doesn't look good to have it empty."
    menu:
        ad "Do you have all that?"
        "Uh. Hi.":
            "On the other end, mental gears grind to a halt."
            ad "Who is this? Where's Charles?"
        "I'm sorry, who are you?":
            "On the other end, mental gears grind to a halt."
            ad "Who are {i}you{/i}? Where's Charles?"
    show admin stressed at right
    "The voice goes silent again. On the other end, you hear furious typing."
    ad "Oh he resigned."
    ad "That's great, that's fine." 
    ad "If I finish the paperwork and start driving now..." 
    ad "...budgeting a generous half-hour each night for sleep..." 
    ad "...I could get to the museum by Thursday."
    ad "Which would leave... twenty-minutes to prep for the gala."

    menu:                                               
        "I could do it.":          
            ad "You could?"
            "What IT is exactly, you're not sure."
        "Sounds like you're hiring.":          
            "Hey, worth a shot."

    ad "What's your name?"
    jump PlayerNameInput

label PlayerNameInput:
    #player name input
    python:
        pc_name = renpy.input("What is your name?", length=32) #length is maximum length of the string
        pc_name = pc_name.strip()
        if not pc_name:
            renpy.jump("PlayerNameInput")

    pc "My name is [pc_name]!"
    show admin excited at right
    "A gasp crackles over the line."
    ad "Are you {i}the{/i} Dr. [pc_name]?"
    #ad "We spoke after your last visit."
    ad "Your paper on the deontological ramifications of popularized historicity was..."
    ad "Well, I didn't understand much of it, but wow!"

    menu:                                               
        "Yes. [[Lie]":          
            "In this economy, the truth has to be a little flexible."
            #ad "You'll be happy to know we're getting that racoon problem sorted out."
        "Yes?":          
            "Well, it isn't {i}NOT{/i} your name."
        "No.":          
            "Smart to wait until you have the job to start lying."

    show admin at right
    ad "I'm just going to connect you to the hiring manager now."
    "There is a clunk as the receiver is set down."
    "A moment later, the same voice answers the phone."
    ad "Retention and Recruitment, am I speaking with {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [pc_name]?"
    menu:
        "Who else?":
            ad "Wonderful, I've heard great things from the head office so I'm going to fast track you."
        "Yes.":
            ad "Wonderful, I've heard great things from the head office so I'm going to fast track you."
        "We were just speaking.":
            ad "No, that was Head Office, this is Retention and Recruitment."
            ad "I've heard great things though, so I'll fast track you."

    ad "We'll skip to the relevant questions."
    ad "Any relevant work experience?"
    #work experience choices
    menu:               
        ad "Any relevant work experience?"                                
        "I was a gas station attendant.": 
            ad "That's... OK, great!"
        "Mostly gig work.":       
            ad "Good, you'll be wearing plenty of hats here."
            ad "Metaphorically. The raccoons started off in the gift shop."
        "Bouncer.":       
            ad "That's... OK, great!"
        "I've done some painting.":      
            ad "Wonderful! Portraits, landscapes?"
            pc "Mostly houses. A few boats, some propane tanks."
            ad "That's... OK, great!"
        "I um, I've {i}procured{/i} art from private clients.":      
            ad "Do you mean 'for'?"
            pc "No."
        #"I mean, not really?":      
            #ad "That's... well it's not too important."
    
    
    menu:              
        ad "Next: Any relevant skills?"                                 
        "I can really dissociate at work.":
            ad "I'm not sure... oh, it's fine."
        "My friends all treat me like their therapist.":    
            ad "I'm not sure... oh, it's fine."
        "I know how to throw a KILLER party.":   
            ad "We don't have many of those here."
            pc "Ragers, keggers, raves, I'm flexible."
        "Just some light breaking and entering.":      
            ad "Why would you tell me..."
            ad "It's fine. We'll put: 'discretion and '"
        "I've listened to a lot of people complain.":      
            ad "I'm not sure... oh, it's fine."
        #"Afraid not.":      
            #ad "I'm not sure... oh, it's fine."

    menu:             
        ad "Lastly: What's your education background?"                                  
        "I've apprenticed in the trades.":
            ad "Wonderful! Our maintenance budget has really tanked."
        "I listen to like, A LOT of podcasts.":    
            ad "Me too! I have three going right now."
        "I think I took an art course?":   
            ad "You think?"
            pc "I mean, I didn't go."
            ad "OK..."
            ad "It's better than nothing."
        "I've seen The Da Vinci Code":      
            ad "Oh, that is my favorite documentary!"
            ad "I never knew Tom Hanks was a historian."
        "I have over three-hundred college credits.":      
            ad "Oh! What did you major in?"
            pc "I didn't. Never quite graduated."
        #"I'd rather not say.":      
            #ad "Hmm, I guess that works?"

    ad "Ok, great! Let me look this over while I transfer you back."
    "There is a clunk as they set down the receiver."
    ad "Wonderful, I've heard from Retention and Recruitment. They've approved!"
    ad "You are officially our new curator."

label MuseumTour:
    scene museum bg1 with fade
    show admin at right
    ad "This is the foyer."
    ad "These are the famous Davids. Most people don't know they were actually triplets."
    show davids at left
    d "Arguing amongst themselves"

    scene museum bg2 with fade
    ad "This is the antiquities wing."
    ad "We're lucky to have a small collection of Sumerian artifacts."
    show gilgamesh at left
    gi "Ea-Nasir, look sharp! Another of the common-folk has come to bask in my glory. I would envy [them] this opportunity."
    gi "If I didn't pity [them]."
    show eanasir angry at right
    e "Ugh..."
    hide gilgamesh
    hide eanasir
    show sue at center with hpunch
    sue "Roar."
    pc "Did you just {i}say{/i}, \"Roar\"?"
    show admin at right
    ad "Try not to fall behind, I have 57 calls waiting!"

    scene museum bg1 with fade
    show admin at right
    ad "This is the Fine Art wing."
    show theodore at left
    t "Please don't mention Van Gogh."
    show admin at right
    ad "This is, of course, the famous self portrait by Van Gogh."
    show theodore angry at left
    t "God damnit."
    hide theodore
    show arnolfinim at left
    ar "We hate each other."
    show arnolfiniw at left
    ar "So much."
    hide arnolfinim
    hide arnolfiniw
    ad "And our crown jewel, the Mona Lisa."
    show monalisa at left
    m "A cutting remark."
    ad "Next stop, keep up, I have 1078 more calls today."

    scene museum bg2 with fade
    show admin at right
    ad "This is Mixed Media."
    show sunflowers at left
    ad "Sunflowers was originally in the Fine Art wing with the other Van Gogh, until..."
    ad "Well, we couldn't afford to clean the soup off, so now it's here."
    show glimmer at left
    gl "I'm young and unsure."
    hide glimmer
    show sunflowers at left
    su "I hate this soup."
    hide sunflowers
    show saintcatherine at left
    st "I find existence troubling."
    pc "This is still weird."

    scene museum bg2 with fade
    show admin at right
    ad "Lastly, this is the office."
    pc "Surely there's nothing in here that can talk."
    show poster at left
    p "I can talk!"
    pc "Of course you can."
    
    scene museum bg1 with fade
    ad "And that's the tour! You should have everything you need to get started."
    pc "About that, do you know where the keys--"
    ad "Oh and we have our Grand Gala in four days! If it goes bad, the donors might revoke our funding!"
    menu:
        "Hello?":
            "The dial tone does not respond."
        "[[Hang up.]"
    "???" "Psst."
    "No, the vending machine did not just, 'psst' you."
    show vendingmachine
    v "{i}Pssst.{/i} Hey!"
    "Its lights flicker conspiratorially."
    pc "You talk too?"
    pc "Of course you do."
    v "You the new{0} guy{/0}{1} gal{/1}{2}bie{/2}?"
    v "Right on. Here, let me get you the keys."
    "The machine kachunks and grinds. A heavy key ring flies out of the change door."
    menu:
        "Thanks?":
            v "De nada, {0}bro{/0}{1}sis{/1}{2}friendo{/2}."
        "Why do you have these?":
            v "Gotta stay prepped."
    v "So you're the new curator? Like to think I'm a bit of a cu-ra-tor myself. Any questions, ask away."
    menu:
        "Is the museum really going to close in four days?":
            v "Yeah, bummer. But maybe you can save it!"
        "What happened to the last curator?"
    v "Last dude was a bit of a hodad tee-bee-haitch."
    v "Had all these ideas about lighting, layout, merch."
    v "No {i}soul{/i}. Couldn't {i}listen{/i} to the art."
    pc "Yeah, why is the art here... alive?"
    v "Haha, you got it twisted, {0}buddy{/0}{1}girl{/1}{2}buckaroo{/2}."
    v "All art can speak, most people just can't listen."
    v "They got all these {i}ideas{/i} and {i}thoughts{/i}. What art IS, what it ISN'T."
    v "Art speaks so quiet, they can't hear it over their own thoughts."
    pc "So why can {i}I{/i} hear it?"
    v "You must know how to keep your head clear."
    menu:
        "Are you saying I'm stupid?":
            v "Whoa, {0}bro{/0}{1}sis{/1}{2}champ{/2}! No aggro; I'm saying you're {i}zen{/i}."
        "So it's a superpower.":
            v "Heck yes, {0}bro{/0}{1}sis{/1}{2}champ{/2}!"
    v "Now go luck up, busy day tomorrow!"

    scene museum bg1 with fade
    show nighthawks at truecenter
    n "You reckon they'll stay on?"
    n "Nah, they won't even come back."

    scene museum bg1
    "Alright, work starts tomorrow."

    menu:
        "Daily Loop - VERY Work-In-Progress":
            jump DayStart
        "Restart Tour":
            jump MuseumTour
        "Main Menu":
            return

    return
    #jump DayStart

#generates random responses for the phone
label PhoneWaitResponse:
    if phone_wait_count == 0:
        $ phone_wait = "Someone will get it."
        $ phone_wait_count += 1
    else:
        $ phone_wait = renpy.random.choice(["Any minute now.", "Must be on their break.", "Really not my business.", "Wow, just keeps going.", "Isn't it going to go to voicemail?"])
        $ phone_wait_count += 1
    return

label VendingMachineIntro:
        python:
            button_press_count = 0
            selection = 0
        call screen vendingmachineselection          
