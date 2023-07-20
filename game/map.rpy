#map
label call_mapUI:
    show screen gameUI
    call screen MapUI

screen MapUI:
    add "newmap/museum_map.jpg"
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
    imagemap:
        ground "newmap/museum_map.jpg"
        hover "newmap/museum_map_hover.jpg"

        #glimmer
        hotspot (30, 18, 163, 321) action Jump("conv_Admin")
        #sunflowers
        hotspot (217, 12,143,266) action Jump("conv_SoupAndSunflowers")
        #saintcatherine
        hotspot (368,217,141,286) action Jump("conv_SaintCatherine")
        #gilgamesh
        hotspot (544,174,144,288) action Jump("conv_Gilgamesh")
        #sue
        hotspot (707,190,169,331) action Jump("conv_Sue")
        #EaNasir
        hotspot (948,158,116,263) action Jump("conv_EaNasir")
        #Theodore
        hotspot (1106,58,144,283) action Jump("conv_Theodore")
        #MonaLisa
        hotspot (1244,88,268,399) action Jump("conv_MonaLisa")
        #Arnolfini
        hotspot (1456,278,137,255) action Jump("conv_Arnolfini")
        #Nighthawks
        hotspot (749,584,205,154) action Jump("conv_Nighthawks")
        #VendingMachine
        hotspot (1028,622,109,205) action Jump("conv_VendingMachine")
        #Davids
        hotspot (1185,608,248,222) action Jump("conv_Davids")
        #Poster
        hotspot (1443,550,277,245) action Jump("conv_Poster")
        #Admin
        hotspot (1732,595,151,283) action Jump("conv_Admin")

   

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