#Davids

default beat_Davids = 1
default BibleResearched = 0

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
    "You hear the sounds of infighting, again..."
    d "And {i}that's{/i} why I'm the David."
    dm "How many times do we have to go over this? My reputation precedes me..."
    dd "Yeah yeah, dude. First colosal statue of its kind. We get it, we get it."
    db "At 17 feet you sound more like a Goliath than a David."
    menu:
        "Hey could y'all give me the introductions without the insults?":
            d "Oh my! And who might you be?"
            pc "I'm the new curator. The one from yesterday... you know?"
        "[[Retrieve metro cards from your pockets and throw them at the Davids.]":
            d "Hey! Hey! Hey! And who might you be?"
    dd "Yeah bruh, that's why I'm the David. Cuz I'm actually A KID. And how do you know? Because I'm the actual height of...you guessed it... A KID."
    "He stamps his feet and inadvertantly bounces the head of Goliath up in the air before catching it on his feet like a hacky sack."
    db "And you bring inapproriate materials to a museum, like a kid."
    menu:
        "Gross. Could you come off of that thing?":
            pass
    d "We're the highest of High art! "
    dd "Note the pedestal, dude."
    db "With no come down. We can just move around up here."
    "He twists and stretches his limbs, almost doing calesthenics before banging out a push-up or two."
    pc "Ok, so there's like a big one and a small one?"
    db "Both of them...posers...feckless and improvident fuckboys."
    db "How do you expect to defeat a giant by playacting like they both do?"
    menu:
        "Well what's your deal then?":
            pass
        "I already have four or five Davids in my life. Remind me why I need another?":
            pass
    db "Who me? I'm the heroic one. You can take pictures, but I ain't posing. "
    dm "Hark! Tell me, False Davids, did you hear something?"
    dd "I told you. It's THE DAVID not FALSE DAVID."
    db "Just the same old shit I've heard you two squabble about now for years: Who's really the The David?"
    pc "Wait a second. Let me see if I can resolve this real quick: there's a big one, a kid one, and a heroic one?"
    pc "Or you all are supposed to be that same thing rolled up into one?"
    d "The SAME thing?!"
    dm "My gentle docent, despite sharing the name David..."
    menu:
        "I'm sorry! It's just....It's just that y'all are just hurling invectives at each other. Not exactly clear introductions.":
            pass
        "Let me stop you right there. I've had my fill of Davids for today. I'll come back tomorrow and we can try this again.":
            pass
    d "Yes! If you come back tomorrow, we'll be on our best behavior."    
    
    ####
    $ beat_Davids += 1
    jump FreeRoam

