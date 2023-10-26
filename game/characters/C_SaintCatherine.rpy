#SaintCatherine

default beat_SaintCatherine = 1
default SaintHuman = 0
default SaintSaintly = 0
default st_glass = 0
default st_plastic = 0
# 0 is Saint, 1 is Human
default SaintPersonality = 0
default SaintHumanChoice = "NONE"
default SaintHair = 0
default SaintRepaired = 0
default SaintTimeout = 0
#figure out the timing and flags for this
image SaintPortrait = ConditionSwitch(
    "(SaintHair == 1) and (SaintRepaired == 0)", "images/Characters/SaintCatherine/saintbrunettebroken.png",
    "(SaintHair == 0) and (SaintRepaired == 0)", "images/Characters/SaintCatherine/saintblondebroken.png",
    "(SaintHair == 0) and (SaintRepaired == 1) and (st_glass == 0)", "images/Characters/SaintCatherine/saintblondeplastic.png",
    "(SaintHair == 0) and (SaintRepaired == 1) and (st_glass == 1)", "images/Characters/SaintCatherine/saintblondeglass.png",
    "(SaintHair == 1) and (SaintRepaired == 1) and (st_glass == 0)", "images/Characters/SaintCatherine/saintbrunetteplastic.png",
    "(SaintHair == 1) and (SaintRepaired == 1) and (st_glass == 1)", "images/Characters/SaintCatherine/saintbrunetteglass.png")

label conv_SaintCatherine:
########sound start hook here (for beat 1-4 specific track) SPECIFICALLY USE MUSIC CHANNEL.
########Using music channel means should not need a STOP MUSIC command.
    play music "music/B14_W_02.wav" fadein 0.4 volume 0.4
    scene storage bg:
        blur 3
    show SaintPortrait at truecenter:
        zoom .8
        yoffset -100
    jump .use_action
    #menu:
    #    "Beat [beat_SaintCatherine]" if actions > 0 and beat_SaintCatherine < 5:
    #        jump .use_action
    #    "Bye":
    #        st "See ya"
    #        jump FreeRoam
    #    "Reset Beats":
    #        "Beats reset."
    #        $ beat_SaintCatherine = 1
    #        jump conv_SaintCatherine

label .use_action:
    #menu:
    #    st "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_SaintCatherine" + "." + "beat" + "%d" % beat_SaintCatherine
    #    "No, not really.":
    #        st "Understandable."
    #        jump conv_SaintCatherine
    #call advance_time from _call_advance_time_5
    $ SaintTimeout = 1
    jump expression "conv_SaintCatherine" + "." + "beat" + "%d" % beat_SaintCatherine

