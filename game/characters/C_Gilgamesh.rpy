#Gilgamesh

default beat_Gilgamesh = 1
default SongA = 0
default SongB = 0
default SongChoiceLoop = 0
default Beast1 = "NONE"
default Beast2 = "NONE"
default WhatOfEnkiduLoop = 0
default UrukChoice = 0
default BeastChoice = 0
default SongTheme = "NONE"

label conv_Gilgamesh: 
    
    if beat_Gilgamesh != 3:
        scene antiquities bg:
            blur 5
        show gilgamesh at center:
            xoffset 0
        show eanasir at right:
            xoffset -50
            zoom .6
    if beat_Gilgamesh == 3:
        scene foyer bg:
            blur 5
        show admin at truecenter:
    jump .use_action
    #menu:
    #    "Beat [beat_Gilgamesh]" if actions > 0 and beat_Gilgamesh < 5:
    #        jump .use_action
    #    "Bye":
    #        gi "See ya"
    #        jump FreeRoam
    #    "Reset Beats":
    #        "Beats reset."
    #        $ beat_Gilgamesh = 1
    #        jump conv_Gilgamesh

label .use_action:
    #menu:
    #    gi "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_Gilgamesh" + "." + "beat" + "%d" % beat_Gilgamesh
    #    "No, not really.":
    #        gi "Understandable."
    #        jump conv_Gilgamesh
    call advance_time
    jump expression "conv_Gilgamesh" + "." + "beat" + "%d" % beat_Gilgamesh

