#SoupAndSunflowers

default beat_SoupAndSunflowers = 1
default SoupCleanFakeString = "STRING"
default SunflowersCleanFakeString = "STRING"
image SSFakeCleanPortrait = "images/Characters/SoupAndSunflowers/Soup .jpg"
default SoloChoice = "NONE"
default MergeCounter = 0
default Day1Side = "NONE"
default SunflowersWant = "NONE"
default SoupWant = "NONE"
default SoupOutcome = "NONE"

label conv_SoupAndSunflowers:
    show soup at center
    menu:
        "Beat [beat_SoupAndSunflowers]" if actions > 0 and beat_SoupAndSunflowers < 5:
            jump .use_action
        "Bye":
            d "See ya"
            jump FreeRoam
        "Reset Beats":
            "Beats reset."
            $ beat_SoupAndSunflowers = 1
            jump conv_SoupAndSunflowers
        "Set Current Beat":
            menu:
                "1":
                    $ beat_SoupAndSunflowers = 1
                "2":
                    $ beat_SoupAndSunflowers = 2
                "3":
                    $ beat_SoupAndSunflowers = 3
                "4":
                    $ beat_SoupAndSunflowers = 4
            jump conv_SoupAndSunflowers 

label .use_action:
    jump expression "conv_SoupAndSunflowers" + "." + "beat" + "%d" % beat_SoupAndSunflowers
    #menu:
    #    p "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_SoupAndSunflowers" + "." + "beat" + "%d" % beat_SoupAndSunflowers
    #    "No, not really.":
    #        p "Understandable."
    #        jump conv_SoupAndSunflowers
    #return

label .beat1:
    su "Hey psst, [pc_name], right? Pleasure to meet you! I'm Sunflowers."
    su "Listen… I've got a stain on my frame. You can see it, can't you? "
    su "Would you mind helping me out?"
    menu:
        "Happy to!":
            su "Wonderful!"
        "I don't want to mess anything up…":
            su "It'll be fine! Quickly now!"
    #minigame go here
    "I didn't know you were, er, alive. Sorry!"
    so "Hey what the fuck!"
    su "Ignore that, it's the wind!"
    so "You're trying to kill me just like you're killing the planet!"
    su "Oh don't be so dramatic."
    menu:
        "Sorry! I didn't know you were, er, alive.":
            so "I'm just as alive as the next framed splash of color."
        "Great, now I've got soup stains talking to me.":
            so "I'm more than a stain."
    so "And I've got just as much right to be here as any painting."
    so "You can call me Soup. Nothing pretty. I'm not here to be pretty."
    su "As though being pretty is a bad thing."
    so "Prettiness is a distraction."
    menu:
        "How'd you come to be staining Sunflowers' frame, Soup?":
            so "I used to be just a regular can of soup. Not even that famous painting of one, either. But I'm much more than that now."
            su "Oh, here we go…"
        "Aren't you technically vandalism? Or something?":
            so "What if I am? Vandalism grabs attention. I'm not ashamed to admit it."
            su "That's because you're shameless."
    so "I'm a living protest against fossil fuel usage."
    so "My creators threw me at Sunflowers to bring attention to the anti-oil movement."
    so "I need to stay as a reminder. You can't wipe away the coming climate apocalypse."
    su "Nobody wants to go to an art museum and see soup stains on the art!"
    so "It's about the message. Interpretation."
    su "It's also about beauty, and harmony, and-and-"
    so "There will be no beauty or harmony when it's all ash! The people need to know!"
    menu:
        "Look, you both make good points. Pump the brakes a bit.":
            $ MergeCounter += 1
            $ Day1Side = "Both"
            so "What do you know? You tried to erase me!"
            su "Nobody likes a fence-sitter, [pc_name]. Soup is clearly irrational."
            so "Sunflowers thinks saving the planet is irrational. You still think they make good points, [pc_name]?"
            su "Better than yours!"
        "Sunflowers is right. This is an art museum. Not a… soup stain museum. ":
            $ Day1Side = "Sunflowers"
            su "Thank you!"
            so "Better to be a soup stain than an oil stain, like Sunflowers. No more oil! Stop all oil!"
            su "I'm made of seed oil, not petrochemical oil, you dolt!"
        "Soup is right. The environment is more important than one painting.":
            $ Day1Side = "Soup"
            so "Obviously. It's sad that it even needs to be said."
            su "A soup stain is not going to save the world."
            so "Not with that attitude."
            su "You have delusions of grandeur!"
            so "You have delusions of adequacy!"
    "They continue to bicker. You're not making any progress today. You decide to slip away."
    $ beat_SoupAndSunflowers += 1
    jump FreeRoam
