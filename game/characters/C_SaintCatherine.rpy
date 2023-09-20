#SaintCatherine

default beat_SaintCatherine = 1
default st_human = 0
default st_saint = 0
default st_glass = 0
default st_plastic = 0
default st_personality = 0

label conv_SaintCatherine:
    scene saintbackground
    show saintcatherine at right
    menu:
        "Beat [beat_SaintCatherine]" if actions > 0 and beat_SaintCatherine < 5:
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
    st "I've heard your misgivings, [pc_work]. Can I help in some way?"
    pc "You heard me?"
    st "Worries, fears, wishes. Prayers. Everything."
    pc "Who are you?"
    st "I'm... not sure. Listening was my purpose for many years."
    st "It's my joy and purpose to hold space for those in need. I'm Catherine. Or I was."
    st "But I've been in storage for so long, no one's told me who to be. Who they need me to be."
    st "Maybe we can help each other."
    menu:
        "The admin called you St. Catherine.":
            st "So did your predecessor, Charles."
        "What do you need help with?":
            st "It's dark in here. I need light."
    st "Part of me feels powerful. High-born, pursuasive, willing to die for my faith."
    st "These memories are in Latin."
    st "Part of me feels carefree. Low-born, clever, surrounded by friends."
    st "These memories are in French."
    menu:
        "You're two people at once?":
            st "I remember both selves, but I'm not sure which one is is real: the great saint, or the fellow mortal?"
        "Nobody can tell you who to be.":
            st "No, but I want to help. Strong people inspire strength, kind people make room for kindness."
    st "I helped shine light so others could find a way through their darkest moments."
    st "But I'm broken and I'm not sure how to fix it."
    menu:
        "Your sense of self is the most important.":
            st "Thank you. Our guests won't be able to hear me, so my repairs should match my true self. I'll feel more solid that way."
        "We gotta fix the glass by the opening.":
            st "Agreed, and once we discover the truth, I should be repaired with the right materials to reflect that truth."
    st "You've been placed in the shoes of greatness and now have to live up to it. I know what that's like."
    st "I have faith you'll succeed."
    menu:
        "Let's talk materials.":
            st "Glass is the traditional repair, but maybe a modern audience would relate to modern materials?"
        "Do you have some kind of amnesia?":
            st "Prayers have always told me who I am. Without them, I can't make sense of the fragments."
    st "I'd like to talk more, but the others need you."
    st "Come back when you have time."
    #######
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat2:
    st "[pc_name], I'm glad you've returned."
    st "Will you talk with me a while? I think it will help me understand myself."
    menu:
        "Uh, like a pastor?":
            pass
        "You mean like a therapist?":
            pass
    st "Like yourself, silly. I want to know about you. Your world. What the museum guests might need from us."
    menu:
        "Weird, but sure.":
            pass
        "What do you want to know?":
            pass
    st "I'd like to know about your hopes. Please answer honestly. It will help guide me."
    st "You were someone else before the museum. Who do you hope to become, now that you have this role?"
    menu:
        "Powerful, important, and influential.":
            $ st_saint += 1
            st "Yes. As a saint, I could lend shelter and the solace of knowledge to all of our visitors."
        "Unbothered and happy, with lots of freedom.":
            $ st_human += 1
            st "Yeah, look at this huge building! If I were mortal, I could help make this place welcoming and fun."
    st "Thank you for telling me the truth. It resonates."
    st "You've been working tirelessly to help us. To what end? How would you like our visitors to feel?"
    menu:
        "Like we're all connected.":
            st "How lovely, everyday people enjoying the same light. If I were mortal, I'd feel part of that story."
        "Like they learned something.":
            st "An admirable goal. As a saint, the light that shines through me will energize and empower the public."
    st "I think I understand you a little better. Is there anything you'd like to ask me?"
    menu:
        "How did you get broken?":
            st "Oh... Those memories are painful, but I'll tell you."
        "Why did you ask me those questions?":
            st "It's my purpose to shine light. I can do that best if I'm whole."
    st "This break was from war. A shot that ricocheted... a life saved."
    st "This break was from a rock. A little boy, on the worst day of his life."
    st "A seamless repair might erase these stories. Is it wrong to try and fix them?"
    menu:
        "Yes. We could incorporate them.":
            st "Finding perfection in the flaws... That's kind of you. I feel a little more human."
        "No. You deserve repair.":
            st "Aspiring toward perfection no matter we've endured... Most admirable. I feel the divine spark within."
    st "The saint in me resonates with the eternal and inspiring; people's will to be greater than they are."
    st "The mortal in me resonates with the everyday, and the small joys that shape us moment to moment."
    st "Much remains unclear, but I will meditate on what we've discussed."
    #####
    $ beat_SaintCatherine += 1
    jump FreeRoam
