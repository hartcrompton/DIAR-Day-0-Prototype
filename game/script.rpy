#variables
#default vs define
#default variables are meant to be CHANGEABLE. The value is stored in save files.
#define variables are meant to be CONSTANT. Changing a define variable will not be saved.

#when character names start with the same letter, all are given 2-letter abbreviations
#player character
default pc_color = "#fcba03"   
#define n = Character("name", who_prefix="{color=[namecol]}", who_suffix="{/color}")
define pc = Character("[pc_name]", who_prefix="{color=[pc_color]}", who_suffix="{/color}")
define config.rollback_enabled = False

#main characters
define hm = Character("Hiring Manager", color="#ffd65c")
define ar = Character("Arnolfini Portrait")
define arm = Character("Giovanni", image="armlayered", color="#96528d") #man
layeredimage armlayered:
    always:
        "side_arnolfiniman"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side armlayered = LayeredImageProxy("armlayered", Transform(xoffset=0, yoffset=0))

define arw = Character("[arwName]", image="arwlayered", color="#48750b") #woman
default arwName = "The Painted Woman"
layeredimage arwlayered:
    always:
        "side_arnolfiniwoman"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side arwlayered = LayeredImageProxy("arwlayered", Transform(xoffset=0, yoffset=0))

define ard = Character("Dog", image="ardlayered", color="#844016") #dog
layeredimage ardlayered:
    always:
        "side_arnolfinidog"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side ardlayered = LayeredImageProxy("ardlayered", Transform(xoffset=0, yoffset=0))

define d = Character("The Davids", color = "#ffffff")

define dm = Character("David M.", image="dmlayered", color="#ccc9c5") #mikey
image davidm = ConditionSwitch (
    "(DavidsNude == 0)", "images/Characters/Davids/DavidM_nonnude.png",
    "(DavidsNude == 1)", "images/Characters/Davids/DavidM_nude.png"
)
layeredimage dmlayered:
    always:
        "side_davidm"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side dmlayered = LayeredImageProxy("dmlayered", Transform(xoffset=0, yoffset=0))

define db = Character("David B.", image="dblayered", color="#9d9797") #bernini
layeredimage dblayered:
    always:
        "side_davidb"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side dblayered = LayeredImageProxy("dblayered", Transform(xoffset=0, yoffset=0))

define dd = Character("David D.", image="ddlayered", color="#f3f1ed") #donny
image davidd = ConditionSwitch (
    "(DavidsNude == 0)", "images/Characters/Davids/DavidD_nonnude.png",
    "(DavidsNude == 1)", "images/Characters/Davids/DavidD_nude.png"
)
layeredimage ddlayered:
    always:
        "side_davidd"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side ddlayered = LayeredImageProxy("ddlayered", Transform(xoffset=0, yoffset=0))

define gi = Character("Gilgamesh", image="gilayered", color="#c39566")
layeredimage gilayered:
    always:
        "side_gilgamesh"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side gilayered = LayeredImageProxy("gilayered", Transform(xoffset=0, yoffset=0))

#deprecated
define gl = Character("Glimmer")

define m = Character("Mona Lisa", image="mlayered", color="#df8003")
layeredimage mlayered:
    always:
        "side_mona"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side mlayered = LayeredImageProxy("mlayered", Transform(xoffset=0, yoffset=0))

define p = Character("Corgi Poster", image="playered", color="#f2a571")
layeredimage playered:
    always:
        "side_poster"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side playered = LayeredImageProxy("playered", Transform(xoffset=0, yoffset=0))

define st = Character("St. Catherine", image="stlayered", color="#f1d264")
layeredimage stlayered:
    always:
        ConditionSwitch ("SaintHair == 0", "side_saintcatherine", "SaintHair == 1", "side_saintcatherine_b")
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side stlayered = LayeredImageProxy("stlayered", Transform(xoffset=0, yoffset=0))

define so = Character("Soup", image="solayered", color="#f08204")
layeredimage solayered:
    always:
        "side_soup"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side solayered = LayeredImageProxy("solayered", Transform(xoffset=0, yoffset=0))

define su = Character("Sunflowers", image="sulayered", color="#ebe184")
layeredimage sulayered:
    always:
        "side_sunflowers"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side sulayered = LayeredImageProxy("sulayered", Transform(xoffset=0, yoffset=0))

define ss = Character("Soup & Sunflowers", image="sslayered", color="#fdd203")
layeredimage sslayered:
    always:
        "side_soupandsunflowers"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side sslayered = LayeredImageProxy("sslayered", Transform(xoffset=0, yoffset=0))

define ad = Character("Admin", image="adminlayered", color="#5bc3ef")
layeredimage adminlayered:
    always:
        "side_admin"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side adminlayered = LayeredImageProxy("adminlayered", Transform(xoffset=0, yoffset=0))

define e = Character("Ea-Nasir", image="elayered", color="#edc7a1")
layeredimage elayered:
    always:
        "side_eanasir"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side elayered = LayeredImageProxy("elayered", Transform(xoffset=0, yoffset=0))

define n = Character("Nighthawks")

define n1 = Character("Nighthawks", image="n1layered", color="#659274")
layeredimage n1layered:
    always:
        "side_nighthawks1"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side n1layered = LayeredImageProxy("n1layered", Transform(xoffset=0, yoffset=0))

define n2 = Character("Nighthawks", image="n2layered", color="#659274")
layeredimage n2layered:
    always:
        "side_nighthawks2"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side n2layered = LayeredImageProxy("n2layered", Transform(xoffset=0, yoffset=0))

