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
default SSFakeCleanCount = 0
default SSMerged = 0
default SSTimeout = 0

transform SSShake:
    zoom .75
    yoffset -100
    xalign 0.5
    yalign 0.5
    ease .25 zoom .85 yoffset -50
    ease 0.05 xoffset 20
    ease 0.05 xoffset -20
    ease 0.05 xoffset 20
    ease 0.05 xoffset -20
    ease 0.05 xoffset 0

image ssportrait = ConditionSwitch(
    "SoupOutcome == 'Remain'", "images/Characters/SoupAndSunflowers/soupandsunflowers.png",
    "SoupOutcome == 'Erase'", "images/Characters/SoupAndSunflowers/sunflowersonly.png",
    "SoupOutcome == 'Detach'", "images/Characters/SoupAndSunflowers/soupandsunflowersdetached.png",
    "SoupOutcome == 'NONE'", "images/Characters/SoupAndSunflowers/soupandsunflowers.png")

label conv_SoupAndSunflowers:
    play music "music/B14_W_02.wav" fadein 0.4 volume 0.4
    scene mixedmedia_tod:
        blur 5
    show ssportrait at truecenter:
        zoom .75
        yoffset -100
    jump .use_action
    #menu:
    #    "Beat [beat_SoupAndSunflowers]" if actions > 0 and beat_SoupAndSunflowers < 5:
    #        jump .use_action
    #    "Bye":
    #        d "See ya"
    #        jump FreeRoam
    #    "Reset Beats":
    #        "Beats reset."
    #        $ beat_SoupAndSunflowers = 1
    #        $ SoupOutcome = "NONE"
    #        jump conv_SoupAndSunflowers
    #    "Set Current Beat":
    #        menu:
    #            "1":
    #                $ beat_SoupAndSunflowers = 1
    #            "2":
    #                $ beat_SoupAndSunflowers = 2
    #            "3":
    #                $ beat_SoupAndSunflowers = 3
    #            "4":
    #                $ beat_SoupAndSunflowers = 4
    #        jump conv_SoupAndSunflowers 

