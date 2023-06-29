## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map/museum map.png"

    imagebutton:
        xpos 253
        ypos 305
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_BreakRoom")
        
    imagebutton:
        xpos 832
        ypos 305
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_Archive")

    imagebutton:
        xpos 1411
        ypos 305
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_Antiquities")

    imagebutton:
        xpos 253
        ypos 715
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_Contemporary")

    imagebutton:
        xpos 832
        ypos 715
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_FineArt")

    imagebutton:
        xpos 1411
        ypos 715
        idle "map/museum_map_idle.png"
        hover "map/museum_map_hover.png"
        action Jump("call_Lobby")

label call_BreakRoom:
    call screen BreakRoom

screen BreakRoom:
    add "map/rooms/break_room.png"
        
    imagebutton:
        xpos 1187
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house2_pressed")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_Archive:
    call screen Archive

screen Archive:
    add "map/rooms/archive.png"
        
    imagebutton:
        xpos 1187
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house2_pressed")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_Antiquities:
    call screen Antiquities

screen Antiquities:
    add "map/rooms/antiquities.png"

    imagebutton:
        xpos 477
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house1_pressed")
        
    imagebutton:
        xpos 1187
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house2_pressed")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_Contemporary:
    call screen Contemporary

screen Contemporary:
    add "map/rooms/contemporary.png"

    imagebutton:
        xpos 477
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house1_pressed")
        
    imagebutton:
        xpos 1187
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house2_pressed")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_FineArt:
    call screen FineArt

screen FineArt:
    add "map/rooms/fine_art.png"

    imagebutton:
        xpos 477
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house1_pressed")
        
    imagebutton:
        xpos 1187
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house2_pressed")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

label call_Lobby:
    call screen Lobby

screen Lobby:
    add "map/rooms/lobby.png"
        
    imagebutton:
        xpos 1187
        ypos 305
        idle "map/rooms/room_idle.png"
        hover "map/rooms/room_hover.png"
        action Jump("house2_pressed")

    imagebutton:
        xpos 195
        ypos 136
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_mapUI")

#displays the vending machine and allows clicking buttons to select a snack
screen vendingmachineselection:
    add "vending_machine/vendingmachineintro.jpg"

    imagebutton:
        xpos 1519
        ypos 294
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+10, selection+1)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1635
        ypos 294
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+20, selection+2)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1751
        ypos 294
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+30, selection+3)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1519
        ypos 410
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+40, selection+4)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1635
        ypos 410
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+50, selection+5)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1751
        ypos 410
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+60, selection+6)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1519
        ypos 526
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+70, selection+7)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1635
        ypos 526
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+80, selection+8)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1751
        ypos 526
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+90, selection+9)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

    imagebutton:
        xpos 1635
        ypos 642
        idle "vending_machine/button_idle.png"
        hover "vending_machine/button_hover.png"
        action [SetVariable("selection", If(button_press_count == 0, selection+0, selection+0)), SetVariable("button_press_count", button_press_count+1), If(button_press_count >= 1, Jump("vending_machine_checker"))]

            #if button count == 0
                #selection += 10
                #buttoncount += 1
            #else
                #selection += 1
        #image 2
        #image 3
        #image 4
        #image 5
        #image 6
        #image 7
        #image 8
        #image 9
        #image 0
    #else
        #check if valid selection
            #dispense snack OR
            #loop back around
#checks for valid selection, restarts interaction if invalid
label vending_machine_checker:
    python:
        if selection == 15:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 21:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 23:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 25:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 31:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 33:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 35:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 41:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 43:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        elif selection == 44:
            renpy.say(meta, "You selected [selection]")
            renpy.jump("arguing_davids")
        else:
            renpy.say(meta, "You selected INVALID")
            renpy.say(meta, "Please select something else")
            renpy.jump("vending_machine_intro")
            
