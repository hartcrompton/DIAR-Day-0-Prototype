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
default CleanAntiquities = 0
default CleanFineArt = 0
default CleanFoyer = 0
default CleanMixedMedia = 0
default CleaningRoom = "NONE"

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
#foyer
image museumtod = ConditionSwitch(
        "actions == 4", "museum_morning",
        "actions == 3", "museum_day",
        "actions == 2", "museum_evening",
        "actions == 1", "museum_night",
        "actions == 0", "museum_night")
image day_countdown = ConditionSwitch(
        "DayNumber == 1", "day countdown 1",
        "DayNumber == 2", "day countdown 2",
        "DayNumber == 3", "day countdown 3",
        "DayNumber == 4", "day countdown 4",
        "DayNumber == 5", "day countdown 5")
#antiquities
#fineart
#mixedmedia
#office - this will just be a tint matrix

label DayStart:
    scene black with fade
    show day_countdown at truecenter with fade
    $ renpy.pause(3.0)
    #"Day [DayNumber]"
    $ actions = 4
    show screen gameUI
    scene museumtod with fade
    $ days_remaining = 4 - DayNumber
    #meta "It is day [DayNumber]."
    #ad "Good morning! Hope you slept well, you have [days_remaining] days left before the exhibit."

    if DayNumber == 1:
        "Well, here it is, your first day on the job."
        show admin at AdminPortrait
        ad "Good morning, [pc_name]!"
        ad "Everything is {i}fine{/i}. Just wanted to remind you that the Grand Gala is in four days."
        ad "Good luck cleaning and organizing!"
        hide admin
        "The Admin's right, this place is a mess."
    elif DayNumber == 2:
        show admin at AdminPortrait
        ad "[pc_name], hi! I actually went outside yesterday. Did you know grass and trees are, like, alive? Anyway, how are you?"
        ad "But I'm sure you've got LOTS to do, so I'll let you go."
        hide admin
    elif DayNumber == 3:
        show admin at AdminPortrait
        ad "Hello [pc_name], it's time for your performance review!"
        ad "How do you like working at the museum?"
        menu:
            "Did you know the art can talk?":
                pass
            "Everything is {i}very{/i} normal.":
                pass
        ad "Great to hear!"
        "You doubt the Admin heard you at all."
        ad "Let's put a pin in this, talk tomorrow!"
        hide admin
    elif DayNumber == 4:
        show admin at AdminPortrait
        ad "Hi, [pc_name], I hope things are going well."
        ad "I'm sure you don't need me to remind you the Grand Gala is tomorrow."
        ad "Since this might be your last day, we'd better finish that performance review!"
        ad "How is your manager doing, on a scale of one to ten?"
        menu:
            "By manager, do you mean you?":
                pass
            "You're the best. No complaints":
                pass
            "You're never here, and you never help":
                pass
        ad "The form just asks for a number."
        menu:
            "I dunno... seven?":
                pass
            "Nine-hundred and twelve.":
                pass
            "One. The loneliest number.":
                pass
        ad "Perfect, let me write that down."
        menu:
            "I get the sense you're not listening to me.":
                pass
            "Is everything ok?":
                pass
            "Was there a point to all this?":
                pass
        ad "What? I don't -- well, now that you mention it..."
        ad "I love the museum, and I love our community! But I keep hearing about this thing called flow..."
        ad "Where everything goes smoothly, and you're filled with a sense of purpose..."
        ad "Sometimes I wonder what I'm doing here."
        menu:
            "You're a crucial part of the team. The museum needs you.":
                ad "Aw, thanks [pc_name]. You're the best! Another call coming in, talk soon!"
            "Have you ever wanted to, uh, take a class? Or something?":
                ad "A class? A class! Yes, I could... I guess I could do anything! Thanks, [pc_name]. Another call, please hold!"
        "The call drops."
        hide admin


    #ad "The museum's filthy, so you should probably clean."

    menu:
        "[[Clean the Antiquities wing]" if CleanAntiquities == 0:
            $ CleanAntiquities = 1
            $ CleaningRoom =  "antiquities"
            jump DailyCleaning
        "[[Clean the Fine Art wing]" if CleanFineArt == 0:
            $ CleanFineArt = 1
            $ CleaningRoom =  "fineart"
            jump DailyCleaning
        "[[Clean the Foyer]" if CleanFoyer == 0:
            $ CleanFoyer = 1
            $ CleaningRoom =  "foyer"
            jump DailyCleaning
        "[[Clean the Mixed Media wing]" if CleanMixedMedia == 0:
            $ CleanMixedMedia = 1
            $ CleaningRoom =  "mixedmedia"
            jump DailyCleaning

label DailyCleaning:
    scene museumtod
    call minigamestart_cleaning(CleaningRoom) from _call_minigamestart_cleaning
    
    #meta "Now you're free to roam around the museum"
    jump FreeRoam

label FreeRoam:
    scene museumtod with fade
    show screen gameUI
    if actions == 0:
        jump OutOfActions
    else:
        jump call_mapUI
#after that, go into the free roam
#pull up map
#
label OutOfActions:
    "Phew, another day over."
    "On your way out, you overhear the Nighthawks."
    menu:
        "Listen in.":
            jump NighthawksDaily
        "Go Home":
            jump DayEnd

label NighthawksDaily:
    show nighthawks at truecenter:
        zoom .65
        yoffset -125
    call conv_Nighthawks.Poster from _call_conv_Nighthawks_Poster
    call conv_Nighthawks.MonaLisa from _call_conv_Nighthawks_MonaLisa
    call conv_Nighthawks.Davids from _call_conv_Nighthawks_Davids
    call conv_Nighthawks.Gilgamesh from _call_conv_Nighthawks_Gilgamesh
    call conv_Nighthawks.SaintCatherine from _call_conv_Nighthawks_SaintCatherine
    call conv_Nighthawks.SoupAndSunflowers from _call_conv_Nighthawks_SoupAndSunflowers
    call conv_Nighthawks.Arnolfini from _call_conv_Nighthawks_Arnolfini
    jump DayEnd

label DayEnd:    
    #meta "That's the end of day [DayNumber]"
    if DayNumber == 4:
        $ DayNumber = DayNumber + 1
        jump final_exhibit
    $ DayNumber = DayNumber + 1
    scene black with fade
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