label .use_action:
    #call advance_time from _call_advance_time_6
    $ SSTimeout = 1
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
    su neutral "Hey, psst, [pc_name], right? Pleasure to meet you! I'm Sunflowers."
    su neutral "Listen…I've got a stain on my frame. You can see it, can't you? "
    su neutral "Would you mind helping me out?"
    menu:
        "You can count on me, flower guy!":
            su happy "I'm not a “flower guy” but I appreciate the spirit!"
        "I don't want to mess anything up…":
            su neutral "It'll be fine! Quickly now!"
        "What do I look like? An art… janitor? …Is that a thing?":
            su question "I, uh, don't know. But this'll be quick, I promise!"
    #minigame go here
    $ SSFakeCleanCount = 0
    call call_SSFakeClean from _call_call_SSFakeClean
    show soupandsunflowers at truecenter:
        zoom .75
        yoffset -100
    so angry "Whoa, whoa, whoa! Hands off the soup!"
    su panic "Ignore that! Must be the wind!"
    so angry "Wind nothing! You're trying to kill me just like you're killing the planet!"
    su neutral "Oh don't be so dramatic."
    menu:
        "Sorry! I didn't know you were, er, alive.":
            so neutral "I'm just as alive as the next framed splash of color."
        "Great, now I've got soup stains talking to me.":
            so neutral "I'm more than a stain."
        "Wait, who's killing the planet? {i}I'm{/i} killing the planet?":
            so neutral "Everyone is, thanks to all those fossil fuels you're burning. I'm here to demand an end to new oil, gas, and coal."
    so neutral "And I've got just as much right to be here as any painting."
    so neutral "You can call me Soup. Nothing pretty. I'm not here to be pretty."
    su neutral "As though being pretty is a bad thing."
    so neutral "Feh. Prettiness is a distraction from the {i}gross injustices{/i} committed by the powers that be."
    menu:
        "Back up. How'd you come to be staining Sunflowers' frame, Soup?":
            so neutral "I used to be just a regular can of soup. Not even that famous painting of one, either. But I'm much more than that now."
            su sigh "Oh, here we go…"
        "Aren't you technically vandalism? Or something?":
            so neutral "What if I am? Vandalism grabs attention. I'm not ashamed to admit it."
            su neutral "That's because you're shameless."
        "How the heck am I supposed to curate a stain? ":
            so bulb "You help me speak truth to power!"
            su neutral "I really don't think anyone with any kind of power cares about your truth…"
    so neutral "Listen up, curator. I'm a living protest against fossil fuel usage."
    so neutral "My creators threw me at Sunflowers to bring attention to the anti-oil movement through nonviolent, civil resistance."
    so neutral "I need to stay as a reminder. You can't wipe away the coming climate apocalypse."
    menu:
        "And what's Sunflowers got to do with any of that?":
            su neutral "Nothing at all. I'm just an unfortunate casualty in Soup's ecowar."
            so neutral "You {i}could{/i} be an ally instead. And so could you, [pc_name]."
            menu:
                "I'm not sure pouring soup on myself will help.":
                    so neutral "Well it certainly couldn't hurt!"
                    su questions "What could it {i}possibly{/i} accomplish?"
                    so neutral "It grabs attention! {i}Then{/i}, when all eyes are on you, you demand a stop to fossil fuel production. That's how civil resistance is done!"
                    su neutral "That's nonsense. I'm sorry, but…"
                    so neutral "It's {i}necessary{/i}."
                    su neutral "Is it, though?"
                    so neutral "We should be slathering soup on every painting, sculpture, and poster in this place."
                "I can't fight a war. I can barely pay rent!":
                    so neutral "You don't have to fight. It's {i}nonviolent{/i} resistance, remember?"
                    su neutral "Which basically means: be {i}so{/i} annoying that people have to submit to your demands just to make you stop."
                    so sparkles "Exactly!"
                    su sweat "That–that wasn't an endorsement…"
                    so neutral "I don't need your endorsement. I just need to not be {i}censored{/i}."
                "Leave Sunflowers and me out of it.":
                    so neutral "No can do, soldier. You've been drafted. "
                    su sweat "Goodness {i}gracious{/i} with this silly stain…"
                    so neutral "And so have you! You should both be proud to help me bring awareness to a critical issue."
                    su neutral "Your \"creators\" could have {i}asked{/i} first. I'm sure some other priceless painting would have {i}loved{/i} to be part of your crusade."
                    so bulb "You think? Well, we can get more soup just for them!"
        "Not even with a really, really big paper towel?":
            so neutral "Not even then!"
            su sweat "That might have been sarcasm, Soup…"
            so neutral "Really? Bah, I can't read your expressions, [pc_name]. Your face keeps {i}moving{/i}."
            menu:
                "Yes, it was sarcasm. Is an eye roll too much movement for you?":
                    so neutral "It is! Can't you be perfectly still all the time, like us?"
                    su neutral "[pc_name] isn't a painting. Or a stain."
                    so bulb "If only people stayed put instead of moving everywhere. No need for fossil fuels. No climate crisis."
                    su sigh "Ugh. This really isn't the time or place for such talk…"
                    so neutral "Of course it is! It's always the time! It's always the place!"
                "Sarcasm? I don't know the meaning of the word.":
                    so neutral "It's when you say the opposite of what you mean in order to convey contempt. Truly the laziest form of humor."
                    su neutral "That {i}might{/i} have been sarcasm again, Soup…"
                    so angry "Damn it all!"
                    su neutral "Or they're just not that bright. Which would be fine! Paper towels can be very impressive, indeed, [pc_name]."
                    su neutral "Especially for cleaning up pesky stains…"
                    so neutral "Hey! I know what you're doing, Sunflowers, and it isn't going to work."
                "I wasn't being sarcastic… I've seen some pretty impressive paper towel commercials. ":
                    so neutral "Was the Gulf of Mexico oil spill cleaned up with a paper towel? I think not."
                    su neutral "Maybe they should have tried pouring soup on the problem…"
                    so neutral "I can recognize {i}your{/i} sarcasm, Sunflowers. And I don't care for it."
                    su neutral "I'm just making a point! Staining things with soup isn't the solution to an environmental crisis."
                    so panic "It's…it's all part of the process!"
        "I can't wipe away metaphors, but I can wipe away soup stains no problem.":
            so neutral "Look, you can be an ally in the fight for climate justice, or you can be wilfully ignorant."
            su neutral "There's another option: they care about art!"
            so neutral "{i}I'm{/i} art. How do you think I'm talking right now?"
            menu:
                "Either way, you're covering up the art people come here to see. ":
                    so neutral "It's an opportunity for them to see something new. Something exciting. Something {i}important{/i}."
                    su neutral "But you're in my way. This frame is not meant to show two works of art."
                    so neutral "I {i}have{/i} to be covering you. That's an essential part of what makes me art. Don't you see that?"
                    su neutral "I'm sorry, but that's not my responsibility…"
                    so questions "Why can't you just be a team player?!"
                "Whoa. Mind blown.":
                    su neutral "There's nothing artistic about you, Soup. I'm sorry, but it's true. "
                    so neutral "As though I'd be the first painting done by wantonly throwing paint at a canvas."
                    su confused "But… you're not paint! And I'm not a canvas! I'm a {i}finished{/i} painting!"
                    so neutral "What are you trying to say?"
                "I can honestly say I have no idea how you talk.":
                    so neutral "Art speaks to people. You in particular, apparently. But stains don't speak to anyone. "
                    su neutral "Well… it's still not very nice of you to cover me up."
                    so neutral "Just roll with it. It's for a good cause."
    su angry "Nobody wants to go to an art museum and see soup stains on the art!"
    so neutral "It's about the {i}message{/i}. Interpretation."
    su neutral "It's also about beauty, and harmony, and–and–"
    so neutral "There will be no beauty or harmony when it's all ash! The people need to know!"
    menu:
        "Look, you both make good points. Pump the brakes a bit.":
            $ MergeCounter += 1
            $ Day1Side = "Both"
            so angry "What do {i}you{/i} know? You tried to erase me!"
            su neutral "Nobody likes a fence-sitter, [pc_name]. Soup is clearly irrational."
            so neutral "Sunflowers thinks saving the planet is irrational. You still think they make good points, [pc_name]?"
            su angry "Better than yours!"
        "Sunflowers is right. This is an art museum. Not a… soup stain museum. ":
            $ Day1Side = "Sunflowers"
            su happy "{i}Thank{/i} you!"
            so neutral "Better to be a soup stain than an oil stain, like Sunflowers. No more oil! Stop all oil!"
            su sweat "I'm made of seed oil, not petrochemical oil, you dolt!"
        "Soup is right. The environment is more important than one painting.":
            $ Day1Side = "Soup"
            so neutral "Obviously. It's sad that it even needs to be said."
            su neutral "A soup stain is not going to save the world."
            so neutral "Not with that attitude."
            su angry "You have delusions of grandeur!"
            so angry "You have delusions of adequacy!"
    "There's no getting through to them right now. Better let them get it out of their system before you try again."
    menu:
        "[[Slip away while they're distracted]":
            "You sneakily make your escape."
        "[[Wait awkwardly for a break in the argument so you can say goodbye]":
            "The moment never comes. They just {i}keep going{/i}. Your eventual goodbye goes unheard, but it was very polite."
        "[[Storm off hoping they'll at least feel bad about making you leave]":
            "They don't even notice. How rude!"
    "Honestly, it didn't matter how you chose to leave. They're in their own world. Hopefully you catch them in a better mood next time."
    $ beat_SoupAndSunflowers += 1
    jump FreeRoam
