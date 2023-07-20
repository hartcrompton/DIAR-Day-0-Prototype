#daily loop
#day begins
#admin calls, gives updates
#choice between cleaning and research, this might change since I dunno how valuable the research stuff is
#then the free roaming
#then when out of actions, nighthawks or leave
default DayNumber = 1
default actions = 4

label day_start:
    show screen gameUI
    scene museum bg1
    $ actions = 4
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

label daily_research:
    scene bg research
    call minigamestart("research")
    meta "Now you're free to roam around the museum"
    jump free_roam
    #research minigame goes here
    #admin asks who you want to research, gives you some garbage directions, try to find the book

label free_roam:
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