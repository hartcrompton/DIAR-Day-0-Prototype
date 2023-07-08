#map
label call_mapUI:
    show screen gameUI
    call screen MapUI

screen MapUI:
    add "map/museum map bg.png"
    textbutton "Stats":
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        action ShowMenu("DispositionMenu")
    textbutton "Day [DayNumber]":
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
    textbutton "Remaining Actions: [actions]":
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 60


    #foyer
    imagebutton:
        xpos 253
        ypos 305
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_Foyer")
    #antiquities
    imagebutton:
        xpos 832
        ypos 305
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_Antiquities")
    #fineart
    imagebutton:
        xpos 1411
        ypos 305
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_FineArt")
    #mixedmedia
    imagebutton:
        xpos 253
        ypos 715
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_MixedMedia")
    #office
    imagebutton:
        xpos 832
        ypos 715
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_Office")

label call_Office:
    call screen Office

screen Office:
    add "map/rooms/office_bg.png"

    imagemap:
        ground "map/rooms/office_bg.png"

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