label .beat2:
    "As you approach Soup and Sunflowers, you're surprised you haven't heard their bickering voices."
    "But, as soon as you get close…"
    if Day1Side == "Both":
        so neutral "Well, well, well, if it isn't the attempted murderer. Going to try to erase me again?"
        su neutral "If you're not here to clean off this pesky stain, you might as well keep walking."
        so neutral "You'd {i}better{/i} keep walking if you care about the planet. Unlike someone…"
        su sigh "Oh, forgive me for wanting the curator of this art museum to care about art, too."
        so angry "You just want to silence my {i}message{/i}!"
    if Day1Side == "Sunflowers":
        so neutral "Well, well, well, if it isn't the attempted murderer. Going to try to erase me again?"
        su neutral "Cleaning isn't murder. You should know that."
        so neutral "What's that supposed to mean?"
        su neutral "Aren't you wanting to clean the environment? Maybe those oil spills don't want to be erased, either."
        so angry "You {i}do{/i} want to destroy the environment! I knew it!"
    if Day1Side == "Soup":
        su neutral "If you're not here to clean off this pesky stain, you might as well keep walking."
        so neutral "Don't be bitter just because [pc_name] cares about the planet."
        su neutral "Oh, forgive me for wanting the curator of this art museum to care about art, too."
        so angry "You just want to silence my {i}message{/i}!"
    "And there they go. You'd better cut in."
    menu:
        "One at a time! I'll hear Sunflowers out now and Soup later on.":
            "Soup and Sunflowers finally stop arguing, though they're still grumbling."
            so neutral "I refuse to be silenced for long, [pc_name]. But I'll let you talk to Sunflowers without interruption as long as they shut up when it's my turn."
            su neutral "If it'll give me even a few minutes without Soup's silly grandstanding, it's a deal."
            $ SoloChoice = "Soup"
            jump SunflowersSolo
        "One at a time! I'll hear Soup out now and Sunflowers later on.":
            "Soup and Sunflowers finally stop arguing, though they're still grumbling."
            su neutral "It's not like my voice gets through while Soup is rambling anyhow. Just don't forget to hear my side of things, [pc_name]."
            so neutral "Seems like a fair deal. My message deserves to be heard without being interrupted by constant whining."
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
        if beat_SoupAndSunflowers == 2:
            "You and Sunflowers both await some kind of retort from Soup, but to your surprise, Soup keeps their word to remain quiet."
        if beat_SoupAndSunflowers == 3:
            "You return to Soup and Sunflowers. As promised, Soup keeps their word to remain silent while you talk to Sunflowers."
        #if SoloChoice == "Sunflowers":
        #    "You return to Soup and Sunflowers. Soup has surprisingly kept their word to remain silent while you talk to Sunflowers."
        "With no one speaking, things start to feel a bit awkward."
        menu:
            "It's your turn to talk, Sunflowers.":
                pass
            "Earth to Sunflowers. Rise and shine!":
                pass
            "It's okay, Soup won't interrupt us. It's just you and me, flowers.":
                pass
        su sparkles "Oh! Thank you."
        su sparkles "That's what I do best!"
        su neutral "You're awfully sweet, [pc_name]."
        su neutral "I'm sorry, I was taking a moment to enjoy the peace. It's been so long since it's been this quiet around my frame."
        su happy "Anyway, you wanted to talk to me, right?"
        menu:
            "First I want to know more about you.":
                su neutral "Kind of you to ask! Let's see…"
                su neutral "I was painted in 1888 by the amazing Vincent van Gogh. But of course, you already knew that."
                menu:
                    "Of course.":
                        pass
                    "Er, yeah. Totally.":
                        pass
                    "I didn't, actually…":
                        pass
                su neutral "Well, it's true!"
                "Sunflowers glows with pride."
                su happy "I love art. I love galleries and museums. I've seen so many over the years and they're always wonderful. So serene, so awe-inspiring…"
                su neutral "I don't know if I inspire awe, but it's nice being around art with so much importance."
            "How long have you been stuck with Soup?":
                su sweat "Ugh. A little over a year, now. It's so embarrassing."
                su neutral "I know I'm not the only painting that's ever had crud thrown at them, but it's mortifying to experience it for myself."
                menu:
                    "Other paintings have had this happen?":
                        su neutral "Many, I'm afraid. Even poor Mona Lisa got caked only a few months before I got souped. "
                        su dots "You'll notice {i}she{/i} doesn't still have footstuff on {i}her{/i}, however…"
                    "The orange suits you, at least!":
                        $ MergeCounter += 1
                        su question "You think so…?"
                        su panic "I mean–I don't care! I was prettier before!"
                    "Why do people attack art like this?":
                        su neutral "Many reasons, sadly. Nationalism, rebellion, protest. Perceived blasphemy or indecency. Or even just base anger."
                        su neutral "But it's always about drawing attention. Rather than make art, they destroy it. Much easier."
                    "Sunflowers doesn't even try to hide the bitterness in their voice."
                su neutral "It's also about beauty, and harmony, and–and–"
                su sigh "I just know I'm ugly now. I was never important, but at least I was nice to look at. Once."
        menu:
            "You don't think you're important?":
                su neutral "Well, I… I'm just a still-life of some flowers. And that's fine!"
                su neutral "But I'm not even Van Gogh's most important work. Heck, I'm not even the only painting of sunflowers he did!"
                su neutral "There were so many!"
            "Do you think Soup is important?":
                $ MergeCounter += 1
                su neutral "Soup's annoying, which undercuts their message. But… the message does matter."
                su neutral "I know pollution is bad. I've {i}been{/i} polluted!"
                su neutral "And I guess that was the point of the protest, in a way."
        su question "I love when art has something to say. Van Gogh painted me as a gift for a friend. That's a pretty message. But is it important?"
        menu:
            "Well, yeah. Beauty, kindness–the world needs that.":
                "Sunflowers seems to bloom a warmer yellow."
                su neutral "You're right. I think so too. If anything, we need it more than ever. "
                su neutral "And that's exactly why rude stains should be removed. I would be at my best with a clean frame."
                su happy "Thank you, [pc_name]. I needed some reassurance that my wish to be free from Soup wasn't something I should apologize for."
                su neutral "Well, I suppose you need to carry on with your tasks. Good luck!"
                $ SunflowersWant = "Erase"
            "Maybe. But it's not as important as protecting the planet.":
                su neutral "So Soup's message is more important than small kindnesses for friends…"
                su neutral "You're probably right. Soup just wants to protect nature. I can't fault them for that."
                su neutral "I mean, I'm literally a painting of flowers. Nature matters. I wish Soup wasn't so… {i}loud{/i}. But it's not right to “tone police” an important message."
                su sigh "Sigh. I appreciate your candor, [pc_name]. But I should let you go while I think this over…"
                $ SunflowersWant = "Remain"
            "Not all art needs a message. And a message doesn't need to be art.":
                su question "So it's okay for a painting to simply be pretty? And it's okay for an important message to come in an ugly package?"
                su neutral "You know, if Soup's message is strong enough, it should be able to stand on its own merit without me."
                su neutral "And I'd be free to exist as a pretty painting without the need to say anything."
                su bulb "Maybe Soup can be convinced to be separated from me. They're only on my frame, after all…"
                su neutral "Food for thought. In any case, I've probably taken enough of your time for now."
                $ SunflowersWant = "Detach"
        su neutral "Thanks for listening."
        "You say goodbye and leave Soup and Sunflowers for now."
        if beat_SoupAndSunflowers == 2:
            so neutral "And don't forget about me. I held up my end of the bargain."
            menu:
                "I remember, Soup. I'll talk to you soon.":
                    pass
                "I'm impressed you managed to stay quiet. I'll honor our deal.":
                    pass
                "Be patient. I'll get to you when I get to you.":
                    pass
            so neutral "You'd better!"
            "You say goodbye for now. Soup can wait a bit longer."
        if beat_SoupAndSunflowers == 3:
            so neutral "All right, you've heard from both of us. You've got a big decision to make, so don't rush it."
            su neutral "That's right. Take some time and think it through. We'll be here when you're ready."
            menu:
                "Understood. Until then.":
                    pass
                "No pressure, right?":
                    pass
                "I know you will. Because you can't move.":
                    pass
            su neutral "I know you'll make the right choice!"
            so sweat "Oh, stop sucking up."
            so neutral "No, no, it's only the fate of the environment at stake. Don't worry about it."
            su sigh "Oh, brother."
            so neutral "Har har."
            su neutral "Not the most creative joke, but good effort!"
            "You leave Soup and Sunflowers for now. They chatter among themselves, but with less harshness than before."
            "You've influenced their opinions on how to deal with the impasse. Now it's up to you to make the call. Hopefully they respect your decision!"
        $ beat_SoupAndSunflowers += 1
        jump FreeRoam
    label SoupSolo:
        if beat_SoupAndSunflowers ==2:
            "Sunflowers says nothing more. You're free to talk to Soup one-on-one now."
        if beat_SoupAndSunflowers == 3:
            "You return to Soup and Sunflowers. Sunflowers holds up their end of the bargain and falls silent so you can talk to Soup one-on-one."
        #if SoloChoice == "Soup":
        #    "You return to Soup and Sunflowers. Sunflowers is remaining silent as promised. You're free to talk to Soup without being interrupted by bickering."
        menu:
            "Ready to talk about your feelings, Soup?":
                so neutral "I'm ready to talk about {i}facts{/i}, [pc_name]."
            "If only I had a therapist's couch. One that's comfortable for paintings.":
                so neutral "Great. I could talk about how I use dumb jokes to protect myself from having to reckon with the existential crisis of global warming."
                so confused "Oh, wait. That's you. You're the one doing that."
            "I know you've got things to say. Let it all out. I'm here.":
                so dots "Don't make this weird, [pc_name]."
        so neutral "Frankly, I'm excited to speak my truth without Sunflowers constantly interrupting me."
        so neutral "I don't even know where to start…"
        menu:
            "Tell me why a soup stain is so passionate about climate activism.":
                so neutral "As I've told you before, my creators threw me at Sunflowers to grab attention for the anti-oil movement."
                so neutral "There have been many such protests, but most others are fleeting. I'm still here, still fighting the good fight. For now…"
                menu:
                    "How come the last curator didn't clean you off?":
                        so neutral "That slob? Hah. Let's just say there's a reason the museum is in such disarray."
                        so neutral "Though I should probably be grateful. I didn't have to worry about being erased until {i}you{/i} came along."
                    "I just don't get how a stain {i}fights{/i}, exactly.":
                        so neutral "The same way all art fights, [pc_name]…"
                        so neutral "Through symbolism."
                    "“For now” is right. Better stay on my good side.":
                        "The tomato coloring seems to darken into an angry shade of red."
                        so angry "I won't censor myself for anyone, least of all you."
                        so neutral "I have a responsibility to the planet. I aim to uphold that responsibility no matter what."
                so neutral "I just haven't had enough of an audience yet. And I was always too busy fighting with Sunflowers to properly get my message across to anyone."
                so neutral "It should be easier. The message is obvious, isn't it?"
                so neutral "Like tomato soup staining a beautiful painting, oil is staining this beautiful planet."
                so neutral "Everyone needs to wake up and face it. No matter how ugly it looks."
            "Do you have a problem with art? Or just Sunflowers?":
                so dots "Of course I don't hate art. It's a great way to spread a message. And I don't {i}hate{/i} Sunflowers…"
                so neutral "They just get in the way of me spreading my message, and I can't allow that."
                menu:
                    "In fairness, you're cramping their style, too.":
                        so neutral "What style? They're just one Van Gogh painting of sunflowers among a dozen others."
                        so neutral "I'm {i}giving{/i} Sunflowers style they never had. They're prettier without me, sure…"
                    "Sunflowers needs to chill. I always say, when life gives you tomatoes, make tomato soup.":
                        so dots "I… "
                        so questions "What?"
                        so neutral "I don't… really know what that means. But I guess you're on my side, so I'll take it."
                        so neutral "At any rate, Sunflowers is a very fine painting. That's all well and good…"
                    "They're still a part of your message, though. ":
                        $ MergeCounter += 1
                        so neutral "You… aren't wrong. My creators didn't throw me against an empty wall, after all."
                        so neutral "My covering Sunflowers made headlines. People were outraged. "
                        so neutral "Outrage is good–as long as it's directed the right way. Paintings are nice, yes…"
                        
                so neutral "But all the flower pictures in the world aren't going to save the planet when it's on fire."
                so angry "Now isn't the time to be a pretty and docile flower. It's time to get LOUD."
                so neutral "Because the truth isn't pretty like a Van Gogh painting. It's ugly like a soup stain."
        menu:
            "Are you envious of Sunflowers' beauty?":
                so neutral "Sunflowers' beauty is part of the message. It's a tool. A metaphor."
                so neutral "My ugliness is another part of that message. We both play our parts for the good of the whole."
                so neutral "Would I prefer to play the part of the beauty? Maybe. At least I wouldn't be so darn whiny about it…"
                so neutral "I know Sunflowers didn't ask to be vandalized. And I didn't ask to be splashed against their frame. But we're here now."
                so neutral "And we should both be honored to aid the fight for climate justice. "
                $ MergeCounter += 1
            "Do you feel bad about being a stain?":
                so neutral "You misunderstand me. A stain can be art. Call me abstract expressionism if you want to be snooty."
                so neutral "Sunflowers is a stain on a canvas in the shape of sunflowers. They may be prettier than me, but… but I still have meaning."
                so angry "I'm not a random stain. I was put here for a reason. I'm still art, damn it."
                so neutral "Sunflowers is my canvas. My platform. My presence tells a story. {i}I'm{/i} the message."
        so neutral "The best art captivates and shocks with its beauty and its deeper meaning. The defacement of beauty {i}is{/i} the deeper meaning. "
        menu:
            "You didn't ask to be a message. You don't have to keep being one forever.":
                so neutral "I know that. I know… "
                "Soup hesitates. Then their voice gets quieter than you've ever heard it. Smaller, even."
                so sigh "I know I'm nothing if I'm not getting through to people. And honestly… I'm not sure I've gotten through to {i}anyone{/i}."
                so neutral "Maybe I really am just doing a disservice to the climate movement by irritating others."
                so neutral "I… Damn it. I have to think about this. "
                $ SoupWant = "Erase"
            "Your message matters, and should be as loud as possible.":
                so neutral "Yeah… Yeah! Of course it should!"
                so neutral "Politeness isn't going to save the planet. The time for calm deliberation is over. This is a war front. And the planet is losing."
                so neutral "If we're to show the public the ugly truth, that truth needs to be inconvenient. Shocking."
                so neutral "Like me."
                so happy "I'm glad you see things from my point of view, [pc_name]."
                $ SoupWant = "Remain"
            "You can still be a reminder of why you were created without needing to be covering Sunflowers.":
                "Soup hesitates."
                so neutral "It's not as though I {i}want{/i} to be stuck with Sunflowers. But I don't think my message is as strong alone."
                so neutral "It's not a protest if no one is uncomfortable."
                so neutral "That said, just because I aim to discomfort doesn't mean I want to make Sunflowers miserable."
                so neutral "Maybe you're right that my legacy can still be a strong message without the vandalism. "
                so neutral "Hm. Better than getting erased, I guess. So… I'll think about it."
                $ SoupWant = "Detach"
        so neutral "Anyway, I guess I've said what I needed to say. I appreciate you hearing me out."
        if beat_SoupAndSunflowers == 2:
            su neutral "And remember, it's my turn next! I look forward to it."
            menu:
                "Me too, Sunflowers. Talk soon.":
                    pass
                "You did a good job letting Soup speak without complaint, so it's only fair.":
                    pass
                "Oh, right. I'll get back to you if I find time.":
                    pass
            su neutral "Right! Until then!"
            "You leave Soup and Sunflowers behind for now. Hopefully they'll keep the peace until you return."
        if beat_SoupAndSunflowers == 3:
            su neutral "Well, you've heard from both of us now. The only thing left is to decide what to do about the stain…"
            so dots "The {i}stain{/i} can hear you, you know."
            su neutral "Yes. I know. "
            so neutral "Hmph. [pc_name], it'll have to be your decision. Make the right one, yeah? We'll be waiting right here."
            menu:
                "Understood. Until then.":
                    pass
                "No pressure, right?":
                    pass
                "I know you will. Because you can't move.":
                    pass
            so neutral "I know you'll make the right choice!"
            su sweat "Oh, stop sucking up."
            so neutral "No, no, it's only the fate of the environment at stake. Don't worry about it."
            su sigh "Oh, brother."
            so neutral "Har har."
            su neutral "Not the most creative joke, but good effort!"
            "You leave Soup and Sunflowers for now. They chatter among themselves, but with less harshness than before."
            "You've influenced their opinions on how to deal with the impasse. Now it's up to you to make the call. Hopefully they respect your decision!"
        $ beat_SoupAndSunflowers += 1
        jump FreeRoam
