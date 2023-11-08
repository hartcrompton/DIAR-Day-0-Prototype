#map
default TokenHovered = "NONE"
image TimeOfDayBG = ConditionSwitch(
    "DayNumber == 1", "tod bg day1",
    "DayNumber == 2", "tod bg day2",
    "DayNumber == 3", "tod bg day3",
    "DayNumber == 4", "tod bg day4")

image TimeOfDayOverlay = ConditionSwitch(
    "actions == 4", "tod morning",
    "actions == 3", "tod noon",
    "actions == 2", "tod evening",
    "actions == 1", "tod night",
    "actions == 0", "tod night")

image MapOverlay = "UI/Map/map bg.png"

label call_mapUI:
    #scene black with fade
    $ TokenHovered = "NONE"
    call screen MapUI
    #show screen gameUI

image SaintTokenSwitch = ConditionSwitch(
    "SaintHair == 0", "Characters/SideImages/side_saintcatherine.png",
    "SaintHair == 1", "Characters/SideImages/side_saintcatherine_b.png")
image SaintTimeoutToken:
    "SaintTokenSwitch"
    matrixcolor SaturationMatrix(0)
image SaintToken = ConditionSwitch(
    "SaintTimeout == 0", "SaintTokenSwitch",
    "SaintTimeout >= 1", "SaintTimeoutToken")

image GilgameshTimeoutToken:
    "Characters/SideImages/side_gilgamesh.png"
    matrixcolor SaturationMatrix(0)
image GilgameshToken = ConditionSwitch(
    "GilgameshTimeout == 0", "Characters/SideImages/side_gilgamesh.png",
    "GilgameshTimeout >= 1", "GilgameshTimeoutToken")

image CorgiTimeoutToken:
    "Characters/SideImages/side_poster.png"
    matrixcolor SaturationMatrix(0)
image CorgiToken = ConditionSwitch(
    "PosterTimeout == 0", "Characters/SideImages/side_poster.png",
    "PosterTimeout >= 1", "CorgiTimeoutToken")

image SSTimeoutToken:
    "Characters/SideImages/side_soupandsunflowers.png"
    matrixcolor SaturationMatrix(0)
image SSToken = ConditionSwitch(
    "SSTimeout == 0", "Characters/SideImages/side_soupandsunflowers.png",
    "SSTimeout >= 1", "SSTimeoutToken")

image MonaTimeoutToken:
    "Characters/SideImages/side_mona.png"
    matrixcolor SaturationMatrix(0)
image MonaToken = ConditionSwitch(
    "MonaTimeout == 0", "Characters/SideImages/side_mona.png",
    "MonaTimeout >= 1", "MonaTimeoutToken")

image DavidsTimeoutToken:
    "Characters/SideImages/side_davids.png"
    matrixcolor TintMatrix("#6b6b6b")
image DavidsToken = ConditionSwitch(
    "DavidsTimeout == 0", "Characters/SideImages/side_davids.png",
    "DavidsTimeout >= 1", "DavidsTimeoutToken")

image ArnolfiniTimeoutToken:
    "Characters/SideImages/side_arnolfinimap.png"
    matrixcolor SaturationMatrix(0)
image ArnolfiniToken = ConditionSwitch(
    "ArnolfiniTimeout == 0", "Characters/SideImages/side_arnolfinimap.png",
    "ArnolfiniTimeout >= 1", "ArnolfiniTimeoutToken")

image BeatProgressEmpty = "map/BeatProgressPips.png"
image BeatProgressFull = "map/BeatProgressPipsFilled.png"

transform TokenHover:
    ease .15 yoffset -30

transform TokenUnhover:
    ease .15 yoffset 0

transform PipHover:
    xoffset 24
    yoffset 85
    ease .1 alpha 1.0

transform PipUnhover:
    xoffset 24
    yoffset 85
    ease .1 alpha 0.0

