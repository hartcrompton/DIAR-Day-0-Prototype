#game ending
default GoodLine1 = 0
default GoodLine2 = 0
default ClosedLine_ar = 0
default ClosedLine_d = 0
default ClosedLine_gi = 0
default ClosedLine_m = 0
default ClosedLine_st = 0
default ClosedLine_ss = 0
default ClosedLine_p = 0

label final_exhibit:
    meta "It's the final exhibit today!"
    call CalculateOutcome
    if ExhibitOutcome == 1:
        jump MuseumSaved
    if ExhibitOutcome == 0:
        jump MuseumClosed
    #call TotalDisposition
    #meta "Current disposition is: [d_Total]"
    #if d_Total >= 0:
    #    meta "That means the museum is saved!" 
    #if d_Total < 0:
    #    meta "That means the museum is closing :("
    #outcomes for individual characters go here

    #call MuseumOutcome
    return

label MuseumSaved:
    #have each main character line with a conditional of the end flag
    "You did it!"
    if beat_Arnolfini == 5:
        ar "Arnolfini complete line!"
        call conv_Arnolfini.Outcome
    if beat_Davids == 5:
        d "Arnolfini complete line!"
        call conv_Davids.Outcome
    if beat_Gilgamesh == 5:
        ar "Arnolfini complete line!"
        call conv_Gilgamesh.Outcome
    if beat_MonaLisa == 5:
        ar "Arnolfini complete line!"
        call conv_MonaLisa.Outcome
    if beat_SaintCatherine == 5:
        ar "Arnolfini complete line!"
        call conv_SaintCatherine.Outcome
    if beat_SoupAndSunflowers == 5:
        ar "Arnolfini complete line!"
        call conv_SoupAndSunflowers.Outcome
    if beat_Poster == 5:
        ar "Arnolfini complete line!"
        call conv_Poster.Outcome
    ad "Well, you did it."
    menu:
        ad "Think you'll stay on?"
        "Of course.":
            pass
        "Hell no.":
            pass
        
    return

label AllOutcomes:
    scene AllEndings
    call conv_Arnolfini.Outcome
    call conv_Davids.Outcome
    call conv_Gilgamesh.Outcome
    call conv_MonaLisa.Outcome
    call conv_SaintCatherine.Outcome
    call conv_SoupAndSunflowers.Outcome
    call conv_Poster.Outcome
    return

label MuseumClosed:
    "Whoopsie, museum is closed."
    #
    python:
        import random
        arr_BeatPairs = []
        arr_GoodLines = []
        arr_BeatPairs.append(("ar", beat_Arnolfini))
        arr_BeatPairs.append(("d", beat_Davids))
        arr_BeatPairs.append(("gi", beat_Gilgamesh))
        arr_BeatPairs.append(("m", beat_MonaLisa))
        arr_BeatPairs.append(("st", beat_SaintCatherine))
        arr_BeatPairs.append(("ss", beat_SoupAndSunflowers))
        arr_BeatPairs.append(("p", beat_Poster))
        BeatMax = 0
        BeatMax2 = 0
        #need to make this also select the minimums
        for a, b in arr_BeatPairs:
            if b > BeatMax:
                BeatMax = b
            if b < BeatMax and b > BeatMax2:
                BeatMax2 = b
        for a, b in arr_BeatPairs:
            if b == BeatMax:
                arr_GoodLines.append(a)
        LineCount = len(arr_GoodLines)
        if LineCount < 2:
            for a, b in arr_BeatPairs:
                if b == BeatMax2:
                    arr_GoodLines.append(a)
        #select lines 
        if LineCount >= 2:
            arr_GoodLinesSampled = random.sample(arr_GoodLines, 2)
            GoodLine1 = arr_GoodLinesSampled[0]
            GoodLine2 = arr_GoodLinesSampled[1]
            #while GoodLine1 == GoodLine2
                #GoodLine2 = random.choice(arr_Goodlines)
    
        
        #if BeatMax >= 2:
            #do something
        #if BeatMax < 2:
            #do something
    
    "First line is [GoodLine1]"
    "Second line is [GoodLine2]"
    menu:
        "Did it work?":
            return
            

        #then check GoodLines length. if 2 or greater, then good to go, if not, need to run through this again
            
    #Top two lines
    #Bottom two lines
    #Find maximum value
    #add maxes to new arr
    #if arr len > 2, then do random choice
    #if arr len < 2, then do it again
    #return two most complete characters
        #put each character and beat into array
        #append [Arnolfini, b_Arnolfini] etc.
        #two vars, Highest, SecondHighest
        #Iterate through list based on beat
            #if i > Highest
                # SecondHighest = Highest
                # Highest = i
            #if i > SecondHighest but =< Highest
            # SecondHighest = i
    #pick two random lowest
        #same as above, but opposite
    #using the selected characters, do the ending script
    return

#call this to determine good or b ad
label MuseumOutcome:
    #sum completion flags
    #if greater than 3 or 4 (TBD) then Good End
        #jump
    #else Bad End
        #jump
    return