#day 0
label gameintroduction:
    scene museum bg1
    meta "You're in a crappy museum because you missed your bus in the rain."
    meta "The museum is deserted, no one even working the front desk."
    meta "The rain is not stopping."
    meta "You have just enough cash for something from the vending machine."
    call TotalDisposition
    meta "Current disposition is: [d_Total]"
    #vending machine "minigame" goes here
    jump vending_machine_intro

#I am using WAY too few labels in this prototype
label arguing_davids:
    d "But do you have to {i}stand{/i} on the head? It's grisly."
    meta "A voice echoes through the hall, but you still can't see anyone."

    #menus are used for player choices / dialogue
    menu:                                               
            "\"Hello?\"":                                
                meta "Your voice echoes like a ghost with no one to haunt."
            "Where is that coming from?":                                 
                meta "You look for the sound."

    d "Anyway it's \"David and Goliath\" not \"Goliath and Goliath\" you oversized fool."

    scene museum bg1
    show davids
    meta "The voices seem to come from somewhere behind a trio of statues."

    meta "Moving closer, the voices are clearer."
    meta "They're not... coming from the statues, are they?"

    menu:                                               
        "Step over the velvet rope.":          
            meta "Cautiously, you raise a leg over the rope."

    meta "It feels wrong, like being in a school hallway after hours."
    scene museum bg1 with hpunch:
    show davids
    meta "An alarm blares through the museum, you nearly drip as you hop back from the rope."

    menu:                                               
        "\"I DIDN'T TOUCH ANYTHING!\"":          
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

    #Show bubble vs regular text
    #Bubbles seem to be VERY labor intensive
    show admin excited at right
    ad "Admin jumps into their long list of things that need to get done."
    show admin stressed at right
    ad "Panic sets in when they realize there's no one left working at the museum."

    menu:                                               
        "\"I could do it.\"":          
            meta "What IT exactly is, you're not sure of."
        "\"Sounds like you're hiring.\"":          
            meta "Hey, worth a shot."

    ad "What\'s your name?"

    #player name input
    python:
        pc_name = renpy.input("What is your name?", length=32) #length is maximum length of the string
        pc_name = pc_name.strip()

        if not pc_name:
            pc_name = "NoName"

    pc "My name is [pc_name]!"
    show admin excited at right
    ad "Wow, are you {i}the{/i} [pc_name]?"
    ad "Your paper on the deontological ramifications of popularized historicity was..."
    ad "Well, I didn't understand much of it, but wow!"

    menu:                                               
        "\"Yes.\"":          
            meta "In this economy, the truth has to be a little flexible."
        "\"Yes?\"":          
            meta "Well, it isn't {i}NOT{/i} your name."
        "\"No.\"":          
            meta "Maybe wait until you have the job to start lying."

    show admin at right
    ad "OK, let's skip over most of the paperwork."
    ad "Any relevant work experience?"

    #work experience choices
    menu:               
        ad "Any relevant work experience?"                                
        "\"I was a library page (in 7th grade).\"":
            $ pc_work = 1    
            ad "That's... OK, great!"
        "\"Mostly gig work.\"":    
            $ pc_work = 2      
            ad "That's... OK, great!"
        "\"Does line cook count?\"":   
            $ pc_work = 3       
            ad "That's... OK, great!"
        "\"I can really twirl a sign.\"":      
            $ pc_work = 4    
            ad "That's... OK, great!"
        "\"I mean, not really?\"":      
            $ pc_work = 5    
            ad "That's... well it's not too important."
    
    #This dialogue line shows up twice so that the question is still visible in the menu
    ad "Any relevant skills?"

    menu:              
        ad "Any relevant skills?"                                 
        "\"I can really dissociate at work.\"":
            $ pc_skills = 1    
            ad "I'm not sure... oh, it's fine."
        "\"Graphic design is my passion.\"":    
            $ pc_skills = 2      
            ad "I'm not sure... oh, it's fine."
        "\"I know how to throw a KILLER party.\"":   
            $ pc_skills = 3       
            ad "I'm not sure... oh, it's fine."
        "\"I always get a five-finger discount.\"":      
            $ pc_skills = 4    
            ad "I'm not sure... oh, it's fine."
        "\"Afraid not.\"":      
            $ pc_skills = 5    
            ad "I'm not sure... oh, it's fine."

    ad "Lastly, what's your education background?"

    menu:             
        ad "Lastly, what's your education background?"                                  
        "\"I've apprenticed in the trades.\"":
            $ pc_education = 1    
            ad "Hmm, I guess that works?"
        "\"I listen to like, A LOT of podcasts.\"":    
            $ pc_education = 2      
            ad "Hmm, I guess that works?"
        "\"I think I left PBS on once?\"":   
            $ pc_education = 3       
            ad "Hmm, I guess that works?"
        "\"I've been to Italy!\"":      
            $ pc_education = 4    
            ad "Hmm, I guess that works?"
        "\"I'd rather not say.\"":      
            $ pc_education = 5 
            ad "Hmm, I guess that works?"

    ad "Ok, great! I'll take care of the filing."
    ad "I'm sure you're eager to start your journey here, so take the headset and follow along!"

    scene museum bg1
    show admin at right
    ad "This is the lobby"

    scene museum bg2
    ad "This is antiquities"
    show gilgamesh at left
    gi "Something rude about the admin"
    pc "What?"
    show admin at right
    ad "Moving on."

    scene museum bg1
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
    pc "WHAT IS HAPPENING?"
    ad "Next stop, keep up, I have 1078 more calls today"

    scene museum bg2
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
    
    scene museum bg1
    ad "That's the tour! Remember to lock up! Fate of the museum is decided in one week!"
    pc "This sucks"
    show vendingmachine
    v "Psst. Keys are in the drawer."
    pc "You talk too?"
    v "Yeah, don't worry about it. Let me give you helpful advice."
    v "This is my helpful advice."
    pc "This is still weird but thanks for the helpful advice."
    v "You're welcome. Also if the museum closes then I GET CRUSHED INTO A CUBE."
    pc "Oh shit!"
    hide vendingmachine
    meta "PC locks up, maybe some more brief encounters with pieces."
    meta "On the way out, encounter Nighthawks"
    show nighthawks at truecenter
    n "You reckon they'll stay on?"
    n "Nah, they won't even come back."

    scene museum bg1
    n "Alright, that's the first day, see you tomorrow."
    jump day_start

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
