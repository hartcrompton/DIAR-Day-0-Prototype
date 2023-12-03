#Davids

default beat_Davids = 1
default BibleResearched = 0
default DefinitiveDave = "NONE"
default b2_DefinitiveDave = "NONE"
default DavidsTimeout = 0
default DavidsNude = 0
image davids = ConditionSwitch (
    "(DavidsNude == 0)", "images/Characters/Davids/davids_nonnude.png",
    "(DavidsNude == 1)", "images/Characters/Davids/davids_nude.png"
)

label conv_Davids:
    play music "music/B14_W_02.wav" fadein 0.4 volume 0.4
    scene foyer_tod:
        blur 5
    show davids at center
    if (actions > 0) and (beat_Davids < 5):
        jump .use_action
    else:
        return
    #d "You're talking to me, the Davids!"
    #menu:
    #    "Beat [beat_Davids]" if actions > 0 and beat_Davids < 5:
    #        jump .use_action
    #    "Bye":
    #        d "See ya"
    #        jump FreeRoam
    #    "Reset Beats":
    #        "Beats reset."
    #        $ beat_Davids = 1
    #        jump conv_Davids

label .use_action:
    #menu:
    #    d "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_Davids" + "." + "beat" + "%d" % beat_Davids
    #    "No, not really.":
    #        d "Understandable."
    #        jump conv_Davids
    #call advance_time from _call_advance_time_1
    $ DavidsTimeout = 1
    jump expression "conv_Davids" + "." + "beat" + "%d" % beat_Davids

label .beat1:
    "You hear the sounds of infighting, again…"
    d "You're wrong! It can only be me! There's one David in the story, and one David out here!"
    dm neutral "The true David would have a form to match the legacy of King David himself!"
    dd neutral "At seventeen feet you're more like {i}the Goliath{/i} than {i}the David{/i}."
    db neutral "The form is that of a shepherd. Strong, agile, and mortal. The true David is obviously me."
    menu:
        "Hey, would you three calm down, please?":
            pass
        "Excuse me, hello?":
            pass
        "Shut the hell up! I can hear you from across the museum!":
            pass
    db neutral "Who are you? State your business."
    dd neutral "Whoa, sorry, geez."
    dm neutral "Who might you be, that you can comprehend my euphonic voice?"
    menu:
        "I'm the new kid on the job.":
            pass
        "I'm the curator. I was just hired.":
            pass
    dd neutral "Another David! Oh no. This one can walk, too."
    db neutral "I'm not afraid of you, New David. I will face any foe."
    dm neutral "You two are such boors. I highly doubt this is another David. What is your name, stranger?"
    pc  "I'm [pc_name]."
    if pc_name == "David":
        dm neutral "Well, I stand corrected, it is another David."
    menu:
        "Are you brothers or something?":
            db surprise "Brothers?! How dare you. I don't look anything like these prissy posers."
            pass
        "Who put you in the same room?":
            dm neutral "Don't you know anything about museums? We're arranged according to our proper places."
            pass
    dd confused "Don't pretend like you know what you're talking about, you…false witness!"
    menu:
        "What's so bad about having three of you here?":
            pass
        "I already have enough Davids in my life. Why do I need another?":
            pass
    db neutral "I'm the heroic one. You can take pictures, but I'm not posing. "
    dm neutral "Ugh…Did the pipes break again? All I heard was a lot of hot air."
    dd neutral "See? SEE? It's always like this. I'm not gonna back down. The real David would {i}never{/i} back down!"
    pc  "So you're the big fancy version, a kid version, and a fighter version?"
    pc  "Aren't you different takes on the same thing?"
    db angry "HOW DARE YOU!"
    dm neutral "My gentle docent, despite sharing the name David…"
    dd sad "You don't understand us at all! I can't believe this!"
    menu:
        "I'm sorry! It's hard to follow when you're constantly fighting!":
            pass
        "Deep down, you're all the same, aren't you?":
            pass
    dm neutral "No. That cannot be the case. There must be only one David."
    db neutral "One definitive David"
    dd neutral "Yeah! I agree!"
    dm neutral "Well. We agree on that at least. Give us time to collect ourselves and we'll try again tomorrow."

    ####
    $ beat_Davids += 1
    jump FreeRoam

