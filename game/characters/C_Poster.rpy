#Poster

default beat_Poster = 1
default p_b3_c1 = 0
default CorgiPortraitStage = "base"
image corgiportrait = "/Characters/Poster/corgi base.png"

label conv_Poster:
    scene posterbackground
    if CorgiPortraitStage == "base":
        show corgi base at truecenter:
            yoffset -125
            zoom .9
    if CorgiPortraitStage == "flag":
        show corgi flag at truecenter:
            yoffset -125
            xoffset -115
            zoom .9
    if CorgiPortraitStage == "final":
        show corgi final at truecenter:
            yoffset -125
            xoffset -115
            zoom .9
    p "You're talking to me, the Poster!"
    menu:
        #"[[Chat a little.]":
        #    p "We're chatting a little now!"
        #    pc "We sure are."
        #    jump conv_Poster
        "Beat [beat_Poster]" if actions > 0 and beat_Poster < 5:
            #p "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            p "See ya"
            jump FreeRoam
        "Reset Beats":
            "Beats reset."
            $ CorgiPortraitStage = "base"
            $ beat_Poster = 1
            jump conv_Poster

label .use_action:
    #menu:
    #    p "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_Poster" + "." + "beat" + "%d" % beat_Poster
    #    "No, not really.":
    #        p "Understandable."
    #        jump conv_Poster
    jump expression "conv_Poster" + "." + "beat" + "%d" % beat_Poster

label .beat1:
    p "Did I help yesterday?"
    pc "I have to say, I didn't expect a poster to also be able to talk."
    p "How else could I help motivate you without talking?"
    pc "I mean...fair enough."
    p "So did I help? Was your day better?"
    menu:
        "Yes, you definitely helped!":
            p "Oh that's good, thank you! Maybe that means I can help even more people in this place."
        "Nah, not really.":
            p "Oh...oh no. Then how could I ever hope to help everyone in this place?"
    pc "Why do you even want to do that?"
    p "I just need to! I feel like I'm missing something, something that will help me do better."
    pc "What do you need? I don't even know how-"
    p "I'm sure there's something in this room. Can you look around for me? It'd mean the world!"
    call minigamestart_corgi("1")
    #minigame go here
    #p "I need something that can help me cheer people on"
    #p "Wrong object dialogue"
    #p "Wrong object dialogue"
    #p "Wrong object dialogue"
    #p "Wrong object dialogue"
    #p "That's perfect!"
    $ CorgiPortraitStage = "flag"
    hide corgi
    show corgi flag at truecenter:
        xoffset -115
        yoffset -125
        zoom .9
    p "This will help me so much, I mean look at it!"
    "The corgi poster made a grunting noise, seemingly as an attempt to wave the little flag."
    "Wow, look at me! I hope me and my little flag here helps make your day the best it can be! Good luck!"
    #####
    $ beat_Poster += 1
    jump FreeRoam
    
label .beat2:
    p "Hope you do your best today! And thank you for helping yesterday, it really helps me emphasize my words! Watch!"
    "Again, the poster seems to indicate its waving the flag. Again, nothing actually happens."
    p "I feel so free!"
    p "I hope I'm helping you out at least somewhat, unlike the last person who was here."
    pc "What happened?"
    p "The last employee here seemed really happy and I thought I was helping. Cheering them on, words of encouragement, everything!"
    pc "Well that's good, right?"
    p "I thought so. They were always pleasant to me."
    p "...but eventually they started to ignore me. Or maybe they just couldn't hear me anymore."
    p "I tried to yell as loud as I could, but nothing. They didn't even so much as glance at me, like they were sleep walking."
    p "Then one day, they stopped coming here. I never saw them again."
    p "Its all my fault! I should've tried harder to help them, but I wasn't enough."
    p "So I really gotta help you so you don't leave too! You are staying, right?"
    menu:
        "Yes, I'm staying!":
            p "Yay! Great!"
            p "Have a great day today! Do your best!"
            $ p_b2_c1 = "a"
        "I'm not sure":
            p "Oh no, I'm messing it up again! Was the flag not enough? Can you still hear me?"
            p "Well regardless, hope today is a great one. Do your best..."
            $ p_b2_c1 = "b"
    ####
    $ beat_Poster += 1
    jump FreeRoam
