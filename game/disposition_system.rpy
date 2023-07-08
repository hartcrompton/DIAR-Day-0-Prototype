#disposition system

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