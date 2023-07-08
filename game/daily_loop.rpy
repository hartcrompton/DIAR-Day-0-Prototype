#daily loop
#day begins
#admin calls, gives updates
#choice between cleaning and research, this might change since I dunno how valuable the research stuff is
#then the free roaming
#then when out of actions, nighthawks or leave
default daynumber = 1
default actions = 4

label day_start:
    if daynumber == 7:
        jump final_exhibit
    scene lobby bg morning
    $ actions = 4
    $ days_remaining = 7 - daynumber
    meta "It is day [daynumber]."
    show admin at right
    ad "Good morning! Hope you slept well, you have [days_remaining] days left before the exhibit."
    if daynumber == 1:
        ad "Since it's your first day, let me tell you what to do."
    elif daynumber == 2:
        ad "It's your second day!"
    elif daynumber == 3:
        ad "It's your third day!"
    elif daynumber == 4:
        ad "It's your fourth day!"
    elif daynumber == 5:
        ad "It's your fifth day!"
    elif daynumber == 6:
        ad "It's your sixth day!"
    elif daynumber == 7:
        ad "It's the last day!"

    ad "The museum's filthy, so you might want to clean."
    ad "But you don't know much, so maybe you want to research."

    menu:
        "I'll clean today.":
            jump daily_cleaning
        "I need to do some research.":
            jump daily_research

label daily_cleaning:
    #cleaning minigame goes here
    call minigamestart("cleaning")

label daily_research:
    call minigamestart("research")
    #research minigame goes here
    #admin asks who you want to research, gives you some garbage directions, try to find the book

label free_roam:
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
    jump day_end

label day_end:
    $ daynumber = daynumber - 1
    return