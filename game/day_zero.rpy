#day 0

label GameIntroduction:
    scene intro bg1
    #leaving the interview, missed bus, chased by the rain into an empty museum.
    "Hiring Manager" "Dear Applicant,"
    "Hiring Manager" "Every journey begins somewhere."
    "Hiring Manager" "Yours, unfortunately, does not begin with us."
    "So, the interview hadn't gone {i}great{/i}."
    "And your day didn't improve when you missed your bus and the rain chased you into this forlorn museum."

    scene museum bg1 with fade
    "No job."
    "Wet clothes."
    "Two dollars and thirty-six cents in your pocket."
    "Just enough for a vending machine dinner."
    jump VendingMachineIntro

label DayZero:
    scene museum bg1
    "Your sad little snack doesn't last long."
    "Outside, the rain still falls."
    "???" "But do you have to {i}stand{/i} on the head? It's grisly."
    "A voice echoes through the empty hall."

    menu:                                               
        "Hello?":                                
            "Your voice echoes like a ghost with no one to haunt."
        "Where is that coming from?":                                 
            "You certainly don't see anyone."

    "???" "It's {i}David{/i} and Goliath not {i}Goliath{/i} and Goliath you oversized buffoon."

    scene museum bg1
    show davids
    "The voices come from somewhere behind a trio of statues."
    "They're not... coming from the statues, are they?"
    "All that's stopping you from getting closer is the impenetrable velvet rope."

    menu:                                               
        "[[Step over the velvet rope.]":          
            "Cautiously, you raise a leg over the rope."
        "[[Duck under.]":          
            "You crouch and prepare to breach the perimeter."

    "It feels wrong, like being in a school hallway after hours."
    scene museum bg1 with hpunch:
    show davids
    #sound effect go here

    menu:                                 
        "An alarm blares through the museum."               
        "I DIDN'T TOUCH ANYTHING!":          
            "You can tell that to the judge. Knowing your luck, you won't even get parole."
        "[[Freeze and act small.]":          
            "You're not the first person who tried to get too close to a museum piece."

    scene museum bg1 with hpunch:
    show davids
    "The alarm sounds again and again."
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
    "Hold on-"
    ad "Then I need you to get down in the archives and chase the raccoons out again."
    "I don't think-"
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
    "The voice goes silent again. You hear furious typing."
    ad "Oh. He resigned."
    #revise
    ad "That's great, that's fine." 
    ad "If I finish the paperwork and start redesigning the brochures now..."
    ad "...send out the press releases and donor letters..."
    ad "...budgeting a generous half-hour for sleep..."
    ad "Which would leave... twenty-minutes to prep for the gala."

    menu:                                               
        "I could do it.":          
            ad "You could?"
            "What IT is exactly, you're not sure."
        "Sounds like you're hiring.":          
            "Hey, worth a shot."
            ad "Are we?"
            ad "Yes! We are!"

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
    show admin excited at right
    "A gasp crackles over the line."
    ad "Are you {i}the{/i} Dr. [pc_name]?"
    ad "We spoke after your last visit."
    ad "Your paper on the deontological ramifications of popularized historicity was..."
    ad "Well, I didn't understand much of it, but wow!"

    #revise
    menu:                                               
        "Yes. [[Lie]":     
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

    show admin at right
    hide admin
    "There is a clunk as the receiver is set down."
    "A moment later, the same voice answers the phone."
    show admin at right
    ad "Retention and Recruitment, am I speaking with {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [pc_name]?"
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
    
    
    menu:              
        ad "Next: Any relevant skills?"                                 
        "I can really dissociate at work.":
            ad "Oh my, that must be nice."
        "My friends all treat me like their therapist.":    
            ad "Friends? Wow, I'll put, 'great social skills.'"
        "I know how to throw a KILLER party.":   
            pc "Ragers, keggers, raves, I'm flexible."
        "Just some light breaking and entering.":      
            ad "Hmm, let's put: 'discretion and experience with tools.'"
        "I've listened to a lot of people complain.":      
            ad "Ah, we do get a lot of those here."
        "Afraid not.":      
            ad "I'm not sure... oh, it's fine."

    menu:             
        ad "Lastly: What's your education background?"                                  
        "I've apprenticed in the trades.":
            ad "Wonderful! Our maintenance budget has really tanked."
        "I listen to like, A LOT of podcasts.":    
            ad "Me too! I have three going right now."
        "I think I took an art course?":   
            ad "You think?"
            pc "I mean, I didn't go."
            ad "Well, that's better than nothing!"
        "I've seen The Da Vinci Code":      
            ad "Oh, that is my favorite documentary!"
            ad "I never would have guessed Tom Hanks was a historian."
        "I have over three-hundred college credits.":      
            ad "Oh! What did you major in?"
            pc "I didn't. Never quite graduated."
        "I'd rather not say.":      
            ad "Well, it's not that important."

    ad "Ok, great! Let me look this over while I transfer you back."
    hide admin
    "Once again, they set down the receiver."
    show admin excited at right
    ad "Wonderful, I've heard back from Retention and Recruitment. They've approved!"
    ad "You are officially our new Curator."
    pc "Curator?"
    ad "Now I'm sure you're eager to get started so take the handset and follow along."

