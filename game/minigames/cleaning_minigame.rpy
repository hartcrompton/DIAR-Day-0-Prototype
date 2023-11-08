image TempCleaningBackground = False

init python:
    import math
    import pygame
    import time
    #renpy.add_layer("middle", above="master")

    # Value that determines zoom level -H
    zoomfactor = 1
    
    #Main game-running function -H
    class MinigameCleaning(renpy.Displayable):

        def __init__(self, child, diff_items, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(MinigameCleaning, self).__init__(**kwargs)

            self.child = renpy.displayable(child)

            # The width and height of us, and our child.
            #I think this just resets the values between each run -H
            self.width = 0
            self.height = 0
            self.width_offset = 0
            self.height_offset = 0
            
            #gap between images -H
            self.gutter = 5
            
            self.the_score = 0
            self.end_start = None
            self.end_delay = 0
            # The winner.
            self.winner = False
            
            self.diff_items = diff_items
            
            
            self.score_bubble = None

        def render(self, width, height, st, at):

            # Create a render from the child.
            # Render is the thing to be drawn, Blit is the function that actually draws it -H
            child_render = renpy.render(self.child, width, height, st, at)
            
            # Gets the size of the render from the input image -H
            self.width, self.height = child_render.get_size()
            # zoomfactor is used here to adjust the scale of the images, trickles down to anything else using these values -H
            self.width = self.width * zoomfactor
            self.height = self.height * zoomfactor
            # Offsets to center the images -H
            self.x_offset = 0
            self.y_offset = (height/2 - self.height/2)

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)
            render.zoom(zoomfactor,zoomfactor)

            # Blit (draw) the child's render to our render.
            #These draw the two background images, left and right -H
            render.blit(child_render, (0 + self.x_offset-self.gutter, 0 + self.y_offset))
            #render.blit(child_render, (self.width+self.gutter + self.x_offset, 0 + self.y_offset))
            
            #This loop renders the overlaid difference images -H
            for index,i in enumerate(self.diff_items):
                # Create a render from the child.
                diff_render = renpy.render(i.myimage, width, height, st, at)
                #zoomfactor used to scale the overlaid images -H
                if (i.left):
                    render.blit(diff_render, (i.x * zoomfactor - self.gutter + self.x_offset, i.y * zoomfactor + self.y_offset))
                #if (i.right):
                    #render.blit(diff_render, (i.x * zoomfactor + self.gutter + self.width + self.x_offset, i.y * zoomfactor + self.y_offset))
            
            # shows and fades the popup score bubbles -H
            if (self.score_bubble):
                if (self.score_bubble.start == None) :
                    self.score_bubble.start = st
                self.score_bubble.st = st-self.score_bubble.start
                myalpha = max(1.0 - self.score_bubble.st / self.score_bubble.duration, 0.0)
                self.score_bubble.y -= self.score_bubble.st/2
                
                score_bubble_img = Transform(child=self.score_bubble.myimage, alpha=myalpha)
                score_img = renpy.render(score_bubble_img, width, height,  st, at)
                render.blit(score_img,(self.score_bubble.x,self.score_bubble.y))
                if (self.score_bubble.st  > self.score_bubble.duration):
                    self.score_bubble = None
            
            # gives current score and final score -H
            if (self.end_start):
                if (self.end_start<0):
                    self.end_start = st
                if (st > self.end_start + self.end_delay):
                    self.winner = True
                    renpy.timeout(0)
                score = self.count_differences()
                score_txt = Text("All items found in %d seconds." % (self.end_start + self.end_delay), size=24)
                score_img = renpy.render(score_txt, width, height,  st, at)
                render.blit(score_img, (self.width - 200 + self.x_offset,self.height + self.y_offset))
            else:
                score = self.count_differences()
                score_txt = Text("Differences: %d    Current Score: %d" % (score,self.the_score), size=24)
                score_img = renpy.render(score_txt, width, height,  st, at)
                render.blit(score_img, (self.width - 190 + self.x_offset,self.height + self.y_offset))
            renpy.redraw(self,0) 
            
            
            # Return the render.
            return render
            
            
        def count_differences(self):
            myscore = 0
            for index,i in enumerate(self.diff_items): 
                if i.right != i.left:
                    myscore += 1
            return myscore
            
        # runs when you click, checks what you clicked -H
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP: 

            # iterates through all overlaid images and sees if you clicked in bounds -H 
            # Check if one of the items
                clicked = False
                for index,i in enumerate(self.diff_items): 
                    if i.left != i.right:
                        #left side
                        #zoomfactor needed to make sure the clickable bounds match the visible images -H
                        if (i.x * zoomfactor + self.x_offset-self.gutter <= x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset) :  
                            i.left = i.right
                            clicked = True
                            break
                            
    
                        #right side
                        #elif (i.x * zoomfactor + self.x_offset + self.width+self.gutter <= x <= i.x * zoomfactor + self.width + i.w * zoomfactor + self.x_offset+self.gutter) and (i.y * zoomfactor <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):   
                            #i.right = i.left 
                            #clicked = True
                            #break
                        
                #plays sound effects on click -H
                if (clicked):
                    #self.score_bubble = Bubble_Text("+20", "#0f0",72,3, x-5, y-5)
                    #renpy.call_in_new_context("TestPosterLines")
                    self.the_score += 20  
                elif (self.x_offset <= x <= self.width*2 + self.x_offset) and (self.y_offset <= y <= self.height + self.y_offset):
                    #self.score_bubble = Bubble_Text("-5", "#f00",72,3, x-5, y-5)
                    
                    self.the_score = max(0,self.the_score - 5)  
               
                #game ends when no differences remain -H
                if self.count_differences() == 0:
                    self.end_start = -1
                    
            if self.winner:
                    return (self.the_score)
                    
        #randomizes the overlay images
        def randomizeItems(self, difference_count):
            #randomzing at start:
            for index,i in enumerate(self.diff_items): 
                i.left = renpy.random.choice([True, False])
                
            iterations = 0
            while self.count_differences() < difference_count and iterations < 100:
                i = renpy.random.choice(self.diff_items)
                i.left = renpy.random.choice([True, False])
                #i.right = not i.left
                iterations += 1
    
    #final image that displays after game ends -H
    class afterImage(renpy.Displayable):
        def __init__(self, child, diff_items, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(afterImage, self).__init__(**kwargs)

            # The child.
            self.child = renpy.displayable(child)

            # The width and height of us, and our child.
            self.width = 0
            self.height = 0
            
            self.diff_items = diff_items
            
            
        def render(self, width, height, st, at):

            # Create a render from the child.
            child_render = renpy.render(self.child, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (0, 0))
            
            
            for index,i in enumerate(self.diff_items):
                # Create a render from the child.
                diff_render = renpy.render(i.myimage, width, height, st, at)
                if (i.left):
                    render.blit(diff_render, (i.x, i.y))

            # Return the render.
            return render

    #these are the overlaid images that will be randomly selected, very manually intensive -H
    #Currently the images are hardcoded. This can be broken out into a separate function that can import different images -H
    diff_items = []
    cc = Position(xpos=0.5, xanchor='center', ypos=0.5, yanchor='center')
    


#Ok, this kind of works, but
label TestPosterLines():
    $ ui.add(difference_image)
    #$ renpy_blur(difference_image, 1.5)
    p "This is a test line."
    return

transform CleaningAlphaIn:
    xalign 0.5
    yalign 0.5
    alpha 0.0
    ease 1.0 alpha 1.0

label minigamestart_cleaning(gameimage="notdefault"):
    #scene black with fade
    if gameimage == "antiquities":
        python:
            diff_items = []
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 41, 863, 110, 210))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 361, 951, 217, 120))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 813, 907, 173, 122))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 1128, 886, 179, 107))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 1438, 831, 211, 174))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 487, 529, 60, 77))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 496, 635, 121, 62))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 646, 699, 148, 108))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 796, 598, 128, 77))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 1019, 583, 83, 108))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 1288, 668, 107, 93))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning antiquities overlay.png", 383, 65, 270, 190))
            difference_image = MinigameCleaning("antiquities_tod", diff_items)
    if gameimage == "fineart":
        python:
            diff_items = []
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 41, 863, 110, 210))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 361, 951, 217, 120))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 813, 907, 173, 122))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1128, 886, 179, 107))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1438, 831, 211, 174))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 487, 529, 60, 77))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 496, 635, 121, 62))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 646, 699, 148, 108))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 796, 598, 128, 77))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1019, 583, 83, 108))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1288, 668, 107, 93))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 383, 65, 270, 190))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 767, 112, 295, 186))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1690, 0, 230, 550))
            difference_image = MinigameCleaning("fineart_tod", diff_items)
    if gameimage == "mixedmedia":
        python:
            diff_items = []
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 42, 881, 103, 194))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 273, 923, 205, 100))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 695, 739, 109, 109))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 721, 889, 193, 113))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 1120, 684, 79, 98))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 1261, 898, 202, 112))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 1673, 896, 195, 168))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 1410, 762, 79, 56))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 1477, 696, 102, 62))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 1632, 654, 62, 70))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 1682, 0, 238, 494))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning mixedmedia overlay.png", 851, 34, 328, 187))
            difference_image = MinigameCleaning("mixedmedia_tod", diff_items)
    if gameimage == "foyer":
        python:
            diff_items = []
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 82, 910, 84, 136))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 460, 979, 250, 95))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 797, 891, 235, 148))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 1320, 849, 201, 112))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 1649, 879, 214, 189))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 1393, 698, 100, 73))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 1614, 184, 225, 541))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 1012, 392, 122, 159))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 767, 29, 465, 263))
            diff_items.append(STD_Item("images/minigame/cleaning/cleaning foyer overlay.png", 384, 605, 83, 88))
            difference_image = MinigameCleaning("foyer_tod", diff_items)
    if gameimage == "default":
        return
    python:
        #time and score may not really be relevant to us -H
        starttime = renpy.time.time()
        the_score = 0
        renpy.block_rollback()
        #we need to be able to input an argument here
        
        difference_image.randomizeItems(7)
        #TempCleaningBackground = difference_image
        ui.add(At(difference_image, CleaningAlphaIn))
        #ui.textbutton("Give Up", clicked=ui.returns(difference_image.the_score), xalign=0.98, yalign=0.1)
        winner = ui.interact(suppress_overlay=False, suppress_underlay=False)
        winner = difference_image.the_score
        elapsed = round(renpy.time.time() - starttime)
        the_score += winner
        renpy.block_rollback()

    if (difference_image.count_differences() == 0):
        $ timebonus = int(100 * max((1.0 - ((elapsed - 20.0)/40.0)),0.0))
        $ the_score += timebonus
    return