label .beat2:
    d "Over here!"
    dm neutral "[pc_name], you've returned!"
    dd neutral "All right, [pc_name] is back!"
    db neutral "You've got gumption. I'll give you that. "
    menu:
        "I was hoping to chat more and get to know you three.":
            pass
        "I want to know more about what you bring to this exhibit.":
            pass
    db neutral "Ask your questions and be done with it."
    dm neutral "Obviously, I'm the most qualified to hold forth on that topic."
    dd neutral "And me! I will address your queries AND be done with it."
    menu:
        "Obviously I know that. But I also know a few Daves, a Davey, and went to school with like five other Davids too.":
            pass
        "So which Davids are you?":
            pass
    #needs some sort of transition from the first response
    dm neutral "The Biblical David. The grand vision of a great figure."
    dd neutral "The shepherd boy who combined bravery and skill."
    db neutral "…The one who slew Goliath."
    menu:
        "Okay so you were a kid soldier…or something?":
            pass
        "So you're an important king from the Bible.":
            pass
    dm neutral "Not only the Bible. From history. Important texts contain the stories of important people."
    dd neutral "Yes! David was brave from childhood, and an important king!"
    menu:
        "Oh, like King Arthur.":
            dm dots "…"
            db dots "…"
            dd dots "…"
            dd confused "NO! NOT LIKE KING ARTHUR!"
            db neutral "What an imitator. Pulling a sword out of a rock doesn't compare to felling an actual giant."
            dm neutral "Does this look like a room full of Arthurs to you? I implore you to attend to our current issue."
            dm neutral "We are the young shepherd boy…"
            dd neutral "Chosen by like the actual God himself."
            db neutral "To be the King of his chosen people."
        "Ah! Yes, that's right. I remember now.":
            pass
        "We found something you agree on. Excellent.":
            pass
    dm neutral "I'm sure my reputation precedes me. {i}Michelangelo's{/i} David, cut free from a single piece of marble."
    dm neutral "I am seventeen feet tall and still a young man, beautiful and numinous, in tribute to the truth of David's works and legacy."
    dm sparkle "Is it any wonder that my picture is on art history textbooks year after year?"
    dd neutral "YOU'RE SO BORING!"
    db neutral "You look like you're standing before a weekly drawing class, not the field of battle. "
    dd neutral "Yeah! You tell him!"
    dd neutral "I was made the earliest! I'm the most legitimate! {i}Donatello{/i} cast me from bronze a hundred years before you even existed!"
    dd neutral "And at five-foot-seven-inches, I'm the closest to the true David at the moment he chose bravery and saw victory!" 
    menu:
        "An idealized David sounds more comprehensive. More real.":
            pass
        "The real David would be kid-sized, now that you mention it.":
            pass
    dd neutral "Hang, on, I'm not even done yet!"
    dd sparkle "You want ideals in a kid-sized package? I have Goliath's {i}severed head!{/i} Guy's as big as my freaking torso."
    db neutral "Quite the pair, eh? Different models, same shit, I say. "
    menu:
        "And who are you?":
            pass
        "Let me guess, {i}Leonardo's{/i} David.":
            dm neutral "You can't be serious, [pc_name]."
            dd neutral "Leo couldn't have made all this, are you paying attention at all?"
    db neutral "Bernini. I am {i}Bernini's{/i} vision of David. David the moment he became {i}The{/i} David."
    db neutral "Art isn't a beauty pageant, and war is no place for little kids."
    db neutral "All art is in the action. Drama has its actors. Heroes have jobs, kid. I'm here to do mine."
    pc  "Well, after those introductions and impressions, I guess the definitive David so far is…"
    menu:
        "Michelangelo's David.":
            $ b2_DefinitiveDave = "Michelangelo's"
            dm happy "I knew it! You knew it. We all knew it."
            dd sad "Change your answer!"
            db confused "This can't be right."
        "Donatello's David.":
            $ b2_DefinitiveDave = "Donatello's"
            dm sad "Oh no! Your vision is cloudy and imagination dull!"
            dd laugh "Let's go, ha ha, yeah!"
            db confused "You can't be for real? The kid?"
        "Bernini's David.":
            $ b2_DefinitiveDave = "Bernini's"
            dm sigh "Oh no, not him. Hardly anyone knows him!"
            dd question "That dude? He hasn't even slain Goliath yet! Got no goodies to show for it."
            db happy "That a way there, newbie. Now people can see what a real hero is. "

    dm neutral "Let me ask you this, [pc_name] why did you choose who you chose?"
    menu:
        "I'm trying to keep this museum afloat.":
            pass
        "I honestly don't know what makes a David, THE David.":
            pass
        "I don't know, you all bullied me into an answer!":
            pass
    db questions "So we got no satisfactory decision! What do we do about that now?"    
    menu:
        "If I don't know, and you don't know, who else can we turn to?":
            pass
        "You've been around for centuries, how have you dealt with this before?":
            pass
    db neutral "Is there…"
    dm neutral "…anyone who knows us better…"
    dd neutral "…than we know ourselves?"
    d "…"
    d "Come back later, we'll think on it."
    ###
    $ beat_Davids += 1
    jump FreeRoam
