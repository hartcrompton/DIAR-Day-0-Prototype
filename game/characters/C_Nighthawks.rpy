#NighthawksMLines

#arnolfini
default b1_ArLines = 0
default b2_ArLines = 0
default b3_ArLines = 0
default b4_ArLines = 0

#davids
default b1_DLines = 0
default b2_DLines = 0
default b3_DLines = 0
default b4_DLines = 0

#gilgamesh
default b1_GiLines = 0
default b2_GiLines = 0
default b3_GiLines = 0
default b4_GiLines = 0

#mona lisa
default b1_MLines = 0
default b2_MLines = 0
default b3_MLines = 0
default b4_MLines = 0

#poster
default b1_PLines = 0
default b2_PLines = 0
default b3_PLines = 0
default b4_PLines = 0

#saint
default b1_StLines = 0
default b2_StLines = 0
default b3_StLines = 0
default b4_StLines = 0

#soup and sunflowers
default b1_SsLines = 0
default b2_SsLines = 0
default b3_SsLines = 0
default b4_SsLines = 0

label conv_Nighthawks:
    scene foyer bg
    show nighthawks at truecenter
    #p "You're talking to me, the Nighthawks! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Nighthawks
        "Bye":
            p "See ya"
            jump FreeRoam

label .Arnolfini:
    if (beat_Arnolfini == 2) and (b1_ArLines == 0):
        $ b1_ArLines = 1
        n1 "The Arnolfinis are fighting. Again."
        n2 "You’d think they’d eventually run out of things to argue about, but no…honestly, I’m impressed by their mutual devotion to spite."
        n3 "Someone should get them marital counseling. Wait – are they even –"
        n4 "Honestly, who even knows? But enough about that – what else is going on?"
    if (beat_Arnolfini == 3) and (b2_ArLines == 0):
        $ b2_ArLines = 1
        n1 "The Arnolfinis have implored our dear curator to help them sort out their differences. And [they] ARE helping – one of them, at least."
        n2 "Oh, drama! Whose side did the curator take?"
        if if ar_b2_c1 == "a":
            n3 "Missus Arnolfini, she of the many names."
        if ar_b2_c1 == "b":
            n3 "Giovanni, the man himself."
        if ar_b2_c1 == "c":
            n3 "You’ll never guess it – the dog! Who apparently can speak!"
        n4 "Well, this ought to be interesting…let’s see what comes next for the unhappy couple, eh? Anything else interesting happen today?"
    if (beat_Arnolfini == 4) and (b3_ArLines == 0):
        $ b3_ArLines = 1
        n1 "The Arnolfinis have reached a…well, I don’t know if resolution is the right term. An impasse with each other? Let’s go with that."
        n2 "Whatever it is, I’m just glad they’re not yelling at each other. But how exactly did this even happen?"
        n3 "Our ingenious curator used the oldest trick in the conflict resolution handbook. [they!c] appealed to the Arnolfinis’ vanity."
        n4 "Ah, truly…nothing solves issues faster than money. What else?"
    if (beat_Arnolfini == 5) and (b4_ArLines == 0):
        $ b4_ArLines = 1
        if ar_b4_c2 == "a":
            n1 "The curator helped the Arnolfinis define their relationship as husband and wife."
        if ar_b4_c2 == "b":
            n1 "The curator helped the Arnolfinis define their relationship as cousins."
        if ar_b4_c2 == "c":
            n1 "The curator helped the Arnolfinis define their relationship as both spouses AND cousins – which I would rather not think about too much."
        n2 "Whatever their relationship – let’s just hope they stay amicable with each other."
        n3 "Wait. If they’re not fighting…you realize there is nothing stopping the Arnolfinis from trying to make friends with us again, right?"
        n4 "Oh, dear God. Let’s not think about that terrifying possibility. What else is going on?"
    return

