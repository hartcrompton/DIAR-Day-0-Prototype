#SaintCatherine

default beat_SaintCatherine = 1
default SaintHuman = 0
default SaintSaintly = 0
default st_glass = 0
default st_plastic = 0
# 0 is Saint, 1 is Human
default SaintPersonality = 0
default SaintHumanChoice = "NONE"

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
    call advance_time
    jump expression "conv_SaintCatherine" + "." + "beat" + "%d" % beat_SaintCatherine

label .beat1:
    $ SaintHuman = 0
    $ SaintSaintly = 0
    #"The dull gallery wall peeks out through the holes in the stained glass."
    #"You open a door marked \"Staff Only.\" The last fluorescent bulb casts cold light on dusty racks."
    "The dull gallery wall peeks out through the holes in the stained glass."
    "Saint Catherine looks dull and dusty with no light behind her."
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
    st "Though I'm not sure where to begin with these breaks."
    menu:
        "Broken glass, yeah, let's talk materials.":
            st "Glass is the traditional repair, but maybe a modern audience would relate to modern materials?"
        "Breaks in your memory, like amnesia?":
            st "Prayers have always told me who I am. Without them, I can't make sense of the fragments."
    st "It's strange to think I'll be restored after so long."
    st "I wonder what will change?"
    st "But I've kept you long enough. The others need you."
    st "Come back when you have time. I like talking with you."
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
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            pc "Powerful, important, and influential."
            st "From a [pc_work] to a facilitator of public learning. I am glad to support your good works."
            st "As a saint, the light I shine would grant solace and wisdom to all of our visitors."
        "Unbothered and happy, with lots of freedom.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            st "Ouais? I agree. With your background as a [pc_work], you're perfect for this."
            st "Look at this huge building! We'll make this place welcoming and fun."
    st "Thank you for telling me the truth. It resonates."
    menu:
        "Wait, your voice sounds different.":
            if SaintSaintly > SaintHuman:
                st "Speaking with you has given me clarity, that I may return to my sacred work."
            else:
                st "Do I? I feel more relaxed, you know? Like we could be friends." 
        "I shall endeavor to address you properly, O Saint.":
            if SaintSaintly > SaintHuman:
                st "Blessings upon the bold and principled. Be at ease, our work is what matters, not the way you address me."
            else:
                st "Zut alors, please don't, that's not necessary. I'm just a regular person, like you."
    st "You see yourself reflected in the glass, I see myself reflected in you; that's all."
    st "I have another question for you."
    st "How would you like our guests to feel after they visit the museum?"
    menu:
        "Like we're all connected.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            st "How lovely, everyday people enjoying the same light. If I were mortal, I'd feel part of that story."
        "Like they learned something.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
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
    st "Part of me delivered lunches to the glass studio. One of the artists there stared, but we never spoke."
    st "Part of me also debated philosophy -- I protected archivists, students, wheelwrights, and many others."
    st "I've witnessed centuries of joy and sorrow. Shone light on so many when they believed they were alone."
    st "You're the first person who has truly heard me in return."
    st "Yet I keep returning to the same question."
    st "Is one's truest self ephemeral... or eternal?"
    menu:
        "Is this what it's like to listen to prayers all day?":
            pass
        "I've never thought about it before.":
            pass
    st "Perhaps a smaller question... Is the real you your grand deeds, or your everyday moments?"
    menu:
        "Grand deeds. The overall impact of my legacy.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            pass
        "Everyday stuff, for sure. That's more consistent over time.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            pass
    st "Hm..."
    st "I believe you. "
    st "Do you think it's the same for me? What do you believe?"

    menu:
        "Your true nature is mortal.":
            $ SaintHumanChoice = "human"
            $ SaintPersonality = 1
            $ SaintHuman += 1
            st "The glass artist. He'd never seen the saint, so he made her in my likeness."
            pc "Wait, so you're not a saint from Alexandria, you're a random French girl the artist was in love with?"
            st "I didn't mean to deceive you. I don't think he did, either."
        "Your essence is divine.":
            $ SaintHumanChoice = "a saint"
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            st "Yes... I remember. An amalgam of great women; the strength of their ideas. I feel them all."
            st "Hypatia, or St. Dorothea of Alexandria. All of us, philosophers. We reflect each other."
    st "I remain...Catherine."
    st "Do you still feel like an imposter, here?"
    menu:
        "Yeah, a little.":
            pass
        "No, I'm getting the hang of it.":
            pass
    st "I see. Whatever your future holds..."
    st "You remain [pc_name]."
    "The stained glass is less clouded, its colors more vivid."
    st "I feel much improved, my friend. You are a marvel."
    st "All that remains are my repairs. When you have time, of course."

    #####
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat4:

    st "Ah, you've returned! There's still the matter of my repairs."
    st "Charles took some measurements before he left, but never finished the work."
    "A faded note-card taped to the wall indicates the size and shape of each break."
    menu:
        "Sweet, I'll take those.":
            pass
        "Let me double-check they're correct.":
            pass
    st "Can I ask you something else?"
    st "How did you decide my true self was [SaintHumanChoice]?"
    menu:
        "It was best for you.":
            pass
        "It was the right call for the museum.":
            pass
    st "I see. Thank you for telling me. You made the right decision."
    menu:
        "Did Charles already order glass?":
            st "If he did, he never returned with it."
        "I don't know where to start.":
            st "Oh... Well we need tools and materials."
    st "However we proceed, the work must be finished well before the doors open for the gala."
    st "While I do feel better, and I'm grateful; I can't be displayed in this... state."
    menu:
        "I'm not a glass artist!":
            pass
        "Does it have to be glass?":
            pass
    st "I didn't consider that. What else did you have in mind?"
    menu:
        "The vending machine casts welcoming light.":
            pass
        "A modern polymer. Very durable.":
            pass
    st "You want to fix my stained glass... with shards of plastic?"
    pc "Glass isn't the only material that colors light."
    ###if statements here for the divergent dialogue
    if SaintHuman > SaintSaintly:
        st "I'm glad to finally drop the great-and-glorious-saint act, but I don't want to look weird!"
    else:
        st "You would cheapen my efforts to serve humanity by patching me like a common appliance?"
    #are these supposed to be choices?
    menu:
        "It might be our only option.":
            pass
        "Let's talk this through.":
            pass
    st "You're right. Perhaps a modern image would free me from the trappings of the past."
    st "Then again, my full glory would shine for all who need me if we used traditional repairs."
    if SaintHumanChoice == "mortal":
        st "But you told me I was mortal. Have you changed your mind?"
    if SaintHumanChoice == "a saint":
        st "But you told me I was divine. Have you changed your mind?"
    #are these supposed to be choices?
    menu:
        "You're your own person, Catherine.":
            pass
        "Let's try something else.":
            pass
    pc "Your breaks represent the history you've lived through. They'll mean different things to different guests."
    pc "Why don't I say the word, and you tell me how it feels. How YOU feel. Not me telling you."
    if SaintHumanChoice == "mortal":
        st "How I feel... as just Catherine. Yes. Go ahead."
    if SaintHumanChoice == "a saint":
        st "How I feel... as Saint Catherine of Alexandria. Yes. Go ahead."
    menu:
        "Plastic, to keep your stories.":
            if SaintHuman > SaintSaintly:
                st "Honestly... I love it. It's beautiful. Everyone will see the work we've done together. I'm excited."
            else:
                st "It feels... Tawdry. Like my greater ideals will collapse to single points in time."
                st "If I were mortal then plastic would work, but that presentation no longer suits me."
        "Glass, true to tradition.":
            if SaintSaintly > SaintHuman:
                st "Beautiful. I would feel restored, light in spirit, and fully present with those who need me."
            else:
                st "Well, I... I'd do my best to be a 'proper' saint. Even though we know I'm not."
                st "But saints start as regular people, right? Maybe that's the miracle, to let the flaws be forgotten."
    st "That's how I feel. And your vision for the museum is important, too."
    st "Am I what I was, and still [SaintHumanChoice]?"
    menu:
        "Yes, nothing has changed.":
            pass
        "No, I was wrong.":
            $ SaintTemp = SaintSaintly
            $ SaintSaintly = SaintHuman
            $ SaintHuman = SaintTemp
            pass
    st "Good. And my repair... what's it to be?"
    menu:
        "Glass.":
            st "I'm ready."
            $ st_glass = 1
            #minigame go here
            call minigamestart_stainedglass("glass")
            pass
        "Plastic.":
            st "I'm ready."
            $ st_glass = 0
            call minigamestart_stainedglass("plastic")
            pass
    if SaintSaintly > SaintHuman:
        if st_glass == 0:
            st "This is amazing! I feel like myself again! I remember my friends, the smell of lavender and sage..."
        if st_glass == 1:
            st "It's... A masterpiece. Beautiful. I'll do my best to be equal to this honor."
    if SaintHuman > SaintSaintly:
        if st_glass == 0:
            st "Fascinating. A new way to tell an old story. You've done well."
        if st_glass == 1:
            st "My friend, you are a miracle. I remember my purpose, the smell of aromatic frankincense... "
    st "I'm ready to take my place among the others."
    "You hang the stained glass over a window. She casts colors all over."
    st "The view is beautiful from here. I can see everyone. Their sadness... Their joy..."
    st "I'm not lonely anymore."
    st "Thank you."
    "Following lines play during ending:"
    if SaintPersonality == 1:
        if st_glass == 0:
            st "The saint is a welcoming presence emphasizing the evolving story of art... "
            st "...including those who protected, restored, and changed the work in the intervening centuries."
        if st_glass == 1:
            st "The saint shines down with kindness, evoking the time and place of its manufacture rather than the grand ideals it represents."
            st "Visitors swear they've seen a girl just like her serving coffee at the diner down the street."
    if SaintPersonality == 0:
        if st_glass == 0:
            st "The saint is a commanding yet jarring presence, almost punk, the juxtaposition of high ideals from base material mirroring and echoing her relationship to artisans and wheelwrights."
            st "Visitors leave energized to fight for what they believe in."
        if st_glass == 1:
            st "The saint shines inspiring light on all. Benches in her gallery space prove comforting place to sit while weighing difficult decisions."
            st "Visitors leave with the sense that they have been heard and seen, empowered with the right questions to find the answers they seek."
    #####
   
    
    ###
    
    $ beat_SaintCatherine += 1
    jump FreeRoam

