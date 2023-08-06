#disposition system

default HoveredName = "Test"
default CharacterBio = "None selected."
default CharacterBeat = "0"
#character bios
default ArnolfiniBio = "Arnolfini bio goes here. Arnolfini bio goes here. Arnolfini bio goes here. Arnolfini bio goes here. Arnolfini bio goes here."
default TheDavidsBio = "The Davids bio goes here. The Davids bio goes here. The Davids bio goes here. The Davids bio goes here. The Davids bio goes here."
default GilgameshBio = "Gilgamesh bio goes here. Gilgamesh bio goes here. Gilgamesh bio goes here. Gilgamesh bio goes here. Gilgamesh bio goes here."
default GlimmerBio = "Glimmer bio goes here. Glimmer bio goes here. Glimmer bio goes here. Glimmer bio goes here. Glimmer bio goes here."
default MonaLisaBio = "Mona Lisa bio goes here. Mona Lisa bio goes here. Mona Lisa bio goes here. Mona Lisa bio goes here. Mona Lisa bio goes here."
default PosterBio = "Poster bio goes here. Poster bio goes here. Poster bio goes here. Poster bio goes here. Poster bio goes here."
default SaintCatherineBio = "Saint Catherine bio goes here. Saint Catherine bio goes here. Saint Catherine bio goes here. Saint Catherine bio goes here. Saint Catherine bio goes here."
default SoupAndSunflowersBio = "Soup and Sunflowers bio goes here. Soup and Sunflowers bio goes here. Soup and Sunflowers bio goes here. Soup and Sunflowers bio goes here. Soup and Sunflowers bio goes here."
default AdminBio = "Admin bio goes here. Admin bio goes here. Admin bio goes here. Admin bio goes here. Admin bio goes here."
default EaNasirBio = "Ea-Nasir bio goes here. Ea-Nasir bio goes here. Ea-Nasir bio goes here. Ea-Nasir bio goes here. Ea-Nasir bio goes here."
default NighthawksBio = "Nighthawks bio goes here. Nighthawks bio goes here. Nighthawks bio goes here. Nighthawks bio goes here. Nighthawks bio goes here."
default SueBio = "Sue bio goes here. Sue bio goes here. Sue bio goes here. Sue bio goes here. Sue bio goes here."
default TheodoreBio = "Theodore bio goes here. Theodore bio goes here. Theodore bio goes here. Theodore bio goes here. Theodore bio goes here."
default VendingMachineBio = "Vending Machine bio goes here. Vending Machine bio goes here. Vending Machine bio goes here. Vending Machine bio goes here. Vending Machine bio goes here."

screen DispositionMenu:
    #add "UI/Disposition/DispositionMenuBG.png"
    #imagemap:
        #ground "UI/Disposition/DispositionMenuBG.png"
       # hover "UI/Disposition/newmap/museum_map.jpg"
        #idle "UI/Disposition/DispositionMenuBG.png"
        #hotspot (1800, 200, 100, 100) 
        #hovered [SetVariable("TestName", "NewName")] unhovered [SetVariable("TestName", "OldName")]
    imagemap:
        ground "UI/Bios/bio bg.jpg"
        hover "UI/Bios/bio bg hover.jpg"

        #arnolfini
        hotspot (47, 100, 180, 180) action [SetVariable("HoveredName", "Arnolfini")] hovered [SetVariable("HoveredName", "Arnolfini"), SetVariable("CharacterBio", ArnolfiniBio), SetVariable("CharacterBeat", beat_Arnolfini)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #davids
        hotspot (270, 100, 180, 180) action [SetVariable("HoveredName", "The Davids")] hovered [SetVariable("HoveredName", "The Davids"), SetVariable("CharacterBio", TheDavidsBio), SetVariable("CharacterBeat", beat_Davids)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (493, 100, 180, 180) action [SetVariable("HoveredName", "Gilgamesh")] hovered [SetVariable("HoveredName", "Gilgamesh"), SetVariable("CharacterBio", GilgameshBio), SetVariable("CharacterBeat", beat_Gilgamesh)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (716, 100, 180, 180) action [SetVariable("HoveredName", "Glimmer")] hovered [SetVariable("HoveredName", "Glimmer"), SetVariable("CharacterBio", GlimmerBio), SetVariable("CharacterBeat", beat_Glimmer)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (47, 322, 180, 180) action [SetVariable("HoveredName", "Mona Lisa")] hovered [SetVariable("HoveredName", "Mona Lisa"), SetVariable("CharacterBio", MonaLisaBio), SetVariable("CharacterBeat", beat_MonaLisa)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (270, 322, 180, 180) action [SetVariable("HoveredName", "Poster")] hovered [SetVariable("HoveredName", "Poster"), SetVariable("CharacterBio", PosterBio), SetVariable("CharacterBeat", beat_Poster)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (493, 322, 180, 180) action [SetVariable("HoveredName", "Saint Catherine")] hovered [SetVariable("HoveredName", "Saint Catherine"), SetVariable("CharacterBio", SaintCatherineBio), SetVariable("CharacterBeat", beat_SaintCatherine)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (716, 322, 180, 180) action [SetVariable("HoveredName", "Soup and Sunflowers")] hovered [SetVariable("HoveredName", "Soup and Sunflowers"), SetVariable("CharacterBio", SoupAndSunflowersBio), SetVariable("CharacterBeat", beat_SoupAndSunflowers)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (47, 544, 180, 180) action [SetVariable("HoveredName", "Admin")] hovered [SetVariable("HoveredName", "Admin"), SetVariable("CharacterBio", AdminBio), SetVariable("CharacterBeat", False)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (270, 544, 180, 180) action [SetVariable("HoveredName", "Ea-Nasir")] hovered [SetVariable("HoveredName", "Ea-Nasir"), SetVariable("CharacterBio", EaNasirBio), SetVariable("CharacterBeat", False)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (493, 544, 180, 180) action [SetVariable("HoveredName", "Nighthawks")] hovered [SetVariable("HoveredName", "Nighthawks"), SetVariable("CharacterBio", NighthawksBio), SetVariable("CharacterBeat", False)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (716, 544, 180, 180) action [SetVariable("HoveredName", "Sue")] hovered [SetVariable("HoveredName", "Sue"), SetVariable("CharacterBio", SueBio), SetVariable("CharacterBeat", False)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (47, 766, 180, 180) action [SetVariable("HoveredName", "Theodore")] hovered [SetVariable("HoveredName", "Theodore"), SetVariable("CharacterBio", TheodoreBio), SetVariable("CharacterBeat", False)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]
        #arnolfini
        hotspot (270, 766, 180, 180) action [SetVariable("HoveredName", "Vending Machine")] hovered [SetVariable("HoveredName", "Vending Machine"), SetVariable("CharacterBio", VendingMachineBio), SetVariable("CharacterBeat", False)] unhovered [SetVariable("HoveredName", "???"), SetVariable("CharacterBio", '--'), SetVariable("CharacterBeat", False)]

    #arnolfini
    #$ d_LabelName = d_Label.ValueToLabel(d_Arnolfini)
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
                if CharacterBeat:
                    text "Beats Progress: [CharacterBeat] / 4" size 40
                text [CharacterBio] size 40

                
    
    textbutton "Return":
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        action Return()

#deprecated
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
#deprecated
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