label .beat3:
    d "But that's what I've been saying!"
    pc  "Oh God. You three again. Well, you've had the night to think. What's the plan?"
    dm neutral "Indeed, indeed, my dear, [pc_name]. Yes, yes, this time I have a–"
    db neutral "He means \"we.\""
    dd neutral "Yeah as in \"we\" came up with a solution."
    menu:
        "Consult an expert like myself? [[Beam a smile]":
            d "Not {i}an{/i} expert…{i}the{/i} expert."
            d "THE SOURCE!"
        "Let's hear it.":
            d "Not just {i}any{/i} expert…{i}the{/i} expert."
            d "THE SOURCE!"
    menu:
        "The what?":
            pass
        "It worries me a little that you're all enthusiastic and in agreement…":
            pass
    db neutral "Scuttlebutt around the vending machine is that you can read. "
    dd neutral "Aloud {i}and{/i} silently!"
    db neutral "And that you can make it down stairwells no problem."
    dm neutral "There are rumors that beneath our very feet, hidden in the shelves of archives, is a copy of…"
    d "The Bible!"
    d "{i}Our{/i} source!"
    menu:
        "Oh God…":
            pass
        "Of course. How could I not see this coming?":
            pass
    d "Exactly!"
    db neutral "Kid, if you could let us know what the original passage says about us taking out that old Philistinian oaf, Goliath…"
    dd neutral "This old lug I got at my feet right here!"
    dm neutral "Then you could tell us who the definitive David is!"
    pc  "You want me to go read the Bible for you?"
    "They all slowly nod their heads."
    label DavidResearchChoice:
        menu:
            "[[Lie] Psh. I have it memorized. I don't need to run an errand.":
                d "You have the Bible memorized?"
                dm neutral "All chapters and verses…committed to memory?"
                dd neutral "That's a lot of words…not going to lie."
                db neutral "You shooting us straight?"
                pc  "Uh…yeah…of course. All of it…Right up here…In my mind palace."
                d "Well in that case we can't wait to hear what you think tomorrow!"
                pc  "Erm…right! Yes…tomorrow."
                $ BibleResearched = -1
            "You know what? I'm done. Time to separate you.":
                pc  "I'm just gonna shove you each in a corner until the Gala is over."
                d "No please! Wait!"
                pc "What is it now?"
                dm neutral "Give us one last chance!"
                dd neutral "We'll be good! We promise! "
                db neutral "We're on our last legs here. If you don't help us out…it could…"
                d "Crumble us!"
                menu:
                    "Sorry, my Daves. It's to the corner with you all!":
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
                hide davids
                scene archives bg
                "You descend the chilly stairwell that leads to the archives."
                pc "I really hope snooping around this archive settles things for those three. "
                call call_catalogue("Davids") from _call_call_catalogue
                label DavidsResearch:
                    $ renpy.set_return_stack([])
                    scene archives bg
                    hide screen ResearchMinigameDrawerUI
                    hide screen ResearchMinigameUI
                    show bible overlay
                    show book overlay
                    "{color=#ffffff}1 Samuel 17:38-40{/color}" "Then Saul dressed David in his own tunic. He put a coat of armor on him and a bronze helmet on his head."
                    "{color=#ffffff}1 Samuel 17:38-40{/color}" "David fastened on his sword over the tunic and tried walking around, because he was not used to them. \"I cannot go in these,\" he said to Saul, \"because I am not used to them.\" So he took them off."
                    "{color=#ffffff}1 Samuel 17:38-40{/color}" "Then he took his staff in his hand, chose five smooth stones from the stream, put them in the pouch of his shepherd's bag and, with his sling in his hand, approached the Philistine."
                    hide bible overlay
                    hide book overlay
                    "You slam the book shut, a constellation of dust leaps to the air, illuminated by the overhead light…"
                    pc  "Geez…I can see every one of those three in that passage."
                    pc  "Could it be all of them?"
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
        "For the first time ever, the Davids' wing is silent. Not even a peep from them."
        pc  "Uh…guys?"
        "But all you find—where the three heroes once stood—is a pile of dismembered bronze and marble."
        menu:
            "Actually this is a good thing…I couldn't stand them.":
                pass
            #little on the nose
            "Oh no! I didn't mean for this to happen…":
                pass
        "You bend down to pick up the only recognizable artifact in the rubble: a single sling shot."
        jump DavidsEnd

    label DavidsIntact:
        d "Well, well, look who it is!"
        dm neutral "Here to administer your final judgement, I see."
        dd neutral "Can't believe you can memorize a whole book, let alone the good book itself."
        db neutral "That's no mean feat, kid. Impressive stuff."
        pc  "Yeah…erm…well…"
        dm neutral "Once you settle this once and for all, this museum can claim to house the definitive David. "
        dm neutral "I can't wait to see how impressed museum goers will be with me."
        dd neutral "Puh-leeee-sssuhh! [pc_name] is going to be choosing me anyways. "
        db neutral "Nobody in their right mind will choose either of you two. This is a hero's exhibit, not Biblical cosplaying."
        d "So, using that memory of yours, who's it going to be? Who's the definitive David?"
        pc  "From what I remember of the Bible, the definitive David is:"
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
        dm neutral "Without a shadow of a doubt! "
        dd neutral "Oh, dude. You can't be serious!"
        db neutral "A total nude?"
        dd neutral "He's not even wearing a hat!"
        db neutral "Not even shoes."
        dm neutral "Never mind hat nor shoes! A colossal nude is the perfect form to convey the profundity of God's plan."
        jump DavidsEnd

    label DonatelloTrue:
        dd neutral "Let's go! That's what I'm saying."
        dm neutral "Alack! Nay rather…"
        db neutral "Fucking pathetic. Went with the kid?"
        dd neutral "Good luck competing for seconds, you losers."
        "He picks up the head of Goliath and gives it a kiss."
        dd neutral "We did it, big guy! Two heads are better than one! Our very own exhibit on youthful vigor."
        jump DavidsEnd

    label BerniniTrue:
        db neutral "You did the right thing, kid."
        dm neutral "Do you want this to be an art exhibit or a calisthenics class?!"
        dd neutral "This guy's face is barely visible. It's all shadowy and hidden. Dude don't even look at the audience!"
        db neutral "Cool it, you two. No more beauty pageant masquerading as art."
        "He begins to coil in position, flexing and swinging his sling."
        db neutral "Call me old-fashioned, but I'm just here to get the job done."
        jump DavidsEnd

    label BibleResearched:
        $ DefinitiveDave = "all"
        #this has gotta get broken up
        d "Look at you! We knew you'd be back."
        dm neutral "You can read! You can REALLY read!"
        dd neutral "And make it down stairs!"
        db neutral "And back up them too."
        d "We thank you!"
        pc  "Just getting my steps and my reading in for the week. "
        pc  "I have some good news…or at least I think it's pretty good."
        pc  "Turns out the source has it all."
        dd neutral "Who's {i}Et Al{/i}?"
        dm neutral "Ah yes, I remember Et well."
        pc  "No, not {i}et al{/i}. The source…it's more complex than I thought…"
        $ DefM = 0
        $ DefD = 0
        $ DefB = 0
        label TheDefinitiveDavid:
            menu:
                "It's got this idea that David, despite being just a mortal, can approach being an ideal human." if DefM == 0:
                    $ DefM = 1
                    dm neutral "Thus it is me who–"
                    pc "Hold on, there's more."
                    jump TheDefinitiveDavid
                "It also has the concept that David, though a kid, can do what grown-ups can't, even behead a giant." if DefD == 0:
                    $ DefD = 1
                    dd neutral "I told you, you 40 pounds of bronze replicated skull, you!"
                    pc "That's not all."
                    jump TheDefinitiveDavid
                "There's the theme that David, even though he doesn't say much, is a hero of duty, action, bravery." if DefB == 0:
                    $ DefB = 1
                    db neutral "Not a lie to my ears."
                    pc "Just wait a second."
                    jump TheDefinitiveDavid
        pc  "The source says you {i}all{/i} define David. Heroes are complicated people, not singular in any one respect. "
        "The Davids look at eachother and shrug their collective shoulders. "
        pc  "I know you each beat Goliath alone."
        pc  "But together as an exhibit, you can beat the greatest challenge you heroes face: pride."
        "The Davids start to cry."
        if beat_Gilgamesh >= 3:
            pc  "Oh, please. No more tears. I've already had to weather that storm with Gilgamesh."
        else:
            pc "Oh, please. No more tears. I'm pretty sure we don't have flood insurance."
    $ StoryCompletedTotal += 1
    label DavidsEnd:
        $ beat_Davids += 1
    jump FreeRoam

