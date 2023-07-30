#daily loop
#day begins
#admin calls, gives updates
#choice between cleaning and research, this might change since I dunno how valuable the research stuff is
#then the free roaming
#then when out of actions, nighthawks or leave
default DayNumber = 1
default actions = 4
default time_of_day = 1

image museum_morning:
    "images/rooms/museum bg1.jpg"
    matrixcolor TintMatrix("#ede493")
image museum_day:
    "images/rooms/museum bg1.jpg"
image museum_evening:
    "images/rooms/museum bg1.jpg"
    matrixcolor TintMatrix("#c27f02")
image museum_night:
    "images/rooms/museum bg1.jpg"
    matrixcolor TintMatrix("#546280")

image museumtod = ConditionSwitch(
        "actions == 4", "museum_morning",
        "actions == 3", "museum_day",
        "actions == 2", "museum_evening",
        "actions == 1", "museum_night",
        "actions == 0", "museum_night")


label day_start:
    $ actions = 4
    show screen gameUI
    scene museumtod
    $ days_remaining = 4 - DayNumber
    meta "It is day [DayNumber]."
    show admin at right
    ad "Good morning! Hope you slept well, you have [days_remaining] days left before the exhibit."
    ad "time of day change"
    if DayNumber == 1:
        ad "Since it's your first day, let me tell you what to do."
    elif DayNumber == 2:
        ad "It's your second day!"
    elif DayNumber == 3:
        ad "It's your third day!"
    elif DayNumber == 4:
        ad "It's the last day!"


    ad "The museum's filthy, so you might want to clean."
    ad "But you don't know much, so maybe you want to research."

    menu:
        "I'll clean today.":
            jump daily_cleaning

label daily_cleaning:
    #cleaning minigame goes here
    scene museum bg1
    call minigamestart_cleaning("cleaning")
    meta "Now you're free to roam around the museum"
    jump free_roam

label free_roam:
    scene mapbg
    show screen gameUI
    if actions == 0:
        jump out_of_actions
    else:
        jump call_mapUI
#after that, go into the free roam
#pull up map
#
label out_of_actions:
    pc "Wow I'm really tired, I must be out of ACTIONS for the day."
    menu:
        "Listen to the Nighthawks.":
            jump nighthawks_daily
        "Go Home":
            jump day_end

label nighthawks_daily:
    n "We'll say something about the player actions here."
    jump day_end

label day_end:    
    meta "That's the end of day [DayNumber]"
    if DayNumber == 4:
        jump final_exhibit
    $ DayNumber = DayNumber + 1
    jump day_start

label advance_time:
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