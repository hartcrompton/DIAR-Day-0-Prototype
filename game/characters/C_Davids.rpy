#Davids

default beat_Davids = 1
default BibleResearched = 0
default DefinitiveDave = "NONE"
default b2_DefinitiveDave = "NONE"

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
    call advance_time
    jump expression "conv_Davids" + "." + "beat" + "%d" % beat_Davids

label .beat1:
    "You fear the sounds of infighting, again…"
    d "You're wrong! It can only be me! There's one David in the story, and one David out here!"
    dm "The true David would have a form to match the legacy of King David himself!"
    dd "At 17 feet you're more like {i}the Goliath{/i} than {i}the David{/i}."
    db "The form is that of a shepherd. Strong, agile, and mortal. The true David is obviously me."
    menu:
        "Hey, would you three calm down, please?":
            pass
        "Excuse me, hello?":
            pass
        "Shut the hell up! I can hear you from the lobby!":
            pass
    db "Who are you? State your business."
    dd "Woah, sorry, geez."
    dm "Who might you be, that you can comprehend my euphonic voice?"
    menu:
        "I'm the new kid on the job.":
            pass
        "I'm the curator. I was just hired.":
            pass
    dd "Another David! Oh no. This one can walk, too."
    db "I'm not afraid of you, New David. I will face any foe."
    dm "You two are such boors. I highly doubt this is another David. What is your name, stranger?"
    pc "I'm [pc_name]."
    if pc_name == "David":
        dm "Well, I stand corrected, it is another David."
    menu:
        "Are you, like, brothers or something?":
            db "Brothers?! How dare you. I don't look anything like these prissy posers."
            pass
        "Who put you in the same room?":
            dm "Don't you know anything about museums? We're arranged according to our proper places."
            pass
    dd "Don't pretend like you know what you're talking about, you… false witness!"
    menu:
        "What's so bad about having three of you here?":
            pass
        "I already have four or five Davids in my life. Remind me why I need another?":
            pass
    db "I'm the heroic one. You can take pictures, but I'm not posing. "
    dm "Ugh…Did the pipes break again? All I heard was a lot of hot air."
    dd "See? SEE? It's always like this. I'm not gonna back down. The real David would {i}never{/i} back down!"
    pc "So you're the big fancy version, a kid version, and a fighter version?"
    pc "Aren't you different takes on the same thing?"
    db "HOW DARE YOU!"
    dm "My gentle docent, despite sharing the name David…"
    dd "You don't understand us at all! I can't believe this!"
    menu:
        "I'm sorry! It's hard to follow when you're contantly fighting!":
            pass
        "Deep down, you're all the same, aren't you?":
            pass
    dm "No. That cannot be the case. There must be only one David."
    db "One definitive David"
    dd "Yeah! I agree!"
    dm "Well. We agree on that at least. Give us time to collect ourselves and we'll try again tomorrow."

    ####
    $ beat_Davids += 1
    jump FreeRoam

