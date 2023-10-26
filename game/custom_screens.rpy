## Screen with Stats Button

style TODStyle is text:
        color "ffffff"
        size 40

style style_CurrentDay is text:
        color "ffffff"
        size 40
        bold True

style style_OtherDay is text:
        color "ffffff"
        size 20

screen gameUI:
    textbutton "":
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        action ShowMenu("DispositionMenu")
    

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.

#refactor this ugly thing to use imagemap instead
#displays the vending machine and allows clicking buttons to select a snack
screen vendingmachineselection:
    add "vending_machine/vendingmachineminigame.jpg"

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

#checks for valid selection, restarts interaction if invalid
label vending_machine_checker:
    python:
        if selection == 11:
            #renpy.say(meta, "You selected 'Blue Raspberry Kettle Chips'?")
            renpy.jump("DayZero")
        elif selection == 21:
            #renpy.say(meta, "Thes BBQ chips weren't even packaged this decade.")
            renpy.jump("DayZero")
        elif selection == 23:
            #renpy.say(meta, "A knockoff of a knockoff. Likely half sawdust.")
            renpy.jump("DayZero")
        #elif selection == 25:
            #renpy.say(meta, "'Chunky' Chocolate Chip.")
            #renpy.jump("DayZero")
        elif selection == 31:
            #renpy.say(meta, "The Snickers bar flops against the glass. It does not fall.")
            renpy.jump("DayZero")
        elif selection == 33:
            #renpy.say(meta, "You selected [selection]")
            renpy.jump("DayZero")
        elif selection == 37:
            #renpy.say(meta, "You selected [selection]")
            renpy.jump("DayZero")
        elif selection == 41:
            #renpy.say(meta, "The can has no label. Did someone can this at home?")
            renpy.jump("DayZero")
        elif selection == 43:
            #renpy.say(meta, "You selected [selection]")
            renpy.jump("DayZero")
        elif selection == 44:
            #renpy.say(meta, "The bag says, 'Bliss.' The taste says, 'Sorrow.'")
            renpy.jump("DayZero")
        else:
            renpy.say(meta, "The machine beeps. That option must be out of stock.")
            renpy.say(meta, "Please select something else.")
            renpy.jump("VendingMachineIntro")
            
