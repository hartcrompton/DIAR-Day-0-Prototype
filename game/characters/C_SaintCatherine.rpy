#SaintCatherine

default beat_SaintCatherine = 1
default st_human = 0
default st_saint = 0
default st_glass = 0
default st_plastic = 0

label conv_SaintCatherine:
    scene saintbackground
    show saintcatherine at right
    menu:
        "Beat [beat_SaintCatherine]" if actions > 0 and beat_SaintCatherine < 5:
            st "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            st "See ya"
            jump FreeRoam
        "Reset Beats":
            "Beats reset."
            $ beat_SaintCatherine = 1
            jump conv_SaintCatherine

label .use_action:
    #menu:
    #    st "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_SaintCatherine" + "." + "beat" + "%d" % beat_SaintCatherine
    #    "No, not really.":
    #        st "Understandable."
    #        jump conv_SaintCatherine
    jump expression "conv_SaintCatherine" + "." + "beat" + "%d" % beat_SaintCatherine

label .beat1:
    #"This is a stained glass of Saint Catherine of Alexandria. It's French. Or Roman? Either way, it's broken."
    "You open a door marked staff only. The last fluorescent bulb casts cold light on dusty racks."
    st "I've heard your misgivings, [pc_work]. Can I help in some way?"
    pc "You heard me?"
    st "Worries, fears, wishes. Prayers. Everything."
    pc "Who are you?:"
    st "I'm... not sure. Listening was my purpose for many years."
    st "It's my joy and purpose to hold space for those in need. I'm Catherine. Or I was."
    st "But I've been in storage for so long, no one's told me who to be. Who they need me to be."
    st "Maybe we can help each other."
    pc "The admin called you St. Catherine."
    st "So did your predecessor, Charles."
    pc "What do you need help with?"
    st "It's dark in here. I need light."
    st "Part of me feels powerful. High-born, pursuasive, willing to die for my faith."
    st "These memories are in Latin."
    st "Part of me feels carefree. Low-born, clever, surrounded by friends."
    st "These memories are in French."
    menu:
        st "You were someone else before the museum. Who do you hope to become?"    
        "Powerful":
            $ st_saint = 1
            $ st_human = 0
            st "Yes. We have a duty. We can give shelter and and the solace of knowledge to all visitors."
        "Friendly":
            $ st_human = 1
            $ st_saint = 0
            st "Yeah, look at this huge building! We can make this place welcoming and fun."
    "The glass seems clearer after spending time with you."
    st "We'll figure out how together."
    if st_human:
        st "Let me think about where to begin. See you soon!"
    if st_saint:
        st "Give me some time to think on it. meditate on the matter."

    "You have [actions] action(s) left."
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat2:
    if st_human:
        "Seeing Catherine feels like seeing an old friend. You relax immediately."
    if st_saint:
        "The moment you reenter storage to see St. Catherine, you feel energized."
    st "I've thought on our problem. I need to shine light on the hall."
    st "It will bring solace and clarity to everyone who visits us."
    st "But the rays must be whole. I must be whole."
    pc "How do we fix the rays?"
    st "The holes in my glass must be repaired."
    st "This break was from war. A shot that ricocheted... a life saved."
    st "This break was from a rock. A little boy, on the worst day of his life."
    st "My colors must be true."
    "A seamless glass repair might erase these stories."
    "Glass isn't the only material that colors light."
    if st_human:
        "She might warm to modern materials, rather than being stuck in the role she was assigned."
    if st_saint:
        "She might prefer traditional materials, so her full glory will shine for all who need her."
    pc "I'll see what we have and get back to you."

    "You have [actions] action(s) left."
    $ beat_SaintCatherine += 1
    jump FreeRoam
label .beat3:
    "The stained glass should come out of storage soon."
    if st_human:
        "All this warm, welcoming energy needs a bigger space."
    if st_saint:
        "If she can calm your mind in this little room, imagine what she'll do for visitors."
    st "Thank you for visiting me. I feel more myself than I have in ages."
    if st_human:
        st "I delivered lunches to the glass studio. One of the artists there stared, but we never spoke."
        pc "Wait, so you're not a saint from Alexandria, you're a random French girl the artist was in love with?"
        st "I didn't mean to deceive you. Or anyone. I'm sorry."
    if st_saint:
        st "I debated philosophy. I protected archivists, students, wheelwrights, and many others."
        pc "Are you just you, or a mix of people from the time?"
        st "Hypatia, or St. Dorothea of Alexandria. Philosophers, both. Perhaps we reflect each other."
    st "I remain...Catherine."
    menu:
        st "Do you still feel like an imposter, here?"
        "Yeah, a little.":
            pass
        "No, I'm getting the hang of it.":
            pass
    st "I see. Whatever you choose..."
    st "You remain [pc_name]."
    st "Do we have what we need to fix my glass?"
    menu:
        pc "Here's what I'm thinking..."
        "Plastic, very modern.":
            if st_human:
                st "How innovative! That sounds perfect."
            if st_saint:
                st "Unexpected, but we shall see."
        "Glass, keep it classic.":
            if st_human:
                st "...Oh. Well, I'll do my best to be a 'proper' saint."
            if st_saint:
                st "Agreed. Your hard work will be celebrated; I'll see to it."
    st "Let's take some measurements before you decide."
    st "The artists used a particular technique for repairs, I'll tell you all about it when you return."
    "As you work, you discuss the other works of art. The museum. Your hopes, and worries."
    "She listens."
    "The two of you measure out the pieces needed."

    "You have [actions] action(s) left."
    $ beat_SaintCatherine += 1
    jump FreeRoam
label .beat4:
    "With materials in hand, you return to your friend in storage."
    st "Is today the day? What have you decided?"
    menu:
        "Glass":
            $ st_glass = 1
            $ st_plastic = 0
            "Glass minigame"
        #jump to glass minigame
        "Plastic":
            $ st_plastic = 1
            $ st_glass = 0
            "Plastic minigame"
        #jump to plastic minigame
    if st_human:
        if st_plastic:
            st "This is amazing! I feel like myself again! I remember my friends, the smell of lavender and sage..."
        if st_glass:
            st "It's... A masterpiece. Beautiful. I'll do my best to be equal to this honor."
    if st_saint:
        if st_plastic:
            st "Fascinating. A new way to tell an old story. You've done well."
        if st_glass:
            st "My friend, you are a miracle. I remember my purpose, the smell of aromatic frankincense... "
    st "Shall we go to the gallery, together?"
    "You hang the stained glass over a window. She casts colors all over."
    st "The view is beautiful from here. I can see everyone. Their sadness... Their joy..."
    st "I'm not lonely anymore."
    st "Thank you."

    "You have [actions] action(s) left."
    $ beat_SaintCatherine += 1
    jump FreeRoam