label MuseumTour:
    scene museum bg1 with fade
    show admin at right
    ad "This is the Grand Foyer."
    ad "These are our Davids. Most people don't know they were actually triplets."
    hide admin
    show davids at left
    d "I'm David."
    hide davids
    show davids at center
    d "I'm David."
    hide davids
    show davids at right
    d "I'm David."
    hide davids
    show davids at center
    "But as you approach, the echo fractures into three different voices, each one placing more emphasis on claiming identity for the one true David."
    dm "Prithee! I should have said I'm {i}the{/i} David."
    dd "No that's what I'm saying, {i}I'm{/i} the David. "
    db "Fools, you both, for I'm {i}the David{/i}."
    hide davids
    show admin at right
    pc "They sure seem to be talking a lot. Why do we have three of them?"
    ad "Moving on!"

    scene museum bg2 with fade
    ad "This is the Antiquities wing."
    ad "We're lucky to have a small collection of Sumerian artifacts."
    show gilgamesh at left
    gi "Nasir, look sharp! Another of the common-folk has come to bask in my glory. Ah to have such an opportunity."
    gi "I'd envy [them] if I didn't pity [them]."
    show eanasir angry at right
    e "Ugh..."
    hide gilgamesh
    hide eanasir
    #show sue at center with hpunch
    #sue "Roar."
    #pc "Did you just {i}say{/i}, \"Roar\"?"
    #revise
    pc "Can't you hear that?"
    show admin at right
    ad "Try not to fall behind, I have 57 calls waiting!"

    scene museum bg1 with fade
    show admin at right
    ad "This is the Fine Art wing."
    show theodore at left
    t "Please don't mention Van Gogh."
    show admin at right
    ad "This is, of course, the famous self-portrait by Van Gogh."
    show theodore angry at left
    t "God damnit."
    hide theodore
    show arnolfiniw at left
    arw "I didn't take it. What makes you think I took it?"
    ad "This is the Arnolfini Portrait, note the lovely detail!"
    hide admin
    show arnolfinim at right
    arm "I know you have it! Who else took it? The dog?!"
    ard "You two can't even move, how could something actually be stolen?"
    arw "Shush!"
    arm "Stay out of it!"
    hide arnolfinim
    hide arnolfiniw
    show admin at right
    ad "Often imitated and duplicated, our French collection includes the Mona Lisa!"
    show monalisa angry at left
    m "French? I'm Florentine, {i}bischero{/i}. And this sopping [pc_work], alike in dignity with this illustrious institution."
    pc "Hey!"
    m "Water remains the driving force of all nature. When it drives this place into the ground we can all go home."
    #revise
    hide monalisa
    ad "Please don't interrupt the tour!"

    scene museum bg2 with fade
    show admin at right
    ad "This is the Mixed Media wing."
    show sunflowers at left
    ad "Sunflowers was in the Fine Art wing with the other Van Gogh, until..."
    ad "Well, we couldn't afford to clean the soup off, so now it's here."
    su "I hate this soup."
    ad "(We decided to close the cafe after that incident.)"
    hide sunflowers
    show glimmer at left
    gl "If only we had a lunch special...the finest chicken nuggets and chardonnay. The kids can have bubble tea."
    hide glimmer
    show saintcatherine sad at left
    ad "This is a stained glass of Saint Catherine of Alexandria. It's French. Or Roman? Either way, it's broken."
    st "It's so dark. Where am I?"
    st "Who am I?"
    st "Please... I know you can't hear me, but I'm here."
    pc "Is she alright?"
    ad "Who? Nevermind, one more stop."

    scene museum bg2 with fade
    show admin at right
    ad "Lastly, this is the Office."
    "Surely there's nothing in here that can talk."
    p "Good luck!"
    pc "Who just said that?"
    show poster at left
    "You turn to see an inspirational poster hanging on the wall."
    p "I...I hope you do your best! I'm rooting for you!"
    
    scene museum bg1 with fade
    show admin excited at right
    ad "And that's the tour! As you can see, it's all very straightforward."
    pc "No, hold on, they were {i}talking{/i}--"
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
    pc "Yeah, the Admin mentioned that. Why is the museum closing?"
    v "You met the reasons."
    #v "They've been twisted up inside themselves so long, even they don't know what they're about."
    v "Anybody with a feel for art is gonna run screaming. No offense."
    pc "Why can I hear them? The Admin couldn't."
    #v "You got it twisted, {0}buddy{/0}{1}girl{/1}{2}buckaroo{/2}."
    show vendingmachine happy
    v "{i}All{/i} art can speak, most people just can't {i}listen.{/i}"
    v "They got all these {i}ideas{/i} and {i}thoughts{/i}. What art IS, what it ISN'T."
    v "But art speaks so quiet, they can't hear it over their own thoughts."
    pc "So why can {i}I{/i} hear it?"
    "The Vending Machine pauses with an electric hum."
    v "I guess you know how to keep your head clear."
    "Or empty."
    menu:
        "Are you saying I'm stupid?":
            v "Whoa, {0}bro{/0}{1}sis{/1}{2}champ{/2}! No aggro; I'm saying you're {i}zen{/i}."
        "So it's a superpower.":
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
            v "Dude was a bit of a hodad tee-bee-haitch."
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

    scene museum bg1 with fade
    "Four days."
    "Four days to save a dysfunctional gallery of art from itself. And maybe save your job with it."
    "But that can wait for tomorrow."
    "As [pc_name] leaves, someone whispers behind [them], unnoticed. (Or is that somebodies, plural?)"
    show nighthawks at truecenter
    n "Think our new curator is going to make it?"
    n "After THAT first day? Doubtful."
    if NameLie == 1:
        n "Like watching a slow-moving car crash. I mean, everyone knows the REAL Dr. [pc_name] is currently summering in the Hamptons with Banksy."
    if NameLie == 0:
        n "Like watching a slow-moving car crash. I mean, choosing {i}honesty{/i}? Everyone knows lying in interviews is a sacred and time-honored practice."
    n "I'd be shocked if [they] even come[s] back tomorrow."

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
    elif phone_wait_count > 0 and phone_wait_count < 11:
        $ phone_wait = renpy.random.choice(["Any minute now.", "Must be on their break.", "Really not my business.", "Wow, just keeps going.", "Isn't it going to go to voicemail?", "Whistle nonchalantly."])
        $ phone_wait_count += 1
    else:
        $ phone_wait = renpy.random.choice(["Wow, that could drive you nuts.", "Must be a LONG break.", "Someone must be coming.", "Whistle nonchalantlier."])
        $ phone_wait_count += 1
    return

label VendingMachineIntro:
        python:
            button_press_count = 0
            selection = 0
        call screen vendingmachineselection          
