import pygame


#Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)


Tasten =["X","Circle","Square","Triangle","L1","R1","L3","R3","Share","PS","Option","Touchpad"]
Achsen =["L3 H.","L3 V.","L2    ","R3 H.","R3 V.","R2    "]


class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None,20)

    def print(self, screen, textString):
        textBitmap =self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x,self.y])
        self.y += self.line_hight

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_hight = 15

    def Einzug(self):
        self.x += 10
    def Rueckzug(self):
        self.x -= 10
pygame.init()

#Fenster Größe
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PS4 Controller Auslesen")
done = False

clock = pygame.time.Clock()

pygame.joystick.init()

textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
    # Flag that we are done so we exit this loop

    screen.fill(WHITE) 
    textPrint.reset()
    
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    textPrint.print (screen, "Number of joysticks: {}".format(joystick_count) ) 
    textPrint.Einzug() # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i) 
        joystick.init()
        
        textPrint.print(screen, "Joystick {}".format(i) ) 
        textPrint.Einzug()

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print (screen, "Joystick Name: {}".format(name) )
        axes = joystick.get_numaxes()
        textPrint.print (screen, "Number of axes: {}".format(axes) )
        textPrint.Einzug()

        for i in range( axes ):
            axis = joystick.get_axis( i )
            Achse = Achsen [i] 
            textPrint.print (screen, "Axis {} value: {:.3f}".format(Achse, axis) ) 
        textPrint.Rueckzug()
        #gaspedal = joystick.get_axis(5)
        #print (gaspedal)

        buttons = joystick.get_numbuttons()
        textPrint.print (screen, "Number of buttons: {}".format(buttons) ) 
        textPrint.Einzug()

        for i in range( buttons ):
            button = joystick.get_button( i ) 
            Taste = Tasten[i]
            textPrint.print (screen, "Button {} value: {}".format(Taste,button) ) 
        textPrint.Rueckzug()
    # Hat switch. All or nothing for direction, not like joysticks.
    # Value comes back in an array.
        hats = joystick.get_numhats() 
        textPrint.print (screen, "Number of hats: {}".format(hats) ) 
        textPrint.Einzug()
        
        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrint.print (screen, "Hat {} value: {}".format(i, str(hat)) ) 
        textPrint.Rueckzug()
        textPrint.Rueckzug() 


        pygame.display.flip()
# Limit to 20 frames per second
        clock.tick(20)
pygame.quit ()