label .beat2:
    d "You came back!"
    dm "(placeholder) probably only because after all I am..."
    dd "You've got a good chance of recognizing my face and this guy's. "
    "He kicks the head and a thud resonantes in the quarter of the museum."
    db "You came back. You got gumption. I'll give you that. "
    pc "That's enough out of you all. I want some real introductions.  Not formal bickering between you."
    "They all strike their famous pose."
    d "We are The Davids!"
    menu:
        "Obviously I know that. It's all you all talk about. But I also know a few Daves, a Davey, and went to school with like five other Davids too.":
            pass
        "So which Davids are you?":
            pass
    dm "The Biblical. The original."
    dd "The one who slew Goliath."
    db "The one to combine bravery and skill."
    menu:
        "Ok so you were a kid soldier... or something?":
            pass
        "I thought you already had a star named after you...":
            pass
    d "Well we were a King too!"
    pc "Oh... like King Aruthur."
    dm "..."
    db "..."
    dd "..."
    d "NO. NOT LIKE KING ARTHUR!"
    dm "We are the young shepherd boy..."
    dd "Chosen by like the actual God himself."
    db "To be the King of his chosen people."
    menu:
        "Ah! Yes yes yes. That's right. I remember now.":
            pass
        "Ok ok ok. I get it. This is coming back to me.":
            pass
    dm "Then I'm sure you'll recognize me most easily. Michelangelo's David. Molded from a single piece of marble."
    dm "A work of art whose body became an ideal. A testament to the potential material reality contains. And a face that now graces Art History textbooks year after year."
    dd "BO RAAAANGG"
    db "Look like you're standing before a weekly drawing class, not no field of battle. "
    dd "Get 'em Bernini David!"
    dd "And besides, I'm older. Donatello cooked me up about a hundred years before. Sculpted in bronze, my dude."
    dd "And at 5 foot 7 inches, a dead ringer for adolscent bravery and ambition. "
    dd "I mean how brave can it be to beat Goliath when you're 17 feet tall, Mikey Dave?"
    dm "For shame!"
    dd "You want some more authenticity? Check this artifact. The severed of Goliath. Note the scale. Guy's as big as my freakin' torso."
    db "Quite the pair. eh (placeholder)? Different models, same shit, I say. "
    menu:
        "And who are you?":
            pass
        "Another one? I can't even with this. I'm done.":
            $ beat_Davids += 1
            jump FreeRoam
    db "The name's Bernini's David, couple of hundred years after these two yahoos."
    db "Long enought after to know art ain't no beauty pagent.  That being a hero ain't about philosophizing neither."
    db "Art is an action. Drama has its actors. And a heroes got jobs, kid. And so I'm here to do mine.  "
    db "Now if you'll excuse, I need to Baroque about a bit, and explore all three dimensions."
    pc "So after first introductions and impressions I'm feeling that the definitive David so far is"
    menu:
        "Michelangelo's David":
            dm "I knew it! You knew it. We all knew it."
            dd "Change your answer!"
            db "This can't be right."
        "Donnatello's David":
            dm "Oh no! Your vision is cloud and imagination dull!"
            dd "Let's goooooooo!"
            db "You can't be for real? The kid?"
        "Bernini's David":
            dm "Oh no, not him. Hardly any one knows him!"
            dd "That dude? He hasn't even slayed Goliath yet! Got no goodies to show for it."
            db "That a way there, newbie.  Now people can see what a hero is. "
    pc "Oh don't get mad! "
    pc "Well, I'll be honest, your introductions stink, so don't blame me."
    d "There must be another way to show him/her/them..."
    pc "Can someone make a case for you all besides.... you know, you all?"
    d "Something more authoritative than...us? "
    pc "Think on it tonight, and I'll be back tomorrow. But arguing your case yourselves isn't working."
    d "We'll find a way!"
    ###
    $ beat_Davids += 1
    jump FreeRoam
label .beat3:
    d "But that's what I've been saying!"
    pc "Oh, God. You three agian. Well, you've had the night to think. What ya got?"
    dm "Forsooth, my dear (placeholder). Yes, yes, this time I have a--"
    db "He means \"we.\""
    dd "Yeah as in \"we\" came up with a solution."
    pc "Consult an expert like myself?"
    "You beam a smile."
    d "Not an expert...the expert."
    d "THE SOURCE!"
    pc "The what?"
    db "Scuttlebutt around the vending machine is that you can read. "
    dd "Aloud and silently!"
    db "And that you can make it down stairwells no problem."
    dm "There are rumors that beneath our very feet, hidden in the shelves of archives, is a copy of..."
    d "The Bible"
    d "Our source!"
    pc "Oh God..."
    d "Exactly!"
    db "Kid, if you could let us know what the original passage says about us taking out ol Philistenian Oaf, Goliath..."
    dd "He makes a winky face with the head of Goliath."
    dm "then you could tell us who is the definitve David!"
    pc "You want me to go read the bible for you?"
    "They all slowly nod their heads."
    label DavidResearchChoice:
        menu:
            "[[Lie] Psh. I got that memorized. I don't need to run you no errand.":
                d "You have the Bible memorized?"
                dm "All chapters and verses...committed to memory?"
                dd "That's a lot of words...Not gonna lie."
                db "You shootin us straight?"
                pc "Uhhhh...yeah... of course. All of it...Right up here... In my mind palace."
                d "Well in that case we can't wait to hear what you think tomorrow!"
                pc "Erm...right!...Yes...Tomorrow!"
                $ BibleResearched = -1
            "I'm so done with y'all that I can't even stand to look at you. Time to escort you to your corners.":
                d "No please! Wait!"
                pc "What is it now?"
                dm "Give us one last chance!"
                dd "We'll be good! We promise! "
                db "We're on our last legs here. If you don't help us out...it could..."
                d "Crumble us!"
                menu:
                    "Sorry, my Daves. It's to the corner with y'all!":
                        #bad end
                        $ BibleResearched = 0
                        $ beat_Davids += 1
                        jump FreeRoam
                    "Nevermind":
                        jump DavidResearchChoice
            "Of course I'll head to the archives for y'all.":
                #archives
                d "We can't wait to hear what you find! Be safe on the stairs!"
                "research minigame in the archive"
                $ BibleResearched = 1
                #minigame go here
    #######
    $ beat_Davids += 1
    jump FreeRoam
