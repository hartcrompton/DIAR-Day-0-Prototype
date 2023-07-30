#day 0


label gameintroduction:
    scene museum bg1
    meta "You're in a crappy museum because you missed your bus in the rain."
    meta "The museum is deserted, no one even working the front desk."
    meta "The rain is not stopping."
    meta "You have just enough cash for something from the vending machine."
    jump vending_machine_intro

#I am using WAY too few labels in this prototype
label dayzero:
    scene museum bg1
    d "But do you have to {i}stand{/i} on the head? It's grisly."
    meta "A voice echoes through the hall, but you can't see anyone."

    menu:                                               
            "Hello?":                                
                meta "Your voice echoes like a ghost with no one to haunt."
            "Where is that coming from?":                                 
                meta "You look for the sound."

    d "It's {i}David{/i} and Goliath not {i}Goliath{/i} and Goliath you oversized freak."

    scene museum bg1
    show davids
    meta "The voices seem to come from somewhere behind a trio of statues."

    meta "Moving closer, the voices are clearer."
    meta "They're not... coming from the statues, are they?"
    meta "All that's stopping you from getting closer is the velvet rope."

    menu:                                               
        "Step over the velvet rope.":          
            meta "Cautiously, you raise a leg over the rope."

    meta "It feels wrong, like being in a school hallway after hours."
    scene museum bg1 with hpunch:
    show davids
    meta "An alarm blares through the museum."
    meta "Player nearly trips jumping back."

    menu:                                               
        "I DIDN'T TOUCH ANYTHING!":          
            meta "Tell that to the judge."
        "Freeze and act small.":          
            meta "You're not the first person who tried to get too close to a museum piece."

    scene museum bg1 with hpunch:
    show davids
    meta "The alarm blares again."
    meta "Oh. It's just the phone."

    scene museum bg1 with hpunch:
    meta "It's not stopping either."

    #cutesy little phone interaction
    label get_the_phone:
        scene museum bg1 with hpunch:
        call phone_wait_response
        menu:                                               
            "Answer the Phone":      
                meta "You answer the phone."    
            "[phone_wait]":          
                jump get_the_phone

    show admin excited at right
    ad "Admin jumps into their long list of things that need to get done."
    show admin stressed at right
    ad "Panic sets in when they realize there's no one left working at the museum."

    menu:                                               
        "I could do it.":          
            meta "What IT exactly is, you're not sure of."
        "Sounds like you're hiring.":          
            meta "Hey, worth a shot."

    ad "What\'s your name?"
    jump playernameinput

label playernameinput:
    #player name input
    python:
        pc_name = renpy.input("What is your name?", length=32) #length is maximum length of the string
        pc_name = pc_name.strip()
        if not pc_name:
            renpy.jump("playernameinput")

    pc "My name is [pc_name]!"
    show admin excited at right
    ad "Wow, are you {i}the{/i} Dr. [pc_name]?"
    ad "I thought you said you woldn't visit."
    ad "Your paper on the deontological ramifications of popularized historicity was..."
    ad "Well, I didn't understand much of it, but wow!"

    menu:                                               
        "Yes. [[Lie]":          
            meta "In this economy, the truth has to be a little flexible."
        "Yes?":          
            meta "Well, it isn't {i}NOT{/i} your name."
        "No.":          
            meta "Smart to wait until you have the job to start lying."

    show admin at right
    ad "OK, let's skip over most of the paperwork."
    ad "Any relevant work experience?"

    #work experience choices
    menu:               
        ad "Any relevant work experience?"                                
        "I was a gas station attendant.": 
            ad "That's... OK, great!"
        "Mostly gig work.":       
            ad "That's... OK, great!"
        "Bouncer.":       
            ad "That's... OK, great!"
        "Painter.":      
            ad "Portraits, landscapes?"
            pc "Mostly houses. A few boats, some propane tanks."
            ad "That's... OK, great!"
        "I um, I've procured art for private clients.":      
            ad "That's... OK, great!"
        #"I mean, not really?":      
            #ad "That's... well it's not too important."
    
    ad "Any relevant skills?"
    menu:              
        ad "Any relevant skills?"                                 
        "I can really dissociate at work.":
            ad "I'm not sure... oh, it's fine."
        "My friends all treat me like their therapist.":    
            ad "I'm not sure... oh, it's fine."
        "I know how to throw a KILLER party.":   
            ad "I'm not sure... oh, it's fine."
        "Just some light breaking and entering.":      
            ad "Why would you tell me... oh, it's fine."
        "I've listened to a lot of people complain.":      
            ad "I'm not sure... oh, it's fine."
        #"Afraid not.":      
            #ad "I'm not sure... oh, it's fine."
    ad "Lastly, what's your education background?"

    menu:             
        ad "Lastly, what's your education background?"                                  
        "I've apprenticed in the trades.":
            ad "Hmm, I guess that works?"
        "I listen to like, A LOT of podcasts.":    
            ad "Hmm, I guess that works?"
        "I think I took an art course?":   
            ad "You think?"
            pc "I mean, I didn't go."
            ad "Hmm..."
            ad "It's better than nothing."
        "I've seen The Da Vinci Code":      
            ad "Hmm, I guess that works?"
        "I've got over three-hundred college credits.":      
            ad "Oh! What did you major in?"
            pc "I didn't. Never quite graduated."
        #"I'd rather not say.":      
            #ad "Hmm, I guess that works?"

    ad "Ok, great! I'll take care of the filing."
    ad "I'm sure you're eager to start your journey here, so take the phone and follow along!"