label .beat2:
    "As you approach Soup and Sunflowers, you're surprised you haven't heard their bickering voices."
    "But as soon as you get close…"
    if Day1Side == "Both":
        so "Well, well, well, if it isn't the attempted murderer. Going to try to erase me again?"
        su "If you're not here to clean off this pesky stain, you might as well keep walking."
        so "You better keep walking if you care about the planet. Unlike someone…"
        su "Oh, forgive me for wanting the curator of this art museum to care about art, too."
        so "You just want to silence my message!"
    if Day1Side == "Sunflowers":
        so "Well, well, well, if it isn't the attempted murderer. Going to try to erase me again?"
        su "Cleaning isn't murder. You should know that."
        so "What's that supposed to mean?"
        su "Aren't you wanting to clean the environment? Maybe those oil spills don't want to be erased, either."
        so "You do want to destroy the environment! I knew it!"
    if Day1Side == "Soup":
        su "If you're not here to clean off this pesky stain, you might as well keep walking."
        so "Don't be bitter just because [pc_name] cares about the planet."
        su "Oh, forgive me for wanting the curator of this art museum to care about art, too."
        so "You just want to silence my message!"
    "And there they go. You better cut in."
    menu:
        "One at a time! I'll hear Sunflowers out today and Soup tomorrow.":
            so "Fine. Fuck you, and I'll see you tomorrow."
            $ SoloChoice = "Soup"
            jump SunflowersSolo
        "One at a time! I'll hear Soup out today and Sunflowers tomorrow.":
            su "Good luck. Talk to you tomorrow."
            $ SoloChoice = "Sunflowers"
            jump SoupSolo
    $ beat_SoupAndSunflowers += 1
    jump FreeRoam
