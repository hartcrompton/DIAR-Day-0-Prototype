default Card1Title = "Guybrush"
default Card2Title = "Gilgamesh"
default Card3Title = "Gilead"
default Card4Title = "Gourmandise"
default Card5Title = "Gator"
default CardTitleVisible = 1
default CardHovered = 0
default TempCharacter = "None"

init python:
    renpy.add_layer("middle", above="master")

#so for me, the card cat is the inventory
screen inventory():
    layer "middle"
    add Solid("#244")
    modal renpy.get_screen("wait_for_user") # if you don't need modal, omit this line
    sensitive renpy.get_screen("wait_for_user")
    textbutton "Item" action Return("DrawerStuck") align (.5, .5)
    textbutton "Return" action Return("exit") align (.5, .6)
#this doesn't change
screen wait_for_user():
    pass
#this is what should call the catalogue up
label call_inventory():
    label .repeat:
    show screen inventory()
    call screen wait_for_user()
    if _return == "exit":
        hide screen inventory
        return

    show layer middle at unfocus
    call expression _return
    show layer middle at reset
    jump .repeat

label call_catalogue():
    label .repeat:
    show screen ResearchMinigameUI()
    call screen wait_for_user()
    if _return == "exit":
        hide screen ResearchMinigameUI
        return

    show layer middle at unfocus
    call expression _return
    show layer middle at reset
    jump .repeat

label DrawerStuck:
    "Drawer stuck!"
    return

transform unfocus:
    blur 10

label ResearchMinigame(ResearchCharacter="Default"):
    #jump ResearchTransition
    $ TempCharacter = ResearchCharacter
    jump ResearchTransition

label ResearchTransition:
    call screen ResearchMinigameUI

screen ResearchMinigameUI():
    layer "middle"
    modal renpy.get_screen("wait_for_user") # if you don't need modal, omit this line
    sensitive renpy.get_screen("wait_for_user")
    imagemap:
        ground "images/minigame/research/ResearchBg1.jpg"
        hover "images/minigame/research/ResearchBg1Hover.jpg"

        #clicking one should call the drawer screen with the appropriate letter
        hotspot (393, 81, 228, 137) action Call("ResearchMinigameDrawer", "A") #call up the appropriate second screen
        hotspot (621, 81, 228, 137) action Call("ResearchMinigameDrawer", "B") #call up the appropriate second screen
        hotspot (848, 81, 228, 137) action Call("ResearchMinigameDrawer", "C")#call up the appropriate second screen
        hotspot (1076, 81, 228, 137) action Call("ResearchMinigameDrawer", "D")#call up the appropriate second screen
        hotspot (1304, 81, 228, 137) action Call("ResearchMinigameDrawer", "E")#call up the appropriate second screen

        hotspot (393, 218, 228, 137) action Call("ResearchMinigameDrawer", "F")#call up the appropriate second screen
        hotspot (621, 218, 228, 137) action Call("ResearchMinigameDrawer", "G")#call up the appropriate second screen
        hotspot (848, 218, 228, 137) action Call("ResearchMinigameDrawer", "H")#call up the appropriate second screen
        hotspot (1076, 218, 228, 137) action Call("ResearchMinigameDrawer", "I")#call up the appropriate second screen
        hotspot (1304, 218, 228, 137) action Call("ResearchMinigameDrawer", "J")#call up the appropriate second screen

        hotspot (393, 354, 228, 137) action Return("DrawerStuck") #call up the appropriate second screen K
        hotspot (621, 354, 228, 137) action Call("ResearchMinigameDrawer", "L")#call up the appropriate second screen
        hotspot (848, 354, 228, 137) action Call("ResearchMinigameDrawer", "M")#call up the appropriate second screen
        hotspot (1076, 354, 228, 137) action Call("ResearchMinigameDrawer", "N")#call up the appropriate second screen
        hotspot (1304, 354, 228, 137) action Call("ResearchMinigameDrawer", "O")#call up the appropriate second screen

        hotspot (393, 491, 228, 137) action Call("ResearchMinigameDrawer", "P")#call up the appropriate second screen
        hotspot (621, 491, 228, 137) action Call("ResearchMinigameDrawer", "Q")#call up the appropriate second screen
        hotspot (848, 491, 228, 137) action Call("ResearchMinigameDrawer", "R")#call up the appropriate second screen
        hotspot (1076, 491, 228, 137) action Call("ResearchMinigameDrawer", "S")#call up the appropriate second screen
        hotspot (1304, 491, 228, 137) action Call("ResearchMinigameDrawer", "T")#call up the appropriate second screen

        hotspot (393, 628, 228, 137) action Call("ResearchMinigameDrawer", "U")#call up the appropriate second screen
        hotspot (621, 628, 228, 137) action Call("ResearchMinigameDrawer", "V")#call up the appropriate second screen
        hotspot (848, 628, 228, 137) action Call("ResearchMinigameDrawer", "W")#call up the appropriate second screen
        hotspot (1076, 628, 228, 137) action Call("ResearchMinigameDrawer", "X")#call up the appropriate second screen
        hotspot (1304, 628, 228, 137) action Call("ResearchMinigameDrawer", "Y")#call up the appropriate second screen

        hotspot (848, 764, 228, 137) action Call("ResearchMinigameDrawer", "Z")#call up the appropriate second screen