label museumtour:
    scene museum bg1 with fade
    show admin at right
    ad "This is the foyer."
    ad "These are the Davids."
    $ the_davids = "The Davids"
    show davids at left
    d "Arguing amongst themselves"
    pc "They sure seem to be talking. Weird."
    ad "Moving on!"

    scene museum bg2 with fade
    ad "This is antiquities"
    show gilgamesh at left
    gi "Something rude about the admin."
    show eanasir at right
    e "Exasperated."
    hide gilgamesh
    hide eanasir
    show sue at center with hpunch
    sue "Roar."
    pc "Did you just {i}say{/i}, \"Roar\"?"
    show admin at right
    ad "I am oblivious to this weirdness. Moving on!"

    scene museum bg1 with fade
    show admin at right
    ad "This is the Fine Art wing"
    show theodore at left
    t "Please don't mention Van Gogh."
    show admin at right
    ad "This is the famous self portrait by Van Gogh."
    show theodore angry at left
    t "God damnit."
    hide theodore
    show arnolfinim at left
    ar "We hate each other."
    show arnolfiniw at left
    ar "So much."
    hide arnolfinim
    hide arnolfiniw
    pc "WHAT IS HAPPENING?"
    ad "And of course, the Mona Lisa."
    show monalisa at left
    m "A cutting remark."
    ad "Next stop, keep up, I have 1078 more calls today."

    scene museum bg2 with fade
    show admin at right
    ad "This is mixed media"
    show sunflowers at left
    ad "Sunflowers was originally in the fine art wing, until..."
    ad "Well, we couldn't afford to clean it, so now it's here."
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
    ad "That's the tour! Remember to lock up! Fate of the museum is decided in four days!"
    pc "I have several questions."
    ad "Already hanging up."
    pc "This sucks."
    show vendingmachine
    v "Psst. Keys are in the drawer."
    pc "You talk too?"
    v "Yeah, don't worry about it. Let me give you helpful advice."
    v "This is my helpful advice."
    pc "This is still weird but thanks for the helpful advice."
    v "You're welcome. Also if the museum closes then I GET CRUSHED INTO A CUBE."
    pc "Oh shit!"

    scene museum bg1 with fade
    meta "PC locks up."
    meta "On the way out, encounter Nighthawks"
    show nighthawks at truecenter
    n "You reckon they'll stay on?"
    n "Nah, they won't even come back."

    scene museum bg1
    meta "Alright, work starts tomorrow."

    menu:
        "Daily Loop - VERY Work-In-Progress":
            jump day_start
        "Restart Tour":
            jump museumtour
        "Main Menu":
            return

    return
    #jump day_start

#generates random responses for the phone
label phone_wait_response:
    if phone_wait_count == 0:
        $ phone_wait = "Someone will get it."
        $ phone_wait_count += 1
    else:
        $ phone_wait = renpy.random.choice(["Any minute now.", "Must be on their break.", "Really not my business.", "Wow, just keeps going.", "Isn't it going to go to voicemail?"])
        $ phone_wait_count += 1
    return

label vending_machine_intro:
        python:
            button_press_count = 0
            selection = 0
        call screen vendingmachineselection          