label .beat3:
    if SoloChoice == "Sunflowers":
        jump SunflowersSolo
    if SoloChoice == "Soup":
        jump SoupSolo
    label SunflowersSolo:
        if SoloChoice == "Sunflowers":
            "You return to Soup and Sunflowers. Soup has surprisingly kept their word to remain silent while you talk to Sunflowers."
        su "I can finally hear myself think!"
        su "So what did you want to talk about, [pc_name]?"
        menu:
            "First I want to know more about you.":
                su "I was painted in 1888 by Vincent van Gogh."
                su "I love art. I love galleries and museums. They're so serene, so awe-inspiring."
                su "I don't know if I inspire awe, but it's nice being around art with so much importance."
            "How long have you been stuck with Soup?":
                su "Ugh. A little over a year, now. It's so embarrassing."
                su "I never asked to be the victim of that anti-oil protest. I don't even know what it was all about."
                su "I just know I'm ugly now. I was never important, but at least I was nice to look at. Once."
        menu:
            "You don't think you're important?":
                su "Well, I… I'm just a still-life of some flowers. And that's fine!"
                su "But I'm not even Van Gogh's most important work. Heck, I'm not even the only painting of sunflowers he did!"
                su "There were so many!"
            "Do you think Soup is important?":
                $ MergeCounter += 1
                su "Soup's annoying, which undercuts their message. But the message matters."
                su "I know pollution is bad. I've been polluted!"
                su "And I guess that was the point of the protest, in a way."
        su "I love when art has something to say. Van Gogh painted me as a gift for a friend. That's a pretty message. But is it important?"
        menu:
            "Beauty and kindness are very important.":
                $ SunflowersWant = "Erase"
                "Sunflowers seems to bloom a warmer yellow."
                su "You're right. I think so too. The world is better with beauty and kindness. "
                su "And that's exactly why rude stains should be removed. I would be at my best with a clean frame."
                su "Thank you, [pc_name]. I needed your reassurance that my wish to be free from Soup wasn't something I should apologize for."
                su "Well, I suppose you need to carry on with your tasks. Good luck!"
            "Maybe. But it's not as important as protecting the planet.":
                $ SunflowersWant = "Remain"
                su "So Soup's message is more important than small kindnesses for friends…"
                su "You're probably right. Soup just wants to protect nature. I can't fault them for that."
                su "I mean, I'm literally a painting of flowers. Nature matters. I wish Soup wasn't so… loud. But it's not right to “tone police” an important message."
                su "Sigh. I appreciate your candor, [pc_name]. But I should let you go while I think this over…"
            "Not all art needs a message. And a message doesn't need to be art.":
                $ SunflowersWant = "Detach"
                su "So it's okay for a painting to simply be pretty? And it's okay for an important message to come in an ugly package?"
                su "You know, if Soup's message is strong enough, it should be able to stand on its own merit without me."
                su "And I'd be free to exist as a pretty painting without the need to say anything."
                su "Maybe Soup can be convinced to be separated from me. They're only on my frame, after all…"
                su "Food for thought. In any case, I've probably taken enough of your time for today."
        su "We'll talk again soon."
        "You say goodbye and leave Soup and Sunflowers for now."
        $ beat_SoupAndSunflowers += 1
        jump FreeRoam
    label SoupSolo:
        if SoloChoice == "Soup":
            "You return to Soup and Sunflowers. Sunflowers is remaining silent as promised. You're free to talk to Soup without being interrupted by bickering."
        so "It's good to be able to speak my truth without Sunflowers interrupting me."
        so "Let's do this."
        menu:
            "Tell me why you're so passionate about climate activism.":
                so "As I've told you before, my creators threw me at Sunflowers to grab attention for the anti-oil movement."
                so "Like tomato soup staining a beautiful painting, oil is staining this beautiful planet."
                so "Everyone needs to wake up and face it. No matter how ugly it looks."
            "Do you have a problem with art? Or just Sunflowers?":
                so "Of course I don't hate art. It's a great way to spread a message. Nor do I hate Sunflowers."
                so "But all the pretty flower pictures in the world aren't going to save the planet when it's on fire."
                so "Now isn't the time to be a pretty and docile flower. It's time to get LOUD."
                so "Because the truth isn't pretty like a Van Gogh painting. It's ugly like a soup stain."
        menu:
            "Are you envious of Sunflowers' beauty?":
                $ MergeCounter += 1
                so "Sunflowers' beauty is part of the message. It's a tool. A metaphor."
                so "My ugliness is a part of that message. We both play our parts for the good of the whole."
                so "Would I prefer to play the part of the beauty? Maybe. At least I wouldn't be so darn whiny about it…"
                so "I know Sunflowers didn't ask to be vandalized. And I didn't ask to be splashed against their frame. But we're here now."
                so "And we should both be honored to aid the fight for climate justice. "
            "Do you feel bad about being a stain?":
                so "You misunderstand me. A stain can be art. Call me abstract expressionism if you want to be snooty."
                so "Sunflowers is a stain on a canvas in the shape of sunflowers. They may be prettier than me, but… but I still have meaning."
                so "I'm not a random stain. I was put here for a reason. I'm still art, damn it."
                so "Sunflowers is my canvas. My platform. My presence tells a story. I'm the message."
        so "The best art captivates and shocks with its beauty and its deeper meaning. The defacement of beauty is the deeper meaning. "
        menu:
            "You didn't ask to be a message. You don't have to keep being one forever.":
                $ SoupWant = "Erase"
                so "I know that. I know… "
                "Soup hesitates. Then their voice gets quieter than you've ever heard it. Smaller, even."
                so "I know I'm nothing if I'm not getting through to people. And honestly… I'm not sure I've gotten through to anyone."
                so "Maybe I really am just doing a disservice to the climate movement by irritating others."
                so "I… Damn it. I have to think about this. "
            "Your message matters, and should be as loud as possible.":
                $ SoupWant = "Remain"
                so "Yeah… Yeah! Of course it should!"
                so "Politeness isn't going to save the planet. The time for calm deliberation is over. This is a war front. And the planet is losing."
                so "If we're to show the public the ugly truth, that truth needs to be inconvenient. Shocking."
                so "Like me."
                so "I'm glad you see things from my point of view, [pc_name]."
            "You can still be a reminder of why you were created without needing to be covering Sunflowers.":
                $ SoupWant = "Detach"
                "Soup hesitates."
                so "It's not as though I want to be stuck with Sunflowers. But I don't think my message is as strong alone."
                so "It's not a protest if no one is uncomfortable."
                so "That said, just because I aim to discomfort doesn't mean I want to make Sunflowers miserable."
                so "Maybe you're right that my legacy can still be a strong message without the constant need for vandalism. "
                so "Hm. It would certainly be preferable to erasure. So I'll think about it."
        so "We'll talk again soon."
        "You say goodbye and leave Soup and Sunflowers for now."
        $ beat_SoupAndSunflowers += 1
        jump FreeRoam