label .beat2:
    d "Over here!"
    dm "[pc_name], you've returned!"
    dd "All right, [pc_name] is back!"
    db "You've got gumption. I'll give you that. "
    menu:
        "I was hoping to chat more and get to know you three.":
            pass
        "I want to know more about what you bring to this exhibit.":
            pass
    db "Ask your questions and be done with it."
    dm "Obviously, I'm the most qualified to hold forth on that topic."
    dd "And me! I will address your queries AND be done with it."
    menu:
        "Obviously I know that. But I also know a few Daves, a Davey, and went to school with like five other Davids too.":
            pass
        "So which Davids are you?":
            pass
    #needs some sort of transition from the first response
    dm "The Biblical David. The grand vision of a great figure."
    dd "The shephard boy who combined bravery and skill."
    db "… The one who slew Goliath."
    menu:
        "Ok so you were a kid soldier… or something?":
            pass
        "So you're an important king from the Bible.":
            pass
    dm "Not only the Bible. From history. Important texts contain the stories of important people."
    dd "Yes! David was brave from childhood, and an important king!"
    menu:
        "Oh, like King Arthur.":
            dm "…"
            db "…"
            dd "…"
            dd "NO! NOT LIKE KING ARTHUR!"
            db "What an imitator. Pulling a sword out of a rock doesn't compare to felling an actual giant."
            dm "Does this look like a room full of Arthurs to you? I implore you to attend to our current issue."
            dm "We are the young shepherd boy …"
            dd "Chosen by like the actual God himself."
            db "To be the King of his chosen people."
        "Ah! Yes, that's right. I remember now.":
            pass
        "We found something you agree on. Excellent.":
            pass
    dm "I'm sure my reputation precedes me. {i}Michelangelo's{/i} David, cut free from a single piece of marble."
    dm "I am seventeen feet tall and still a young man, beautiful and numinous, in tribute to the truth of David's works and legacy."
    dm "Is it any wonder that my picture is on art history textbooks year after year?"
    dd "YOU'RE SO BORING!"
    db "You look like you're standing before a weekly drawing class, not the field of battle. "
    dd "Yeah! You tell him!"
    dd "I was made the earliest! I'm the most legitimate! {i}Donatello{i} cast me from bronze a hundred years before you even existed!"
    dd "And at five-foot-seven-inches, I'm the closest to the true David at the moment he chose bravery and saw victory!"    
    menu:
        "An idealized David sounds more comprehensive. More real.":
            pass
        "The real David would be kid-sized, now that you mention it.":
            pass
    dd "Hang, on, I'm not even done yet!"
    dd "You want ideals in a kid-sized package? I have Goliath's {i}severed head!{/i} Guy's as big as my freaking torso."
    db "Quite the pair, eh? Different models, same shit, I say. "
    menu:
        "And who are you?":
            pass
        "Let me guess, {i}Leonardo's{/i} David.":
            dm "You can't be serious, [pc_name]."
            dd "Leo couldn't have made all this, are you paying attention at all?"
    db "Bernini. I am {i}Bernini's{/i} vision of David. The David the moment he became The David."
    db "Art isn't a beauty pageant, and war is no place for little kids."
    db "All art is in the action. Drama has its actors. Heroes have jobs, kid. I'm here to do mine."
    pc "So after first introductions and impressions I'm feeling that the definitive David so far is"

    menu:
        "Michelangelo's David":
            $ b2_DefinitiveDave = "Michelangelo's"
            dm "I knew it! You knew it. We all knew it."
            dd "Change your answer!"
            db "This can't be right."
        "Donatello's David":
            $ b2_DefinitiveDave = "Donatello's"
            dm "Oh no! Your vision is cloudy and imagination dull!"
            dd "Let's go, ha ha, yeah!"
            db "You can't be for real? The kid?"
        "Bernini's David":
            $ b2_DefinitiveDave = "Bernini's"
            dm "Oh no, not him. Hardly any one knows him!"
            dd "That dude? He hasn't even slayed Goliath yet! Got no goodies to show for it."
            db "That a way there, newbie. Now people can see what a real hero is. "

    dm "Let me ask you this, [pc_name] why did you choose who you chose?"
    menu:
        "I'm trying to keep this museum afloat.":
            pass
        "I honestly don't know what makes a David, THE David.":
            pass
        "I don't know, I feel like you all bullied me into an answer!":
            pass
    db "So we got no satisfactory decision! What do we do about that now?"    
    menu:
        "If I don't know, and you don't know, who else can we turn to?":
            pass
        "You've been around for centuries, how have you dealt with this before?":
            pass
    db "Is there…"
    dm "… Anyone who knows us better…"
    dd "… than we know ourselves?"
    d "…"
    d "Come back later, we'll think on it."
    ###
    $ beat_Davids += 1
    jump FreeRoam