label ResearchMinigameDrawer(ResearchLetter="Default"):
    call screen ResearchMinigameDrawerUI
    
screen ResearchMinigameDrawerUI:
    #called letter used to supply drawer titles
    #needs to be some logic such that only the correct one is clickable
    #if ResearchLetter == "A"
        #CardTitle1 = "A1"
        #CardTitle1 = "A2"
        #CardTitle1 = "A3"
        #CardTitle1 = "A4"
        #CardTitle1 = "A5" etc
    
    imagemap:
        ground "images/minigame/research/ResearchBg2.jpg"
        hover "images/minigame/research/ResearchBg2Hover.jpg"

        #cards
        hotspot (467, 588, 989, 124) action [NullAction()] hovered [SetVariable("CardHovered", 1)] unhovered [SetVariable("CardHovered", 0)]
        hotspot (507, 515, 906, 69) action [NullAction()] hovered [SetVariable("CardHovered", 2)] unhovered [SetVariable("CardHovered", 0)] 
        hotspot (548, 442, 823, 73) action [NullAction()] hovered [SetVariable("CardHovered", 3)] unhovered [SetVariable("CardHovered", 0)]
        hotspot (588, 369, 740, 73) action [NullAction()] hovered [SetVariable("CardHovered", 4)] unhovered [SetVariable("CardHovered", 0)]
        hotspot (628, 293, 658, 73) action [NullAction()] hovered [SetVariable("CardHovered", 5)] unhovered [SetVariable("CardHovered", 0)]
    imagebutton:
        xpos 100
        ypos 100
        idle "map/rooms/back_idle.png"
        hover "map/rooms/back_hover.png"
        action Jump("call_catalogue")
    frame:
        xalign 0
        yalign 0
        xoffset 352
        yoffset 0
        background None
        xminimum 1214
        xmaximum 1214
        yminimum 1080
        ymaximum 1080
        hbox:
                xalign 0.5
                yalign 0.85
                text "{color=#000000}[ResearchLetter]{/color}" size 80
        hbox:
                xalign 0.5
                yalign 0
                yoffset 645
                text "{color=#000000}[Card1Title]{/color}":
                    size 40
                    if CardHovered == 1:
                        at transform:
                            yoffset -55
                    else:
                        at transform:
                            yoffset 0
    
        hbox:
                xalign 0.5
                yalign 0
                yoffset 575
                text "{color=#000000}[Card2Title]{/color}": 
                    size 40
                    if CardHovered == 1:
                        at transform:
                            alpha 0
                    else:
                        at transform:
                            alpha 1
                    if CardHovered == 2:
                        at transform:
                            yoffset -55
                    else:
                        at transform:
                            yoffset 0
        hbox:
                xalign 0.5
                yalign 0
                yoffset 500
                text "{color=#000000}[Card3Title]{/color}": 
                    size 40
                    if CardHovered == 2:
                        at transform:
                            alpha 0
                    else:
                        at transform:
                            alpha 1
                    if CardHovered == 3:
                        at transform:
                            yoffset -55
                    else:
                        at transform:
                            yoffset 0
        hbox:
                xalign 0.5
                yalign 0
                yoffset 430
                text "{color=#000000}[Card4Title]{/color}":
                    size 40
                    if CardHovered == 3:
                        at transform:
                            alpha 0
                    else:
                        at transform:
                            alpha 1
                    if CardHovered == 4:
                        at transform:
                            yoffset -55
                    else:
                        at transform:
                            yoffset 0
        hbox:
                xalign 0.5
                yalign 0
                yoffset 360
                text "{color=#000000}[Card5Title]{/color}": 
                    size 40
                    if CardHovered == 4:
                        at transform:
                            alpha 0
                    else:
                        at transform:
                            alpha 1
                    if CardHovered == 5:
                        at transform:
                            yoffset -55
                    else:
                        at transform:
                            yoffset 0

                #if you click the wrong one, no sort interaction aside from some text maybe
                #if you click the right one, jump to the library scene and then you just need to click the correct shelf
                    #could skip that whole step and just transition to the library and you grab the book, maybe do that instead,