label .beat4:
    su "Good to see you again, [pc_name]. I've been feeling better about things since we last spoke."
    so "Same. Feels damn good to have some clarity."
    if SunflowersWant == "Detach":
        su "Soup's message matters. So does my beauty. It's best if you separate Soup and me by removing my frame."
    if SunflowersWant == "Erase":
        su "Soup detracts from my worth as a work of art - and the museum by extension. Cleaning off the stain might be for the best."
    if SunflowersWant == "Remain":
        su "I can't deny that Soup's message is too important to lose. And, like it or not, I help that message be told. So Soup can stay - with my blessing."
    if SoupWant == "Detach":
        so "I can still spread my message without Sunflowers. The history of my creation speaks for itself. You can remove the painting frame to separate us."
    if SoupWant == "Erase":
        so "I see now that I've been more annoying than inspiring, likely to turn people off of the climate movement. I should be erased for the greater good."
    if SoupWant == "Remain":
        so "I'm more convinced than ever that I need to keep fighting for climate justice. And I do that best right where I am."
    if SunflowersWant == SoupWant:
        su "This may be the first time Soup and I have agreed on something. How wonderful!"
    else:
        su "It sounds like we still disagree with what should be done about the stain… "
    so "Whatever the case, you're still the one to make the final decision, [pc_name]. You're the curator here. What will you do?"
    menu:
        "I want to make a change.":
            "erase soup minigame"
            jump MinigamePlaceholder
        "I'm going to leave Soup attached to Sunflowers.":
            $ SoupOutcome = "Remain"
            jump MinigameFinale
        "I'm going to leave you as you are. Because you're no longer two separate works of art - you're one brand new one." if MergeCounter >= 2:
            jump SSMerge
    label SSMerge:
        su "We're… one work of art? "
        so "Yes… Not simply a stain raging against climate change."
        su "And not simply one still-life of flowers among many others…"
        so "Historical significance bringing awareness. Beauty obscured."
        su "A message. A warning. A work of art with something to say."
        so "We're a famous painting whose new face reflects a changing world."
        su "Not “we.”"
        so "No. Not “we”..."
        ss "I."
        ss "I am Soup & Sunflowers. A work of art all my own. A beautiful painting with a striking stain. A metaphor for a poisoned world!"
        ss "Yes. Yes! I'm provocative! I'm daring! I'm going to change hearts and minds, baby!"
        ss "You and me, [pc_name], we're gonna save the world!"
        "The positive vibes are radiating from Soup & Sunflowers."
        menu:
            "I'm glad you know who you are now.":
                ss "Me too, mate. Why be kind and passive like a flower, or rude and aggressive like a stain, when I can be kind and aggressive like a LEADER?"
                ss "That's the real way to win folks over. "
            "Hell yeah we are!":
                ss "Loud and proud, baby! This museum is going to be the spark that lights the fire. I can feel it!"
        ss "Thanks for helping me figure my shit out, [pc_name]. You're a star, mate."
        ss "Now get back out there and curate the FUCK out of this museum! Woo! Planet Earth, let's fucking gooooo!"
        "You take your leave of Soup & Sunflowers, full of energy and ready to take on the world."
        jump SSEnding
    label MinigamePlaceholder:
        menu:
            "placeholder for final minigame"
            "Erase":
                $ SoupOutcome = "Erase"
            "Detach":
                $ SoupOutcome = "Detach"
            "Remain":
                $ SoupOutcome = "Remain"
        jump MinigameFinale
    label MinigameFinale:
        if SoupOutcome != "Erase":
            if SoupWant == SoupOutcome:
                so "I think this is for the best. I'm still here! I can still make a difference! "
            if SoupWant != SoupOutcome:
                so "I can't help feeling this could have gone better. But just like with global warming, things don't always get better. "
        if SunflowersWant == SoupOutcome:
            su "I'm so glad you could help, [pc_name]. Thanks for making me feel confident that this is the right outcome."
        if SunflowersWant != SoupOutcome:
            su "I'm surprised you changed your mind after what you said to me when we spoke…"
        if SoupOutcome != "Erase":
            if (SoupWant == SunflowersWant) and (SoupWant == SoupOutcome):
                so "Never thought I'd wind up agreeing with Sunflowers. But I'm not mad about it."
                su "You know, you might be the best curator I've had, [pc_name]."
            if (SoupWant != SoupOutcome) and (SunflowersWant != SoupOutcome):
                so "Why did you bother talking to us if you were going to ignore both our wishes? Jerk."
                su "Wait, you didn't choose what you said you'd do for either of us? I might even be MORE frustrated now than I was originally!"
        menu:
            "Just doing my job, folks." if ((SoupWant == SunflowersWant) and (SoupWant == SoupOutcome)):
                if SoupOutcome != "Erase":
                    so "Could be better. Could definitely be worse. Look after yourself, [pc_name]. And the planet, too."
                su "I look forward to continuing to work with you! Let's make this place the best it can be. Good luck, [pc_name]!"
                "You say goodbye, feeling like you've made a positive difference."
            "I have my reasons for making that decision. You'll have to make the best of it." if ((SoupWant != SoupOutcome) and (SunflowersWant != SoupOutcome)):
                if SoupOutcome != "Erase":
                    so "Making the best of a bad situation is what we'll all have to do in a warming climate. "
                su "I really hoped you'd be able to help. Not just me, but the museum. Now I'm not so sure you will. Goodbye, [pc_name]."
                "You walk away from the painting and the worsening vibes it's now giving off."
            "There was no pleasing you both. I did my best." if (((SoupWant == SoupOutcome) or (SunflowersWant == SoupOutcome)) and (SoupWant != SunflowersWant)):
                if SoupOutcome != "Erase":
                    if SoupWant == SoupOutcome:
                        so "Soup - I'm glad I was the one to be pleased. I'm going to keep pushing my message thanks to you, [pc_name]. It's not pretty, but it's real. Like me."
                    if SoupWant != SoupOutcome:
                        so "I should be grateful I'm still here. But I'm still pissed you pulled the rug out from under me. I won't forget that."
                if SunflowersWant == SoupOutcome:
                    su "You did just fine, [pc_name]. I'm glad we could talk. Good luck with the museum!"
                if SunflowersWant == SoupOutcome:
                    su "I'm just surprised you chose Soup's wishes over mine, [pc_name]. I hope it was the right choice. So long."
                "You leave the painting feeling conflicted, but you're pretty sure the vibes are better than before. So that's something."
        jump SSEnding
    label SSEnding:
        $ beat_SoupAndSunflowers += 1
        jump FreeRoam


