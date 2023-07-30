#disposition system

default HoveredName = "Test"

screen DispositionMenu:
    #add "UI/Disposition/DispositionMenuBG.png"
    #imagemap:
        #ground "UI/Disposition/DispositionMenuBG.png"
       # hover "UI/Disposition/newmap/museum_map.jpg"
        #idle "UI/Disposition/DispositionMenuBG.png"
        #hotspot (1800, 200, 100, 100) 
        #hovered [SetVariable("TestName", "NewName")] unhovered [SetVariable("TestName", "OldName")]
    imagemap:
        ground "newmap/museum_map.jpg"
        hover "UI/Disposition/DispositionMenuBG.png"

        #glimmer
        hotspot (30, 18, 163, 321) action [SetVariable("HoveredName", "Some really long name that will definitely be forced to wrap")] hovered [SetVariable("HoveredName", "Some really long name that will definitely be forced to wrap.")] unhovered [SetVariable("HoveredName", "OldName")]
        #sunflowers
        hotspot (217, 12,143,266) action Jump("conv_SoupAndSunflowers")
    #arnolfini
    $ d_LabelName = d_Label.ValueToLabel(d_Arnolfini)
    frame:
        xalign 0
        yalign .5
        xoffset 960
        yoffset 0
        xminimum 960
        xmaximum 960
        yminimum 900
        ymaximum 900
        hbox:
            box_wrap True
            spacing 40
            vbox:
                spacing 10
                text [HoveredName] size 40
                text "Beats Progress" size 40
                text "Disposition" size 40
            vbox:
                spacing 10
                text "" size 40
                text "[beat_Arnolfini] / 4" size 40
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