label .beat1:
    $ SaintHuman = 0
    $ SaintSaintly = 0
    #"The dull gallery wall peeks out through the holes in the stained glass."
    "You find the stained glass in a closet marked \"Staff Only.\""
    "The glass is dark and jagged under a layer of dust."
    menu:
        "She's as busted as the museum.":
            pass
        "Where do I start with this?":
            pass
    st neutral "It sounds like you have misgivings, [pc_work]. Can I help in some way?"
    pc  "You can hear me?"
    st neutral "Of course. Worries, fears, wishes. Prayers, if you like."
    pc  "Who are you?"
    st neutral "I'm…not sure. Listening was my duty for many years."
    st neutral "No…it was my joy. It gave me meaning to hold space for those in need. I'm Catherine. Or I was."
    st neutral "But I've been in storage for so long, no prayers have told me who to be."
    st neutral "Maybe we can help each other."
    menu:
        "The admin called you St. Catherine.":
            st neutral "So did your predecessor, Charles; but he wasn't much for contemplation. I feel…"
        "What do you need help with?":
            st neutral "Perhaps you could shed light on on my issue, as I have done for others?"
    st laugh "Part of me feels powerful. High-born, persuasive, willing to die for my faith."
    st neutral "These memories are in Latin."
    st happy "Part of me feels carefree. Low-born, clever, surrounded by friends."
    st neutral "These memories are in French."
    menu:
        "You're two people at once?":
            st neutral "I remember both selves, but I'm not sure which one is real: the great saint, or the mortal woman?"
        "Nobody can tell you who to be.":
            st neutral "No, but I want to help. Strong people inspire strength, kind people nurture kindness."
    st neutral "I've fulfilled both roles. Light filtered through me, people's hopes and worries filtered through them…"
    st neutral "…and together we found a way through the dark."
    st sigh "But now, I…With no light, no prayers, no purpose; I feel broken."
    menu:
        "Your sense of self is the key. That's important.":
            st neutral "Thank you. Our guests won't be able to hear me, so my repairs should match my true self. I'll feel more solid that way."
        "New glass before the gala will fix you right up.":
            st neutral "Agreed, and once we discover the truth, I should be repaired with the right materials to reflect that truth."
    st sweat "You've been placed in the shoes of greatness. Now you must live up to it. I know what that's like."
    st neutral "I have faith in you."
    st question "Though I'm not sure where to begin with these breaks."
    menu:
        "Broken glass. Yes. Let's talk materials.":
            st neutral "Glass is the traditional repair, but maybe a modern audience would relate to modern materials?"
        "Breaks in your memory, like amnesia?":
            st neutral "Prayers have always told me who I am, but they're one-way. Conversation may yield more lasting insight."
    st neutral "I can scarcely believe I'll be restored after so long."
    st neutral "I wonder what will change?"
    st neutral "But I've kept you long enough. The others need you."
    st happy "Come back when you have time. I like talking with you."
    #######
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat2:
    st happy "[pc_name], I'm glad you've returned."
    st question "Will you talk with me awhile? I think it will help me understand myself."
    menu:
        "Uh, like a pastor?":
            pass
        "You mean like a therapist?":
            pass
    st neutral "Like yourself, silly. I want to know about you. Your world. What the museum guests might need from us."
    menu:
        "Weird, but sure.":
            pass
        "What do you want to know?":
            pass
    st neutral "I'd like to know about your hopes. Please answer honestly. It will help guide me."
    st question "You were someone else before the museum. Who do you hope to become, now that you have this role?"
    menu:
        "Powerful, important, and influential.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            st neutral "From a [pc_work] to a facilitator of public learning. I am glad to support your good works."
            st laugh "As a saint, the light I shine would grant wisdom to all of our visitors."
        "Unbothered and happy, with lots of freedom.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            st neutral "{i}Ouais?{/i} I agree. With your background as a [pc_work], you're perfect for this."
            st laugh "I'd like to be more approachable, too. This building is grand, but we'll make it welcoming and fun."
    st neutral "Thank you for telling me the truth. It resonates."
    menu:
        "Wait, your voice sounds different.":
            if SaintSaintly > SaintHuman:
                st neutral "Speaking with you has given me clarity, that I may return to my sacred work."
            else:
                st neutral "Does it? I feel more relaxed. Like we could be friends and skip the formalities a bit." 
        "I shall endeavor to address you properly, O Saint.":
            if SaintSaintly > SaintHuman:
                st neutral "Blessings upon the bold and principled. Be at ease, our work is what matters, not the way you address me."
            else:
                st surprise "{i}Zut alors{/i}, please don't, that's not necessary. We're both supporting the museum's guests, that's all."
    st neutral "You see yourself reflected in the glass, I see myself reflected in you."
    st neutral "Which brings me to my next question."
    st question "How would you like our guests to feel after they visit the museum?"
    menu:
        "Like we're all connected.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            st happy "How lovely, everyday people enjoying the same light. If I were mortal, I'd feel part of that story."
        "Like they learned something.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            st laugh "An admirable goal. As a saint, I would be delighted to help realize its success."
    st question "I think I understand you a little better. Is there anything you'd like to ask me?"
    menu:
        "How did you get broken?":
            st neutral "Oh…Those memories are painful, but I'll tell you."
        "Why did you ask me those questions?":
            st neutral "To ask and receive an answer, how can I resist? To ask and hear nothing…perhaps that's how these happened."
    st neutral "To ask and receive an answer, how can I resist? To ask and hear nothing…perhaps that's how these happened."
    st neutral "This break was from war. A shot that ricocheted…a life saved."
    st neutral "This break was from a rock. A little boy, on the worst day of his life."
    st neutral "A seamless repair might erase these stories."
    st question "I wonder, is it wrong to try and fix them?"
    menu:
        "Yes. We could incorporate the breaks.":
            st surprise "Finding perfection in the flaws…That's kind of you. I feel a little more human."
        "It's not wrong. You deserve proper repair.":
            st laugh "Aspiring toward perfection no matter we've endured…Most admirable. I feel the divine spark within."
    st neutral "The saint in me resonates with the eternal and inspiring; people's will to be greater than they are."
    st neutral "The mortal in me resonates with the everyday, and the small joys that shape us moment to moment."
    st sigh "Much remains unclear, but I will meditate on what we've discussed."
    st neutral "Farewell, my friend."
    #####
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat3:
    st neutral "I'm so glad to see you. I've been thinking our discussions. Do you have a moment?"
    menu:
        "Lots to do, keep it quick.":
            pass
        "Yes, what's on your mind?":
            pass
    st question "My memories feel like two different people. Can you make sense of them?"
    menu:
        "Are you a mix of people from the time?":
            st confused "Roman, Greek, French…There were nine Alexandrias, or was it thirteen? I don't know…It's all muddled."
        "When were you made?":
            st confused "The third century? But my glass was from the fifteenth century…I don't know…I don't know…"
    st neutral "I delivered lunches to the glass studio. One of the artists there stared, but we never spoke."
    st neutral "And I debated philosophy–I protected archivists, students, wheelwrights, and many others."
    st neutral "I've also witnessed centuries of joy and sorrow. Shone light on so many when they believed they were alone."
    st neutral "You're the first person who has truly heard me in return."
    st neutral "Yet I keep returning to the same question: what is at the core?"
    st question "Is one's truest self ephemeral…or eternal?"
    menu:
        "Is this what it's like to listen to prayers all day?":
            pass
        "I've never thought about it before.":
            pass
    if SaintHuman > SaintSaintly:
        st sweat "This is a lot, I know. You're doing great."
    else:
        st sweat "Your patience does you credit."
    st question "Perhaps a smaller question…Is the real you your grand deeds, or your everyday moments?"
    menu:
        "Grand deeds. The overall impact of my legacy.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            pass
        "Everyday stuff, for sure. That's more consistent over time.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            pass
    st confused "Hm…"
    st happy "I believe you. "
    st question "Do you think it's the same for me? What do you believe?"

    menu:
        "Your true nature is mortal.":
            $ SaintHumanChoice = "human"
            $ SaintPersonality = 1
            $ SaintHuman += 1
            $ SaintHair = 1
            st surprise "Of course. The glass artist. He'd never seen the saint, so he made her in my likeness."
            pc  "Wait, so you're not a saint from Alexandria, you're a random French girl the artist had a crush on?"
            st sweat "I didn't mean to deceive you. I don't think he did, either."
        "Your essence is divine.":
            $ SaintHumanChoice = "a saint"
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            $ SaintHair = 0
            st neutral "Yes…I remember. An amalgam of great women; the strength of their ideas. I feel them all."
            st neutral "Hypatia. Saint Dorothea of Alexandria. All of us, philosophers. We reflect each other."
    st sparkle "The question settled at last…"
    st sparkle "I remain…Catherine."
    st question "Do you still feel like an imposter, here?"
    menu:
        "Yeah, a little.":
            pass
        "No, I'm getting the hang of it.":
            pass
    st neutral "I see. Whatever your future holds…"
    st sparkle "You remain [pc_name]."
    "The stained glass is less clouded, its colors more vivid."
    st laugh "I feel much improved, my friend. You are a marvel."
    st neutral "All that remains are my repairs. When you have time, of course."

    #####
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat4:

    st neutral "Ah, you've returned! Shall we discuss the repairs?"
    st sweat "Charles took some measurements before he left, but never finished the work."
    "A faded note-card taped to the wall indicates the size and shape of each break."
    menu:
        "Sweet, I'll take those.":
            pass
        "Let me double-check they're correct.":
            pass
    st neutral "Can I ask you something else?"
    st neutral "When you concluded that my true self was [SaintHumanChoice]…"
    st question "How did you decide?"
    menu:
        "It was best for you.":
            pass
        "It was the right call for the museum.":
            pass
    st happy "I see. Thank you for telling me. You made the right decision."
    if SaintPersonality == 1:
            st neutral "With that behind us, what's the fix-it-up plan?"
    if SaintPersonality == 0:
        st neutral "With that debate settled, let us return to the matter of the glass."
    menu:
        "Did Charles already order glass?":
            st neutral "If he did, he never returned with it."
        "I don't know where to start.":
            st neutral "Tools and materials would be a fine place to start."
    st  "I confess I'm a little worried. The work must be finished well before the doors open for the gala."
    st sad "While I do feel better, and I'm grateful; I can't be displayed in this…state."
    menu:
        "Hiring a glass artist sounds complicated.":
            pass
        "Does it have to be glass?":
            pass
    st question "I didn't consider that. What else did you have in mind?"
    menu:
        "The vending machine casts welcoming light.":
            pass
        "A modern polymer. Very durable.":
            pass
    st surprise "You want to fix my stained glass…with shards of plastic?"
    pc  "Glass isn't the only material that colors light."
    ###if statements here for the divergent dialogue
    if SaintHuman > SaintSaintly:
        st surprise "I'm glad to finally drop the great-and-glorious-saint act, but I don't want to look weird!"
    else:
        st surprise "You would cheapen my efforts to serve humanity by patching me like a common appliance?"
    #are these supposed to be choices?
    menu:
        "It might be our only option!":
            pass
        "Well, let's talk this through.":
            pass
    st sweat "I just…Do you believe a modern image would free me from the trappings of the past?"
    st  "[pc_name], those who need me would benefit most from the light cast by more traditional repairs."
    if SaintHumanChoice == "mortal":
        st question "But you told me I was mortal. Have you changed your mind?"
    if SaintHumanChoice == "a saint":
        st question "But you told me I was divine. Have you changed your mind?"
    #are these supposed to be choices?
    menu:
        "You're your own person, Catherine.":
            pass
        "Let's try something else.":
            pass
    st sigh "…"
    pc  "Your breaks represent the history you've lived through. They'll mean different things to different guests."
    pc "But you just found {i}your{/i} voice."
    pc "Why don't I say the material, and you tell me how it feels. How YOU feel. No prayers. No artists. Just you."
    if SaintHumanChoice == "mortal":
        st bulb "How I feel…as just Catherine. Yes. Go ahead."
    if SaintHumanChoice == "a saint":
        st bulb "How I feel…as Saint Catherine of Alexandria. Yes. Go ahead."
    pc  "Ready? Here we go."
    menu:
        "Plastic, to keep your stories.":
            if SaintHuman > SaintSaintly:
                st sparkle "Honestly…I love it. It's beautiful. Everyone will see the work we've done together. I'm excited."
            else:
                st sad "It feels…Tawdry. Like my greater ideals will collapse to a single point in time."
                st sad "If I were mortal then plastic would work, but that presentation no longer suits me."
        "Glass, true to tradition.":
            if SaintSaintly > SaintHuman:
                st sparkle "Beautiful. I would feel restored, light in spirit, and fully present with those who need me."
            else:
                st sad "Well, I…I'd do my best to be a 'proper' saint. Even though we know I'm not."
                st sad "But saints start as regular people, right? Maybe that's the miracle, to let the flaws be forgotten."
    st neutral "That's how I feel. That said, [pc_name], your vision for the museum is important, too."
    st question "Am I what I was, and still [SaintHumanChoice]?"
    menu:
        "Yes, nothing has changed.":
            st sparkle "Thank you. Your certainty is reassuring."
            pass
        "No, I was wrong.":
            $ SaintTemp = SaintSaintly
            $ SaintSaintly = SaintHuman
            $ SaintHuman = SaintTemp
            if SaintHair == 0:
                $ SaintHair = 1
            else:
                $ SaintHair = 0
            st sparkle "You've reflected on your views. I admire that. "
            pass
    st question "And my repair…what's it to be?"
    menu:
        "Glass.":
            st neutral "I'm ready."
            $ st_glass = 1
            #minigame go here
            call minigamestart_stainedglass("glass") from _call_minigamestart_stainedglass_2
            pass
        "Plastic.":
            st neutral "I'm ready."
            $ st_glass = 0
            call minigamestart_stainedglass("plastic") from _call_minigamestart_stainedglass_3
            pass
    $ SaintRepaired = 1
    scene storage bg
    show SaintPortrait at truecenter:
        zoom .8
    "The artwork has been repaired."
    if SaintSaintly >= SaintHuman:
        if st_glass == 0:
            st sad "Fascinating. A new way to tell an old story. You've done…well."
        if st_glass == 1:
            st sparkles "My friend, you are a miracle. I remember my purpose, the smell of aromatic frankincense…"
    if SaintHuman > SaintSaintly:
        if st_glass == 0:
            st sparkles "This is amazing! I feel like myself again! I remember my friends, the smell of lavender and sage…"
        if st_glass == 1:
            st sad "It's…A masterpiece. Beautiful. I'll do my best to be equal to this honor."
    st sparkles "I'm ready to take my place among the others."
    if SaintSaintly >= SaintHuman:
        if st_glass == 0:
            scene saint end pbl with fade
        if st_glass == 1:
            scene saint end gbl with fade
    if SaintHuman > SaintSaintly:
        if st_glass == 0:
            scene saint end pbr with fade
        if st_glass == 1:
            scene saint end gbr with fade
    "You hang the stained glass over a window. She casts colors all over."
    st sparkles "The view is beautiful from here. I can see everyone. Their sadness…Their joy…"
    st sparkles "I'm not lonely anymore."
    st sparkles "Thank you."
    #####
   
    
    ###
    $ StoryCompletedTotal += 1
    $ beat_SaintCatherine += 1
    jump FreeRoam

