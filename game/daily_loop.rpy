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
image foyer_tod = ConditionSwitch(
        "actions == 4", "foyer morning",
        "actions == 3", "foyer noon",
        "actions == 2", "foyer evening",
        "actions == 1", "foyer night",
        "actions == 0", "foyer night")
image fineart_tod = ConditionSwitch(
        "actions == 4", "fineart morning",
        "actions == 3", "fineart noon",
        "actions == 2", "fineart evening",
        "actions == 1", "fineart night",
        "actions == 0", "fineart night")
image antiquities_tod = ConditionSwitch(
        "actions == 4", "antiquities morning",
        "actions == 3", "antiquities noon",
        "actions == 2", "antiquities evening",
        "actions == 1", "antiquities night",
        "actions == 0", "antiquities night")
image mixedmedia_tod = ConditionSwitch(
        "actions == 4", "mixedmedia morning",
        "actions == 3", "mixedmedia noon",
        "actions == 2", "mixedmedia evening",
        "actions == 1", "mixedmedia night",
        "actions == 0", "mixedmedia night")


#day transition countdown
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
    scene foyer_tod with fade
    $ days_remaining = 4 - DayNumber
    #meta "It is day [DayNumber]."
    #ad "Good morning! Hope you slept well, you have [days_remaining] days left before the exhibit."

    if DayNumber == 1:
        "Well, here it is, your first day on the job."
        show admin at AdminPortrait
        play music "music/Admin_ZY_02.wav" volume 0.6
        ad "Good morning, [pc_name]!"
        ad "Everything is {i}fine{/i}. Just wanted to remind you that the Grand Gala is in four days."
        ad "Good luck cleaning and organizing!"
        play sound "sfx/AdminHangup.wav"
        stop music fadeout 0.3
        hide admin
        "The Admin's right, this place is a mess."
    elif DayNumber == 2:
        show admin at AdminPortrait
        play music "music/Admin_ZY_02.wav" volume 0.6
        ad "[pc_name], hi! I actually went outside yesterday. Did you know grass and trees are, like, alive? Anyway, how are you?"
        ad "But I'm sure you've got LOTS to do, so I'll let you go."
        play sound "sfx/AdminHangup.wav"
        stop music fadeout 0.3
        hide admin
    elif DayNumber == 3:
        show admin at AdminPortrait
        play music "music/Admin_ZY_02.wav" volume 0.6
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
        play sound "sfx/AdminHangup.wav"
        stop music fadeout 0.3
        hide admin
    elif DayNumber == 4:
        show admin at AdminPortrait
        play music "music/Admin_ZY_02.wav" volume 0.6
        ad "Hi, [pc_name], I hope things are going well."
        ad "I'm sure you don't need me to remind you the Grand Gala is tomorrow."
        ad "Since this might be your last day, we'd better finish that performance review!"
        ad "How is your manager doing, on a scale of one to ten?"
        menu:
            "By manager, do you mean you?":
                pass
            "You're the best. No complaints.":
                pass
            "You're never here, and you never help.":
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
        play sound "sfx/AdminHangup.wav"
        stop music fadeout 0.3
        "The call drops."
        hide admin


    #ad "The museum's filthy, so you should probably clean."

    menu:
        "[[Clean the Antiquities wing]" if CleanAntiquities == 0:
            play music "music/Vending_ZV_01.wav" fadein 0.5 volume 0.2
            $ CleanAntiquities = 1
            $ CleaningRoom =  "antiquities"
            jump DailyCleaning
        "[[Clean the Fine Art wing]" if CleanFineArt == 0:
            play music "music/Vending_ZV_01.wav" fadein 0.5 volume 0.2
            $ CleanFineArt = 1
            $ CleaningRoom =  "fineart"
            jump DailyCleaning
        "[[Clean the Foyer]" if CleanFoyer == 0:
            play music "music/Vending_ZV_01.wav" fadein 0.5 volume 0.2
            $ CleanFoyer = 1
            $ CleaningRoom =  "foyer"
            jump DailyCleaning
        "[[Clean the Mixed Media wing]" if CleanMixedMedia == 0:
            play music "music/Vending_ZV_01.wav" fadein 0.5 volume 0.2
            $ CleanMixedMedia = 1
            $ CleaningRoom =  "mixedmedia"
            jump DailyCleaning

label DailyCleaning:
    play music "music/Vending_ZV_01.wav" fadein 0.5 volume 0.2
    scene foyer_tod
    call minigamestart_cleaning(CleaningRoom) from _call_minigamestart_cleaning
    
    #meta "Now you're free to roam around the museum"
    jump FreeRoam_FromCleaning

label FreeRoam:
    scene black with fade
    call advance_time from _call_advance_time
    scene foyer_tod with fade
label FreeRoam_FromCleaning:
    #scene foyer_tod with fade
    show screen gameUI
    if actions == 0:
        jump OutOfActions
    else:
        jump call_mapUI