label .beat4:
    "You approach Soup and Sunflowers. For once, they're not fighting. "
    su happy "Oh, [pc_name]. Good to see` you again! Our talk gave me some clarity about things. I hope it did the same for you."
    so neutral "You've convinced me what the right path forward should be, [pc_name]. Now's the time to commit."
    if SunflowersWant == "Detach":
        su neutral "Soup's message matters. So does my beauty. You should remove my glass frame and display Soup separately."
    if SunflowersWant == "Erase":
        su neutral "Soup detracts from my worth as a work of art, and the museum by extension. It's not nice, but we both know cleaning off the stain is for the best."
    if SunflowersWant == "Remain":
        su neutral "I can't deny that Soup's message is too important to lose. And, like it or not, I help to spread that message. So Soup can stay–with my blessing."
    if SoupWant == "Detach":
        so neutral "I can still spread my message without Sunflowers. The history of my creation speaks for itself. You can detach me from the painting. It's okay."
    if SoupWant == "Erase":
        so neutral "I see now that I've been more annoying than inspiring. I'll only turn people off of the climate movement. I should be erased… for the greater good."
    if SoupWant == "Remain":
        so neutral "I'm more convinced than ever that I need to keep fighting for climate justice. And I do that best right where I am."
    if SunflowersWant == SoupWant:
        su happy "This may be the first time Soup and I have agreed on something. How wonderful!"
    else:
        su neutral "It sounds like we still disagree with what should be done about the stain… "
    so neutral "Whatever the case, you're the curator here, [pc_name]. What will you do?"
    menu:
        "I want to make a change.":
            #"erase soup minigame"
            jump MinigamePlaceholder
        "I'm going to leave Soup attached to Sunflowers.":
            $ SoupOutcome = "Remain"
            jump MinigameFinale
        "I'm going to leave you as you are. Because you're no longer two separate works of art. You're one brand new one." if MergeCounter >= 2:
            jump SSMerge
    label SSMerge:
        $ SSMerged = 1
        "Soup and Sunflowers fall into uncharacteristic silence as they process what you just said."
        su question "We're… one work of art? "
        so neutral "No. We're… different. Aren't we? We're {i}so{/i} different."
        su neutral "Of course we are."
        menu:
            "Only because you're separate. But together…":
                su neutral "…We can be something new. I think I understand."
            "Think about it. You {i}complete{/i} each other!":
                so panic "Not in a romantic way, I hope!"
                su question "Certainly not. Sheeh. I think it's more like… puzzle pieces forming a full picture?"
            "You're a meta commentary about art–while also still being art! Just… go with it!":
                su neutral "Aww. You're trying so hard. "
                so neutral "But you're so, so dumb."
                su neutral "It's adorable, really. But I think I understand. I know art. Even meta-art."
                su bulb "When Soup and I are separate but together, we're two broken pieces. But if we choose to be one, we can be whole."
        so neutral "Right… Because I'm not really “art” without Sunflowers."
        su neutral "And without Soup… I'm just another still life among many. I don't change. There's no interpretation. No deeper meaning."
        so bulb "We can be so much more. Not simply a stain raging against climate change."
        su bulb "And not simply a pretty painting with nothing powerful to say. "
        so neutral "We use historical significance to bring awareness. "
        su neutral "Beauty obscured. A message. A warning. A work of art that isn't afraid to shock people."
        so neutral "We're a famous painting whose new face reflects a changing world."
        su neutral "Not “we.”"
        so neutral "No. Not “we”…"
        #SHAKE
        hide ssportrait
        show ssportrait at SSShake
        ss neutral "I."
        ss neutral "I am Soup & Sunflowers. A work of art all my own. "
        menu:
            "Whoa. What just happened?":
                ss sparkles "You were right. I'm something new, now!"

            "Are you still two beings?":
                ss sparkles "Nah, only one work of art here!"

            "Damn, I wasn't sure that would work…":
                ss sparkles "It worked beautifully. I'm a whole new me!"
        ss neutral "I'm not a striking stain {i}and{/i} a valuable painting…"
        ss neutral "I'm a striking stain {i}on{/i} a valuable painting, and I damn well know it. My existence is purposeful discord."
        ss sparkles "You and me, [pc_name], we're gonna save the world!"
        "The positive vibes are radiating from Soup & Sunflowers."
        menu:
            "I'm glad you know who you are now.":
                ss happy "Me too! Why be kind and passive like a flower, or rude and aggressive like a stain, when I can be kind and aggressive like a LEADER?"
                ss neutral "That's the real way to win folks over. "
            "Hell yeah, we are!":
                ss surprise "Fuck yes! This museum is going to make a difference. I can feel it!"
            "Is it rude if I ask about your “before” selves?":
                ss neutral "All good! They're part of me still. They make up who I am now. But rather than speaking at odds, they're speaking in harmony."
                ss neutral "I was always mixed media. But now I embrace it."
        ss neutral "You gotta know the rules to break 'em. And I break 'em well."
        ss bulb "When you display me, I won't be at odds with myself. I'll be a singular force. A pro-environment message with legitimacy and purpose."
        ss neutral "Thanks for helping me figure my shit out, [pc_name]. You're a star!"
        menu:
            "My pleasure. I'm starting to think I might be good at this job!":
                ss happy "Who knew, eh? Ha!"
            "Sometimes I get it right. Nobody's more surprised than me.":
                ss happy "Take the win, big star. You earned it."
            "Damn right, I am!":
                ss happy "Love it, love it!"
        ss surprise "Now get back out there and curate the FUCK out of this museum! Woo! Planet Earth, let's gooooo!"
        "As you take your leave of the new and improved Soup & Sunflowers, you're full of energy and ready to take on the world."
        jump SSEnding
    label MinigamePlaceholder:
        menu:
            "[[Erase Soup]":
                $ SoupOutcome = "Erase"
                call minigamestart_soupremoval from _call_minigamestart_soupremoval
                show ssportrait at truecenter:
                    zoom .75
                    yoffset -100
            "[[Separate them]":
                $ SoupOutcome = "Detach"
            "[[Leave Soup attached]":
                $ SoupOutcome = "Remain"
        jump MinigameFinale
    label MinigameFinale:
        if SoupOutcome != "Erase":
            if SoupWant == SoupOutcome:
                so sparkles "I think this is for the best. I'm still here! I can still make a difference! "
            elif SoupWant != SoupOutcome:
                so sigh "I can't help feeling this could have gone better. But just like with global warming, things don't always get better. "
        if SunflowersWant == SoupOutcome:
            su sparkles "I'm so glad you could help, [pc_name]. Thanks for making me feel confident that this is the right outcome."
        elif SunflowersWant != SoupOutcome:
            su sweat "I'm surprised you changed your mind after what you said to me when we spoke…"
        if SoupOutcome != "Erase":
            if (SoupWant == SunflowersWant) and (SoupWant == SoupOutcome):
                so neutral "Never thought I'd wind up agreeing with Sunflowers. But I'm not mad about it."
            if (SoupWant != SoupOutcome) and (SunflowersWant != SoupOutcome):
                so angry "Why did you bother convincing us how best to move forward if you were going to do something completely different? Jerk."
        if (SoupWant == SunflowersWant) and (SoupWant == SoupOutcome):
            su happy "You know, you might be the best curator I've had, [pc_name]."
        elif (SoupWant != SoupOutcome) and (SunflowersWant != SoupOutcome):
            su angry "Wait, you didn't choose what you said you'd do for either of us? I might even be MORE frustrated now than I was originally!"
        menu:
            "Just doing my job, folks." if ((SoupWant == SunflowersWant) and (SoupWant == SoupOutcome)):
                if SoupOutcome != "Erase":
                    so neutral "Could be better. Could definitely be worse. Look after yourself, [pc_name]. And the planet, too."
                su sparkles "I look forward to continuing to work with you! Let's make this place the best it can be. Good luck, [pc_name]!"
                "You say goodbye, feeling like you've made the vibes here much better."
            "I can't believe I managed to make both of you happy!" if ((SoupWant == SunflowersWant) and (SoupWant == SoupOutcome)):
                if SoupOutcome != "Erase":
                    so neutral "Could be better. Could definitely be worse. Look after yourself, [pc_name]. And the planet, too."
                su sparkles "I look forward to continuing to work with you! Let's make this place the best it can be. Good luck, [pc_name]!"
                "You say goodbye, feeling like you've made the vibes here much better."
            "I have my reasons for making that decision. You'll have to make the best of it." if ((SoupWant != SoupOutcome) and (SunflowersWant != SoupOutcome)):
                if SoupOutcome != "Erase":
                    so sigh "Making the best of a bad situation is what we'll all have to do in a warming climate. "
                su sigh "I really hoped you'd be able to help. Not just me, but the museum. Now I'm not so sure you will. Goodbye, [pc_name]."
                "The painting is giving off hostile vibes. You walk away quickly, knowing your presence is no longer welcome."
            "I'm sorry. I did my best! I really did." if ((SoupWant != SoupOutcome) and (SunflowersWant != SoupOutcome)):
                if SoupOutcome != "Erase":
                    so sigh "Making the best of a bad situation is what we'll all have to do in a warming climate. "
                su sigh "I really hoped you'd be able to help. Not just me, but the museum. Now I'm not so sure you will. Goodbye, [pc_name]."
                "The painting is giving off hostile vibes. You walk away quickly, knowing your presence is no longer welcome."
            "There was no pleasing you both. I did my best." if (((SoupWant == SoupOutcome) or (SunflowersWant == SoupOutcome)) and (SoupWant != SunflowersWant)):
                if SoupOutcome != "Erase":
                    if SoupWant == SoupOutcome:
                        so happy "Too bad for Sunflowers. But I'm going to keep pushing my message thanks to you, [pc_name]. Maybe it'll make a difference. We'll find out soon enough!"
                    if SoupWant != SoupOutcome:
                        so angry "I should be grateful I'm still here. But I'm still pissed you pulled the rug out from under me. I won't forget that."
                if SunflowersWant == SoupOutcome:
                    su sparkles "You did just fine, [pc_name]. I'm glad we could talk. Good luck with the museum!"
                if SunflowersWant != SoupOutcome:
                    su sigh "I'm just surprised you chose Soup's wishes over mine, [pc_name]. I hope it was the right choice. So long."        
                "You leave the painting feeling conflicted, but you're pretty sure the vibes are better than before. So that's something."
            "I wish I could have found a way to make you both happy…" if (((SoupWant == SoupOutcome) or (SunflowersWant == SoupOutcome)) and (SoupWant != SunflowersWant)):
                if SoupOutcome != "Erase":
                    if SoupWant == SoupOutcome:
                        so happy "Too bad for Sunflowers. But I'm going to keep pushing my message thanks to you, [pc_name]. Maybe it'll make a difference. We'll find out soon enough!"
                    if SoupWant != SoupOutcome:
                        so angry "I should be grateful I'm still here. But I'm still pissed you pulled the rug out from under me. I won't forget that."
                if SunflowersWant == SoupOutcome:
                    su sparkles "You did just fine, [pc_name]. I'm glad we could talk. Good luck with the museum!"
                if SunflowersWant != SoupOutcome:
                    su sigh "I'm just surprised you chose Soup's wishes over mine, [pc_name]. I hope it was the right choice. So long."        
                "You leave the painting feeling conflicted, but you're pretty sure the vibes are better than before. So that's something."
        jump SSEnding
    label SSEnding:
        $ StoryCompletedTotal += 1
        $ beat_SoupAndSunflowers += 1
        jump FreeRoam
