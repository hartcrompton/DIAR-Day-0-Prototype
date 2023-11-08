#Admin

label conv_Admin:
    scene office_bg
    show admin at right
    ad "You're talking to me, the Admin! I'm a side character!"
    menu:
        "[[Chat a little.]":
            ad "We're chatting a little now!"
            pc "We sure are."
            jump conv_Admin
        "Bye":
            ad "See ya"
            jump FreeRoam

label .Outcome:
    if StoryCompletedTotal >= 3:
        if AdminClass == 0:
            "The Admin continued to keep up with current events in the art world, and hosted a lecture series for the Dr. [pc_name]."
            "Dr. [pc_name] had no idea who the Admin was, but signed a copy of [their] paper anyway."
            "It remains framed in the office to this day."
        else:
            "On [pc_name]'s advice, the Admin enrolled in classes and actually went outside."
            "Eventually earning foraging and guide certifications."
            "They now take stressed office workers on wilderness walks as part of Admin Adventures, LLC"
    else:
        "The Admin, overcommitted, disappeared. A tragic example of one who took on too much…and finished nothing."
    return