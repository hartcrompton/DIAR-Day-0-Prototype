#map
default TokenHovered = "NONE"


label call_mapUI:
    $ TokenHovered = "NONE"
    call screen MapUI
    #show screen gameUI

image SaintToken = "Characters/SideImages/side saintcatherine.png"
image GilgameshToken = "Characters/SideImages/side gilgamesh.png"
default giX = 495


image CorgiToken = "Characters/SideImages/side poster.png"
image SSToken = "Characters/SideImages/side soupandsunflowers.png"
image MonaToken = "Characters/SideImages/side mona.png"
image DavidsToken = "Characters/SideImages/side davids.png"
image ArnolfiniToken = "Characters/SideImages/side arnolfinimap.png"
image BeatProgressEmpty = "map/BeatProgressPips.png"
image BeatProgressFull = "map/BeatProgressPipsFilled.png"

transform TokenHover:
    ease .1 yoffset -10

transform TokenUnhover:
    ease .1 yoffset 0

transform PipHover:
    xoffset 12
    yoffset 85
    ease .1 alpha 1.0

transform PipUnhover:
    xoffset 12
    yoffset 85
    ease .1 alpha 0.0

screen MapUI:
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
        ground "map/map_new.png"
        #hover "newmap/museum_map_hover.jpg"

        #glimmer
        #hotspot (30, 18, 163, 321) action Jump("conv_Admin")
        #sunflowers
        #hotspot (217, 12,143,266) action Jump("conv_SoupAndSunflowers")
        #saintcatherine
        hotspot (345,650,97,97) action [Jump("conv_SaintCatherine")] hovered [SetVariable("TokenHovered", "st")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (582,580,97,97) action [Jump("conv_SoupAndSunflowers")] hovered [SetVariable("TokenHovered", "ss")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (806,518,97,97) action [Jump("conv_Davids")] hovered [SetVariable("TokenHovered", "d")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (495,408,97,97) action [Jump("conv_Gilgamesh")] hovered [SetVariable("TokenHovered", "gi")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (760,405,97,97) action [Jump("conv_Arnolfini")] hovered [SetVariable("TokenHovered", "ar")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (582,224,97,97) action [Jump("conv_MonaLisa")] hovered [SetVariable("TokenHovered", "m")] unhovered [SetVariable("TokenHovered", "NONE")]
        hotspot (301,251,97,97) action [Jump("conv_Poster")] hovered [SetVariable("TokenHovered", "p")] unhovered [SetVariable("TokenHovered", "NONE")]
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
        xalign 0
        yalign 1.0
        xoffset 10
        yoffset -10
        xminimum 300
        xmaximum 300
        yminimum 300
        ymaximum 300
        hbox:
            box_wrap True
            spacing 40
            vbox:
                spacing 10
                text "Day [DayNumber] / 4":
                    size 40
                if InfiniteActions == 0:
                    text "Morning":
                        size 20
                        if actions == 4:
                            size 40
                    text "Noon":
                        size 20
                        if actions == 3:
                            size 40
                    text "Evening":
                        size 20
                        if actions == 2:
                            size 40
                    text "Night":
                        size 20
                        if actions == 1:
                            size 40
                if InfiniteActions == 1:
                    text "INFINITE ACTIONS":
                        size 20
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
        xminimum 1062
        xmaximum 1062
        yminimum 982
        ymaximum 982
        #Saint
        frame:
            xminimum 97
            xmaximum 97
            yminimum 97
            ymaximum 97
            background None
            xoffset 345
            yoffset 650
            add "SaintToken":
                zoom .275
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
            xminimum 97
            xmaximum 97
            yminimum 97
            ymaximum 97
            background None
            xoffset 582
            yoffset 580
            add "SSToken":
                zoom .275
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
            xminimum 97
            xmaximum 97
            yminimum 97
            ymaximum 97
            background None
            xoffset 806
            yoffset 518
            add "DavidsToken":
                zoom .275
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
            xminimum 97
            xmaximum 97
            yminimum 97
            ymaximum 97
            background None
            xoffset 495
            yoffset 408
            add "GilgameshToken":
                zoom .275
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
            xminimum 97
            xmaximum 97
            yminimum 97
            ymaximum 97
            background None
            xoffset 760
            yoffset 405
            add "ArnolfiniToken":
                zoom .275
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
            xminimum 97
            xmaximum 97
            yminimum 97
            ymaximum 97
            background None
            xoffset 582
            yoffset 224
            add "MonaToken":
                zoom .275
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
            xminimum 97
            xmaximum 97
            yminimum 97
            ymaximum 97
            background None
            xoffset 301
            yoffset 251
            add "CorgiToken":
                zoom .275
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