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
    st question "You have misgivings, [pc_work]. Can I help in some way?"
    pc  "You can hear me?"
    st neutral "Of course. Worries, fears, wishes. Prayers, if you like."
    pc  "Who are you?"
    st neutral "I'm…not sure."
    st question "I listen. It was my…duty? Joy?"
    st neutral "Wishes, whispers—prayers—the hopes and fears of others shaped me."
    st sad "But here it's just…quiet."
    menu:
        "Do you at least have a name?":
            st sigh "Saint…It's Catherine. Just Catherine."
        "The admin called you Saint Catherine.":
            st neutral "Saint? Your predecessor, Charles, said that as well. It's hard to remember."
        "Are you okay?":
            st neutral "I don't know."
    st laugh "I remember Latin script. Taking Emperor Maxentius' greatest minds to task for persecuting the innocent. And winning."
    st happy "But also--songs in French. Gossiping in town. Carefree days in summer, surrounded by friends."
    st question "I remember both selves, but I'm not sure which is real: the great saint, or the French girl?"
    menu:
        "You're two people at once?":
            st neutral "I've fulfilled both roles. Light filtered through me, people's hopes and worries filtered through them…"
            st happy "…and together we found a way through the dark."
        "You expect {i}me{/i} to tell {i}you{/i} which is real?":
            st neutral "If I'm to help, the answer matters. The strong inspire strength. The kind nurture kindness."
    st confused "But now, I…With no light, no prayers, no purpose; I feel broken."
    menu:
        "I mean…you {i}are{/i} broken.":
            st neutral "…Yes, you're right. It's wise to focus on practical matters. Thank you."
        "New glass before the gala will fix you right up.":
            st neutral "Repairs, yes! But the glass…would it fit true? Would it be {i}fitting{/i}?"
        "Yeah, we'll need to do {i}something{/i} about those sharp edges.":
            st neutral "Stained glass spoke to people once, do people still hear it? Or perhaps something else…"
        "It's just a few bumps and a little memory loss, no sweat.":
            st neutral "You're right. Broken glass and a muddled mind. Perhaps we can find the right treatment for both."
    st question "Can you truly restore me after so long?"
    menu:
        "Yes, of course!":
            pass
        "I mean, I can give it a shot…":
            pass
        "If I can't, we can hire someone.":
            pass
    st neutral "I wonder what will change?"
    st neutral "But I've kept you long enough. The others need you."
    st sweat "You've stepped into the shoes of greatness. Now you must live up to it. I know how that feels."
    st happy "Come back when you have time. I like talking with you."







    # #######
    # st neutral "It sounds like you have misgivings, [pc_work]. Can I help in some way?"
    # pc  "You can hear me?"
    # st neutral "Of course. Worries, fears, wishes. Prayers, if you like."
    # pc  "Who are you?"
    # st neutral "I'm…not sure. Listening was my duty for many years."
    # st neutral "No…it was my joy. It gave me meaning to hold space for those in need. I'm Catherine. Or I was."
    # st neutral "But I've been in storage for so long, no prayers have told me who to be."
    # st neutral "Maybe we can help each other."
    # menu:
    #     "The admin called you St. Catherine.":
    #         st neutral "So did your predecessor, Charles; but he wasn't much for contemplation. I feel…"
    #     "What do you need help with?":
    #         st neutral "Perhaps you could shed light on on my issue, as I have done for others?"
    # st laugh "Part of me feels powerful. High-born, persuasive, willing to die for my faith."
    # st neutral "These memories are in Latin."
    # st happy "Part of me feels carefree. Low-born, clever, surrounded by friends."
    # st neutral "These memories are in French."
    # menu:
    #     "You're two people at once?":
    #         st neutral "I remember both selves, but I'm not sure which one is real: the great saint, or the mortal woman?"
    #     "Nobody can tell you who to be.":
    #         st neutral "No, but I want to help. Strong people inspire strength, kind people nurture kindness."
    # st neutral "I've fulfilled both roles. Light filtered through me, people's hopes and worries filtered through them…"
    # st neutral "…and together we found a way through the dark."
    # st sigh "But now, I…With no light, no prayers, no purpose; I feel broken."
    # menu:
    #     "Your sense of self is the key. That's important.":
    #         st neutral "Thank you. Our guests won't be able to hear me, so my repairs should match my true self. I'll feel more solid that way."
    #     "New glass before the gala will fix you right up.":
    #         st neutral "Agreed, and once we discover the truth, I should be repaired with the right materials to reflect that truth."
    # st sweat "You've been placed in the shoes of greatness. Now you must live up to it. I know what that's like."
    # st neutral "I have faith in you."
    # st question "Though I'm not sure where to begin with these breaks."
    # menu:
    #     "Broken glass. Yes. Let's talk materials.":
    #         st neutral "Glass is the traditional repair, but maybe a modern audience would relate to modern materials?"
    #     "Breaks in your memory, like amnesia?":
    #         st neutral "Prayers have always told me who I am, but they're one-way. Conversation may yield more lasting insight."
    # st neutral "I can scarcely believe I'll be restored after so long."
    # st neutral "I wonder what will change?"
    # st neutral "But I've kept you long enough. The others need you."
    # st happy "Come back when you have time. I like talking with you."
    #######
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat2:
    st happy "[pc_name], I'm glad you've returned."
    st neutral "Will you talk with me awhile? It's nice to be heard for a change."
    menu:
        "Uh, like a pastor?":
            pass
        "You mean like a therapist?":
            pass
    st neutral "Like yourself, silly. I want to know about you. Your world. This museum, and your hopes for it."
    menu:
        "Weird, but sure.":
            pass
        "What do you want to know?":
            pass
        "You've been here longer than me.":
            st neutral "True, but you've been outside this {i}room{/i} longer than me."
            pass
    st neutral "This is a unique chance to have a discussion, rather than being called one thing or another through prayer."
    st neutral "You came to this place quite by accident. Another unique chance."
    st question "You were someone else before the museum. Who do you hope to become, now that you have this role?"
    menu:
        "For once, I'd like to have power and influence.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            st neutral "Like a calling. From a [pc_work] to a facilitator of learning."
            st laugh "As I said to Joan of Arc in her visions: stay true and persevere. Aid will come."
        "I just want to be happy. And free of dead-end jobs.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            st neutral "{i}Ouais?{/i} I agree. From [pc_work] to curator, this is your moment. You're perfect for this."
            st happy "I'd like to be more approachable, too. This building is grand, but we'll make it welcoming and fun."
    st neutral "Thank you for telling me. It resonates."
    menu:
        "Wait, your voice sounds different.":
            if SaintSaintly > SaintHuman:
                st neutral "Speaking with you has given me clarity, that I may return to my sacred work."
            else:
                st neutral "Does it? I feel more relaxed. Like we could be friends and skip the formalities a bit."
        "I shall endeavor to address you properly, O Saint.":
            if SaintSaintly > SaintHuman:
                st laugh "Blessings upon the bold and principled. Be at ease, our work is what matters, not the way you address me."
            else:
                st surprise "{i}Zut alors{/i}, please don't, that's not necessary. We're both supporting the museum's guests, that's all."
    st neutral "You know, I haven't been able to speak to someone before. To see myself reflected."
    st question "Some find such reflecting restorative. Is that what you'd like for our guests as well?"
    menu:
        "I'd want them to feel connected.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            st happy "Everyday, normal people enjoying the same light! That's a story I'd like to be part of."
        "Mostly, I hope they learn something here.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            st laugh "An admirable goal. One I could assist with: teaching is the first and last duty of many saints."
    st question "I think I understand you a little better. Is there anything you'd like to ask me?"
    menu:
        "How did you get broken?":
            st sad "Oh…those memories are painful, but I'll tell you."
        "Why did you ask me those questions?":
            st sigh "To ask and receive an answer, how can I resist? To ask and hear nothing…perhaps that's how these happened."
    st neutral "This break was from war. A shot that ricocheted…a life saved."
    st neutral "This break was from a rock. A little boy, on the worst day of his life."
    st neutral "A seamless repair might erase these stories."
    st question "I wonder, is it wrong to try and fix them?"
    menu:
        "We could try to incorporate the breaks.":
            st surprise "Finding perfection in the flaws…That's so kind. I think I had a neighbor like you. Or someone I worked with."
        "It's not wrong. You deserve proper repair.":
            st laugh "Aspiring toward perfection no matter what we've endured…Poetic, to be broken and yet unbreakable."
    st neutral "Hm…I'm beginning to sort my own memory from the prayers of others."
    st laugh "Part of me stands among the eternal and the inspiring. The advocate. The protector. The One Who Breaks the Wheel."
    st happy "The other part…hah, just wants to lie by the Seine and gossip with my friends."
    st sigh "Forgive me. I need a moment to meditate on this."
    st neutral "Farewell, my friend."



    # st neutral "I'd like to know about your hopes. Please answer honestly. It will help guide me."
    # st question "You were someone else before the museum. Who do you hope to become, now that you have this role?"
    # menu:
    #     "Powerful, important, and influential.":
    #         $ SaintPersonality = 0
    #         $ SaintSaintly += 1
    #         st neutral "From a [pc_work] to a facilitator of public learning. I am glad to support your good works."
    #         st laugh "As a saint, the light I shine would grant wisdom to all of our visitors."
    #     "Unbothered and happy, with lots of freedom.":
    #         $ SaintPersonality = 1
    #         $ SaintHuman += 1
    #         st neutral "{i}Ouais?{/i} I agree. With your background as a [pc_work], you're perfect for this."
    #         st laugh "I'd like to be more approachable, too. This building is grand, but we'll make it welcoming and fun."
    # st neutral "Thank you for telling me the truth. It resonates."
    # menu:
    #     "Wait, your voice sounds different.":
    #         if SaintSaintly > SaintHuman:
    #             st neutral "Speaking with you has given me clarity, that I may return to my sacred work."
    #         else:
    #             st neutral "Does it? I feel more relaxed. Like we could be friends and skip the formalities a bit." 
    #     "I shall endeavor to address you properly, O Saint.":
    #         if SaintSaintly > SaintHuman:
    #             st neutral "Blessings upon the bold and principled. Be at ease, our work is what matters, not the way you address me."
    #         else:
    #             st surprise "{i}Zut alors{/i}, please don't, that's not necessary. We're both supporting the museum's guests, that's all."
    # st neutral "You see yourself reflected in the glass, I see myself reflected in you."
    # st neutral "Which brings me to my next question."
    # st question "How would you like our guests to feel after they visit the museum?"
    # menu:
    #     "Like we're all connected.":
    #         $ SaintPersonality = 1
    #         $ SaintHuman += 1
    #         st happy "How lovely, everyday people enjoying the same light. If I were mortal, I'd feel part of that story."
    #     "Like they learned something.":
    #         $ SaintPersonality = 0
    #         $ SaintSaintly += 1
    #         st laugh "An admirable goal. As a saint, I would be delighted to help realize its success."
    # st question "I think I understand you a little better. Is there anything you'd like to ask me?"
    # menu:
    #     "How did you get broken?":
    #         st neutral "Oh…Those memories are painful, but I'll tell you."
    #     "Why did you ask me those questions?":
    #         st neutral "To ask and receive an answer, how can I resist? To ask and hear nothing…perhaps that's how these happened."
    # st neutral "To ask and receive an answer, how can I resist? To ask and hear nothing…perhaps that's how these happened."
    # st neutral "This break was from war. A shot that ricocheted…a life saved."
    # st neutral "This break was from a rock. A little boy, on the worst day of his life."
    # st neutral "A seamless repair might erase these stories."
    # st question "I wonder, is it wrong to try and fix them?"
    # menu:
    #     "Yes. We could incorporate the breaks.":
    #         st surprise "Finding perfection in the flaws…That's kind of you. I feel a little more human."
    #     "It's not wrong. You deserve proper repair.":
    #         st laugh "Aspiring toward perfection no matter we've endured…Most admirable. I feel the divine spark within."
    # st neutral "The saint in me resonates with the eternal and inspiring; people's will to be greater than they are."
    # st neutral "The mortal in me resonates with the everyday, and the small joys that shape us moment to moment."
    # st sigh "Much remains unclear, but I will meditate on what we've discussed."
    # st neutral "Farewell, my friend."
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
    st question "You have clarity where I do not. These memories in French and Latin, can you help me make sense of them?"
    menu:
        "So you're a mix of people?":
            st confused "Roman, Greek, French…There were nine Alexandrias, or was it thirteen? I don't know…it's all muddled."
        "When were you made?":
            st confused "The third century? But my glass was from the fifteenth century…I don't know…I don't know…"
    st neutral "I delivered lunches to the glass studio. One of the artists there stared, but we never spoke."
    st neutral "And I debated philosophy–I protected archivists, students, wheelwrights, and many others."
    st neutral "I've also witnessed centuries of joy and sorrow. Shone light on so many when they believed they were alone."
    st neutral "You're the first person who has truly heard me in return."
    st sigh "And yet I have no idea what to say."
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
        "People only remember the big stuff. Grand deeds last.":
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            pass
        "The real you is your day-to-day self. Grand deeds are a blip.":
            $ SaintPersonality = 1
            $ SaintHuman += 1
            pass
    st neutral "Hm…"
    st happy "I believe you. "
    st question "Do you think it's the same for me? What do you believe?"
    menu:
        "I think you were just a girl from France. That's more plausible.":
            $ SaintHumanChoice = "human"
            $ SaintPersonality = 1
            $ SaintHuman += 1
            $ SaintHair = 1
            st surprise "Of course. The glass artist. He'd never seen the saint, so he made her in my likeness. A crush."
            st sweat "I didn't mean to deceive you. I don't think he did, either."
        "I think you truly are a saint.":
            $ SaintHumanChoice = "a saint"
            $ SaintPersonality = 0
            $ SaintSaintly += 1
            $ SaintHair = 0
            st laugh "Yes…I remember. An amalgam of great women; the strength of their ideas. I feel them all."
            st laugh "Hypatia. Saint Dorothea of Alexandria. All of us, philosophers. We reflect each other."
    st sparkle "The question is settled at last."
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






    # st question "My memories feel like two different people. Can you make sense of them?"
    # menu:
    #     "Are you a mix of people from the time?":
    #         st confused "Roman, Greek, French…There were nine Alexandrias, or was it thirteen? I don't know…It's all muddled."
    #     "When were you made?":
    #         st confused "The third century? But my glass was from the fifteenth century…I don't know…I don't know…"
    # st neutral "I delivered lunches to the glass studio. One of the artists there stared, but we never spoke."
    # st neutral "And I debated philosophy–I protected archivists, students, wheelwrights, and many others."
    # st neutral "I've also witnessed centuries of joy and sorrow. Shone light on so many when they believed they were alone."
    # st neutral "You're the first person who has truly heard me in return."
    # st neutral "Yet I keep returning to the same question: what is at the core?"
    # st question "Is one's truest self ephemeral…or eternal?"
    # menu:
    #     "Is this what it's like to listen to prayers all day?":
    #         pass
    #     "I've never thought about it before.":
    #         pass
    # if SaintHuman > SaintSaintly:
    #     st sweat "This is a lot, I know. You're doing great."
    # else:
    #     st sweat "Your patience does you credit."
    # st question "Perhaps a smaller question…Is the real you your grand deeds, or your everyday moments?"
    # menu:
    #     "Grand deeds. The overall impact of my legacy.":
    #         $ SaintPersonality = 0
    #         $ SaintSaintly += 1
    #         pass
    #     "Everyday stuff, for sure. That's more consistent over time.":
    #         $ SaintPersonality = 1
    #         $ SaintHuman += 1
    #         pass
    # st confused "Hm…"
    # st happy "I believe you. "
    # st question "Do you think it's the same for me? What do you believe?"

    # menu:
    #     "Your true nature is mortal.":
    #         $ SaintHumanChoice = "human"
    #         $ SaintPersonality = 1
    #         $ SaintHuman += 1
    #         $ SaintHair = 1
    #         st surprise "Of course. The glass artist. He'd never seen the saint, so he made her in my likeness."
    #         pc  "Wait, so you're not a saint from Alexandria, you're a random French girl the artist had a crush on?"
    #         st sweat "I didn't mean to deceive you. I don't think he did, either."
    #     "Your essence is divine.":
    #         $ SaintHumanChoice = "a saint"
    #         $ SaintPersonality = 0
    #         $ SaintSaintly += 1
    #         $ SaintHair = 0
    #         st neutral "Yes…I remember. An amalgam of great women; the strength of their ideas. I feel them all."
    #         st neutral "Hypatia. Saint Dorothea of Alexandria. All of us, philosophers. We reflect each other."
    # st sparkle "The question settled at last…"
    # st sparkle "I remain…Catherine."
    # st question "Do you still feel like an imposter, here?"
    # menu:
    #     "Yeah, a little.":
    #         pass
    #     "No, I'm getting the hang of it.":
    #         pass
    # st neutral "I see. Whatever your future holds…"
    # st sparkle "You remain [pc_name]."
    # "The stained glass is less clouded, its colors more vivid."
    # st laugh "I feel much improved, my friend. You are a marvel."
    # st neutral "All that remains are my repairs. When you have time, of course."

    #####
    $ beat_SaintCatherine += 1
    jump FreeRoam
    