label .beat3:
    d "But that's what I've been saying!"
    pc "Oh, God. You three agian. Well, you've had the night to think. What do you got?"
    dm "Indeed, indeed, my dear, [pc_name]. Yes, yes, this time I have a–"
    db "He means \"we.\""
    dd "Yeah as in \"we\" came up with a solution."
    menu:
        "Consult an expert like myself?":
            "You beam a smile."
            d "Not an expert… the expert."
            d "THE SOURCE!"
    menu:
        "The what?":
            pass
        "It always worries me a little when you all are enthusiastic and in agreement...":
            pass
    db "Scuttlebutt around the vending machine is that you can read. "
    dd "Aloud and silently!"
    db "And that you can make it down stairwells no problem."
    dm "There are rumors that beneath our very feet, hidden in the shelves of archives, is a copy of…"
    d "The Bible!"
    d "{i}Our{/i} source!"
    menu:
        "Oh God…":
            pass
        "Of course. How could I not see this coming?":
            pass
    d "Exactly!"
    db "Kid, if you could let us know what the original passage says about us taking out that old Philistenian oaf, Goliath…"
    dd "This old lug I got at my feet right here!"
    dm "Then you could tell us who is the definitve David!"
    pc "You want me to go read The Bible for you?"
    "They all slowly nod their heads."
    label DavidResearchChoice:
        menu:
            "[[Lie] Psh. I got that memorized. I don't need to run you no errand.":
                d "You have the Bible memorized?"
                dm "All chapters and verses… committed to memory?"
                dd "That's a lot of words… not going to lie."
                db "You shooting us straight?"
                pc "Uh… yeah… of course. All of it… Right up here…In my mind palace."
                d "Well in that case we can't wait to hear what you think tomorrow!"
                pc "Erm… right!… Yes… Tomorrow!"
                $ BibleResearched = -1
            "You know what? I'm done. Time to separate you.":
                pc "I can't look at you anymore. I'm just gonna shove you each in a corner until the gala is over."
                d "No please! Wait!"
                pc "What is it now?"
                dm "Give us one last chance!"
                dd "We'll be good! We promise! "
                db "We're on our last legs here. If you don't help us out… it could…"
                d "Crumble us!"
                menu:
                    "Sorry, my Daves. It's to the corner with y'all!":
                        #bad end
                        $ BibleResearched = 0
                        $ beat_Davids += 1
                        jump FreeRoam
                    "Let me think.":
                        jump DavidResearchChoice
            "Of course I'll head to the archives for you.":
                #archives
                d "We can't wait to hear what you find! Be safe on the stairs!"
                $ BibleResearched = 1
                #minigame go here
                #will probably need some player response lines
                call call_catalogue("Davids")
                label DavidsResearch:
                    $ renpy.set_return_stack([])
                    scene archives bg
                    hide screen ResearchMinigameDrawerUI
                    hide screen ResearchMinigameUI
                    "The player reads the relevant Bible passage."
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
        pc "Uh… guys?"
        "But all you find where the three heroes once stood is a pile of dismembered bronze and marble."
        menu:
            "Actually this is a good thing… Couldn't stand those guys….":
                pass
            #little on the nose
            "Oh no! I feel guilty.":
                pass
        "You bend down to pick up the only recognizable artificat in the rubble, a single sling shot."
        jump DavidsEnd

    label DavidsIntact:
        d "Well well, look who it is!"
        dm "Here to administer your final judgement, I see."
        dd "Can't believe you can memorize a whole book, let alone the good book itself."
        db "That's no mean feat, kid. Impressive stuff."
        pc "Yeah… erm… well…"
        dm "Once you settle this once and for all, this museum can claim to house the definitive David. "
        dm "I can't wait to see how impressed museum goers will be with me."
        dd "Puh-leeee-sssuhh! [pc_name] is going to be choosing me anyways. "
        db "Nobody in their right mind will choose either of you two. This is a hero's exhibit, not Biblical cosplaying."
        d "So, using that memory of yours, who's it going to be? Who's the definitive David?"
        pc "From what I remember of the Bible, the definitive David is…"
        menu:
            "Michelangelo's David.":
                $ DefinitiveDave = "dm"
                jump MichelangeloTrue
            "Donatello's David.":
                $ DefinitiveDave = "dd"
                jump DonatelloTrue
            "Bernini's David.":
                $ DefinitiveDave = "db"
                jump BerniniTrue

    label MichelangeloTrue:
        dm "Without a shadow of a doubt! "
        dd "Oh, dude. You can't be serious!"
        db "A total nude?"
        dd "He's not even wearing a hat!"
        db "Not even shoes."
        dm "Never mind hat nor shoes! A colossal nude is the perfect form to convey the profundity of God's plan."
        jump DavidsEnd

    label DonatelloTrue:
        dd "Let's go! That's what I'm saying."
        dm "Alack! Nay rather…"
        db "Fucking pathetic.  Went with the kid?"
        dd "Good luck competing for seconds, you losers."
        "He picks up the head of Goliath and gives it a kiss."
        dd "We did it, big guy! Two heads are better than one! Our very own exhibit on youthful vigor."
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
        $ DefinitiveDave = "all"
        #this has gotta get broken up
        d "Look at you! We knew you'd be back."
        dm "You can read! You can REALLY read!"
        dd "And make it down stairs!"
        db "And back up them too."
        d "We thank you!"
        pc "Just getting my steps and my reading in for the week. "
        pc "I have some good news… or at least I think it's pretty good."
        pc "Turns out the source has it all."
        dd "Who's {i}Et Al{i}?"
        dm "Ah yes, I remember Et well."
        pc "No. Not et al. The source… it's more complex than I thought…"
        pc "It's got this idea that David, despite being just a mortal, can approach being an ideal human."
        dm "Thus it is me who–"
        pc "It's also got this idea that David, though a kid, can do what grown-ups can't, even behead a giant."
        dd "I told you, you 40 pounds of bronze replicated skull, you!"
        pc "It's also got this idea that David, even though he doesn't say much, is a hero of duty, action, bravery."
        db "Not a lie to my ears."
        pc "Point being, the source says you all define David. Heroes are complicated people, not singular in any one respect. "
        "The Davids look at eachother and shrug their collective shoulders. "
        pc "I know alone you each beat a Goliath."
        pc "But as an exhibit, together you can beat the greatest challenge you heroes face: pride."
        "The Davids start to cry."
        pc "Oh please. No more tears. I've already had to weather that storm with Gilgamesh."
    $ StoryCompletedTotal += 1
    label DavidsEnd:
        $ beat_Davids += 1
    jump FreeRoam

