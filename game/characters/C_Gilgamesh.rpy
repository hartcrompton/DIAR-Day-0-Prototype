#Gilgamesh

default beat_Gilgamesh = 1

label conv_Gilgamesh:
    scene gilgameshbg
    show gilgamesh at right
    menu:
        "Beat [beat_Gilgamesh]" if actions > 0 and beat_Gilgamesh < 5:
            gi "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            gi "See ya"
            jump FreeRoam
        "Reset Beats":
            "Beats reset."
            $ beat_Gilgamesh = 1
            jump conv_Gilgamesh

label .use_action:
    #menu:
    #    gi "Whoa, sure you want to use an action?"
    #    "Yeah, why not.":
    #        $ actions = actions - 1
    #        jump expression "conv_Gilgamesh" + "." + "beat" + "%d" % beat_Gilgamesh
    #    "No, not really.":
    #        gi "Understandable."
    #        jump conv_Gilgamesh
    jump expression "conv_Gilgamesh" + "." + "beat" + "%d" % beat_Gilgamesh

label .beat1:
    gi "Go ahead, take it all in."
    gi "Hard to believe someone like you could be in the same room as someone like me."
    gi "This is essentially my throne room."
    pc "It's right next to the ball pit."
    gi "Yes. AS the Spartans had their agoge, so I have the ball pit."
    pc "I don't even know who you are."
    gi "Oh I get it."
    gi "You're a real jester. Bit of a rascal."
    gi "Understandable, lots of people use humor to cover for inadequacy."
    menu:
        "OK, but who are you?":
            gi "Gilgamesh, of course you've heard of me."
        "Why are you holding a lion?"
        "So were you someone famous?":
            gi "I was the king of kings."
    pc "Sorry, doesn't ring a bell."
    gi "Slayer of monsters?"
    pc "Uh-uh."
    gi "Oh gods, you're serious."
    gi "Could it be that my name is not so well known as I thought? No, this person is just ignorant."
    gi "They wrote a book about me, you know."
    gi "Go read it. Then come back and be amazed."
    e "Just humor him, it's really the only way to shut him up."
    e "Just uh, try not to mention Enkidu."
    menu:
        "Who's Enkidu?":
            e "Gilgamesh's companion. Things didn't end well. Don't bring it up."
        "Why shouldn't I mention him?":
            e "There are just some things from people's pasts we don't need to dredge up."
    "Research minigame, find the Epic of Gilgamesh. Skim it in as little or much detail as the player likes. Always ends with the player learning about Enkidu."

    "You have [actions] action(s) left."
    $ beat_Gilgamesh += 1
    jump FreeRoam
label .beat2:
    gi "Ah you're back. And suitably amazed, I'm sure."
    pc "Player asks about Uruk, Gil's city."
    gi "Gil gives some plainly incorrect answers."
    pc "Asks about beasts Gil fought."
    gi "Half right answers, half wrong."
    pc "Last, player brings up Enkidu."
    e "What are you doing?"
    gi "Yeah, he was great."
    gi "We toppled temples, shattered the gates, shook the city's palaces. At last, we grappled each other, all our strength laid bare."
    pc "What?"
    e "He means he had a crush."
    pc "Oh. So it must have been hard for you when he died."
    e "God damnit."
    gi "When he WHAT?!"
    pc "Yup, he died."
    gi "Oh... of course. But surely it was in great battle against a terrible beast."
    menu:
        "Not really.":
            pass
        "No, he was sick.":
            pass
    gi "That's impossible."
    pc "Kinda your fault actually."
    gi "What."
    pc "Gods made him sick because you pissed them off."
    gi "WHAT."
    pc "Died in your arms."
    gi "Gil is 100 percent not able to process this info."
    e "Ea-Nasir is pissed. He did tell you not to do this."
    gi "I think I need some time alone."
    
    "You have [actions] action(s) left."
    $ beat_Gilgamesh += 1
    jump FreeRoam
label .beat3:
    ad "Hey the water alarm's going off in the antiquities wing."
    pc "Weird."
    pc "Ok, yep, flooded."
    gi "Sobbing profusely"
    e "Says something that doesnt help."
    gi "Sobs harder"
    "Cleaning variety minigame where the player mops up the tears."
    gi "Really the worst part about this is it makes me feel bad."
    gi "Oh gods, is this what guilt feels like? I hate it."
    gi "Wish you'd never told me."
    e "It really wasn't your fault."
    menu:
        "It doesn't matter whose fault it is":
            pc "What matters is you're screwing up my museum"
            pc "I don't care about your legends or your gods."
            pc "But I can't have some statue ruining my exhibit."
            pc "So act your damn age and behave."
        "Actually it kinda was.":
            pc "You were a huge pain in the ass."
            pc "You pissed off your people."
            pc "You pissed off the gods."
            pc "You kinda got Enkidu killed."
            pc "And now you're crying because it made YOU feel bad?"
    pc "Nothing bad happened to you, stop feeling sorry for yourself."
    gi "How dare you."
    pc "You call yourself the master of beasts?"
    pc "You call yourself a king?"
    pc "Act like it."
    gi "I need some time to think."

    "You have [actions] action(s) left."
    $ beat_Gilgamesh += 1
    jump FreeRoam
label .beat4:
    gi "Sorry you had to see that"
    gi "Kingly emotions are so much bigger than regular people's, I'm sure it was overwhelming for you."
    pc "Bro, come on."
    gi "But now I need your aid."
    gi "The world has forgotten the tramp of my boots."
    gi "I need to go on a quest"
    pc "And how do you plan to do that?"
    gi "With you, my noble squire of course."
    pc "Where are you going?"
    gi "The place all statues fear to go."
    gi "Down the stairs."
    "Would be a good place to have some sort of mechanic or minigame. Need to think of how to gamify going down the stairs"
    "Gil reads the epic himself, is immediately traumatized"
    gi "That's it?"
    gi "I fail?"
    gi "I grow old and return home empty handed?"
    menu:
        "Yup, you screwed up pretty bad.":
            pass
        "No, you came back to Uruk with what you needed, not what you wanted.":
            pass
    gi "So my epic, my legend is just a tale of..."
    menu:
        "Fucking up":
            pass
        "Learning and getting over yourself.":
            pass
    gi "And now I'm just a monument to..."
    menu:
        "Fucking up.":
            pc "Enkidu would have been fine if you had just controlled yourself."
            pc "And the museum would be doing better if you weren't suffocating people with your ego"
        "Whatever you want to be.":
            pc "This is a second chance."
            gi "To fail?"
            e "Oh my god shut up."
            pc "To be something else."
    pc "The old you (and let's be honest, the current you) was a huge jackass whose choices made his lover die."
    pc "Maybe now you have a chance to make choices so you won't be ashamed to meet Enkidu again someday."
    gi "By the gods, peasant, you're right!"
    "Outcome of either melancholy or royalty."

    
    "You have [actions] action(s) left."
    $ beat_Gilgamesh += 1
    jump FreeRoam