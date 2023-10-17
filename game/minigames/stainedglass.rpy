init python:
    import math
    import pygame
    import time

    # Value that determines zoom level -H
    zoomfactor = 1
         
    #Main game-running function -H
    class StainedGlassRepair(renpy.Displayable):

        def __init__(self, child, diff_items, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(StainedGlassRepair, self).__init__(**kwargs)

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
            self.end_delay = 1
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
            self.x_offset = (width/2 - self.width) 
            self.y_offset = (height/2 - self.height/2)

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)
            render.zoom(zoomfactor,zoomfactor)

            # Blit (draw) the child's render to our render.
            #These draw the two background images, left and right -H
            #render.blit(child_render, (0 + self.x_offset-self.gutter, 0 + self.y_offset))
            render.blit(child_render, (self.width+self.gutter + self.x_offset, 0 + self.y_offset))
            
            #This loop renders the overlaid difference images -H
            for index,i in enumerate(self.diff_items):
                # Create a render from the child.
                diff_render = renpy.render(i.myimage, width, height, st, at)
                #zoomfactor used to scale the overlaid images -H
                if (i.left):
                    render.blit(diff_render, (i.x * zoomfactor - self.gutter + self.x_offset, i.y * zoomfactor + self.y_offset))
                if (i.right):
                    render.blit(diff_render, (i.x * zoomfactor + self.gutter + self.width + self.x_offset, i.y * zoomfactor + self.y_offset))
            
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
                #render.blit(score_img, (self.width - 200 + self.x_offset,self.height + self.y_offset))
            else:
                score = self.count_differences()
                score_txt = Text("Differences: %d    Current Score: %d" % (score,self.the_score), size=24)
                score_img = renpy.render(score_txt, width, height,  st, at)
                #render.blit(score_img, (self.width - 190 + self.x_offset,self.height + self.y_offset))
            renpy.redraw(self,0) 
            
            
            # Return the render.
            return render
            
        #count as each piece is moved to the right
        def count_differences(self):
            myscore = 0
            for index,i in enumerate(self.diff_items): 
                #i.right is False by default, so if every i.right has been assigned an image then this returns 0
                if not i.right:
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
                        if i.left != False:
                        #left side
                        #zoomfactor needed to make sure the clickable bounds match the visible images -H
                            if (i.x * zoomfactor + self.x_offset-self.gutter <= x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset) :  
                                i.temp = i.left
                                i.left = False
                                i.right = i.temp
                                clicked = True
                                break
                                
        
                            #right side
                            elif (i.x * zoomfactor + self.x_offset + self.width+self.gutter <= x <= i.x * zoomfactor + self.width + i.w * zoomfactor + self.x_offset+self.gutter) and (i.y * zoomfactor <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):   
                                i.temp = i.left
                                i.left = False
                                i.right = i.temp
                                clicked = True
                                break
                        
                #plays sound effects on click -H
                #if (clicked):
                    #self.score_bubble = Bubble_Text("+20", "#0f0",72,3, x-5, y-5)
                   # self.the_score += 20  
                #elif (self.x_offset <= x <= self.width*2 + self.x_offset) and (self.y_offset <= y <= self.height + self.y_offset):
                    #self.score_bubble = Bubble_Text("-5", "#f00",72,3, x-5, y-5)
                    #self.the_score = max(0,self.the_score - 5)  
               
                # -H
                if self.count_differences() == 0:
                    if self.end_start != -1:
                        self.end_start = -1
                    
            if self.winner:
                    return (self.the_score)
                    
        #misleading name, has been refactored to just fill in all the items from the diff_items array
        def randomizeItems(self, difference_count):
            #randomzing at start:
            for index,i in enumerate(self.diff_items): 
                i.left = renpy.random.choice([True, False])
                
            #must be array size
            iterations = 3
            #while self.count_differences() < difference_count and iterations < 100:
            while iterations >= 0:
                i = diff_items[iterations]
                i.left = True
                #i.right = not i.left
                iterations -= 1
    

    #Currently the images are hardcoded. This can be broken out into a separate function that can import different images -H
    cc = Position(xpos=0.5, xanchor='center', ypos=0.5,yanchor='center')
    
    



label minigamestart_stainedglass(materialchoice="default"):
    scene storage bg:
        blur 3
    if materialchoice == "default":
        return
    if materialchoice == "glass":
        python:
            diff_items = []
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintGlass.png", 37,23,89,118))
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintGlass.png", 205,105,124,69))
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintGlass.png", 35,343,65,155))
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintGlass.png", 163,280,95,125))
    if materialchoice == "plastic":
        python:
            diff_items = []
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintPlastic.png", 37,23,89,118))
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintPlastic.png", 205,105,124,69))
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintPlastic.png", 35,343,65,155))
            diff_items.append(STD_Item("images/minigame/StainedGlass/SaintPlastic.png", 163,280,95,125))
        #time and score may not really be relevant to us -H
    python:
        starttime = renpy.time.time()
        the_score = 0
        renpy.block_rollback()
        #we need to be able to input an argument here
        difference_image = StainedGlassRepair("images/minigame/StainedGlass/SaintBroken.png", diff_items)
        difference_image.randomizeItems(4)
        ui.add(difference_image)
        #ui.textbutton("Give Up", clicked=ui.returns(difference_image.the_score), xalign=0.98, yalign=0.1)
        winner = ui.interact(suppress_overlay=False, suppress_underlay=False)
        winner = difference_image.the_score
        elapsed = round(renpy.time.time() - starttime)
        the_score += winner
        renpy.block_rollback()

    #image difference_image_img = afterImage("images/mona.png", diff_items)
    if materialchoice == "glass":
        show saintcatherineglass at cc
        #meta "Repaired with [materialchoice]."
    if materialchoice == "plastic":
        show saintcatherineplastic at cc
        #meta "Repaired with [materialchoice]."
    #if (difference_image.count_differences() == 0):
        #$ timebonus = int(100 * max((1.0 - ((elapsed - 20.0)/40.0)),0.0))
        #$ the_score += timebonus
    return