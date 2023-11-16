#game ending
default GoodLine1 = 0
default GoodLine2 = 0
default ClosedLine_ar = 0
default ClosedLine_d = 0
default ClosedLine_gi = 0
default ClosedLine_m = 0
default ClosedLine_st = 0
default ClosedLine_ss = 0
default ClosedLine_p = 0

label final_exhibit:
    scene black with fade
    show day countdown 4 at truecenter with fade
    $ renpy.pause(1.0)
    show day_countdown at AlphaIn
    $ renpy.pause(4.5)
    jump AllOutcomes
    return

label AllOutcomes:
    scene foyer bg with fade:
        blur 5
    play music "music/Admin_ZY_02.wav" volume 0.6
    show admin at truecenter:
        zoom .8
    ad "Today's the day!"
    menu:
        "You sound happy.":
            ad "I'm not! But if I stop smiling the stress will catch up!"
        "Wish me luck.":
            ad "I'm sure you've done your best!"
        "Are you nervous?":
            ad "Not at all! I just have that thing where I feel like my stomach is going inside out."
    ad "Oh, big donor on the other line, I hope the Gala goes well!"
    play sound "sfx/AdminHangup.wav"
    stop music fadeout 0.3
    hide admin
    play sound "sfx/InteriorSound.wav" volume 0.5
    play sfx2 "sfx/Gallery_Crowd.wav" volume 0.7 fadein 5.0
    "Anyway, it's out of your hands now."
    "Through the window, you already see press and caterers arriving."
    "Nothing left to do but open the doors and let the Grand Gala begin."
    stop music fadeout 1.0
    scene black with fade
    #SOUND EFFECTS HERE OF CROWD, DRINKS, PHOTOS, ETC.
    if StoryCompletedTotal >= 3:
        play music "music/Ending_Good_S_02.wav" volume 0.5
        "The Grand Gala was a blur."
        "But somehow, you managed it."
        "The artworks were compelling, filled with renewed energy and meaning."
        "Guests, donors, historians, and more were enthralled by the collection."
    else:
        play music "music/Ending_Bad_R_01.wav" volume 0.5
        "The day was a blur."
        "And--in spite of your best efforts--the Grand Gala was a mess."
        "The art was disjointed and unfulfilled."
        "The donors were unimpressed, to say the least."
        "Even the catering was uneven, with some guests trying their luck with out-of-date candy from the vending machine."
    call conv_Arnolfini.Outcome from _call_conv_Arnolfini_Outcome_1
    call conv_Davids.Outcome from _call_conv_Davids_Outcome_1
    call conv_Gilgamesh.Outcome from _call_conv_Gilgamesh_Outcome_1
    call conv_MonaLisa.Outcome from _call_conv_MonaLisa_Outcome_1
    call conv_SaintCatherine.Outcome from _call_conv_SaintCatherine_Outcome_1
    call conv_SoupAndSunflowers.Outcome from _call_conv_SoupAndSunflowers_Outcome_1
    call conv_Poster.Outcome from _call_conv_Poster_Outcome_1
    call conv_Admin.Outcome from _call_conv_Admin_Outcome
    call conv_VendingMachine.Outcome from _call_conv_VendingMachine_Outcome
    scene black with fade
    if StoryCompletedTotal >= 3:
        "In the wake of the Gala, you've already received several emails from collectors and interviewers, all eager to meet the new curator."
        "That is, if you decide to stay on."
    else:
        "In the wake of the Gala, you go back to your life."
        "The museum closes. Most pieces return to private collections, some find their ways into renowned museums."
        "But none forget the first curator who could really hear them."
    stop sfx2 fadeout 0.5
    scene black
    show credits end at truecenter with fade
    $ renpy.pause(30.0)
    show credits_art end at truecenter with fade
    $ renpy.pause(10.0)
    show credits_audio end at truecenter with fade
    $ renpy.pause(10.0)
    stop music
    $ renpy.set_return_stack([])
    return