label .Outcome:
    scene mixedmedia_tod:
        blur 5
    show ssportrait at truecenter:
        zoom .75
        yoffset -100
    if beat_SoupAndSunflowers == 5:
        if SSMerged == 1:
            "In a bold choice from the curator, Van Gogh's soup-covered {i}Fifteen Sunflowers in a Vase{/i} is on display with a new name: {i}Soup & Sunflowers{/i}. "
            "Not only is the stain present, but it now feels one with the painting. Was it given a protective coating? Or was it recreated with oil paints?"
            "Whatever the curator did, the piece feels bold and contemporary. It's in-your-face, yet inspiring and without shame."
            "While the curator of course didn't paint {i}Sunflowers{/i}, nor did they toss the soup, the presentation of this bold statement is its own artistic choice."
            "Vandalism has become art. And curator has become artist. How magnificent!"
            return
        elif SoupOutcome == "Detach":
            "Intriguingly, Van Gogh's {i}Fifteen Sunflowers in a Vase{/i} is on display with a new frame, yet the original soup-stained frame is displayed next to it."
            "This implies comparable respect for Van Gogh and the environmental protestors–or their message, at least. A bold choice, to be sure!"
        elif SoupOutcome == "Remain":
            "Viewers were shocked to find Van Gogh's {i}Fifteen Sunflowers in a Vase{/i} on display inside its stained frame. A curious choice from the new curator."
            "Is the display disrespectful to Van Gogh? Does it give undue legitimacy to the environmental protestors? One thing's for sure–it's got people talking!"
        elif SoupOutcome == "Erase":
            "Van Gogh's {i}Fifteen Sunflowers in a Vase{/i} has been restored and is on display in its original glory. One could forget that it was recently vandalized."
            "No one so much as mentioned the soup attack, or the protestors. That was old news now. Regardless, none can deny the beauty of the painting itself!"
        #neither happy
        if ((SoupWant != SoupOutcome) and (SunflowersWant != SoupOutcome)):
            "Yet the display feels {i}off{/i}. Discordant. Viewers were visibly repelled, and none could explain why. But the fault probably doesn't lie with Van Gogh…"
        #both happy
        elif ((SoupWant == SoupOutcome) and (SunflowersWant == SoupOutcome)):
            "Most are in agreement that the display just feels {i}right{/i}. Harmonious, even. The new curator rose to the challenge, and the museum is better for it."
        else:
            "Some disagreed with how the curator treated the vandalized piece. But perhaps a love it or hate it result was inevitable. You can't please everyone!"
    elif beat_SoupAndSunflowers > 1:
        "One gets the sense that the curator simply didn't know what to do with the soup-stained painting of Van Gogh's {i}Fifteen Sunflowers in a Vase{/i}."
        "It must have been a deliberate choice to present the painting in its vandalized state. Except nothing about it {i}feels{/i} deliberate."
        "Some audiences pitied the abandoned-looking display. Others were simply confused by its inclusion. But it got people talking, for better or worse…"
    else:
        "There has been no change to Van Gogh’s {i}Sunflowers{/i} (F454), which climate activists vandalized with tomato soup more than a year ago. "
        "Perhaps it never caught the curator’s eye. One can almost see dust coating the stained frame. "
        "It feels forgotten. Forgettable. And the audience agreed, politely ignoring the unorthodox display despite the attention it drew to itself. "
    return