label .beat3:
    st "I'm so glad to see you. I heard we have a grand event soon. Do you have a moment?"
    menu:
        "Lots to do, keep it quick.":
            pass
        "Yeah, what's on your mind?":
            pass
    st "My memories feel like two different people. Can you make sense of them?"
    menu:
        "Are you a mix of people from the time?":
            st "Part of me is Roman, but also Greek, or maybe French? It's so muddled... I don't know."
        "When were you made?":
            st "The third century? But my glass was from the fifteenth century... I don't know... I don't know..."
    st "I delivered lunches to the glass studio. One of the artists there stared, but we never spoke."
    st "I also debated philosophy. I protected archivists, students, wheelwrights, and many others."
    st "I've witnessed centuries of joy and sorrow. Shone light on so many when they believed they were alone."
    st "You're the first person who has truly heard me in return."
    st "Please, we don't have much time. For this age, for this moment, who am I?"
    menu:
        "Your true nature is mortal.":
            $ st_human += 1
            st "The glass artist. He'd never seen the saint, so he made her in my likeness."
            pc "Wait, so you're not a saint from Alexandria, you're a random French girl the artist was in love with?"
            st "I didn't mean to deceive you. I don't think he did, either."
        "Your essence is divine.":
            $ st_saint += 1
            st "Yes... I remember. I feel them all."
            pc "Are you just you, or a mix of people from the time?"
            st "Hypatia, or St. Dorothea of Alexandria. Philosophers, both. Perhaps we reflect each other."
    st "I remain...Catherine."
    st "Do you still feel like an imposter, here?"
    menu:
        "Yeah, a little.":
            pass
        "No, I'm getting the hang of it.":
            pass
    st "I see. Whatever you choose..."
    st "You remain [pc_name]."
    "The stained glass is less clouded, its colors more vivid."
    st "I feel much improved, my friend. You are a marvel."
    st "All that remains are my repairs. When you have time, of course."

    #####
    $ beat_SaintCatherine += 1
    jump FreeRoam
label .beat4:
    st "Ah, you've returned!  (maybe another \"how are you feeling\" question? Do you feel weird making this decision for me? What is self determination in a museum context?)"
    "FINAL DISCUSSION WHERE THE PLAYER AND SAINT WEIGH GLASS VS. PLASTIC, REFLECT ON SAINT'S JOURNEY, PLAYER'S CHOICES"
    pc "Here's what I'm thinking..."
    "Glass isn't the only material that colors light."
    if st_human >= st_saint:
        "She might warm to modern materials, rather than being stuck in the role she was assigned."
    if st_saint >= st_human:
        "She might prefer traditional materials, so her full glory will shine for all who need her."
    pc "I'll see what we have and get back to you."
    "The stained glass should come out of storage soon."
    if st_human >= st_saint:
        "All this warm, welcoming energy needs a bigger space."
    if st_saint >= st_human:
        "If she can calm your mind in this little room, imagine what she'll do for visitors."
    st "Do we have what we need to fix my glass?"
    pc "Here's what I'm thinking..."
    menu:
        "Plastic, very modern.":
            if st_human >= st_saint:
                st "How innovative! That sounds perfect."
            if st_saint >= st_human:
                st "Unexpected, but we shall see."
                st "I was hoping for ..."
        "Glass, keep it classic.":
            if st_human >= st_saint:
                st "...Oh. Well, I'll do my best to be a 'proper' saint."
                st "I was hoping for ..."
            if st_saint >= st_human:
                st "Agreed. Your hard work will be celebrated; I'll see to it."
    "As you take measurements, you discuss the other works of art. The museum. Your hopes, and worries."
    "She listens."
    st "The materials you choose will represent all that we've discussed, so others may know me as well as you do."
    st "What is it to be? "
    menu:
        "Glass.":
            $ st_glass = 1
            #minigame go here
            pass
        "Plastic.":
            $ st_glass = 0
            #minigame go here
            pass
    if st_human >= st_saint:
        if st_glass == 0:
            st "This is amazing! I feel like myself again! I remember my friends, the smell of lavender and sage..."
        if st_glass == 1:
            st "It's... A masterpiece. Beautiful. I'll do my best to be equal to this honor."
    if st_saint >= st_human:
        if st_glass == 0:
            st "Fascinating. A new way to tell an old story. You've done well."
        if st_glass == 1:
            st "My friend, you are a miracle. I remember my purpose, the smell of aromatic frankincense... "
    st "Shall we go together? Let there be light!"
    "You hang the stained glass over a window. She casts colors all over."
    st "The view is beautiful from here. I can see everyone. Their sadness... Their joy..."
    st "I'm not lonely anymore."
    st "Thank you."
    
    ###
    
    $ beat_SaintCatherine += 1
    jump FreeRoam