label .beat1:
    "The atmosphere of the Antiquities Wing is oppressive."
    gi "Well, what are you?"
    #gender neutralify this
    gi "Peasant, or king?"
    menu:
        "King? Let's go with king.":
            gi "Doubtful, a true king needn't announce it."
        "Technically peasant I guess.":
            gi "Yes, you do have that look about you."
        "It doesn't work that way anymore.":
            gi "But it does, and always has. Royalty is more than a crown."
    gi "Now go on, take it in."
    gi "Hard to believe someone like {i}you{/i} could be in the same room as someone like {i}me{/i}."
    menu:
        "Is it?":
            pass
        "I don't even know who you are.":
            pass
    "Gilgamesh rocks with laughter."
    gi "You stand before my throne and pretend not to know me?"
    e "Throne? You're just standing around."
    menu:
        "Who are you two?":
            e "I am Ea-nasir, and this loadmouthed rock is--"
            hide gilgamesh
            show gilgamesh at center with hpunch
            gi "GILGAMESH!"
        "The tablet's right, I don't see a throne.":
            gi "True royalty needs no carven throne."
            gi "Nasir, why haven't you announced me yet?"
            e "I'm sure you can do that yourself. Forgive me, I am Ea-nasir."
            gi "And I am..."
            hide gilgamesh
            show gilgamesh at center with hpunch
            gi "GILGAMESH!"
    gi "..."
    gi "You're allowed to grovel now."
    menu:
        "Who?":
            gi "Come now, don't play coy. You surely know me."
            e "Not everyone knows you."
            gi "Oh, don't be absurd."
        "Were you some king?":
            gi "... Some king?"
            gi "KING of kings. "
            gi "Son of Ninsun and Lugalbanda!"
            gi "Heir to Uruk and its thousand palaces!"
            gi "Slayer of beasts and subduer of GODS!"
        "Why are you holding a lion?":
            gi "What?!"
            gi "Because I am Master of Beasts!"
            gi "Heir to divinity and royalty!"
            gi "I pick my teeth with the bones of the Bull of Heaven!"
    menu:
        "Wow, cool.":
            pass
        "I'm new here, so...":
            pass
    gi "Nasir! Be this another of your tricks?"
    e "Sadly no, though I enjoy it all the same."
    gi "Eugh. Even a viper would have to bow its head to gaze upon you."
    menu:
        "OK, you're up HERE. I need you down HERE.":
            e "..."
            gi "..."
            gi "How dare you!"
        "I see why nobody visits this wing.":
            gi "They should be so lucky as to even glimpse me!"
    gi "Your kings today must be fat and lax."
    pc "We don't really have kings."
    e "Oh?"
    gi "No! This is worse than I feared."
    gi "But ignorance is what one must expect from peasants."
    gi "Heed me: In the vaults of this place is a tome."
    gi "A record of my royal deeds."
    gi "Read it, and you will understand."
    gi "Now go, awe will not inspire itself."
    "Gilgamesh, mercifully, falls silent."
    e "He'll be like that for a while."
    e "I welcome the reprieve."
    menu:
        "Who are you again?":
            e "Ea-nasir, former copper merchant."
            e "Though perhaps not a terribly good one."
        "Is he always like that?":
            e "No, I'd say you caught him on a good day."
    e "And you must be the new curator."
    menu:
        "Maybe not for long if I need to make Gilgamesh behave.":
            pass
        "I guess I am. I don't know what I expected. Not this.":
            pass
    e "My sympathies. Life has a way of surprising us."
    e "I hate to say it, but you should humor him, if only to shut him up."
    menu:
        "He mentioned a vault?":
            e "The Archive. First left from the Foyer, I believe."
        "So there's actually a book about him?":
            e "Yes. Loud, boisterous, and preposterous, just like him."
    e "You should know: He's not as familiar with his own story as you'd think."
    e "He's tried very hard to forget what happened."
    e "To him. To Enkidu."
    menu:
        "You make it sound bad.":
            e "It's life, it can't all be good."
        "I haven't heard of Enkidu.":
            e "You will. Would that it were Enkidu in this museum instead."
    e "One last thing."
    e "Don't talk about Enkidu."
    e "Gilgamesh is already irritating enough, I'd prefer to leave him in blissful ignorance."
    hide gilgamesh
    hide easnasir
    "Let's see what the archive has on Gilgamesh."
    call call_catalogue("Gilgamesh")
    label GilgameshResearch:
        $ renpy.set_return_stack([])
        scene archives bg
        hide screen ResearchMinigameDrawerUI
        hide screen ResearchMinigameUI
        show epicofgilgamesh bg
        "Player learns That Gil was KING of URUK"
        "He was a real pain in the ass until ENKIDU showed up and beat him in a fight"
        "They became best friends / lovers"
        "ISHTAR sent the BULL OF HEAVEN to humble them. Gil killed it, which pissed her off even more."
        "ISHTAR killed ENKIDU"
        "GIl went kinda CRAZY and fought to the END OF THE WORLD to find IMMORTALITY"
        "Long story short, HE DIDN'T. But he returned to URUK and found PEACE."
        "ALSO: Something about Ea-nasir having a past scamming people with shoddy copper"
        #return
    $ beat_Gilgamesh += 1
    jump FreeRoam
