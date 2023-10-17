image TempCleaningBackground = False

init python:
    import math
    import pygame
    import time
    #renpy.add_layer("middle", above="master")

    # Value that determines zoom level -H
    zoomfactor = 1
    
    #Main game-running function -H
    class MinigameCorgi(renpy.Displayable):

        def __init__(self, child, diff_items, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(MinigameCorgi, self).__init__(**kwargs)

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
                self.score_bubble.st = st-self.score_bubble.start -2
                myalpha = max(1.0 - self.score_bubble.st / self.score_bubble.duration, 0.0)
                #self.score_bubble.y -= self.score_bubble.st/2
                if (self.score_bubble.x > 945):
                    self.score_bubble.x = 945
                if (self.score_bubble.y > 892):
                    self.score_bubble.y = 892
                score_bubble_img = Transform(child=self.score_bubble.myimage, alpha=myalpha)
                textbox_img = Transform(text_overlay, alpha=myalpha)
                score_img = renpy.render(score_bubble_img, width, height,  st, at)
                textbox_overlay = renpy.render(textbox_img, width, height,  st, at)
                render.blit(textbox_overlay, (self.score_bubble.x,self.score_bubble.y -785))
                render.blit(score_img,(self.score_bubble.x + 194,self.score_bubble.y + 33))
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
                if self.count_differences() == 0:
                    self.end_start = -1
                    if self.end_delay >= 1:
                        self.end_delay -= 1
                if self.winner:
                        return (self.the_score)
            # iterates through all overlaid images and sees if you clicked in bounds -H 
            # Check if one of the items
                clicked = False
                for index,i in enumerate(self.diff_items): 
                    if i.left != i.right:
                        #left side
                        #zoomfactor needed to make sure the clickable bounds match the visible images -H
                        if (i.x * zoomfactor + self.x_offset-self.gutter <= x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset) :  
                            #if (gameimage == "1"):
                            if (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[0].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[0].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                self.score_bubble = Bubble_Text(corgi_barks[0], "#ffffff",30,3, x, y)
                                if gameimage == "1":
                                    self.end_start = -1
                            elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[1].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[1].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                self.score_bubble = Bubble_Text(corgi_barks[1], "#ffffff",30,3, x, y)
                            elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[2].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[2].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                self.score_bubble = Bubble_Text(corgi_barks[2], "#ffffff",30,3, x, y)
                                
                            elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[3].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[3].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                self.score_bubble = Bubble_Text(corgi_barks[3], "#ffffff",30,3, x, y)
                                if gameimage == "2":
                                    self.end_start = -1
                            elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[4].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[4].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                self.score_bubble = Bubble_Text(corgi_barks[4], "#ffffff",30,3, x, y)
                            elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[5].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[5].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                self.score_bubble = Bubble_Text(corgi_barks[5], "#ffffff",30,3, x, y)
                            else:
                                self.score_bubble = Bubble_Text("Keep looking!", "#ffffff",30,3, x, y)
                            i.left = i.right
                            clicked = True
                            #item 1
                            #item 2
                            #item 3
                            #item 4
                            #item 5
                            #item 6
                            break
                        #I need something that can help me cheer people on!			Hint for the right object
                        #No, that's not it. Though I bet you could something delicious in that!			Mug selected
                        #Watch out for any fuzzy bits, though. It's been sitting there awhile.			Mug selected
                        #That won't work. Though I've seen it make tasty snacks before that'll be sure to give you energy!			Toaster selected
                        #I've seen that can be useful for various things, but no, not for cheering. Please don't use that on me!			Stapler
                        #Definitely not, unfortunately. I think I've seen something scurrying in and out of that lately. Careful!			Bag of Chips
                        #That's perfect!			Right object selected (small flag)
    
                        #right side
                        #elif (i.x * zoomfactor + self.x_offset + self.width+self.gutter <= x <= i.x * zoomfactor + self.width + i.w * zoomfactor + self.x_offset+self.gutter) and (i.y * zoomfactor <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):   
                            #i.right = i.left 
                            #clicked = True
                            #break
                        
                #plays sound effects on click -H
                if (clicked):
                    #self.score_bubble = Bubble_Text("That's perfect!", "#ffffff",72,3, x-5, y-5)
                    #renpy.call_in_new_context("TestPosterLines")
                    self.the_score += 20  
                elif (self.x_offset <= x <= self.width*2 + self.x_offset) and (self.y_offset <= y <= self.height + self.y_offset):
                    #self.score_bubble = Bubble_Text("-5", "#f00",72,3, x-5, y-5)
                    
                    self.the_score = max(0,self.the_score - 5)  
               
                #game ends when no differences remain -H
                if self.count_differences() == 0:
                    if self.end_start != -1:
                        self.end_start = -1
                    
            if self.winner:
                    return (self.the_score)
                    
        #randomizes the overlay images
        def randomizeItems(self, difference_count):
            #randomzing at start:
            for index,i in enumerate(self.diff_items): 
                i.left = renpy.random.choice([True, False])
                
            #must be array size
            iterations = 5
            #while self.count_differences() < difference_count and iterations < 100:
            while iterations >= 0:
                i = diff_items[iterations]
                i.left = True
                #i.right = not i.left
                iterations -= 1
    
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
label TestCorgiLines():
    $ ui.add(difference_image)
    #$ renpy_blur(difference_image, 1.5)
    p "This is a test line."
    return



label minigamestart_corgi(gameimage="notdefault"):
    scene monaofficegame
    if gameimage == "1":
        python:
            #barks
            corgi_barks = []
            corgi_barks.append("That's perfect!")
            corgi_barks.append("No, that's not it. Though I bet you could something\ndelicious in that!")
            corgi_barks.append("Definitely not, unfortunately. I think I've seen\nsomething scurrying in and out of that lately. Careful!")
            corgi_barks.append("That won't work. Though I've seen it make tasty \nsnacks before that'll be sure to give you energy!")
            corgi_barks.append("I've seen that can be useful for various things,\nbut no, not for cheering. Please don't use that on me!")
            corgi_barks.append("Watch out for any fuzzy bits, though.\nIt's been sitting there awhile.")
            #overlaid objects
            # __________________
            #|                  |
            #|  1    2    3     |
            #|                  |
            #|    4    5    6   |
            #|__________________|
            diff_items = []
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay1.jpg", 57, 316, 325, 208))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay1.jpg", 823, 452, 213, 181))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay1.jpg", 1268, 467, 155, 156))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay1.jpg", 470, 770, 287, 300))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay1.jpg", 1240, 731, 268, 204))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay1.jpg", 1610, 835, 222, 207))
    if gameimage == "2":
        python:
            #barks
            corgi_barks = []
            # mug toaster stapler staples chips pompom
            corgi_barks.append("The wire on that looks busted. Not exactly inspiring.\nMore flammable than anything.")
            corgi_barks.append("Ooh still not sure that'll work. Did you clean it yet?\nI feel like the fuzzy things are getting bigger.")
            corgi_barks.append("I saw that thing crawling out of there earlier today.\nI'm naming it Geoffrey.")
            corgi_barks.append("Oh those will be perfect! Yes! Let's get the tape!")
            corgi_barks.append("{i}shudder{/i} Keep that away from me, please!")
            corgi_barks.append("I really dont like that thing. Those teeth?\nThey'd hurt my little paws!")
            #overlaid objects
            # __________________
            #|                  |
            #|  1    2    3     |
            #|                  |
            #|    4    5    6   |
            #|__________________|
            diff_items = []
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay2.jpg", 57, 316, 325, 208))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay2.jpg", 823, 452, 213, 181))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay2.jpg", 1268, 467, 155, 156))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay2.jpg", 470, 770, 287, 300))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay2.jpg", 1240, 731, 268, 204))
            diff_items.append(STD_Item("images/minigame/Corgi/CorgiOfficeOverlay2.jpg", 1610, 835, 222, 207))
    if gameimage == "default":
        return
    python:
        #time and score may not really be relevant to us -H
        starttime = renpy.time.time()
        the_score = 0
        renpy.block_rollback()
        #we need to be able to input an argument here
        difference_image = MinigameCorgi("images/minigame/Corgi/CorgiOfficeBase.jpg", diff_items)
        difference_image.randomizeItems(5)
        text_overlay = TextRender("images/minigame/corgi/CorgiBarkOverlay.png")
        #TempCleaningBackground = difference_image
        ui.add(difference_image)
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