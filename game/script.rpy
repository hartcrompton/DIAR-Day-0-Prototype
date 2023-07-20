#variables
#default vs define
#default variables are meant to be CHANGEABLE. The value is stored in save files.
#define variables are meant to be CONSTANT. Changing a define variable will not be saved.

#where character names start with the same letter, all are given 2-letter abbreviations
#player character
define pc = Character("[pc_name]")

#main characters
define ar = Character("Arnolfini Portrait") #like The Davids, probably will also have separate characters for the couple + dog
define d = Character("[the_davids]") #will probably need to also have three separate david characters
define gi = Character("Gilgamesh")
define gl = Character("Glimmer")
define m = Character("Mona")
define st = Character("St. Catherine")
define so = Character("Soup")
define su = Character("Sunflowers")

#side characters
define ad = Character("Admin")
#define ad = Character("Admin", image="admin", kind=bubble)
define e = Character("Ea-Nasir")
define n = Character("Nighthawks")
define p = Character("Poster")
define s = Character("Sue")
define t = Character("Theodore")
define v = Character("Vending Machine")

#utility characters
define meta = Character("") #used for text that does not come from any specific character

#character name variables
default pc_name = "Firstname Lastname"
default the_davids = "???"

#player backgrounds
default pc_work = 0
default pc_skills = 0
default pc_education = 0

#choice variables
default phone_wait_count = 0


default d_Arnolfini = 0
default d_Davids =  0
default d_Gilgamesh = 0
default d_Glimmer = 0
default d_MonaLisa = 0
default d_SaintCatherine = 0
default d_Soup = 0
default d_Sunflowers = 0

#disposition tier values - not really useful anymore
define d_Tier1 = -150
define d_Tier2 = -95
define d_Tier3 = -80
define d_Tier4 = -50
define d_Tier5 = 0
define d_Tier6 = 50
define d_Tier7 = 35

default d_Total = 0

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

#d_Label.ValueToLabel(d_Arnolfini)

# The game starts here.
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene museum bg1

    #will need to make this changeable through the preferences menu too
    call pronounselection
    meta "You picked [selectedpronouns], right on."
    meta "[they!c] [are] eating [their] apple."
    meta "[they!c] eat[s] [their] apple."

    jump gameintroduction

label end:
    return

