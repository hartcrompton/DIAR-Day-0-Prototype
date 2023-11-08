#VendingMachine

label conv_VendingMachine:
    scene foyer_bg
    show vendingmachine at right
    p "You're talking to me, the VendingMachine! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_VendingMachine
        "Bye":
            p "See ya"
            jump FreeRoam

label .Outcome:
    if StoryCompletedTotal >= 3:
        "The vending machine happily dispenses snacks to the public, with one small glitch…"
        "On rainy days, when someone shows up drenched and down on their luck, a snack drops out for free."
        "A tribute to [pc_name], who saved their home. "
    else:
        "The museum closed, and the Vending Machine was emptied, crushed, cubed, and left in a landfill; never to be recycled."
        "{i}You can't save 'em all,{/i} the cube thinks. Over, and over, and over."
    return