label .beat4:
    st question "Ah, you've returned! Shall we discuss the repairs?"
    st sweat "Charles took some measurements before he left, but never finished the work."
    "A faded note-card taped to the wall indicates the size and shape of each break."
    menu:
        "Sweet, I'll take those.":
            pass
        "Let me double-check they're correct.":
            pass
    st neutral "Can I ask you something else?"
    st question "What made you decide I was [SaintHumanChoice]?"
    menu:
        "It was best for you.":
            pass
        "It was the right call for the museum.":
            pass
    st happy "I see. For what it's worth, I think you made the right decision."
    if SaintHumanChoice == "a saint":
        st neutral "With that debate settled, let us return to the matter of the glass."
    else:
        st neutral "With that behind us, what's the fix-it-up plan?"
    menu:
        "Did Charles already order glass?":
            st  "If he did, he never returned with it."
        "I don't know where to start.":
            st happy "Tools and materials would be a fine place to start."
    st  "I confess I'm a little worried. The work must be finished well before the doors open for the gala."
    st sad "While I do feel better, and I'm grateful; I can't be displayed in this…state."
    menu:
        "I'm not sure we have the budget to hire an artist.":
            pass
        "Wait, does it have to be glass?":
            pass
    st question "I didn't consider that. What else did you have in mind?"
    menu:
        "Have you met the Vending Machine? It casts a nice light.":
            pass
        "I can find some plastic. Way less fragile than glass.":
            pass
    st surprise "You want to fix my stained glass…with shards of plastic?"
    pc  "Glass isn't the only thing that colors light."
    if SaintHumanChoice == "a saint":
        st surprise "You would cheapen my efforts to serve humanity by patching me like a common appliance?"
    else:
        st surprise "I'm glad to finally drop the great-and-glorious-saint act, but I don't want to look weird!"
    menu:
        "It might be our only option!":
            pass
        "Well, let's talk this through.":
            pass
    if SaintHumanChoice == "a saint":
        st  "[pc_name], those who need me would benefit most from the light cast by more traditional repairs."
    else:
        st sweat "I just…Do you believe a modern image would free me from the trappings of the past?"
    st question "Besides, you told me I was [SaintHumanChoice]. Have you changed your mind?"
    menu:
        "You're your own person, Catherine.":
            pass
        "Let's try something else.":
            pass
    pc  "Why don't I say the material, and you tell me how it feels. Just as yourself."
    if SaintHumanChoice == "human":
        st bulb "How I feel…as just Catherine?"
    else:
        st bulb "How I feel…as Saint Catherine of Alexandria?"
    pc  "Yeah, no outside opinions from prayers or artists. I say the material, then you say what you think."
    pc  "Ready? Here we go."
    menu:
        "Plastic: to keep your stories.":
            if SaintHuman > SaintSaintly:
                st sparkle "Honestly…I love it. It's beautiful. Everyone will see the work we've done together. I'm excited."
            else:
                st sad "It feels…tawdry. Like my greater ideals will collapse to a single point in time."
                st sad "Plastic doesn't suit me. It wouldn't. Not as the saint I am now."
        "Glass: true to tradition.":
            if SaintSaintly > SaintHuman:
                st sparkle "Beautiful. I would feel restored, light in spirit, and fully present with those who need me."
            else:
                st sad "Well, I…I'd do my best to be a 'proper' saint. Even though we know I'm not."
                st sad "Saints start as regular people, right? Maybe that's the miracle, to erase the flaws, even if they were important to {i}me{/i}."
    st neutral "That's how I feel, [pc_name]. But I respect your vision for the museum…"
    st question "Am I what I was, and still [SaintHumanChoice]?"
    menu:
        "Yes, nothing has changed.":
            st sparkle "Thank you. Your certainty is reassuring."
        "No, I was wrong.":
            $ SaintTemp = SaintSaintly
            $ SaintSaintly = SaintHuman
            $ SaintHuman = SaintTemp
            if SaintHair == 0:
                $ SaintHair = 1
            else:
                $ SaintHair = 0
            st sparkle "You've reflected on your views. I admire that. "
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
    scene storage bg:
        blur 3
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
            st sad "It's…a masterpiece. Beautiful. I'll do my best to be equal to this honor."
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
    st sparkles "The view is beautiful from here. I can see everyone. Their sadness…their joy…"
    st sparkles "I'm not lonely anymore."
    st sparkles "Thank you."
    




    # ################
    # st neutral "Ah, you've returned! Shall we discuss the repairs?"
    # st sweat "Charles took some measurements before he left, but never finished the work."
    # "A faded note-card taped to the wall indicates the size and shape of each break."
    # menu:
    #     "Sweet, I'll take those.":
    #         pass
    #     "Let me double-check they're correct.":
    #         pass
    # st neutral "Can I ask you something else?"
    # st neutral "When you concluded that my true self was [SaintHumanChoice]…"
    # st question "How did you decide?"
    # menu:
    #     "It was best for you.":
    #         pass
    #     "It was the right call for the museum.":
    #         pass
    # st happy "I see. Thank you for telling me. You made the right decision."
    # if SaintPersonality == 1:
    #         st neutral "With that behind us, what's the fix-it-up plan?"
    # if SaintPersonality == 0:
    #     st neutral "With that debate settled, let us return to the matter of the glass."
    # menu:
    #     "Did Charles already order glass?":
    #         st neutral "If he did, he never returned with it."
    #     "I don't know where to start.":
    #         st neutral "Tools and materials would be a fine place to start."
    # st  "I confess I'm a little worried. The work must be finished well before the doors open for the gala."
    # st sad "While I do feel better, and I'm grateful; I can't be displayed in this…state."
    # menu:
    #     "Hiring a glass artist sounds complicated.":
    #         pass
    #     "Does it have to be glass?":
    #         pass
    # st question "I didn't consider that. What else did you have in mind?"
    # menu:
    #     "The vending machine casts welcoming light.":
    #         pass
    #     "A modern polymer. Very durable.":
    #         pass
    # st surprise "You want to fix my stained glass…with shards of plastic?"
    # pc  "Glass isn't the only material that colors light."
    # ###if statements here for the divergent dialogue
    # if SaintHuman > SaintSaintly:
    #     st surprise "I'm glad to finally drop the great-and-glorious-saint act, but I don't want to look weird!"
    # else:
    #     st surprise "You would cheapen my efforts to serve humanity by patching me like a common appliance?"
    # #are these supposed to be choices?
    # menu:
    #     "It might be our only option!":
    #         pass
    #     "Well, let's talk this through.":
    #         pass
    # st sweat "I just…Do you believe a modern image would free me from the trappings of the past?"
    # st  "[pc_name], those who need me would benefit most from the light cast by more traditional repairs."
    # if SaintHumanChoice == "mortal":
    #     st question "But you told me I was mortal. Have you changed your mind?"
    # if SaintHumanChoice == "a saint":
    #     st question "But you told me I was divine. Have you changed your mind?"
    # #are these supposed to be choices?
    # menu:
    #     "You're your own person, Catherine.":
    #         pass
    #     "Let's try something else.":
    #         pass
    # st sigh "…"
    # pc  "Your breaks represent the history you've lived through. They'll mean different things to different guests."
    # pc "But you just found {i}your{/i} voice."
    # pc "Why don't I say the material, and you tell me how it feels. How YOU feel. No prayers. No artists. Just you."
    # if SaintHumanChoice == "mortal":
    #     st bulb "How I feel…as just Catherine. Yes. Go ahead."
    # if SaintHumanChoice == "a saint":
    #     st bulb "How I feel…as Saint Catherine of Alexandria. Yes. Go ahead."
    # pc  "Ready? Here we go."
    # menu:
    #     "Plastic, to keep your stories.":
    #         if SaintHuman > SaintSaintly:
    #             st sparkle "Honestly…I love it. It's beautiful. Everyone will see the work we've done together. I'm excited."
    #         else:
    #             st sad "It feels…Tawdry. Like my greater ideals will collapse to a single point in time."
    #             st sad "If I were mortal then plastic would work, but that presentation no longer suits me."
    #     "Glass, true to tradition.":
    #         if SaintSaintly > SaintHuman:
    #             st sparkle "Beautiful. I would feel restored, light in spirit, and fully present with those who need me."
    #         else:
    #             st sad "Well, I…I'd do my best to be a 'proper' saint. Even though we know I'm not."
    #             st sad "But saints start as regular people, right? Maybe that's the miracle, to let the flaws be forgotten."
    # st neutral "That's how I feel. That said, [pc_name], your vision for the museum is important, too."
    # st question "Am I what I was, and still [SaintHumanChoice]?"
    # menu:
    #     "Yes, nothing has changed.":
    #         st sparkle "Thank you. Your certainty is reassuring."
    #         pass
    #     "No, I was wrong.":
    #         $ SaintTemp = SaintSaintly
    #         $ SaintSaintly = SaintHuman
    #         $ SaintHuman = SaintTemp
    #         if SaintHair == 0:
    #             $ SaintHair = 1
    #         else:
    #             $ SaintHair = 0
    #         st sparkle "You've reflected on your views. I admire that. "
    #         pass
    # st question "And my repair…what's it to be?"
    # menu:
    #     "Glass.":
    #         st neutral "I'm ready."
    #         $ st_glass = 1
    #         #minigame go here
    #         call minigamestart_stainedglass("glass") from _call_minigamestart_stainedglass_2
    #         pass
    #     "Plastic.":
    #         st neutral "I'm ready."
    #         $ st_glass = 0
    #         call minigamestart_stainedglass("plastic") from _call_minigamestart_stainedglass_3
    #         pass
    # $ SaintRepaired = 1
    # scene storage bg
    # show SaintPortrait at truecenter:
    #     zoom .8
    # "The artwork has been repaired."
    # if SaintSaintly >= SaintHuman:
    #     if st_glass == 0:
    #         st sad "Fascinating. A new way to tell an old story. You've done…well."
    #     if st_glass == 1:
    #         st sparkles "My friend, you are a miracle. I remember my purpose, the smell of aromatic frankincense…"
    # if SaintHuman > SaintSaintly:
    #     if st_glass == 0:
    #         st sparkles "This is amazing! I feel like myself again! I remember my friends, the smell of lavender and sage…"
    #     if st_glass == 1:
    #         st sad "It's…A masterpiece. Beautiful. I'll do my best to be equal to this honor."
    # st sparkles "I'm ready to take my place among the others."
    # if SaintSaintly >= SaintHuman:
    #     if st_glass == 0:
    #         scene saint end pbl with fade
    #     if st_glass == 1:
    #         scene saint end gbl with fade
    # if SaintHuman > SaintSaintly:
    #     if st_glass == 0:
    #         scene saint end pbr with fade
    #     if st_glass == 1:
    #         scene saint end gbr with fade
    # "You hang the stained glass over a window. She casts colors all over."
    # st sparkles "The view is beautiful from here. I can see everyone. Their sadness…Their joy…"
    # st sparkles "I'm not lonely anymore."
    # st sparkles "Thank you."
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
                "Catherine was a welcoming presence who emphasized the evolving story of art…"
                "…including those who had protected, restored, and changed the work in the intervening centuries."
            if st_glass == 1:
                scene saint end gbr
                "Catherine shone down with kindness, evoking the time and place of her manufacture rather than the grand ideals she represents."
                "Visitors swore they'd seen a girl just like her serving coffee at a diner downtown."
        if SaintSaintly >= SaintHuman:
            if st_glass == 0:
                scene saint end pbl
                "The saint became a commanding yet jarring presence, almost punk…"
                "…the juxtaposition of high ideals from base material mirrored and echoed her relationship to artisans and wheelwrights."
                "Visitors left energized to fight for what they believe in."
            if st_glass == 1:
                scene saint end gbl
                "The saint shone with the light of inspiration. Many were drawn to sit in her gallery to weigh difficult decisions."
                "Visitors left with the sense that they have been heard and seen, empowered with the right questions to find the answers they seek."
    elif beat_SaintCatherine > 1:
        scene storage bg:
            blur 3
        show SaintPortrait at truecenter:
            zoom .8
            yoffset -100
        "The saint enjoyed a brief bit of fame after a visitor's post about her went viral. Unfortunately, the good and bad faith arguing kept Catherine locked in doubt."
        "At certain angles, tears could be seen on her face; but that may just have been a flaw in the glass."
    else:
        #bad
        scene storage bg:
            blur 3
        show SaintPortrait at truecenter:
            matrixcolor TintMatrix("#999999")
            zoom .8
            yoffset -100
        "The saint was discovered in an unlocked room, leaning against the wall. A simple “Untitled, Anonymous” curation plaque discarded lay on the floor next to her. " 
        "The odd visitor who did see her was overcome with a sense of loss and abandonment, and had difficulty speaking their mind for several days."
    return