#map
label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map/museum map.png"

    imagebutton:
        xpos 253
        ypos 305
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
        hotspot (218, 458, 500, 414) action Preference("display", "fullscreen") alt _("Display Fullscreen")
        #poster button
        hotspot (1082, 376, 735, 467) action Jump("conv_poster")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")