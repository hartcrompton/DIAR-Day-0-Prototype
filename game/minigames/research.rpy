default Card1Title = "Guybrush"
default Card2Title = "Gilgamesh"
default Card3Title = "Gilead"
default Card4Title = "Gourmandise"
default Card5Title = "Gator"
default CardTitleVisible = 1
default CardHovered = 0
default TempCharacter = "None"
image card1 = "images/minigame/research/test/card1.png"
image drawerfront = "images/minigame/research/test/drawerfront.png"

init python:
    renpy.add_layer("middle", above="master")
    #arr_GilgameshCards = ["Gator", "Gourmand", "Gilgamesh", "Gilead", "Guybrush"]
    #arr_DavidsCards = ["Dinosaur", "Donatello", "Deontology", "David", "Dionysus"]
    CardTitles = {"G": ["Gator", "Gourmand", "Gilgamesh", "Gilead", "Guybrush"], "D": ["Dinosaur", "Donatello", "Deontology", "David", "Dionysus"]}

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
    call expression _return from _call_expression
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
    call expression _return from _call_expression_1
    show layer middle at reset
    jump .repeat

label DrawerStuck:
    "Drawer stuck!"
    return

transform unfocus:
    blur 10

transform CardUp:
    ease .1 yoffset -55

transform CardDown:
    ease .1 yoffset 0

transform CardFirst:
    yoffset 645

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
        ground "images/minigame/research/research catalogue base.jpg"
        hover "images/minigame/research/research catalogue hover.jpg"

        #clicking one should call the drawer screen with the appropriate letter
        hotspot (294,66,261,157) action Call("ResearchMinigameDrawer", "A") #call up the appropriate second screen
        hotspot (294,224,261,157) action Call("ResearchMinigameDrawer", "B") #call up the appropriate second screen
        hotspot (294,384,261,157) action Call("ResearchMinigameDrawer", "C")#call up the appropriate second screen
        hotspot (294,540,261,157) action Call("ResearchMinigameDrawer", "D")#call up the appropriate second screen
        hotspot (294,699,261,157) action Call("ResearchMinigameDrawer", "E")#call up the appropriate second screen

        hotspot (572,66,261,157) action Call("ResearchMinigameDrawer", "F")#call up the appropriate second screen
        hotspot (572,224,261,157) action Call("ResearchMinigameDrawer", "G")#call up the appropriate second screen
        hotspot (572,384,261,157) action Call("ResearchMinigameDrawer", "H")#call up the appropriate second screen
        hotspot (572,540,261,157) action Call("ResearchMinigameDrawer", "I")#call up the appropriate second screen
        hotspot (572,699,261,157) action Call("ResearchMinigameDrawer", "J")#call up the appropriate second screen

        hotspot (848,66,261,157) action Return("DrawerStuck") #call up the appropriate second screen K
        hotspot (848,224,261,157) action Call("ResearchMinigameDrawer", "L")#call up the appropriate second screen
        hotspot (848,384,261,157) action Call("ResearchMinigameDrawer", "M")#call up the appropriate second screen
        hotspot (848,540,261,157) action Call("ResearchMinigameDrawer", "N")#call up the appropriate second screen
        hotspot (848,699,261,157) action Call("ResearchMinigameDrawer", "O")#call up the appropriate second screen

        hotspot (1123,66,261,157) action Call("ResearchMinigameDrawer", "P")#call up the appropriate second screen
        hotspot (1123,224,261,157) action Call("ResearchMinigameDrawer", "Q")#call up the appropriate second screen
        hotspot (1123,384,261,157) action Call("ResearchMinigameDrawer", "R")#call up the appropriate second screen
        hotspot (1123,540,261,157) action Call("ResearchMinigameDrawer", "S")#call up the appropriate second screen
        hotspot (1123,699,261,157) action Call("ResearchMinigameDrawer", "T")#call up the appropriate second screen

        hotspot (1399,66,261,157) action Call("ResearchMinigameDrawer", "U")#call up the appropriate second screen
        hotspot (1399,224,261,157) action Call("ResearchMinigameDrawer", "V")#call up the appropriate second screen
        hotspot (1399,384,261,157) action Call("ResearchMinigameDrawer", "W")#call up the appropriate second screen
        hotspot (1399,540,261,157) action Call("ResearchMinigameDrawer", "X")#call up the appropriate second screen
        hotspot (1399,699,261,157) action Call("ResearchMinigameDrawer", "Y")#call up the appropriate second screen

        hotspot (848,857,261,157) action Call("ResearchMinigameDrawer", "Z")#call up the appropriate second screen