label .beat3:
    pc "Got anything to help me stay confident today?"
    if p_b2_c1 == "b":
        p "If you're just going to leave like the last person did, why even try?"
        pc "I might stay!"
        p "Sure..."
        p "Well what if I have something to help cheer you up?"
        p "...what is it?"
        p "What if I brought you out to show you the whole museum? "
        p "I mean okay, I guess."
        pc "I have to do some cleaning and could really use the motivation..."
        p "Oh! I think I can help with that. Maybe."
        call minigamestart_cleaning_corgi
        #minigame go here
        #p "Impressive!"
        #p "No holding back!"
        #p "Splendid job!"
        #p "Yeah, lets go!"
        p "Cleanup complete! Go you!"
        p "Thank you, that really helped! And you did an amazing job with the cleaning!"
    if p_b2_c1 == "a":
        p "Good morning! I'm thrilled to help you any way I can!"
        pc "Good to hear!" 
    p "I was thinking, remember when I said I wanted to motivate this entire place? The art place? This artsy building place?"
    pc "You mean museum?"
    p "Museum, yes! Thank you!"
    pc "Well what if I moved you somewhere outside this room where more people could see you?"
    p "Ooh, really? Where do you think would be best? Somwhere clean, I'm sure!"
    menu:
        "The Museum Entrance":
            $ p_b3_c1 = "Museum Entrance"
        "The Ticket Counter":
            $ p_b3_c1 = "Ticket Counter"
        "By The Restrooms":
            $ p_b3_c1 = "Restroom"
    p "That should work! Wow, this is so exciting I feel like I could burst!"
    p "But I feel like I'm still missing something. Can you help?"
    pc "Again?"
    p "Yeah, just one more thing. The flag is great but if I'm going to be out amongst the people, I think I need a little more flair!"
    call minigamestart_corgi("2")
    #minigame go here
    #p "Wrong item dialogue"
    #p "Wrong item dialogue"
    #p "Wrong item dialogue"
    #p "Wrong item dialogue"
    #p "Wrong item dialogue"
    #p "I think that'll work! Yes!"
    #p "This is perfect, thank you! I'm rooting for you!"
    hide corgi
    show corgi final at truecenter:
        xoffset -115
        yoffset -125
        zoom .9
    $ CorgiPortraitStage = "final"
    "The corgi poster seems to indicate its doing something with their new pom-poms. Of course, they don't move, but it's the thought that counts!"

    $ beat_Poster += 1
    jump FreeRoam
label .beat4:
    ####
    p "*sigh* Well good luck today."
    pc "Something the matter?"
    p "You found these things for me to hold to help, but what if it's not enough? What if you still leave?"
    p "*GASP!*"
    p "What if EVERYONE leaves???"
    pc "You know, it doesn't matter if I stay or leave.That one employee leaving wasn't your fault."
    p "It wasn't?"
    pc "I don't know, maybe you motivated them so well they moved on to bigger and better things!"
    p "What you do ISN'T the most important job in the world?"
    menu:
        "No, it's not that important.":
            p "Oh, okay..."
        "Yes, sorry, you're right. Nothing is more important than what I do!":
            p "Good! I thought so."
    pc "Either way it doesn't matter what I do. You help people no matter what, tyring to give them the confidence to keep going each day."
    pc "Its not your fault how they receive that. They might have more going on than you know!"
    p "I guess that's true. I can't control beyond what I can say. And what I say is all about helping people be the best they can be!"
    pc "Exactly.  All you can do is try to be encouraging and be satisfied that you're doing your best."
    p "Yeah, you're right! As long as I'm happy and doing my best to help, that's enough."
    pc "That's the spirit!"
    p "You know what? I think I'm ready to move out of this room."
    p "I love helping you, but I think I'm ready to support more people with my cheering!"
    pc "You sure?"
    p "Positive!"
    p "You mentioned the [p_b3_c1] - I think I'm ready to be moved out there!"
    p "Do you think I'm ready?"
    pc "One-hundred percent!"
    p "Good! I know I am, I just wanted you to confirm it! I've helped you be more confident in yourself too, you know!"
    "You take the poster out to the [p_b3_c1]."
    p "I love it here! Now do your best!"
    p "Haha, I can say to so many people now! Do your best! You do your best too! Yes, especially you over there!"
    pc "I will, with support from you!"
    "Even though the poster still is static and unmoving, you feel like its smiler has somehow, someway, gotten bigger."
    p "Hooray!"

    "You have [actions] action(s) left."
    $ beat_Poster += 1
    jump FreeRoam

label .OutcomeA:
    "The corgi poster enjoyed its new placement out in the museum, constnatly and joyfully shouting words of encouragement to all who passed by, whether they heard it or not."
    return
label .OutcomeB:
    "The corgi poster was happy to have a new employee to encourage, but were left feeling they could be helpingmore people if they could've just gotten out of the office."
label .OutcomeU:
    "The corgi poster sat lonely in the office, wondering why there words of encouragement never reached [PC]. Were they not helpful enough?"