label .beat2:
    pc "Well, I read it."
    gi "..."
    pc "..."
    gi "..."
    menu:
        "Are you waiting for something?":
            gi "Astonishment, awe, the usual."
        "I said I read your book.":
            gi "{i}Epic{/i}. But yes, good."
    gi "Now come, you've beheld the truth."
    gi "All my accomplishments and accolades."
    gi "Am I not true royalty? The king of kings?"
    menu:
        "There have been a {i}lot{/i} of kings.":
            gi "Don't be coy. We both know a crown does not a king make."
        "I'll admit it, I was impressed.":
            gi "Observe, Nasir. Deference is its own reward."
        "You were a royal pain in the ass.":
            gi "Impudent as before, but what should I have expected."
    menu:
        "So, you'll behave for the exhibit now?":
            gi "Perhaps. But what proof do I have you kept your word?"
        "I read it, OK. Can you at least relax for the week?":
            gi "And what proof is there, hm?"
    gi "I've grown familiar with honey-tongued lies from being next to this charlatan."
    e "At least {i}I{/i} don't nauseate guests with my mere presence."
    menu:
        "Nasir, what is he talking about?":
            e "Just simple mistakes."
            gi "Mistakes? Even now he lies. He was a cheat and swindler."
            e "Yes, you {i}do{/i} like to remind me of my failings."
        "Is this gossip? I love gossip.":
            gi "No, merely the truth."
            gi "He was a cheat and swindler. He took good coin and returned trash."
            e "Yes, I'm sorry I didn't kill anyone. Then I'd at least be remembered fondly."
    gi "But enough of our deceitful companion."
    gi "Tell me of my adventures."
    $ UrukChoice = 0
    $ BeastChoice = 0
    label AdventureChoice:
        menu:
            "You ruled Uruk." if UrukChoice == 0:
                $ UrukChoice = 1
                gi "Indeed, can you even imagine a city of its equal?"
                pc "Did it really have a thousand palaces?"
                gi "Of course."
                pc "And ten-thousand temples?"
                gi "Naturally."
                menu:
                    "[[Lie] And ferris wheels and merry-go-rounds?":
                        gi "Thousands of them."
                        pc "You don't even know what those last two are!"
                        gi "I don't need to. If they are great, then my city must have had them."
                    "Enough about Uruk.":
                        pass
                jump AdventureChoice
            "You fought many beasts." if BeastChoice == 0:
                $ BeastChoice = 1
                gi "{i}Bested{/i}. I {i}bested{/i} many beasts. Which was your favorite?"
                menu:
                    "Humbaba.":
                        gi "Ah yes, the beast of cedars."
                        pc "How many terrors did he have again?"
                        gi "I- well, of course {i}I{/i} know. Why don't {i}you{/i} tell me?"
                        menu:
                            "Seven.":
                                gi "No, that can't be, I'm sure it was more."
                            "[[Lie] Seventy.":
                                gi "Yes. Truly a terrible foe."
                            "[[Lie] Seven-hundred.":
                                gi "Yes. Truly a terrible foe."
                    "The Bull of Heaven.":
                        gi "Ah yes, sent by Enki to test me."
                        menu:
                            "Pretty sure it was Ishtar who sent it.":
                                gi "What? Oh, of course. That was... just a little test for you."
                            "How tall was it? The book never said.":
                                gi "A hundred hand-spans. At least."
                                pc "Really? Only a hundred?"
                                gi "How foolish of me. It was two-hundred, at least. Maybe even three."
                        e "I only pray you didn't murder some poor farmer's cow."
                    "[[Make one up.]":
                        menu:
                            "The Chicken...":
                                $ Beast1 = "The Chicken"
                                pass
                            "The Alpaca...":
                                $ Beast1 = "The Alpaca"
                                pass
                            "The Crawfish...":
                                $ Beast1 = "The Crawfish"
                                pass
                        menu:
                            "... of Misgivings.":
                                $ Beast2 = "of Misgivings"
                                pass
                            "... of Pasteurization.":
                                $ Beast2 = "of Pasteurization"
                                pass
                            "... of Negation.":
                                $ Beast2 = "of Negation"
                                pass
                        pc "I loved your battle against [Beast1] [Beast2]."
                        gi "Uh - yes, of course."
                        gi "The terrible - um - sky-scourge. Sent by Ninlil of the south wind."
                        menu:
                            "Uh-huh. Whatever you say.":
                                pass
                            "I made that one up.":
                                gi "Ah, but you see- the thing is- that was... merely another test!"
                jump AdventureChoice
    gi "But of course, my story is more than my own."
    gi "What of my truest friend, what of Enkidu?"
    "Ea-nasir gives you a {i}look{/i}."
    $ WhatOfEnkiduLoop = 0
    label WhatOfEnkiduChoice:
        menu:
            "[[Glare back at Ea-nasir.]" if WhatOfEnkiduLoop == 0:
                $ WhatOfEnkiduLoop = 1
                "Ea-nasir's stony gaze turns sharper."
                gi "Nasir! How many times must I order you to stop eye-balling my subjects?"
                jump WhatOfEnkiduChoice
            "Was Enkidu really made from clay?":
                gi "Perhaps, but I assure you, his heartblood beat hot as any other."
            "He beat you. A peasant beat a king.":
                gi "{i}First{/i}, he was born from the will of the gods, hardly a peasant."
                gi "Second, he did not \"beat\" me. It was a draw."
                menu:
                    "Not a peasant? He was literally born out of clay.":
                        e "Some might say that's technically {i}lower{/i} than a peasant."
                        gi "Yet {i}he{/i} far exceeded his meager origins."
                        gi "Something that can't be said of {i}everyone{/i} here."
                    "A draw? So that's what you called losing in Sumeria.":
                        gi "I will not argue semantics with a peasant!"
    gi "We fought through the streets."
    gi "We shattered the gates."
    gi "We brought down the very temples."
    gi "And at last we grasped each other, all our strength laid bare."
    menu:
        "It sounds like you two were close.":
            e "Hard to imagine anyone who could stomach his company, let alone love him."
        "Did you love him?":
            e "I doubt he could love anyone as he loves himself."
    gi "{i}Love?{/i} You dare invoke such miniscule sentiment?"
    gi "A goddess loves her worshippers."
    gi "A king loves his people."
    gi "But Enkidu? I did not {i}love{/i} him..."
    gi "He was my heart."
    gi "A lion who allowed my caress."
    gi "For him, I would measure the earth, and find its grand expanse unable to contain him."
    menu:
        "That sounds {i}exactly{/i} like love.":
            gi "And some birds may mimic speech, but is there meaning behind their words?"
        "I'm sorry I asked.":
            gi "Do not be sorry. Be better."
    pc "Either way, it must have been hard."
    e "Hey! Remember what I said? Ix-nay on the kidu-enay eath-day."
    gi "Nasir, enough with your porcine prose."
    gi "Now tell me, what was hard?"
    menu:
        "[[Gently] When, you know...":
            gi "Yes?"
            e "Stop it."
            menu:
                "[[Gently] I mean, when Enkidu...":
                    e "I warned you."
                    gi "Enkidu's glories are as numerous as my own, you'll have to be specific."
                    menu:
                        "[[Gently] So, after the Bull of Heaven...":
                            gi "A noble opponent."
                            menu:
                                "[[Gently] And Ishtar was upset...":
                                    gi "Hah, she was always one for grudges."
                                    e "I told you. He doesn't know."
                                    menu:
                                        "[[Gently] And she... She killed him.":
                                            gi "..."
                                            gi "She killed who?"
                                            pc "Enkidu. Ishtar cursed him."
                                            jump EnkiduDied
                                        "It must have been hard when Ishtar killed him.":
                                            jump EnkiduDied
                                "It must have been hard when Ishtar killed him.":
                                    jump EnkiduDied
                        "It must have been hard when Ishtar killed him.":
                            jump EnkiduDied
                "It must have been hard when Ishtar killed him.":
                    jump EnkiduDied
        "It must have been hard when Ishtar killed him.":
            jump EnkiduDied
    label EnkiduDied:
        gi "..."
        e "{i}This{/i} is on you."
        menu:
            "It happened thousands of years ago. You can't be surprised.":
                pass
            "You really didn't know?":
                pass
            "Actually, it was kind of your fault.":
                pass
        gi "No, no he would have fallen in battle."
        gi "There must have been some insurmountable foe."
        menu:
            "It's all written down.":
                pass
            "I'm sorry you had to find out like this.":
                pass
            "[[Look to Ea-nasir for help.]":
                "For a clay tablet, Ea-nasir does a remarkable job of looking at everything except you."
        gi "I..."
        gi "You need to leave."
        show gilgamesh at left with move:
            xoffset 200
            ease .2 zoom .6
        show eanasir at truecenter with move
        e "I did warn you."
        menu:
            "He would have found out sooner or later.":
                pass
            "You could have been a {i}little{/i} more specific.":
                pass
            "Trust me, this is for the best.":
                pass
        e "Oh? Well it's good to see the Admin's hiring standards haven't changed at all."
        e "With any luck, this whole place will be shuttered by the end of the week."
        menu:
            "I'm not going to let that happen.":
                e "Really? Well you certainly seem to be trying."
            "Do you want me to fail?":
                e "Not you specifically."
            "You're just bitter.":
                e "I prefer \"realistic\"."
        gi "LEAVE!"
        "He probably just needs some time with his thoughts. Surely, this will be for the best."
    $ beat_Gilgamesh += 1
    jump FreeRoam