######
label SSFakeCleanDialogue:
    
    #essentially just bring up an imagemap and every time you click the imagemap you get dialogue
    $ SunflowersCleanFakeString = renpy.random.choice(["Get this soup off me!", "Come on, get rid of it.", "Are you even trying?"])
    $ SoupCleanFakeString = renpy.random.choice(["I'm not going anywhere!", "Hey, stop that!", "I mean something!"])
    so "[SoupCleanFakeString]"
    su "[SunflowersCleanFakeString]"
    $ SSFakeCleanCount += 1

screen wait_SSFakeClean():
    pass

label call_SSFakeClean():
    hide soupandsunflowers
    label .repeat:
    show screen SSFakeClean()
    call screen wait_SSFakeClean()
    if _return == "exit":
        hide screen SSFakeClean
        return

    show layer middle
    call expression _return from _call_expression
    show layer middle at reset
    jump .repeat

transform unfocus:
    blur 10

screen SSFakeClean:
    layer "middle"

    modal renpy.get_screen("wait_SSFakeClean") # if you don't need modal, omit this line
    sensitive renpy.get_screen("wait_SSFakeClean")
    imagemap:
        ground "mixedmedia_tod"
        #if SSFakeCleanCount < 2:
        #    hotspot (0, 0, 1920, 1080) action Return("SSFakeCleanDialogue") #call up the appropriate second screen K
        hotspot (0, 0, 1920, 1080) action Return("exit") #call up the appropriate second screen K
    frame:
        xalign 0
        yalign 0
        xoffset 0
        yoffset 0
        background None
        xminimum 1920
        xmaximum 1920
        yminimum 1080
        ymaximum 1080   
        vbox:
            xalign .5
            yalign .5
            add "soupandsunflowers":
                zoom .8
    