define n3 = Character("Nighthawks", image="n3layered", color="#659274")
layeredimage n3layered:
    always:
        "side_nighthawks3"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side n3layered = LayeredImageProxy("n3layered", Transform(xoffset=0, yoffset=0))

define n4 = Character("Nighthawks", image="n4layered", color="#659274")
layeredimage n4layered:
    always:
        "side_nighthawks4"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side n4layered = LayeredImageProxy("n4layered", Transform(xoffset=0, yoffset=0))

define v = Character("Vending Machine", image="vlayered", color="#e78d09")
layeredimage vlayered:
    always:
        "side_vendingmachine"
    group emotion:
        attribute neutral default:
            "neutral"
        attribute happy:
            "happy"
        attribute sad:
            "sad"
        #laugh
        attribute laugh:
            "laugh"
        #bulb
        attribute bulb:
            "bulb"
        #question
        attribute question:
            "question"
        #questions
        attribute questions:
            "questions"
        #sigh
        attribute sigh:
            "sigh"
        #sparkle
        attribute sparkle:
            "sparkle"
        #sparkles
        attribute sparkles:
            "sparkles"
        #surprise
        attribute surprise:
            "surprise"
        #surprises
        attribute surprises:
            "surprises"
        #panic
        attribute panic:
            "panic"
        #sweat
        attribute sweat:
            "sweat"
        #angry
        attribute angry:
            "angry"
        #dots
        attribute dots:
            "dots"
        #exclaim
        attribute exclaim:
            "exclaim"
        attribute confused:
            "confused"
image side vlayered = LayeredImageProxy("vlayered", Transform(xoffset=0, yoffset=0))

image SaveOverlay = "slot_idle_background"

define sue = Character("Sue")
define t = Character("Theodore")

default StoryCompletedTotal = 0

#utility characters
define meta = Character("") #deprecated, no use

#character name variables
default pc_name = "Player Name"

#player backgrounds
default pc_work = 0
default pc_skill = 0
default pc_education = 0

#choice variables
default phone_wait_count = 0

#character disposition trackers - deprecated, to be removed
default d_Arnolfini = 0
default d_Davids =  0
default d_Gilgamesh = 0
default d_Glimmer = 0
default d_MonaLisa = 0
default d_SaintCatherine = 0
default d_Soup = 0
default d_Sunflowers = 0

#disposition tier values - deprecated, to be removed
define d_Tier1 = -150
define d_Tier2 = -95
define d_Tier3 = -80
define d_Tier4 = -50
define d_Tier5 = 0
define d_Tier6 = 50
define d_Tier7 = 35
default d_Total = 0

#function to return disposition label from value - deprecated, to be removed
init python:
    
    renpy.music.register_channel("sfx2", "music")
    class d_LabelFromValue():

        def __init__(self):
            self.value = 0
            self.label = "none"

        def ValueToLabel(self, value):
            if value == 0:
                self.label = "Terrible"
            elif value == 1:
                self.label = "Bad"
            elif value == 2:
                self.label = "Unpleasant"
            elif value == 3:
                self.label = "Neutral"
            elif value == 4:
                self.label = "OK"
            elif value == 5:
                self.label = "Good"
            elif value == 6:
                self.label = "Great"
            return self.label

default d_Label = d_LabelFromValue()


# start label is the first bit of game code that gets read
label start(show_credits=0):
    if show_credits == 1:
        scene black with fade
        show credits end at truecenter with fade
        $ renpy.pause(30.0)
        return
    $ StoryCompletedTotal = 0
    scene intro bg
    #pc "TestLine"
    call pronounselection from _call_pronounselection
    menu:
        "Are you okay with a little (artistic) nudity?"
        "No nudity, please.":
            $ DavidsNude = 0
            pass
        "I don't mind nudity.":
            $ DavidsNude = 1
            pass
    menu:
        "And what's your favorite color?"
        "{color=#70d2c2}Blue{/color}":
            $ pc_color = "#70d2c2"
            pass
        "{color=#81c195}Green{/color}":
            $ pc_color = "#81c195"
            pass
        "{color=#fdde8f}Yellow{/color}":
            $ pc_color = "#fdde8f"
            pass
        "{color=#f2948a}Red{/color}":
            $ pc_color = "#f2948a"
            pass
        "{color=#f5dae3}Pink{/color}":
            $ pc_color = "#f5dae3"
            pass
    #pc "This is my color"
    #menu:
    #    "Skip to beats":
    #        jump FreeRoam
    #    "Skip to tour.":
    #        jump MuseumTour
    #    "Continue":
    #        pass

    scene museum bg1
    #will need to make this changeable through the preferences menu too
    #"You picked [selectedpronouns], right on."
    #"[they!c] [are] eating [their] apple."
    #"[they!c] eat[s] [their] apple."
    #"The apple is [theirs]."

    jump GameIntroduction

label end:
    return

#label used for in progress features, only accessible through developer commands
label testing:
    scene testing
    menu:
        "Cleaning":
            call minigamestart_cleaning("cleaning") from _call_minigamestart_cleaning_1
            jump testing
        "Saint Repair":
            menu:
                "Glass":
                    call minigamestart_stainedglass("glass") from _call_minigamestart_stainedglass
                    jump testing
                "Plastic":
                    call minigamestart_stainedglass("plastic") from _call_minigamestart_stainedglass_1
                    jump testing

label MainMenuCredits:
    show credits end at truecenter with fade
    $ renpy.pause(30.0)
    return