label .Outcome:
    if beat_SaintCatherine == 5:
        if SaintPersonality == 1:
            if st_glass == 0:
                st "The saint is a welcoming presence emphasizing the evolving story of art... "
                st "...including those who protected, restored, and changed the work in the intervening centuries."
            if st_glass == 1:
                st "The saint shines down with kindness, evoking the time and place of its manufacture rather than the grand ideals it represents."
                st "Visitors swear they've seen a girl just like her serving coffee at the diner down the street."
        if SaintPersonality == 0:
            if st_glass == 0:
                st "The saint is a commanding yet jarring presence, almost punk, the juxtaposition of high ideals from base material mirroring and echoing her relationship to artisans and wheelwrights."
                st "Visitors leave energized to fight for what they believe in."
            if st_glass == 1:
                st "The saint shines inspiring light on all. Benches in her gallery space prove comforting place to sit while weighing difficult decisions."
                st "Visitors leave with the sense that they have been heard and seen, empowered with the right questions to find the answers they seek."
    elif beat_SaintCatherine > 1:
        "The saint enjoys a brief bit of fame as a visitor’s post about her goes viral. Unfortunately, the good and bad faith arguing keep the saint locked in uncertainty. "
        "At certain angles, tears can be seen on her face; but that may just be a flaw in the glass."
    else:
        #bad
        "The saint is discovered in an unlocked room, leaning against the wall, a sample “untitled, -anonymous” curation plaque discarded on the floor next to her." 
        "When the odd visitor passing by the saint is overcome with a sense of loss and abandonment, and have difficulty speaking their mind for the next several days."
    return