#after that, go into the free roam
#pull up map
#
label OutOfActions:
    stop music fadeout 1.0
    play sfx2 "sfx/InteriorSound.wav" volume 0.4 fadein 0.5
    play music "music/Nighthawks_ZU_01.wav" fadein 0.4 volume 0.4
    show nighthawks at truecenter:
        zoom .65
        yoffset -125
    "Phew, another day over."
    #"On your way out, you overhear the Nighthawks."
    if DayNumber == 1:
        call conv_Nighthawks.beat1 from _call_conv_Nighthawks_beat1
    if DayNumber == 2:
        call conv_Nighthawks.beat2 from _call_conv_Nighthawks_beat2
    if DayNumber == 3:
        call conv_Nighthawks.beat3 from _call_conv_Nighthawks_beat3
    if DayNumber == 4:
        call conv_Nighthawks.beat4 from _call_conv_Nighthawks_beat4
    jump DayEnd

#depcreated, see OutOfActions and c_Nighthawks.rpy
label NighthawksDaily:
    play music "music/Nighthawks_ZU_01.wav" fadein 0.4 volume 0.4
    show nighthawks at truecenter:
        zoom .65
        yoffset -125
    call conv_Nighthawks.Arnolfini from _call_conv_Nighthawks_Arnolfini
    call conv_Nighthawks.Poster from _call_conv_Nighthawks_Poster
    call conv_Nighthawks.MonaLisa from _call_conv_Nighthawks_MonaLisa
    call conv_Nighthawks.Davids from _call_conv_Nighthawks_Davids
    call conv_Nighthawks.Gilgamesh from _call_conv_Nighthawks_Gilgamesh
    call conv_Nighthawks.SaintCatherine from _call_conv_Nighthawks_SaintCatherine
    call conv_Nighthawks.SoupAndSunflowers from _call_conv_Nighthawks_SoupAndSunflowers
    jump DayEnd

label DayEnd:    
    #meta "That's the end of day [DayNumber]"
    $ SSTimeout = 0
    $ MonaTimeout = 0
    $ GilgameshTimeout = 0
    $ SaintTimeout = 0
    $ PosterTimeout = 0
    $ ArnolfiniTimeout = 0
    $ DavidsTimeout = 0
    if DayNumber == 4:
        $ DayNumber = DayNumber + 1
        jump final_exhibit
    $ DayNumber = DayNumber + 1
    scene black with fade
    jump DayStart

#this needs to get refactored, TOD uses a conditionswitch now
label advance_time:
    #clear timeouts
    if SSTimeout >= 2:
        $ SSTimeout = 0
    elif SSTimeout == 1:
        $ SSTimeout += 1
    if MonaTimeout >= 2:
        $ MonaTimeout = 0
    elif MonaTimeout == 1:
        $ MonaTimeout += 1
    if GilgameshTimeout >= 2:
        $ GilgameshTimeout = 0
    elif GilgameshTimeout == 1:
        $ GilgameshTimeout += 1
    if SaintTimeout >= 2:
        $ SaintTimeout = 0
    elif SaintTimeout == 1:
        $ SaintTimeout += 1
    if PosterTimeout >= 2:
        $ PosterTimeout = 0
    elif PosterTimeout == 1:
        $ PosterTimeout += 1
    if ArnolfiniTimeout >= 2:
        $ ArnolfiniTimeout = 0
    elif ArnolfiniTimeout == 1:
        $ ArnolfiniTimeout += 1
    if DavidsTimeout >= 2:
        $ DavidsTimeout = 0
    elif DavidsTimeout == 1:
        $ DavidsTimeout += 1

    if InfiniteActions == 1:
        $ actions = 4
        return
    if actions > 0:
        $ actions = actions - 1
    #morning - can be deleted, actions will never equal 4 in this label
    #if actions == 4:
    #    image background1:
    #        "images/rooms/museum bg1.jpg"
    #        matrixcolor TintMatrix("#ede493")
    #    image background2:
    #        "images/rooms/museum bg2.jpg"
    #        matrixcolor TintMatrix("#ede493")
    ##noon
    #if actions == 3:
    #    image background1:
    #        "images/rooms/museum bg1.jpg"
    #    image background2:
    #        "images/rooms/museum bg2.jpg"
    ##evening
    #if actions == 2:
    #    image background1:
    #        "images/rooms/museum bg1.jpg"
    #        matrixcolor TintMatrix("#c27f02")
    #    image background2:
    #        "images/rooms/museum bg2.jpg"
    #        matrixcolor TintMatrix("#c27f02")
    ##night
    #if actions == 1:
    #    image background1:
    #        "images/rooms/museum bg1.jpg"
    #        matrixcolor TintMatrix("#546280")
    #    image background2:
    #        "images/rooms/museum bg2.jpg"
    #        matrixcolor TintMatrix("#546280")
    #if actions == 0:
    #    image background1:
    #        "images/rooms/museum bg1.jpg"
    #        matrixcolor TintMatrix("#546280")
    #    image background2:
    #        "images/rooms/museum bg2.jpg"
    #        matrixcolor TintMatrix("#546280")
    return