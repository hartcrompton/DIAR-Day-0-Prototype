#daily loop
#day begins
#admin calls, gives updates
#choice between cleaning and research, this might change since I dunno how valuable the research stuff is
#then the free roaming
#then when out of actions, nighthawks or leave
default DayNumber = 1
default actions = 4
default time_of_day = 1
default InfiniteActions = 0

#the different times of day are just recolored versions of the same background
image museum_morning:
    "images/rooms/foyer bg.jpg"
    matrixcolor TintMatrix("#ede493")
image museum_day:
    "images/rooms/foyer bg.jpg"
image museum_evening:
    "images/rooms/foyer bg.jpg"
    matrixcolor TintMatrix("#c27f02")
image museum_night:
    "images/rooms/foyer bg.jpg"
    matrixcolor TintMatrix("#546280")

#this image automatically changes appearance based on actions
image museumtod = ConditionSwitch(
        "actions == 4", "museum_morning",
        "actions == 3", "museum_day",
        "actions == 2", "museum_evening",
        "actions == 1", "museum_night",
        "actions == 0", "museum_night")

label DayStart:
    $ actions = 4
    show screen gameUI
    scene museumtod
    $ days_remaining = 4 - DayNumber
    meta "It is day [DayNumber]."
    show admin at right
    ad "Good morning! Hope you slept well, you have [days_remaining] days left before the exhibit."

    if DayNumber == 1:
        ad "Since it's your first day, let me tell you what to do."
    elif DayNumber == 2:
        ad "It's your second day!"
    elif DayNumber == 3:
        ad "It's your third day!"
    elif DayNumber == 4:
        ad "It's the last day!"

    ad "The museum's filthy, so you should probably clean."

    menu:
        "Yeah OK.":
            jump DailyCleaning

label DailyCleaning:
    scene museum bg1
    call minigamestart_cleaning("cleaning") from _call_minigamestart_cleaning
    
    meta "Now you're free to roam around the museum"
    jump FreeRoam

label FreeRoam:
    scene mapbg
    show screen gameUI
    if actions == 0:
        jump OutOfActions
    else:
        jump call_mapUI
#after that, go into the free roam
#pull up map
#
label OutOfActions:
    pc "Wow I'm really tired, I must be out of ACTIONS for the day."
    menu:
        "Listen to the Nighthawks.":
            jump NighthawksDaily
        "Go Home":
            jump DayEnd

label NighthawksDaily:
    n "We'll say something about the player actions here."
    jump DayEnd

label DayEnd:    
    meta "That's the end of day [DayNumber]"
    if DayNumber == 4:
        jump final_exhibit
    $ DayNumber = DayNumber + 1
    jump DayStart

#this needs to get refactored, TOD uses a conditionswitch now
label advance_time:
    if InfiniteActions == 1:
        $ actions = 4
        return
    if actions > 0:
        $ actions = actions - 1
    #morning - can be deleted, actions will never equal 4 in this label
    if actions == 4:
        image background1:
            "images/rooms/museum bg1.jpg"
            matrixcolor TintMatrix("#ede493")
        image background2:
            "images/rooms/museum bg2.jpg"
            matrixcolor TintMatrix("#ede493")
    #noon
    if actions == 3:
        image background1:
            "images/rooms/museum bg1.jpg"
        image background2:
            "images/rooms/museum bg2.jpg"
    #evening
    if actions == 2:
        image background1:
            "images/rooms/museum bg1.jpg"
            matrixcolor TintMatrix("#c27f02")
        image background2:
            "images/rooms/museum bg2.jpg"
            matrixcolor TintMatrix("#c27f02")
    #night
    if actions == 1:
        image background1:
            "images/rooms/museum bg1.jpg"
            matrixcolor TintMatrix("#546280")
        image background2:
            "images/rooms/museum bg2.jpg"
            matrixcolor TintMatrix("#546280")
    if actions == 0:
        image background1:
            "images/rooms/museum bg1.jpg"
            matrixcolor TintMatrix("#546280")
        image background2:
            "images/rooms/museum bg2.jpg"
            matrixcolor TintMatrix("#546280")
    return