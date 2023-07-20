#disposition system

screen DispositionMenu:
    add "UI/Disposition/DispositionMenuBG.png"
    #arnolfini
    $ d_LabelName = d_Label.ValueToLabel(d_Arnolfini)
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
                text "" size 40
                text "[beat_Arnolfini] / 4" size 40
                text "[d_LabelName]" size 40
    #davids
    $ d_LabelName = d_Label.ValueToLabel(d_Davids)
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
                text "" size 40
                text "[beat_Davids] / 4" size 40
                text "[d_LabelName]" size 40
    #Gilgamesh
    $ d_LabelName = d_Label.ValueToLabel(d_Gilgamesh)
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
                text "" size 40
                text "[beat_Gilgamesh] / 4" size 40
                text "[d_LabelName]" size 40
    #Glimmer
    $ d_LabelName = d_Label.ValueToLabel(d_Glimmer)
    frame:
        xalign 0
        yalign .9
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
                text "" size 40
                text "[beat_Glimmer] / 4" size 40
                text "[d_LabelName]" size 40
    #MonaLisa
    $ d_LabelName = d_Label.ValueToLabel(d_MonaLisa)
    frame:
        xalign 0
        yalign 0
        xoffset 1080
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "MonaLisa" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "" size 40
                text "[beat_MonaLisa] / 4" size 40
                text "[d_LabelName]" size 40
    #SaintCatherine
    $ d_LabelName = d_Label.ValueToLabel(d_SaintCatherine)
    frame:
        xalign 0
        yalign .3
        xoffset 1080
        yoffset 30
        hbox:
            spacing 40
            vbox:
                spacing 10
                text "SaintCatherine" size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "" size 40
                text "[beat_SaintCatherine] / 4" size 40
                text "[d_LabelName]" size 40
    #Soup
    $ d_LabelName = d_Label.ValueToLabel(d_Soup)
    frame:
        xalign 0
        yalign .6
        xoffset 1080
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
                text "" size 40
                text "[beat_Soup] / 4" size 40
                text "[d_LabelName]" size 40
    #Sunflowers
    $ d_LabelName = d_Label.ValueToLabel(d_Sunflowers)
    frame:
        xalign 0
        yalign .9
        xoffset 1080
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
                text "" size 40
                text "[beat_Sunflowers] / 4" size 40
                text "[d_LabelName]" size 40
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

#call DispositionValueToLabel pass (d_Arnolfini)

label DispositionValueToLabel(d_Value = 0):
    python:
        d_Label = "UNDEFINED"
        if d_Value == 0:
            d_Label = "Terrible"
        elif d_Value == 1:
            d_Label = "Bad"
        elif d_Value == 2:
            d_Label = "Unpleasant"
        elif d_Value == 3:
            d_Label = "Neutral"
        elif d_Value == 4:
            d_Label = "OK"
        elif d_Value == 5:
            d_Label = "Good"
        elif d_Value == 6:
            d_Label = "Great"
    return