label .Outcome:
    scene foyer_tod with fade:
        blur 2
    if beat_Davids == 5:
        if DefinitiveDave == "db":
            show davidb at center
            "Bernini's David stands underneath a single overhead light, casting light on his twisting torso and long shadows at his feet."
            "The soldier before the battlefield. His banner reads…"
            "The Hero's Valor."
        elif DefinitiveDave == "dd":
            show davidd at center
            "Donatello's David stands alone, proudly beaming a smile.  "
            "Now, as the one and true definitive David, the exhibit bears a banner that reads…"
            "Adolescence Ascending: Ephebic Hero, Future King."
        elif DefinitiveDave == "dm":
            show davidm at center
            "Michelangelo's David has somehow had his pedestal placed on another pedestal, and so stands especially tall, almost out of sight."
            "What can be discerned on his face is a mixture of threatening menace, steely resolve, and holy devotion."
            "The exhibit banner reads…"
            "Liberated from Stone, Destined for Heaven."
        elif DefinitiveDave == "NONE":
            show davids destroyed at center
            "The Davids lie in a mess of crumbled stone, graveled marble."
            "Where once stood heroes, now is an undifferentiated heap."
            "On top sits a single stone, which could be used in a slingshot."
        elif DefinitiveDave == "all":
            show davids at center
            "All Davids stand facing outward, having each other's back, in mutual appreciation. Their banner reads…"
            "Conquered, the Hero's Pride."
    elif beat_Davids > 1:
        #need an unresolved line
        "Their prayers unanswered, the Davids lie in a crumbled, ashy heap."
        "On top sits a single stone, which could be used in a slingshot."
    else:
        #bad
        show davids destroyed at center
        "Their prayers unanswered, the Davids lie in a crumbled, ashy heap."
        "On top sits a single stone, which could be used in a slingshot."