label .beat3:
    ad "Hi, how are you, how are things?"
    pc "Well I-"
    ad "That's great! Hey, no big deal, but it looks like the water alarm is going off in the Antiquities Wing."
    ad "Do you think you could maybe see what that's about?"
    menu:
        "Sure.":
            pass
        "Maybe you should call a plumber?":
            pass
        "I think I might know.":
            pass
    "The Admin already hung up."
    scene antiquities flood with fade
    "The antiquities wing is positively {i}flooded{/i}."
    show eanasir at right
    e "Oh you're back, come to make an even bigger mess?"
    menu:
        "OK, {i}this{/i} is not my fault.":
            pass
        "What happened here?":
            pass
        "Maybe, we'll see.":
            pass
    e "You told Gilgamesh exactly what I told you {i}not{/i} to."
    e "He's been sobbing ever since."
    menu:
        "It looks like a flood.":
            e "You didn't even see the worst of it."
            e "The wailing and shouting, it was quite the sight."
        "And you've been doing... what exactly?":
            e "I'm sorry, I didn't realize that {i}I{/i} had been hired as the new curator."
        "Hey, you were all screwed up before I even got here.":
            e "Yes, perhaps you should have stayed away."
    e "At least he seems to have run dry."
    "You sigh. Time to bust out the mop."
    call minigamestart_mop
    scene antiquities bg with fade:
        blur 5
    "Whew. Still a little damp, but at least there isn't any obvious damage."
    show gilgamesh at truecenter
    gi "Enkidu, I failed you!"
    show eanasir at right:
        zoom .7
    e "Oh good, he's starting again."
    "Gilgamesh is clearly on the verge of another flood of tears."
    menu:
        "Hey champ, how're you doing?":
            gi "{i}You{/i}. The prodigal specter, come to haunt me again?"
        "Gil, I need you to hold it together for me.":
            gi "Was it not enough to torment me, you would even deny me my grief?"
        "[[Hit Gilgamesh with the mop.]":
            "The mop slaps loudly against the statue. He hardly seems to notice."
    pc "Any ideas, Nasir?"
    e "He's like a child who's lost its favorite toy."
    menu:
        "He's not a child, he's grieving.":
            pass
        "OK, he's a {i}little{/i} childish, but we still need to fix this.":
            pass
    e "Oh {i}forgive{/i} me. The world must stop for the crocodile tears of a dead king."
    menu:
        "What's your problem?":
            e "Gilgamesh, as always."
            e "Unlike him, I can't hide my mistakes."
        "It's not just his feelings at stake here.":
            e "Yes, your precious {i}museum{/i}. Let it close and be done with it."
            e "Unlike Gilgamesh, I can't hide my mistakes."
    e "Do you know what that's like?"
    menu:
        "From one fuckup to another: Yes.":
            pass
        "Not a clue. I'm a perfect {0}prince{/0}{1}princess{/1}{2}cherub{/2}.":
            pass
        "{i}Everyone{/i} feels that way.":
            pass
    e "You act so noble. We all know you're just here because no one else would take you on."
    menu:
        "Yeah, it's called making the best of a bad situation!":
            pass
        "That's not even true, I care!":
            pass
        "At least I'm not out to sabotage us!":
            pass
    e "How about you stop \"helping\" and just let this dump close?"
    gi "ENOUGH!!!"
    gi "Am I not permitted even a {i}moment{/i} of peace to grieve?"
    menu:
        "Don't worry, I've got a lot to say to you too.":
            pass
        "You're right, this isn't the time.":
            pass
        "Sorry.":
            pass
    e "You've had four-thousand years! When do the rest of us get some peace away from you?"
    menu:
        "Nasir, stop it.":
            pass
        "He's right. Remembering things now doesn't fix anything.":
            pass
        "Another snipe from EITHER of you and I'll push you BOTH down the stairs.":
            e "You wouldn't dare, they'd fire you on the spot."
            menu:
                "Don't try me. [[Give him the crazy eye]":
                    pass
                "Just try to behave.":
                    pass
    e "He just can't handle an ounce of guilt."
    gi "At least my heart beats blood and not venom."
    menu:
        "[[Slap Ea-nasir]":
            e "What was that for?!"
        "[[Slap Gilgamesh]":
            gi "How dare you!"
        "[[Slap both of them]":
            e "What was that for?!"
            gi "How dare you!"
        "[[Slap both of them and yourself for good measure]":
            gi "How dare you!"
            e "What was that for?!"
            pc "Ow!"
            "You're not sure why you included yourself."
    menu:
        "Gil, you need to get over yourself.":
            pc "You feel bad for something you did four-thousand years ago."
            pc "So why don't you feel bad for what you're doing right now?"
            e "Exactly!"
            pc "And {i}you!{/i}"
            pc "Have you ever thought that if the museum closes, you'll still be just as miserable?"
            pc "Aren't you tired of feeling guilty for something no one else cares about?"
        "Nasir, maybe you're the problem.":
            pc "Have you ever thought that if the museum closes, you'll still be just as miserable?"
            pc "Aren't you tired of feeling guilty for something no one else cares about?"
            gi "Precisely!"
            pc "And {i}you!{/i}"
            pc "You feel bad for something you did four-thousand years ago."
            pc "So why don't you feel bad for being a jerk right now?"
    e "It's an act! He only cares about himself."
    menu:
        "I don't think that's true.":
            pc "Tell us about Enkidu."
        "Maybe you're right.":
            gi "He isn't."
            pc "Then tell us about Enkidu."
    gi "..."
    gi "The last thing I told him..."
    pc "What was it?"
    gi "I told him I was afraid."
    menu:
        "Why were you scared?":
            gi "Where I was restless, he was at peace."
            gi "I was afraid, without him, I would return to what I once was."
        "It's hard to imagine you afraid.":
            gi "I suppose spending centuries running from one's fear makes one rather good at it."
            gi "I was afraid, without him, I would return to what I once was."
    "And what did Enkidu say?"
    gi "He told me:"
    gi "\"Hold my hands in yours, that you need not fear what hands like ours might do.\""
    #gi "And then he died."
    e "..."
    menu:
        "Happy, Nasir?":
            pass
        "Thank you, Gil.":
            pass
    gi "Was it truly all my fault?"
    menu:
        "Yes. Absolutely.":
            gi "Hah. So blunt."
            gi "But I see it now."
        "I wouldn't say {i}all{/i}. But kinda.":
            gi "Hah. You're too kind."
        "Does it matter?":
            pc "Would it change anything?"
            gi "Hah. You're right, of course."
    gi "But I'm still afraid."
    gi "I've wasted so much time."
    e "Maybe we both have."
    gi "When I meet Enkidu again, I won't be worthy of him."
    menu:
        "Then change!":
            gi "I'm not sure I know how."
        "I'm not losing my job because you can't get over yourself.":
            gi "But how do I change?"
        "What would make you worthy?":
            gi "I don't know."
    pc "Gil, I can't answer {i}everything{/i} for you."
    $ SongA = 0
    $ SongB = 0
    menu:
        "You ruled the greatest city of Sumeria.":
            $ SongA += 1
        "You fought Humbaba and his seven terrors.":
            $ SongB += 1
    menu:
        "You're the son of a goddess and a king.":
            $ SongA += 1
        "You threw the Bull of Heaven back into heaven.":
            $ SongB += 1
    menu:
        "You battled to the end of the world.":
            $ SongB += 1
        "You brought peace back to Uruk after your journey.":
            $ SongA += 1
    gi "That was all a long time ago..."
    menu:
        "No time like the present.":
            gi "Time is what I have all too much of."
        "[[Slap him again.]":
            "Your hand smacks against the stone."
            "This probably hurts you a lot more than him."
            gi "I'll allow that this time."
        "Come on, what are you? Peasant, or King?":
            "Gilgamesh laughs and gives you a soft smile."
            gi "I'll allow that this once."
    if SongA > SongB:
        gi "All this talk of battle, you've inspired me. I may have a way to honor Enkidu."
    if SongA < SongB:
        gi "But you've reminded me what it means to be a ruler. I may have a way to honor Enkidu."
    gi "Return later, I must think."
    "Ea-nasir throws a sharp glance at Gilgamesh."
    gi "Please. If you would."
    $ beat_Gilgamesh += 1
    jump FreeRoam