label ResearchMinigameDrawer(ResearchLetter="Default"):
    python:
        TempCardTitles = []
        if CardTitles.get(ResearchLetter):
            TempCardTitles = CardTitles.get(ResearchLetter)
            #this could be done through iteration if it needed to work with different numbers of cards
            Card1Title = TempCardTitles[0]
            Card2Title = TempCardTitles[1]
            Card3Title = TempCardTitles[2]
            Card4Title = TempCardTitles[3]
            Card5Title = TempCardTitles[4]
        else:
            renpy.return_statement("DrawerStuck")
    #if ResearchLetter == "G":
    #    $ Card1Title = arr_GilgameshCards[0]
    #    $ Card2Title = arr_GilgameshCards[1]
    #    $ Card3Title = arr_GilgameshCards[2]
    #    $ Card4Title = arr_GilgameshCards[3]
    #    $ Card5Title = arr_GilgameshCards[4]
    #if ResearchLetter == "D":
    #    $ Card1Title = arr_DavidsCards[0]
    #    $ Card2Title = arr_DavidsCards[1]
    #    $ Card3Title = arr_DavidsCards[2]
    #    $ Card4Title = arr_DavidsCards[3]
    #    $ Card5Title = arr_DavidsCards[4]
    #better way to do this if more cards are required
    #
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
        ground "images/minigame/research/test/drawerbghover.jpg"
        #hover "images/minigame/research/ResearchBg2Hover.jpg"

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
        
        vbox:
                xalign 0.5
                yalign 0
                yoffset 345
                add "card1":
                    yoffset 0
                    zoom .68
                    if CardHovered == 5:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
                text "{color=#000000}[Card5Title]{/color}":
                    size 40
                    xalign .5
                    yoffset -390
                    if CardHovered == 5:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
        vbox:
                xalign 0.5
                yalign 0
                yoffset 419
                add "card1":
                    yoffset 0
                    zoom .76
                    if CardHovered == 4:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
                text "{color=#000000}[Card4Title]{/color}":
                    size 40
                    xalign .5
                    yoffset -435
                    if CardHovered == 4:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
        vbox:
                xalign 0.5
                yalign 0
                yoffset 492
                add "card1":
                    yoffset 0
                    zoom .84
                    if CardHovered == 3:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
                text "{color=#000000}[Card3Title]{/color}":
                    size 40
                    xalign .5
                    yoffset -485
                    if CardHovered == 3:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
        vbox:
                xalign 0.5
                yalign 0
                yoffset 565
                add "card1":
                    yoffset 0
                    zoom .92
                    if CardHovered == 2:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
                text "{color=#000000}[Card2Title]{/color}":
                    size 40
                    xalign .5
                    yoffset -530
                    if CardHovered == 2:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
        vbox:
                xalign 0.5
                yalign 0
                yoffset 638
                add "card1":
                    yoffset 0
                    if CardHovered == 1:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
                text "{color=#000000}[Card1Title]{/color}":
                    size 40
                    xalign .5
                    yoffset -575
                    if CardHovered == 1:
                        at transform:
                            CardUp
                    else:
                        at transform:
                            CardDown
        hbox:
            xalign 0.5
            yalign 0.85
            text "{color=#000000}[ResearchLetter]{/color}" size 80
    add "drawerfront"
    
        

                #if you click the wrong one, no sort interaction aside from some text maybe
                #if you click the right one, jump to the library scene and then you just need to click the correct shelf
                    #could skip that whole step and just transition to the library and you grab the book, maybe do that instead,