label .Outcome:
    if beat_SaintCatherine == 5:
        if SaintHuman > SaintSaintly:
            if st_glass == 0:
                scene saint end pbr
                "Catherine is a welcoming presence emphasizing the evolving story of art…"
                "…including those who have protected, restored, and changed the work in the intervening centuries."
            if st_glass == 1:
                scene saint end gbr
                "Catherine shines down with kindness, evoking the time and place of her manufacture rather than the grand ideals she represents."
                "Visitors swear they've seen a girl just like her serving coffee at a diner downtown."
        if SaintSaintly >= SaintHuman:
            if st_glass == 0:
                scene saint end pbl
                "The saint is a commanding yet jarring presence, almost punk, the juxtaposition of high ideals from base material mirroring and echoing her relationship to artisans and wheelwrights."
                "Visitors leave energized to fight for what they believe in."
            if st_glass == 1:
                scene saint end gbl
                "The saint shines inspiring light on all. Benches in her gallery space prove comforting place to sit while weighing difficult decisions."
                "Visitors leave with the sense that they have been heard and seen, empowered with the right questions to find the answers they seek."
    elif beat_SaintCatherine > 1:
        scene storage bg:
            blur 3
        show SaintPortrait at truecenter:
            zoom .8
            yoffset -100
        "The saint enjoys a brief bit of fame as a visitor’s post about her goes viral. Unfortunately, the good and bad faith arguing keep the saint locked in uncertainty. "
        "At certain angles, tears can be seen on her face; but that may just be a flaw in the glass."
    else:
        #bad
        scene storage bg:
            blur 3
        show SaintPortrait at truecenter:
            matrixcolor TintMatrix("#999999")
            zoom .8
            yoffset -100
        "The saint is discovered in an unlocked room, leaning against the wall, a sample “untitled, -anonymous” curation plaque discarded on the floor next to her." 
        "When the odd visitor passing by the saint is overcome with a sense of loss and abandonment, and have difficulty speaking their mind for the next several days."
    return