label .Outcome:
    if beat_Davids == 5:
        if DefinitiveDave == "db":
            "Bernini's David stands underneath a single overhead light, casting light on his twisting torso and long shadows at his feet."
            "The soldier before the battlefield. His banner reads…"
            "The Hero's Valor"
        elif DefinitiveDave == "dd":
            "Donatello's David stands alone, proudly beaming a smile."
            "Now as the one and true definitive David, the exhibit bears a banner that reads…"
            "Adolscence Ascending: Ephebic Hero, Future King"
        elif DefinitiveDave == "dm":
            "Michelangelo's David has somehow had his pedestal placed on another pedestal, and so stands especially tall, almost out of sight."
            "What can be discerned on his face is a mixutre of threatening menace, steely resolve, and holy devotion."
            "The exhibit banner reads…"
            "Liberated From Stone, Destined for Heaven"
        elif DefinitiveDave == "NONE":
            "The Davids lie in a heap of crumbled stone, graveled marble.  Where once stood heroes, now is an undifferentiated heap, on top of which sits a single slingshot."
        elif DefinitiveDave == "all":
            "All Davids stand facing outward, having eachother's back, in mutual appreciation. Their banner reads…"
            "Conquered, The Hero's Pride"
    elif beat_Davids > 1:
        #need an unresolved line
        "Unresolved"
    else:
        #bad
        "The Davids lie in a heap of crumbled stone, graveled marble."
        "Where once stood heroes, now is an undifferentiated heap."
        "On top of which sits a single stone, what could be used in a slingshot."