######
label SSFakeCleanDialogue:
    #essentially just bring up an imagemap and every time you click the imagemap you get dialogue
    $ SunflowersCleanFakeString = renpy.random.choice(["Get this soup off me!", "Come on, get rid of it.", "Are you even trying?"])
    $ SoupCleanFakeString = renpy.random.choice(["I'm not going anywhere!", "Hey, stop that!", "I mean something!"])
    su "[SunflowersCleanFakeString]"
    so "[SoupCleanFakeString]"

screen wait_SSFakeClean():
    pass

label call_SSFakeClean():
    scene museum bg2
    label .repeat:
    show screen SSFakeClean()
    call screen wait_SSFakeClean()
    if _return == "exit":
        hide screen SSFakeClean
        return

    show layer middle
    call expression _return
    show layer middle at reset
    jump .repeat

transform unfocus:
    blur 10

screen SSFakeClean:
    layer "middle"
    

    modal renpy.get_screen("wait_SSFakeClean") # if you don't need modal, omit this line
    sensitive renpy.get_screen("wait_SSFakeClean")
    imagemap:
        ground "images/rooms/museum bg1.jpg"
        hotspot (0, 0, 1920, 1080) action Return("SSFakeCleanDialogue") #call up the appropriate second screen K
    frame:
        xalign .5
        yalign .5
        xoffset 0
        yoffset 0
        background None
        xminimum 450
        xmaximum 450
        yminimum 900
        ymaximum 900    
        vbox:
            add "SSFakeCleanPortrait"
    