label .Davids:
    if (beat_Davids == 2) and (b1_DLines == 0):
        $ b1_DLines = 1
        n1 "Well, I heard the curator spoke with David."
        n2 "That’s not all. They ALSO spoke with David."
        n3 "Oh, and don’t forget, they ALSO ALSO spoke with –"
        n4 "Yes, yes – you’re all very funny. Let’s move on."
    if (beat_Davids == 3) and (b2_DLines == 0):
        $ b2_DLines = 1
        n1 "Our dear curator made a CRITICAL mistake – they called [b2_DefinitiveDave] the REAL David."
        n2 "Oof. Rookie mistake."
        n3 "Bets on which of the other two Davids is going to ‘accidentally’ tip over and crush [pc_name] flat?"
        n4 "No betting in the diner! We’ve been over this…what else?"
    if (beat_Davids == 4) and (b3_DLines == 0):
        $ b3_DLines = 1
        #truth
        if BibleResearched == 1:
            n1 "Stop your sinning, everyone – I hear SOMEONE cracked open the ol’ Bible today."
            n2 "Dear old King James. Or was it the flashy New International?"
            n3 "Does it even matter?"
            n4 "More than you might think. But enough about things that should’ve waited for Sunday – what else?"
        #lie
        if BibleResearched == -1:
            n1 "Stop your sinning, everyone – I hear SOMEONE cracked open the ol’ Bible today."
            n2 "Did you? See, I heard different. QUITE different."
            n3 "I heard differently as well. ‘Memorized’? My, my, my…"
            n4 "Yes, this should be interesting…what else?"
        #annoyed
        if BibleResearched == 0:
            n1 "Stop your sinning, everyone – I hear SOMEONE cracked open the ol’ Bible today."
            n2 "Who cares about that? The Davids got put into separate corners today! Like kindergartners!"
            n3 "Seems…unproductive?"
            n4 "Only time will tell. What else is going on?"
    if (beat_Davids == 5) and (b4_DLines == 0):
        $ b4_DLines = 1
        if BibleResearched == 0:
            n1 "Is there anything else to talk about besides the Davids literally destroying themselves?"
            n2 "I almost feel bad having gossiped about them now. Are we supposed to…hold a funeral or something?"
            n3 "Yes, with all our plentiful shovels and graves. What do you think?"
            n4 "Okay, okay, enough sarcasm. Let’s brighten the mood – what else is happening?"
        if BibleResearched == -1:
            n1 "Ding, ding, ding! We have a winner in the contest of the definitive David!"
            n2 "God, finally. Who is it? My bet’s on the one with the biggest –"
            if DefinitiveDave == "dm":
                n3 "It’s Michelangelo's David!"
            if DefinitiveDave == "dd":
                n3 "It’s Donatello's David!"
            if DefinitiveDave == "db":
                n3 "It’s Bernini's David!"
            n4 "Hm. Not who I would have chosen, but I respect the decision. What else happened?"
        if BibleResearched == -1:
            n1 "Ding, ding, ding! We have a winner in the contest of the definitive David!"
            n2 "God, finally. Who is it? My bet’s on the one with the biggest –"
            n3 "It’s all three of them!"
            n4 "Now, isn’t that a surprise? I guess the real David is the one we found along the way. What else?” "
    return

label .Gilgamesh:
    return

label .MonaLisa:
    if (beat_MonaLisa == 2) and (b1_MLines == 0):
        $ b1_MLines = 1
        n1 "Our curator had the pleasure of speaking with the most famous face ever painted."
        n2 "Ahh, Mona Lisa, so mean, so cold-hearted…I ADORE her."
        n3 "Same. To have the opportunity to talk shit with La Gioconda…truly the highest of honors."
        n4 "Be that as it may…she still can’t sit with us. What else?"
    if (beat_MonaLisa == 3) and (b2_MLines == 0):
        $ b2_MLines = 1
        n1 "Did you hear? Mona Lisa wants to return home."
        n2 "Get some new news – Mona’s wanted that for centuries. What makes today any different?"
        n3 "Because NOW she finally has someone to listen to her."
        n4 "Well…we must wait and see if [pc_name] truly changes anything. What else?"
    if (beat_MonaLisa == 4) and (b3_MLines == 0):
        $ b3_MLines = 1
        n1 "Mona convinced the curator to restore her eyes in the office."
        n2 "Ah, to be able to see so freely…I mean, we can see Chicago, of course. But imagine having the eyes of a Mona Lisa?"
        n3 "I shudder to think what she’ll do with this restored power."
        n4 "Now, now, I’m sure [pc_name] will convince her to use it for good…probably. What else?"
    if (beat_MonaLisa == 5) and (b4_MLines == 0):
        $ b4_MLines = 1
        #alone
        if MonaOutcome == 0:
            n1 "The curator has convinced Mona to remain, it seems."
            n2 "Not an easy feat! How did [they] accomplish that?"
            n3 "Let’s just say there’s a little bit of bribery going on. A little tit for tat."
            n4 "Who would have thought our dear [pc_name] so ruthless? How far {0}he's{/0}{1}she's{/1}{2}they've{/2} come…what else?"
        #kitsch
        if MonaOutcome == 1:
            n1 "Just in time for the exhibit – the Many Monas, now on display!"
            n2 "Nice pitch. But do we like displaying all the Mona Lisas together, or do we find it…gaudy?"
            n3 "Can’t it be both? After all, what’s life without a little camp?"
            n4 "Boring – infinitely more boring. And THIS certainly isn’t. Now, what else happened today?"
        #heist
        if MonaOutcome == 2:
            n1 "Oh, just a daring heist…a scandal to last generations. Nothing terribly exciting."
            n2 "I’ll give our curator this, they certainly take RISKS. But will getting rid of the Mona Lisa pay off – or has this museum just lost its crown jewel?"
            n3 "We won’t have to wait long. The gala  is just around the corner..."
            n4 "No, now, don’t jump to the end so quickly! What else is going on?"

    return