label .beat4:
    if BibleResearched == 1:
        jump BibleResearched
    if BibleResearched == 0:
        jump DavidsDestroyed
    if BibleResearched == -1:
        jump DavidsIntact
        
    label DavidsDestroyed:
        "For the first time ever, the David's wing is silent. Not even a peep from them."
        pc "Uh... guys???"
        "But all you find where the three heroes once stood is a pile of dismembered bronze and marble."
        menu:
            "Actually this is a good thing... Couldn't stand those guys....":
                pass
            "Oh no! I feel guilty.":
                pass
        jump DavidsEnd

    label DavidsIntact:
        d "Well well, look who it is!"
        dm "Here to administer your final judgement, I see."
        "You walk to face The Davids, looking up at their preening faces."
        dd "Can't believe you can memorize a whole book, let alone the good book itself."
        db "That's no mean feat, kid. Impressive stuff."
        pc "Yeah....erm....well...."
        dm "Once you settle this once and for all, this museum can claim to house the definitive David.  I can't wait to see how impressed museum goers will be with me"
        dd "Puh--leeee-sssuhh! (Placeholder) is going to be chosing me anyways. "
        db "Nobody in their right mind is gonna choose either of you two. We're talkin about a hero's exhibit, not Biblical cosplaying."
        d "So, using that memory of yours, who's it going to be? Who's the definitive David?"
        menu:
            pc "From what I remember of the Bible, the definitive David is..."
            "Michelangelo's David":
                jump MichelangeloTrue
            "Donatello's David":
                jump DonatelloTrue
            "Bernini's David":
                jump BerniniTrue

    label MichelangeloTrue:
        dm "Without a shadow of a doubt!"
        dd "Oh duuuuude. You can't be serious!"
        db "A total nude?"
        dd "He's not even wearing a hat!"
        db "Not even shoes."
        dm "Never mind hat nor shoes! A colossal nude is the perfect form to convey the profundity and idealism of God's plan for me."
        jump DavidsEnd

    label DonatelloTrue:
        dd "Let's goooooooo! That's what I'm saying."
        dm "Alack! Nay rather..."
        db "Fuckin' pathetic.  Went with the kid?"
        dd "Good luck competing for seconds, you losers."
        "He picks up the head of Goliath and gives it a kiss."
        dd "We did it, big guy! I told you two trolls. Two heads are better than one! An exhibit about the potential of youthful vigor here we come!"
        jump DavidsEnd

    label BerniniTrue:
        db "You did the right thing, kid."
        dm "Do you want this to be an art exhibit or a calisthenics class?!"
        dd "This guy's face is barely visible. It's all shadowy and hidden. Dude don't even look at the audience!"
        db "Cool it, you two. No more beauty pagent masquerading as art."
        "He begins to coil in position, flexing and swinging his sling."
        db "Call me old fashion, but I'm just here to get the job done."
        jump DavidsEnd

    label BibleResearched:
        d "Look at you! We knew you'd be back."
        dm "You can read! You can REALLY read!"
        dd "And make it down stairs!"
        db "And back up 'em too."
        d "We thank you!"
        pc "Just getting my steps and my reading in for the week. "
        pc "I have some good news... or at least I think it's pretty good."
        pc "Turns out the source has it all."
        d "Who's et al?"
        pc "No. Not et al. The source...it's more complex than I thought..."
        pc "It's got this idea that David, despite being just a mortal, can approach and dare I say embody an ideal human."
        dm "Thus it is me who--"
        pc "It's also got this idea that David, despite just being a kid, can have the capacity to do what grown-ups can't, can even behead a giant."
        dd "I told you, you 40 pounds of bronze replicated skull, you!"
        pc "It's also got this idea that David, despite not having much a reputation for saying much, is a hero marked by duty, action, bravery."
        db "Not a lie to my ears."
        pc "My point is that the source says you all define David. Heroes are complicated people, not singular in any one respect."
        "The Davids look at eachother and shrug their collective shoulders."
        pc "I means sure individually you each beat a David, but together in an exhibit, you can beat the greatest challenge you heros face: pride."
        "The Davids start to cry."
        pc "Oh please. No more tears. I've already had to weather that storm with Gilgamesh."

    label DavidsEnd:
        "You have [actions] action(s) left."
    $ beat_Davids += 1
    jump FreeRoam