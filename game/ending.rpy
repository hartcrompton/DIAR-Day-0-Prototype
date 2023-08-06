#game ending
label final_exhibit:
    meta "It's the final exhibit today!"
    #call TotalDisposition
    #meta "Current disposition is: [d_Total]"
    #if d_Total >= 0:
    #    meta "That means the museum is saved!" 
    #if d_Total < 0:
    #    meta "That means the museum is closing :("
    #outcomes for individual characters go here

    #call MuseumOutcome
    return

label GoodEnd:
    #have each main character line with a conditional of the end flag
    return

label BadEnd:
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