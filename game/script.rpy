#variables
#default vs define
#default variables are meant to be CHANGEABLE. The value is stored in save files.
#define variables are meant to be CONSTANT. Changing a define variable will not be saved.

#when character names start with the same letter, all are given 2-letter abbreviations
#player character
define pc = Character("[pc_name]")

#main characters
define ar = Character("Arnolfini Portrait")
define arm = Character("Giovanni", image="arnolfiniman", color="#96528d") #man
define arw = Character("[arwName]", image="arnolfiniwoman", color="#48750b") #woman
default arwName = "The Painted Woman"
define ard = Character("Dog", image="arnolfinidog", color="#844016") #dog

define d = Character("The Davids", color = "#ffffff")
define dm = Character("David M.", image="davidm", color="#ccc9c5") #mikey
define db = Character("David B.", image="davidb", color="#9d9797") #bernini
define dd = Character("David D.", image="davidd", color="#f3f1ed") #donny
define gi = Character("Gilgamesh", image="gilgamesh", color="#c39566")
define gl = Character("Glimmer")
define m = Character("Mona Lisa", image="mona", color="#df8003")
define p = Character("Corgi Poster", image="poster", color="#cb7b39")
define st = Character("St. Catherine", image="saintcatherine", color="#f1d264")
define so = Character("Soup", image="soup", color="#f08204")
define su = Character("Sunflowers", image="sunflowers", color="#ebe184")
define ss = Character("Soup & Sunflowers", image="soupandsunflowers", color="#fdd203")

#side characters
define ad = Character("Admin", image="adminlayered")
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
image side adminlayered = LayeredImageProxy("adminlayered", Transform(xoffset=0, yoffset=0))
define e = Character("Ea-Nasir", image="eanasir", color="#edc7a1")
define n = Character("Nighthawks")
define n1 = Character("Nighthawks", image="nighthawks1", color="#659274")
define n2 = Character("Nighthawks", image="nighthawks2", color="#659274")
define n3 = Character("Nighthawks", image="nighthawks3", color="#659274")
define n4 = Character("Nighthawks", image="nighthawks4", color="#659274")
define sue = Character("Sue")
define t = Character("Theodore")
define v = Character("Vending Machine", image="vendingmachine")

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
label start:
    $ StoryCompletedTotal = 0
    scene museum bg1
    call pronounselection from _call_pronounselection
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