#Poster

default beat_Poster = 1
default p_b3_c1 = 0

label conv_Poster:
    scene posterbackground
    show poster at left
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
    p "Did I help?"
    pc "Didn't expect a poster to also talk"
    p "How else could I help motivate you without talking?"
    pc "Fair enough"
    p "So did I help? Was your day better?"
    menu:
        "Yes, you helped.":
            p "Oh good! I hope I can do the same for everyone in the museum"
        "No, you didn't help.":
            p "Oh then how can I motivate everyone in the museum?"
    pc "Why do you want to do that?"
    p "I just need to! I feel like I'm missing something, something that will help me do better."
    pc "What do you need? I don't even know how-"
    p "I'm sure there's something in this room. I'll help!"
    "\"I Spy\" minigame where the PC searches the room on a single screen for an object that will help the poster out. The poster will give a single hint and there will be a few selectable objects (about 5) on screen for the player to click. Each one elcits a bard from the poster, with the minigame ending with the correct object clicked on."
    p "Thank you so much, this will help a ton! Hopefully! Now do your best today!"    

    "You have [actions] action(s) left."
    $ beat_Poster += 1
    jump FreeRoam
    
label .beat2:
    p "Hope you do your best today! And thank you for helping yesterday, it really helps me emphasize my words! Watch!"
    "The poster does not move, for it is a poster."
    p "I feel so free!"
    p "Sorry for not giving a reason for motiviation."
    pc "What happened?"
    p "The last employee here seemed really happy and I thought I was helping!"
    pc "That's great!"
    p "They showed up every day and seemed happy"
    p "But eventually they stopped hearing me, at least I think they did"
    p "I tried to be louder, but they just heard me less"
    p "Then one day they just stopped showing up"
    p "Its all my fautl, I should've tried harder but I wasnt good enough"
    p "So I have to help you even more so you stay? You are, aren't  you?"
    menu:
        "Yes, I'm staying!":
            p "Oh I'm glad!"
            $ p_b2_c1 = "a"
        "I'm not sure":
            p "Oh, I'm messing it up again! Was the flag (or whatever item from the Beat 1 minigame) not enough?"
            $ p_b2_c1 = "b"

    "You have [actions] action(s) left."
    $ beat_Poster += 1
    jump FreeRoam
label .beat3:
    pc "Got anything to help me stay confident today?"
    if p_b2_c1 == "b":
        p "If you're just going to leave like the last person because I'm bad at my job, why try?"
        pc "I could still say! I think I have something to cheer you up."
        p "What is it?"
        pc "What if I brought you out to show you the whole museum?"
        p "Okay, I guess..."
        pc "I have to do some cleaning and could really use the motivation"
        p "I think I can help! Maybe."
        "Cleaning minigame where the poster gets to give a motiviating quip after each item is picked up"
        p "Thank you, that really helped!"
    if p_b2_c1 == "a":
        p "Good morning! I'm thrilled to help you any way I can!"
        pc "Good to hear!"
    p "I was thinking, I want to motivate everyone but I don't even know anything outside of this room!"
    pc "What if I moved you somewhere where more people could see you?"
    p "Really? What would you suggest?"
    menu:
        "The Museum Entrance":
            $ p_b3_c1 = "Museum Entrance"
        "The Ticket Counter":
            $ p_b3_c1 = "Ticket Counter"
        "By The Restrooms":
            $ p_b3_c1 = "Restroom"
    p "Oh I think that'd be nice!"
    p "But I feel like I'm still missing something. Can you help?"
    pc "Again?"
    p "Yeah, just one more thing."
    "Same \"I Spy\" minigame as Beat 1 with the same mechanics - 5 objects in the room and each selection gets a bark from the poster, with the minigame ending when the correct object (a pom pom) is selected."
    p "This is perfect, thank you! I'm rooting for you!"
    "The poster seems to indicate it's doing something with the object to cheer you on, but again, its a poster and cannot really move."    

    "You have [actions] action(s) left."
    $ beat_Poster += 1
    jump FreeRoam
label .beat4:
    p "Good luck today..."
    pc "Something wrong?"
    p "You found these things for me to hold to help, but what if it's not enough? What if you leave?"
    pc "It doesn't matter if I stay or leave, that one employee leaving wasn't your fault."
    p "It wasn't?"
    pc "Maybe you motivated them so well they moved on to bigger and better things!"
    p "What you do ISN'T the most important job in the world?"
    menu:
        "No, it's not. Not that important.":
            p "Oh, okay..."
        "Yes, sorry, you're right. Nothing is more important!":
            p "Oh, okay! I thought so!"
    pc "Either way it doesn't matter what I do. You help people no matter what, giving them the confidence to move forward each day."
    p "Yeah, you're right! As long as I'm happy and doing my best to help, that's enough."
    pc "That's the spirit!"
    p "I think I'm ready to move out of this break room."
    p "I love helping you, but I think I'm ready to support more people with my cheering!"
    pc "You sure?"
    p "Positive!"
    p "You mentioned the [p_b3_c1] - I think I'm ready to be moved out there...do you think I'm ready?"
    pc "You're ready!"
    p "I know I am! I just wanted you to confirm it! I've helped you be more confident in yourself too, you know!"
    "You take the poster out to the [p_b3_c1]"
    p "I love it here! Now do your best!"
    pc "I will, with support from you!"
    p "Hooray!"

    "You have [actions] action(s) left."
    $ beat_Poster += 1
    jump FreeRoam