label .beat4:
    gi "You came back, I wasn't sure you would."
    menu:
        "Of course I did.":
            pass
        "Yeah, you two aren't the easiest to be around.":
            pass
        "What do you need?":
            pass
    gi "It chafes my very soul to say it..."
    gi "But I need your help."
    e "He's been working up to saying that for hours."
    gi "Yes, {i}thank you{/i}, Nasir. I'm sure [they] needed to know that."
    gi "I want to sing for Enkidu."
    gi "That wherever he is, he may hear my words and know them true."
    pc "What sort of song did you have in mind?"
    #conditional on beat 3 choices
    if SongA < SongB:
        gi "A song of great battles, and greater victory."
    else:
        gi "A song from my heart, red as blood on a holy day."
    gi "What do you think?"
    $ SongChoiceLoop = 0
    label SongChoice:
        menu:
            "Something bombastic.":
                $ SongTheme = "battle"
                pc "Big and loud, like the stories about your battles."
                if SongA < SongB:
                    gi "Of course, a song to shake the earth!"
                else:
                    gi "Really? I hadn't considered that."
            "Something romantic.":
                $ SongTheme = "romance"
                pc "Just speak from your heart, that's always best."
                #conditionals
                if SongA > SongB:
                    gi "Yes, so he knows our hearts beat the same."
                else:
                    gi "Really? I hadn't considered that."
            "You know him better than me." if SongChoiceLoop == 0:
                $ SongChoiceLoop = 1
                gi "True, but I would value your judgement. Mine has been... clouded."
                jump SongChoice
        gi "A song of [SongTheme] then, you're sure?"
        menu:
            "Do it. Enkidu would love it.":
                pass
            "Hm, let me think.":
                jump SongChoice
    gi "That settles it then. Nasir, I have little right to ask, but will you translate for our friend?"
    e "Not because you're asking. I just don't want to see their blank stare."
    if SongTheme == "romance":
        "Gilgmesh settles into his song, his voice low and heavy like honey."
        gi "{i}Mu-ti-in cag-ja mu-lu ki-ig-ga-aj-ju- / Hi-li-zu aj-ze-ba-am lal-am ku-ku-da-{/i}"
        e "Bridegroom, dear to my heart- / Goodly is your beauty, honeysweet-"
        gi "Gi-ru cag-ja mu-lu ki-ig-ga-aj-ju- / Hi-li-zu aj-ze-ba-am lal-am ku-ku-da-"
        e "Lion, dear to my heart- / Goodly is your beauty, honeysweet."
        gi "Id na-an-ba-al-le id-zu ḫe-me-en-"
        e "Do not dig a canal, let me be your canal... Oh my."
        gi "A-šag na-an-ur-ru a-šag-zu ḫe-me-en-"
        e "Do not plough a field, plough--"
        "You never knew a clay tablet could blush, but Ea-nasir blushes deeply all the same."
        menu:
            "What's wrong?":
                pass
            "What is he singing?":
                pass
        e "He is... declaring his love."
        e "Directly."
        e "VERY directly."
        gi "X tur-tur-me aš-zu ḫe-am-"
        "Gilgmesh finishes his song. Just in time too, it looked like Ea-nasir was about to crack."
        gi "Ah... I can only pray Enkidu hears it."
        e "I would have prayed that {i}only{/i} he could hear it."
        gi "Ah, young Nasir. I could share many more songs of devotion."
        e "Eugh, I would sooner shatter."
    if SongTheme == "battle":
        #he-zu he-zu-am dnanna li-bi2-in-dug4-ga za-a-kam bi2-in-dug4-ga 
        #It must be known! It must be known! Nanna has not yet spoken out! He has said, "He is yours!" 
        gi "An-gin mah-a-za he-zu-am / ki-gin dajal-la-za he-zu-am!" 
        e "Be it known that you are lofty as the heavens! As broad as the earth!"
        #gi "ki bal gul-gul-lu-za he-zu-am "
        #e "Be it known that you destroy the rebel lands! "
        gi "kur-ra gu de2-e-za he-zu-am "
        e "Be it known that you roar in distant lands! That you crush heads!"
        gi "ur-gin ad gu-u-za he-zu-am "
        e "Be it known that you devour corpses like a dog! "
        menu:
            "He did {i}what?{/i}":
                e "It's metaphorical. I hope."
            "What does that mean?":
                e "...It was a different time."
        #gi "igi huc-a-za he-zu-am "
        #e "Be it known that your gaze is terrible!"
        #gi "igi huc-bi il-il-i-za he-zu-am "
        #e "Be it known that you lift your terrible gaze! "
        gi "igi gun-gun-na-za he-zu-am / u-ma gub-gub-bu-za he-zu-am "
        e "Be it known that you have flashing eyes! That you always stand triumphant!"
        "Gilgamesh finishes his song, the final note reverberating through the hall."
        gi "Ah... I can only pray Enkidu hears it."
        e "I'd be surprised if {i}anyone{/i} couldn't hear it."
    gi "And you, [pc_name], give me your thoughts. Was my song not as great as my legend?"
    menu:
        "It was beautiful.":
            pass
        "It was... beautiful?":
            pass
        "I've... never heard anything like it.":
            pass
        "I just wish I'd understood all of it.":
            pass
    gi "I'm glad you were here to listen."
    gi "And know that come this \"Grand Gala\" not a single guest will leave without a song in their hearts."
    pc "Just be nice. That's enough."
    e "Don't worry, I'll keep my eye on him."
    gi "Of course you will, who could look away?"
    "Well, he's still Gilgamesh, but as you walk away, you feel the oppressive atmosphere of the Anitquities Wing recede."
    $ beat_Gilgamesh += 1
    $ StoryCompletedTotal += 1
    jump FreeRoam

label .Outcome:
    if beat_Gilgamesh == 5:
        "Completed ending"
        if SongA > SongB:
            "Under the steady gaze of Gilgamesh, the Antiquities Wing is warm and welcoming."
            "Several vistors catch themselves humming--even singing--out of fashion love songs."
        else:
            "Under the fierce gaze of Gilgamesh, visitors leave the Antiquities Wing energized with a new fervor for life."
            "Several find themselves eager to take take up ill-advised hobbies such as mountain-climbing and novel-writing."
    elif beat_Gilgamesh > 1:
        "Visitors find themselves staring at the carving of Gilgamesh, looking for something that should be there, but isn't."
        "Eventually, they wander out of the Antiquities Wing feeling that they've just forgotten something."
    else:
        "Like still air in deep summer, the Antiquities Wing remains oppressive."
        "The few visitors that trickle in turn away in discomfort and disappointment."
        "The plaque next to Gilgamesh describes his epic deeds, but the statue hardly lives up to the legend."