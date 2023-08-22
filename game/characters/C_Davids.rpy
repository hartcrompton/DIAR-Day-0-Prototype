#Davids

default beat_Davids = 1

label conv_Davids:
    scene davidsbg
    show davids at right
    d "You're talking to me, the Davids!"
    menu:
        "Beat [beat_Davids]" if actions > 0 and beat_Davids < 5:
            jump .use_action
        "Bye":
            d "See ya"
            jump FreeRoam
        "Reset Beats":
            "Beats reset."
            $ beat_Davids = 1
            jump conv_Davids

label .use_action:
    #menu:
    #    d "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_Davids" + "." + "beat" + "%d" % beat_Davids
    #    "No, not really.":
    #        d "Understandable."
    #        jump conv_Davids
    jump expression "conv_Davids" + "." + "beat" + "%d" % beat_Davids

label .beat1:
    "You fear the sounds of infighting, again..."
    d "And that's why I'm the David."
    dm "How many times do we have to go over this? My reputation precedes me..."
    dd "Yeah yeah, dude. First colosal statue of its kind. We get it, we get it."
    db "At 17 feet you sound more like a Goliath than a David."
    pc "Hey could y'all give me the introductions without the insults?"
    pc "Alright, alright. Enough out of you dudes and Daves."
    dd "Yeah dude, that's why I'm the David. Cuz I'm actually A KID. And how do you know? Because I'm the actual height of...you guessed it... A KID."
    "He stamps his feet and inadvertantly bounces the head of Goliath up in the air before catching it on his feet like a hacky sack."
    db "And you bring inapproriate materials to a museum, like a kid." 
    "He scowls at both Davids."
    db "Both of ya...posers...feckless and improvident fuckboys."
    "He twists and stretches his limbs, almost doing calesthenics before banging out a push-up or two."
    db "How do you expect to defeat a giant by playacting like you both are?"
    pc "Can y'all even hear me? Just trying to help out here ok? I'll check back tomorrow."
    pc "I already have four or five Davids in my life. Remind me why I need another?"
    dm "Hark! Tell me, False Davids, did you hear something?"
    dd "I told you. It's THE DAVID not FALSE DAVID."
    db "Just the same old shit I've heard you two squabble about now for years: Who's really the The David?"

    "You have [actions] action(s) left."
    $ beat_Davids += 1
    jump FreeRoam

label .beat2:
    d "Ah you there... Yes... you? Do you know who we are?"
    dm "(placeholder) probably only know who I am because after all I am..."
    dd "You've got a good chance of recognizing my face and this guy's" 
    "He kicks the head and a thud resonantes in the quarter of the museum."
    db "Something to make clear that he's the only legitimate one because he's not posing but doing."
    pc "That's enough out of you all. I want some real introductions.  Not formal bickering between you."
    "They all strike their famous pose."
    d "We are The Davids!"
    pc "Obviously I know that. It's all you all talk about. But I also know a few Daves, a Davey, and went to school with like five other Davids too."
    pc "So which Davids are you?"
    dm "The Biblical. The original."
    dd "The one who slew Goliath."
    db "The one to combine bravery and skill."
    pc "Ok so you were a kid soldier... or something?"
    pc "I thought you already had a star named after you..."
    d "Well we were a King too!"
    pc "Oh like King Aruthur "
    "For the first time, the Davids are stunned into silence."
    "But only for a moment--"
    d "NO. NOT LIKE KING ARTHUR!"
    dm "We are the young shepherd boy..."
    dd "Chosen by like the actual God himself"
    db "To be the King of his chosen people."
    pc "Ah! Yes yes yes. That's right. I remember now."
    pc "Ok ok ok. I get it. This is coming back to me."
    dm "How would either of you know? None of us can even read the original source material anyway!"
    pc "The player chimes in and can say they remember the Bible of the top of their head and that you’ll tell them all tomorrow who you think represents the meaning of source material. OR the player can suggest they investigate the archives and read the source material on-site themselves. OR the player can also forgo both of the above options and immediately separate The Davids to ease the tension."
    "Research minigame. The player finds a copy of the bible and read the passage of David and Goliath "
    
    "You have [actions] action(s) left."
    $ beat_Davids += 1
    jump FreeRoam
label .beat3:
    "If the player choses to go read the source material: The Davids are pleased and are suddenly very nice to the Player and shower them with praise."
    "If the player choses to separate the Davids to ease the tension: They bridle and complain as the player moves them seperate corners. "
    d "If the player chose to go read The Source, then The Davids are keen to know \"Who’s the most David of them all?\""
    pc "The player has the choice to answer \"all\" \"Donnatello’s David\" \"Michelangelo’s David\" or \"Bernini’s David.\""
    d "If the player chose to not go read The Bible, then The Davids are a bit rude to the player. “Someone not doing the reading?” “Too good for the good book?”"
    pc "The player has the choice to answer “Donnatello’s David” “Michelangelo’s David” or “Bernini’s David.” But not \"all.\""
    pc "The player can return them to their corners, this time with velvet rope traps for each, with them facing the wall, away from the viewer.  "

    "You have [actions] action(s) left."
    $ beat_Davids += 1
    jump FreeRoam
label .beat4:
    "If the player chose “All”, then the Davids are no longer bickering, they are finally complementing each other, valuing how each one brings a different aesthetic to bear on the story. All is well."
    "If the player chose one particular David, then that David is thankful to the player while the others are commiserating with each other."
    "If the player chose return them to their corners, then the player is shocked to see that their wing is quiet, with the Davids now an indistinguishable mess of limbs and heads, with the only identifiable artifact, a single slingshot. "

    "You have [actions] action(s) left."
    $ beat_Davids += 1
    jump FreeRoam