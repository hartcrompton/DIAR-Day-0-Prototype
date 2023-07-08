#game ending
label final_exhibit:
    meta "It's the final exhibit today!"
    call TotalDisposition
    meta "Current disposition is: [d_Total]"
    if d_Total >= 0:
        meta "That means the museum is saved!" 
    if d_Total < 0:
        meta "That means the museum is closing :("
    #outcomes for individual characters go here
    return