label .Poster:
    if (beat_Poster == 2) and (b1_PLines == 0):
        $ b1_Plines = 1
        n1 "Our dear curator spent a lot of time in the office today. Shirking duties, perhaps?"
        n2 "I can’t think of any other reason to be in there. Except that –"
        n3 "Oh, don’t mention THEM. ‘Motivational art’? Sure. Motivate me to leave the museum."
        n4 "Enough gatekeeping. It’s not attractive. What else is happening?"
    if (beat_Poster == 3) and (b2_PLines == 0):
        $ b2_Plines = 1
        n1 "More time in the office for dear [pc_name]. Getting ‘motivated’."
        n2 "Honestly. All this fine, priceless art, and [they] choose[s] to spend [their] time chatting with a dollar store poster?"
        n3 "You’re going to eat those elitist words of yours. The corgi has a FLAG now."
        n4 "God, the world will never be the same. What else?"
    if (beat_Poster == 4) and (b3_PLines == 0):
        $ b3_Plines = 1
        n1 "I mean, there IS the fact [pc_name] has chosen to –"
        n2 "Ugh, I beg you, don’t say it again. It was hard enough to hear the first time that our illustrious, underqualified curator is putting a POSTER out on display."
        n3 "Well, I for one support the idea. Things were getting a little stuffy around here."
        n4 "We’ll see. What else?"
    if (beat_Poster == 5) and (b4_PLines == 0):
        $ b4_Plines = 1
        n1 "Well, I can’t help but feel quite MOTIVATED for some reason…"
        n2 "You joke, but I think displaying the motivational poster in the museum WORKS. I can’t tell if it’s the second flag, or –"
        n3 "No, no. It’s the…SINCERITY of it all. Sometimes it’s good to be reminded that not everything needs to be buried under three layers of jaded pretension."
        n4 "Who would have thought – self-growth, right here in the diner! What other surprises do we have in store for today?"
    return

label .SaintCatherine:
    if (beat_SaintCatherine == 2) and (b1_StLines == 0):
        $ b1_StLines = 1
        n1 "Well, the curator met the broken woman."
        n2 "Don’t be cruel. Saint Catherine deserves better than being called broken."
        n3 "But is it not accurate? The stained glass needs to be repaired – in more ways than one."
        n4 "Yes – and is that not what a curator is for? Let’s see what changes…and in what way. Anything else going on?"
    if (beat_SaintCatherine == 3) and (b2_StLines == 0):
        $ b2_StLines = 1
        n1 "Repairs are underway for St. Catherine. Or, rather – repairs have been planned."
        n2 "Good! But there’s multiple ways to repair a crack...which way is our dear curator leaning?"
        n3 "I’m not sure yet. Whatever it is, hopefully it suits the subject in question."
        n4 "And who is the subject, truly? That’s the real question…but enough about that for now. What else is going on?"
    if (beat_SaintCatherine == 4) and (b3_StLines == 0):
        $ b3_StLines = 1
        n1 "Identity crisis in Alexandria! Who is the REAL Saint Catherine? More at eleven."
        n2 "You’re not funny. But…the question merits examination. Who IS Saint Catherine?"
        n3 "I don’t think that’s a question we can answer. If there’s anyone who COULD, it’d be –"
        n4 "Careful now. We wouldn’t want to influence anyone eavesdropping…what else?"
    if (beat_SaintCatherine == 5) and (b4_StLines == 0):
        $ b4_StLines = 1
        if SaintPersonality == 1:
            if st_glass == 0:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in a rather…unorthodox material."
                n3 "Catherine seems happy enough. Plastic is not what I would have thought of, but perhaps guests might see it as more…approachable?"
                n4 "We won’t know for certain until the gala. Anything else?"
            if st_glass == 1:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in glass, as expected."
                n3 "Catherine seems…conflicted. Will she rise to the mantle she’s only recently questioned?"
                n4 "We won’t know for certain until the gala. Anything else?"
        if SaintPersonality == 0:
            if st_glass == 0:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in glass, as expected."
                n3 "Catherine seems happy enough. And the end result is exactly as expected – but is that a GOOD thing?"
                n4 "We won’t know for certain until the gala. Anything else?"
            if st_glass == 1:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in a rather…unorthodox material."
                n3 "Catherine seems…conflicted. And I get it – a holy woman, rendered in plastic? I can’t tell if it’s utterly daring, or utterly insane."
                n4 "We won’t know for certain until the gala. Anything else?"
    return

label .SoupAndSunflowers:
    return



    if beat_ > 1:
        return
    if beat_ > 2:
        return
    if beat_ > 3:
        return
    if beat_ > 4:
        return
    return