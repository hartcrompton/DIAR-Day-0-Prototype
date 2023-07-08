#disposition system

screen DispositionMenu:
    add "UI/Disposition/DispositionMenuBG.png"
    frame:
        xalign 0
        yalign 0
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Arnolfini" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    frame:
        xalign 0
        yalign .3
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "The Davids" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    frame:
        xalign 0
        yalign .6
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Gilgamesh" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    frame:
        xalign .3
        yalign 0
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Glimmer" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    frame:
        xalign .3
        yalign .3
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Mona Lisa" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    frame:
        xalign .3
        yalign .6
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Saint Catherine" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    frame:
        xalign .6
        yalign 0
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Soup" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    frame:
        xalign .6
        yalign .3
        xoffset 30
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Sunflowers" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "1" size 40
                text "2" size 40
                text "3" size 40
    textbutton "Return":
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        action Return()

label TotalDisposition:
    python:
        arr_dispositions = []
        arr_dispositions.append(d_Arnolfini)
        arr_dispositions.append(d_Davids)
        arr_dispositions.append(d_Gilgamesh)
        arr_dispositions.append(d_Glimmer)
        arr_dispositions.append(d_MonaLisa)
        arr_dispositions.append(d_SaintCatherine)
        arr_dispositions.append(d_Soup)
        arr_dispositions.append(d_Sunflowers)
        d_Total = 0
        for i in arr_dispositions:
            if i == 0:
                d_Total += d_Tier1
            elif i == 1:
                d_Total += d_Tier2
            elif i == 2:
                d_Total += d_Tier3
            elif i == 3:
                d_Total += d_Tier4
            elif i == 4:
                d_Total += d_Tier5
            elif i == 5:
                d_Total += d_Tier6
            elif i == 6:
                d_Total += d_Tier7
    return