image TempCleaningBackground = False

init python:
    import math
    import pygame
    import time
    #renpy.add_layer("middle", above="master")

    # Value that determines zoom level -H
    zoomfactor = 1
    global BarkSpeaker
    BarkSpeaker = "None"
    #Main game-running function -H
    class MinigameCleaningArnolfini(renpy.Displayable):

        def __init__(self, child, diff_items, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(MinigameCleaningArnolfini, self).__init__(**kwargs)

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
            self.end_delay = 3
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
                global BarkSpeaker
                if BarkSpeaker == "arw":
                    textbox_img = Transform(text_overlay_arw, alpha=myalpha)
                elif BarkSpeaker == "arm":
                    textbox_img = Transform(text_overlay_arm, alpha=myalpha)
                else:
                    textbox_img = Transform(text_overlay_ard, alpha=myalpha)
                score_img = renpy.render(score_bubble_img, width, height,  st, at)
                textbox_overlay = renpy.render(textbox_img, width, height,  st, at)
                render.blit(textbox_overlay, (self.score_bubble.x,self.score_bubble.y -785))
                render.blit(score_img,(self.score_bubble.x + 230,self.score_bubble.y + 60))
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
            global BarkSpeaker
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
                if self.end_start != -1:
                    for index,i in enumerate(self.diff_items): 
                        if i.left != i.right:
                            if (i.x * zoomfactor + self.x_offset-self.gutter <= x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset) :
                                if (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[0].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[0].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arw"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[0], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[1].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[1].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arm"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[1], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[2].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[2].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arm"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[2], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[3].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[3].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arw"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[3], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[4].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[4].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arm"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[4], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[5].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[5].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arw"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[5], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[6].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[6].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arw"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[6], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[7].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[7].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arm"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[7], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[8].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[8].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "ard"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[8], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[9].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[9].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arm"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[9], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[10].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[10].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arw"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[10], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[11].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[11].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arm"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[11], "#ffffff",30,3, x, y)
                                elif (i.x * zoomfactor + self.x_offset-self.gutter <= diff_items[12].x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= diff_items[12].y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):
                                    BarkSpeaker = "arw"
                                    self.score_bubble = Bubble_Text(arnolfini_barks[12], "#ffffff",30,3, x, y)
                                else:
                                    BarkSpeaker = "arm"
                                    self.score_bubble = Bubble_Text("Keep looking!", "#ffffff",30,3, x, y)
                                i.left = i.right
                                clicked = True
                                break
                            #left side
                            #zoomfactor needed to make sure the clickable bounds match the visible images -H
                            #if (i.x * zoomfactor + self.x_offset-self.gutter <= x <= i.x * zoomfactor + i.w * zoomfactor + self.x_offset-self.gutter) and (i.y * zoomfactor + self.y_offset <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset) :  
                                #i.left = i.right
                                #clicked = True
                                #break
                            
    
                        #right side
                        #elif (i.x * zoomfactor + self.x_offset + self.width+self.gutter <= x <= i.x * zoomfactor + self.width + i.w * zoomfactor + self.x_offset+self.gutter) and (i.y * zoomfactor <= y <= i.y * zoomfactor + i.h * zoomfactor + self.y_offset):   
                            #i.right = i.left 
                        
                #plays sound effects on click -H
                #renpy.random.choice(["Impressive!", "No holding back!", "Splendid job!", "Yeah, lets go!"])
                if (clicked):
                    #self.score_bubble = Bubble_Text(renpy.random.choice(["Placeholder", "Placeholder", "Placeholder", "Placeholder"]), "ffffff",48,3, x-15, y-5)
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



label minigamestart_cleaning_arnolfini(gameimage="notdefault"):
    scene cleaning bg
    python:
        diff_items = []
        arnolfini_barks = []
        #stains
        arnolfini_barks.append("Oh, I love green. I had an outfit that color.")
        arnolfini_barks.append("I think I killed a man once...")
        arnolfini_barks.append("I remember a dress, a veil... was it a wedding?")
        #chips
        arnolfini_barks.append("Ah, food! I've always wanted to try it!")
        arnolfini_barks.append("I think we had something like that at a party!")
        arnolfini_barks.append("Have you ever cooked? Have I?")
        #socks
        arnolfini_barks.append("Nowhere near as fancy as what we wear.")
        arnolfini_barks.append("Didn't we get socks as children one Christmas?\nTogether?")
        arnolfini_barks.append("I have this really intense desire\nto chew on those socks right now.")
        #cups
        arnolfini_barks.append("A drink vessel! Rather plain, isn't it?")
        arnolfini_barks.append("We had drinks with family once! I think...")
        arnolfini_barks.append("What a waste.")
        arnolfini_barks.append("I remember a dinner with wine...")
        #stains
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 383, 65, 270, 150))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 767, 112, 295, 186))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1690, 0, 230, 550))
        #chips
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 487, 529, 60, 77))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 643, 699, 148, 108))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1438, 831, 211, 174))
        #socks
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 796, 598, 128, 77))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 361, 951, 217, 120))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1128, 886, 179, 107))
        #bottles
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 496, 635, 121, 62))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1019, 583, 83, 108))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 813, 907, 173, 122))
        diff_items.append(STD_Item("images/minigame/cleaning/cleaning fineart overlay.png", 1288, 668, 107, 93))
    if gameimage == "default":
        return
    python:
        #time and score may not really be relevant to us -H
        starttime = renpy.time.time()
        the_score = 0
        renpy.block_rollback()
        #we need to be able to input an argument here
        difference_image = MinigameCleaningArnolfini("fineart_tod", diff_items)
        difference_image.randomizeItems(9)
        text_overlay_arm = TextRender("images/minigame/Arnolfini/ARMBarkOverlay.png")
        text_overlay_arw = TextRender("images/minigame/Arnolfini/ARWBarkOverlay.png")
        text_overlay_ard = TextRender("images/minigame/Arnolfini/ARDBarkOverlay.png")
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