screen MapUI:
# window at AlphaIn:
#     xminimum 1920
#     xmaximum 1920
#     yminimum 1080
#     ymaximum 1080
    #add "newmap/museum_map.jpg"
    #textbutton "Stats":
    #    xalign 1.0
    #    yalign 0.0
    #    xoffset -30
    #    yoffset 30
    #    action ShowMenu("DispositionMenu")
    #textbutton "Day [DayNumber]":
    #    xalign 0.0
    #    yalign 0.0
    #    xoffset 30
    #    yoffset 30
    #textbutton "Remaining Actions: [actions]":
    #    xalign 0.0
    #    yalign 0.0
    #    xoffset 30
    #    yoffset 60
    imagemap:
        xalign 0.5
        yalign 0.5
        ground "MapOverlay"
        #hover "newmap/museum_map_hover.jpg"

        #glimmer
        #hotspot (30, 18, 163, 321) action Jump("conv_Admin")
        #sunflowers
        #hotspot (217, 12,143,266) action Jump("conv_SoupAndSunflowers")
        #saintcatherine
        hotspot (345,650,116,116) action [If((beat_SaintCatherine < 5) and (SaintTimeout == 0), Jump("conv_SaintCatherine"), NullAction())] hovered [SetVariable("TokenHovered", "st")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (582,580,116,116) action [If((beat_SoupAndSunflowers < 5) and (SSTimeout == 0), Jump("conv_SoupAndSunflowers"), NullAction())] hovered [SetVariable("TokenHovered", "ss")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (856,518,116,116) action [If((beat_Davids < 5) and (DavidsTimeout == 0), Jump("conv_Davids"), NullAction())] hovered [SetVariable("TokenHovered", "d")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (495,408,116,116) action [If((beat_Gilgamesh < 5) and (GilgameshTimeout == 0), Jump("conv_Gilgamesh"), NullAction())] hovered [SetVariable("TokenHovered", "gi")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (710,405,116,116) action [If((beat_Arnolfini < 5) and (ArnolfiniTimeout == 0), Jump("conv_Arnolfini"), NullAction())] hovered [SetVariable("TokenHovered", "ar")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (582,224,116,116) action [If((beat_MonaLisa < 5) and (MonaTimeout == 0), Jump("conv_MonaLisa"), NullAction())] hovered [SetVariable("TokenHovered", "m")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (301,251,116,116) action [If((beat_Poster < 5) and (PosterTimeout == 0), Jump("conv_Poster"), NullAction())] hovered [SetVariable("TokenHovered", "p")] unhovered [SetVariable("TokenHovered", "NONE")]
        #gilgamesh
        #hotspot (544,174,144,288) action Jump("conv_Gilgamesh")
        #sue
        #hotspot (707,190,169,331) action Jump("conv_Sue")
        #EaNasir
        #hotspot (948,158,116,263) action Jump("conv_EaNasir")
        #Theodore
        #hotspot (1106,58,144,283) action Jump("conv_Theodore")
        #MonaLisa
        #hotspot (1311,109,135,251) action Jump("conv_MonaLisa")
        #Arnolfini
        #hotspot (1456,278,137,255) action Jump("conv_Arnolfini")
        #Nighthawks
        #hotspot (749,584,205,154) action Jump("conv_Nighthawks")
        #VendingMachine
        #hotspot (1028,622,109,205) action Jump("conv_VendingMachine")
        #Davids
        #hotspot (1185,608,248,222) action Jump("conv_Davids")
        #Poster
        #hotspot (1443,550,277,245) action Jump("conv_Poster")
        #Admin
        #hotspot (1732,595,151,283) action Jump("conv_Admin")
    frame:
        xalign .15
        yalign .85
        xoffset 10
        yoffset -10
        xminimum 300
        xmaximum 300
        yminimum 300
        ymaximum 300
        background None
        #hbox:
        #    box_wrap True
        #    spacing 40
        #    vbox:
        #        spacing 10
        #        text "Day [DayNumber] / 4":
        #            size 40
        #        if InfiniteActions == 0:
        #            text "Morning":
        #                size 20
        #                if actions == 4:
        #                    size 40
        #            text "Noon":
        #                size 20
        #                if actions == 3:
        #                    size 40
        #            text "Evening":
        #                size 20
        #                if actions == 2:
        #                    size 40
        #            text "Night":
        #                size 20
        #                if actions == 1:
        #                    size 40
        #        if InfiniteActions == 1:
        #            text "INFINITE ACTIONS":
        #                size 20
        add "TimeOfDayBG":
            zoom .4
        add "TimeOfDayOverlay":
            zoom .4
            #yalign 1
    #textbutton "Stats":
    #    xalign 1.0
    #    yalign 0.0
    #    xoffset -30
    #    yoffset 30
    #    action ShowMenu("DispositionMenu")
    
    frame:
        xalign 0.5
        yalign 0.5
        background None
        xminimum 1175
        xmaximum 1175
        yminimum 988
        ymaximum 988
        #Saint
        frame:
            xminimum 116
            xmaximum 116
            yminimum 116
            ymaximum 116
            background None
            xoffset 345
            yoffset 650
            add "SaintToken":
                zoom .33
                if TokenHovered == "st":
                    at transform:
                        TokenHover
                else:
                    at transform:
                        TokenUnhover
            add "BeatProgressEmpty":
                if TokenHovered == "st":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
            add "BeatProgressFull":
                if beat_SaintCatherine == 1:
                    at transform:
                        crop (0,0,0,0)
                elif beat_SaintCatherine == 2:
                    at transform:
                        crop (0,0,18,17)
                elif beat_SaintCatherine == 3:
                    at transform:
                        crop (0,0,37,17)
                elif beat_SaintCatherine == 4:
                    at transform:
                        crop (0,0,57,17)
                elif beat_SaintCatherine == 5:
                    at transform:
                        crop (0,0,75,17)
                if TokenHovered == "st":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
        #SoupAndSunflowers
        frame:
            xminimum 116
            xmaximum 116
            yminimum 116
            ymaximum 116
            background None
            xoffset 582
            yoffset 580
            add "SSToken":
                zoom .33
                if TokenHovered == "ss":
                    at transform:
                        TokenHover
                else:
                    at transform:
                        TokenUnhover
            add "BeatProgressEmpty":
                if TokenHovered == "ss":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
            add "BeatProgressFull":
                if beat_SoupAndSunflowers == 1:
                    at transform:
                        crop (0,0,0,0)
                elif beat_SoupAndSunflowers == 2:
                    at transform:
                        crop (0,0,18,17)
                elif beat_SoupAndSunflowers == 3:
                    at transform:
                        crop (0,0,37,17)
                elif beat_SoupAndSunflowers == 4:
                    at transform:
                        crop (0,0,57,17)
                elif beat_SoupAndSunflowers == 5:
                    at transform:
                        crop (0,0,75,17)
                if TokenHovered == "ss":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
        #davids
        frame:
            xminimum 116
            xmaximum 116
            yminimum 116
            ymaximum 116
            background None
            xoffset 856
            yoffset 518
            add "DavidsToken":
                zoom .33
                if TokenHovered == "d":
                    at transform:
                        TokenHover
                else:
                    at transform:
                        TokenUnhover
            add "BeatProgressEmpty":
                if TokenHovered == "d":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
            add "BeatProgressFull":
                if beat_Davids == 1:
                    at transform:
                        crop (0,0,0,0)
                elif beat_Davids == 2:
                    at transform:
                        crop (0,0,18,17)
                elif beat_Davids == 3:
                    at transform:
                        crop (0,0,37,17)
                elif beat_Davids == 4:
                    at transform:
                        crop (0,0,57,17)
                elif beat_Davids == 5:
                    at transform:
                        crop (0,0,75,17)
                if TokenHovered == "d":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
        #gilgamesh
        frame:
            xminimum 116
            xmaximum 116
            yminimum 116
            ymaximum 116
            background None
            xoffset 495
            yoffset 408
            add "GilgameshToken":
                zoom .33
                if TokenHovered == "gi":
                    at transform:
                        TokenHover
                else:
                    at transform:
                        TokenUnhover
            add "BeatProgressEmpty":
                if TokenHovered == "gi":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
            add "BeatProgressFull":
                if beat_Gilgamesh == 1:
                    at transform:
                        crop (0,0,0,0)
                elif beat_Gilgamesh == 2:
                    at transform:
                        crop (0,0,18,17)
                elif beat_Gilgamesh == 3:
                    at transform:
                        crop (0,0,37,17)
                elif beat_Gilgamesh == 4:
                    at transform:
                        crop (0,0,57,17)
                elif beat_Gilgamesh == 5:
                    at transform:
                        crop (0,0,75,17)
                if TokenHovered == "gi":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover

        #arnolfini
        frame:
            xminimum 116
            xmaximum 116
            yminimum 116
            ymaximum 116
            background None
            xoffset 710
            yoffset 405
            add "ArnolfiniToken":
                zoom .33
                if TokenHovered == "ar":
                    at transform:
                        TokenHover
                else:
                    at transform:
                        TokenUnhover
            add "BeatProgressEmpty":
                if TokenHovered == "ar":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
            add "BeatProgressFull":
                if beat_Arnolfini == 1:
                    at transform:
                        crop (0,0,0,0)
                elif beat_Arnolfini == 2:
                    at transform:
                        crop (0,0,18,17)
                elif beat_Arnolfini == 3:
                    at transform:
                        crop (0,0,37,17)
                elif beat_Arnolfini == 4:
                    at transform:
                        crop (0,0,57,17)
                elif beat_Arnolfini == 5:
                    at transform:
                        crop (0,0,75,17)
                if TokenHovered == "ar":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
                    
        frame:
            xminimum 116
            xmaximum 116
            yminimum 116
            ymaximum 116
            background None
            xoffset 582
            yoffset 224
            add "MonaToken":
                zoom .33
                if TokenHovered == "m":
                    at transform:
                        TokenHover
                else:
                    at transform:
                        TokenUnhover
            add "BeatProgressEmpty":
                if TokenHovered == "m":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
            add "BeatProgressFull":
                if beat_MonaLisa == 1:
                    at transform:
                        crop (0,0,0,0)
                elif beat_MonaLisa == 2:
                    at transform:
                        crop (0,0,18,17)
                elif beat_MonaLisa == 3:
                    at transform:
                        crop (0,0,37,17)
                elif beat_MonaLisa == 4:
                    at transform:
                        crop (0,0,57,17)
                elif beat_MonaLisa == 5:
                    at transform:
                        crop (0,0,75,17)
                if TokenHovered == "m":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover

        frame:
            xminimum 116
            xmaximum 116
            yminimum 116
            ymaximum 116
            background None
            xoffset 301
            yoffset 251
            add "CorgiToken":
                zoom .33
                if TokenHovered == "p":
                    at transform:
                        TokenHover
                else:
                    at transform:
                        TokenUnhover
            add "BeatProgressEmpty":
                if TokenHovered == "p":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover
            add "BeatProgressFull":
                if beat_Poster == 1:
                    at transform:
                        crop (0,0,0,0)
                elif beat_Poster == 2:
                    at transform:
                        crop (0,0,18,17)
                elif beat_Poster == 3:
                    at transform:
                        crop (0,0,37,17)
                elif beat_Poster == 4:
                    at transform:
                        crop (0,0,57,17)
                elif beat_Poster == 5:
                    at transform:
                        crop (0,0,75,17)
                if TokenHovered == "p":
                    at transform:
                        PipHover
                else:
                    at transform:
                        PipUnhover



   
#remove all this
label call_Office:
    call screen Office

screen Office:
    add "map/rooms/office_bg.png"

    imagemap:
        ground "map/rooms/office_bg.png"
        hover "map/rooms/office_bg_hover.png"

        #admin button
        hotspot (218, 458, 500, 414) action Jump("conv_Admin")
        #poster button
        hotspot (1082, 376, 735, 467) action Jump("conv_Poster")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_Foyer:
    call screen Foyer

screen Foyer:
    add "map/rooms/foyer_bg.png"

    imagemap:
        ground "map/rooms/foyer_bg.png"

        #davids button
        hotspot (124, 361, 977, 638) action Jump("conv_Davids")
        #nighthawks button
        hotspot (1342, 125, 441, 241) action Jump("conv_Nighthawks")
        #vending machine button
        hotspot (1411, 493, 302, 440) action Jump("conv_VendingMachine")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_Antiquities:
    call screen Antiquities

screen Antiquities:
    add "map/rooms/Antiquities_bg.png"

    imagemap:
        ground "map/rooms/Antiquities_bg.png"

        #gilgamesh button
        hotspot (153, 292, 311, 724) action Jump("conv_Gilgamesh")
        #EaNasir button
        hotspot (629, 579, 447, 420) action Jump("conv_EaNasir")
        #sue button
        hotspot (1245, 497, 570, 425) action Jump("conv_Sue")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_FineArt:
    call screen FineArt

screen FineArt:
    add "map/rooms/FineArt_bg.png"

    imagemap:
        ground "map/rooms/FineArt_bg.png"

        #mona lisa button
        hotspot (102, 249, 486, 724) action Jump("conv_MonaLisa")
        #Arnolfini button
        hotspot (675, 243, 533, 730) action Jump("conv_Arnolfini")
        #theodore button
        hotspot (1500, 408, 335, 407) action Jump("conv_Theodore")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_MixedMedia:
    call screen MixedMedia

screen MixedMedia:
    add "map/rooms/MixedMedia_bg.png"

    imagemap:
        ground "map/rooms/MixedMedia_bg.png"

        #saint catherine button
        hotspot (158, 203, 467, 774) action Jump("conv_SaintCatherine")
        #glimmer button
        hotspot (745, 191, 429, 797) action Jump("conv_Glimmer")
        #Soup and Sunflowers button
        hotspot (1285, 231, 545, 717) action Jump("conv_Sunflowers")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")