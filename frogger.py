# final3.py - Frog Game
# Jiamin Li
# Create a python game in which there is a road with lanes of cars
# Moving in opposite direction
# And a frog which the user interacts with, by pressing up and down
# Buttons to successfully maneuver the frog across,
# With a banner on top of the window

from graphics import *
from time import sleep
from random import *

WIDTH = 800
HEIGHT = 700
FROG = "Frog3.gif"

class Banner:
    # Class for the banner atop the graphics window
    # Showing how many lives and # of crossings made
    def __init__( self, message ):
        """constructor.  Creates a message at the top of the graphics window"""
        self.text = Text( Point( WIDTH//2, 30 ), message )
        self.text.setFill( "black" )
        self.text.setTextColor( "black" )
        self.text.setSize( 20 )
        self.text.setFace( "arial" )
        self.text.setStyle( "bold" )
        
    def draw( self, win ): 
        """draws the text of the banner on the graphics window"""
        self.text.draw( win )
        self.win = win
        
    def setText( self, message ): 
        """change the text of the banner."""
        self.text.setText( message )

class Button:
    # Class for the UP/DOWN buttons
    def __init__( self, x1, y1, w, h, text ):
        p1 = Point( x1, y1 )
        p2 = Point( x1+w, y1+h )
        self.button = Rectangle( p1, p2 ) # creates the shape of the button
        self.button.setFill( "white" )
        self.button.setOutline( "white" )
        self.button.setWidth( 3 )
        self.label = Text( Point( x1+w//2, y1+h//2 ), text ) # inputs text for button (up/down)
        self.clicked = False # if not clicked, will remain false
        
    def draw( self, win ): # draws buttons
        self.button.draw( win )
        self.label.draw( win )

    def isClicked( self, p ): # if user clicks on button..
        # get the X, Y coordinates of Point 1 and Point 2 of the button
        x1, y1 = self.button.getP1().getX(), self.button.getP1().getY()
        x2, y2 = self.button.getP2().getX(), self.button.getP2().getY()

        # if where the user clicked (p) is within the boundaries of the button...
        # make the button turn pink
        if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
            self.clicked = not self.clicked
            self.button.setFill( color_rgb( 253, 68, 142 ) )
            sleep( 0.1 )
            self.button.setFill( "white" )
            return True
        else:
            return False
        
class Wheel:
    # Class for creating the wheels that will belong to the car
    def __init__( self, center, radius ):
        self.c1 = Circle( center, radius )
        self.c2 = Circle( center, radius//3 )
        self.c1.setFill( "black" )
        self.c2.setFill( "grey" )

    def draw( self, win ): # draws the wheels
        self.c1.draw( win )
        self.c2.draw( win )

    def move( self, dx, dy ): # moves the wheels along with the main body car
        self.c1.move( dx, dy )
        self.c2.move( dx, dy )

class Car:
    # Class for creating cars
    def __init__( self, refPoint ):
        x1 = refPoint.getX()
        y1 = refPoint.getY()
        x2 = x1 + 75 
        y2 = y1 + 35
        x3 = x1 + 10
        y3 = y1 - 10
        x4 = x3 + 55
        y4 = y1 
        self.body = Rectangle( Point( x1 , y1 ), Point( x2 , y2 ) )
        self.body.setWidth( 1 )
        self.body.setOutline( "black" )
        self.sBody = Rectangle( Point( x3, y3), Point( x4, y4 ) )
        self.sBody.setWidth( 1 )
        self.sBody.setOutline( "black" )
        self.w1 = Wheel( Point( x1+20, y1+40 ), 8 )
        self.w2 = Wheel( Point( x1+55, y1+40 ), 8 )

    def setFill( self, win ): # randomize colors of cars
        red = randint( 222, 255 )
        green = randint( 5, 247 )
        blue = randint( 106, 243 )
        color = color_rgb( red, green, blue )
        blue, red, green = red, green, blue
        color2 = color_rgb( red, green, blue )
        self.body.setFill( color )
        self.sBody.setFill( color2 )

    def draw( self, win ): # draw the cars
        self.body.draw( win )
        self.sBody.draw( win )
        self.w1.draw( win )
        self.w2.draw( win )

    def getP1( self ): # gets the X, Y coordinates of Point 1 from main body of car
        return self.body.getP1()
    
    def getP2( self ): # gets the X, Y coordinates of Point 2 from main body of car
        return self.body.getP2()
        
    def move( self, dx, dy ): # move te cars
        self.body.move( dx, dy )
        self.sBody.move( dx, dy )
        self.w1.move( dx, dy )
        self.w2.move( dx, dy )

        x = self.body.getP2().getX() # store X coordinate of Point 2 (right edge of car)
        if x > WIDTH + 10: # if car leaves the window, car will come back around, delayed
            self.body.move( -WIDTH-50, 0 )
            self.sBody.move( -WIDTH-50, 0 )
            self.w1.move( -WIDTH-50, 0 )
            self.w2.move( -WIDTH-50, 0 )
        if x < 0 - 10:
            self.body.move( WIDTH+50, 0 )
            self.sBody.move( WIDTH+50, 0 )
            self.w1.move( WIDTH+50, 0 )
            self.w2.move( WIDTH+50, 0 )
            
class Road():
    # This is the class for designing the roads
    def __init__( self, x1, y1, w, h ):
        p1 = Point( x1, y1 )
        p2 = Point( x1+w, y1+h )
        self.rectangle = Rectangle( p1, p2 )
        self.rectangle.setFill( "gray" )

    def draw( self, win ): # draw the road
        self.rectangle.draw( win )

class Frog():
    # This is the class for drawing the frog
    def __init__( self, p ):
        self.img = Image( p, FROG ) # obtains image from computer

    def draw( self, win ): # draw the frog
        self.img.draw( win )

    def move( self, dx, dy ): # move the frog
        self.img.move( dx, dy )

    def getAnchor( self ): # gets location of the frog in Point( x, y )
        return self.img.getAnchor()

    def undraw( self ): # undraws the frog for when it dies or crosses
        self.img.undraw()


def drawRoad( win ):
    # Creating edge of top road and edge of bottom road
    road_top = Road( 0, 150, WIDTH, 25 )
    road_bottom = Road( 0, HEIGHT-250, WIDTH, 25 )
    road_top.draw( win ) 
    road_bottom.draw( win )
    return road_top, road_bottom

def drawButton( win ):
    # Creating the up and down buttons
    upButton = Button( WIDTH-100, 75, 50, 50, "▲" )
    downButton = Button( WIDTH-100, 495, 50, 50, "▼" )
    upButton.draw( win )
    downButton.draw( win )
    return upButton, downButton

def drawCars( win ):
    # Function to draw cars
    # Empty lists 
    carsList = []
    carsList2 = []
    carsList3 = []
    # Lane with 4 cars
    for i in range( 4 ):
        car = Car( Point( 200*i, 200 ) )
        car.setFill( win )
        car.draw( win )
        carsList.append( car )
    # Lane with 3 cars
    for i in range( 3 ):
        car2 = Car( Point( 200*i, 300 ) )
        car2.setFill( win )
        car2.draw( win )
        carsList2.append( car2 )
    # Lane with 3 cars
    for i in range( 3 ):
        car3 = Car( Point( 200*i, 390 ) )
        car3.setFill( win )
        car3.draw( win )
        carsList3.append( car3 )

    return carsList, carsList2, carsList3
        
def main():
    win = GraphWin( "Frogger Game", WIDTH, HEIGHT )
    win.setBackground( color_rgb( 235, 255, 190 ) )
    
    # Draw banner
    banner = Banner( "3 heart(s) left — 0 crossing(s)" )
    banner.draw( win )

    # Draw roads, draw buttons
    road_top, road_bottom = drawRoad( win )
    upButton, downButton = drawButton( win )

    # Draw 3 lanes of cars              
    carsList, carsList2, carsList3 = drawCars( win )

    # Draw frog from image
    frog_point = Point( WIDTH//2, HEIGHT-75 )
    frog = Frog( frog_point )
    frog.draw( win )

    # Initial # of lives count (3)
    # And initial # of times crossed (0)
    lives = 3
    crossed = 0

    # Animation loop
    while True:

        clickedPoint = win.checkMouse()
                
        frogX = frog.getAnchor().getX() # Get points of where the frog is
        frogY = frog.getAnchor().getY() # Placeholder variables

        # If either UP/DOWN buttons are clicked, move the frog
        if clickedPoint != None and upButton.isClicked( clickedPoint ):
            frog.move( 0, -10 )

        if clickedPoint != None and downButton.isClicked( clickedPoint ):
            frog.move( 0, 10 )

        # Move each car in first list
        for car in carsList:
            dx = 0.2
            dy = 0
            car.move( dx, dy )
            # Store points of each car's location
            cx1, cy1 = car.getP1().getX()-20, car.getP1().getY()-20
            cx2, cy2 = car.getP2().getX()+20, car.getP2().getY()+20
            # Get location of frog 
            frogX = frog.getAnchor().getX()
            frogY = frog.getAnchor().getY()
            # If location of frog touches the car close enough,
            # Undraw the frog, and redraw it from its original location
            if cy1 <= frogY <= cy2 and  cx1 <= frogX <= cx2:
                frog.undraw()
                frog = Frog( frog_point )
                frog.draw( win )
                lives = lives - 1 # touching car results in losing 1 life
                banner.setText( "{0:1} hearts left — {1:1} crossing(s)" # banner will reflect # of lives left
                                .format( lives, crossed ) )

        # Move each car in second list, same documentation as above
        for car in carsList2:
            dx = -0.3
            dy = 0
            car.move( dx, dy )
            cx1, cy1 = car.getP1().getX()-20, car.getP1().getY()-20
            cx2, cy2 = car.getP2().getX()+20, car.getP2().getY()+20
            frogX = frog.getAnchor().getX()
            frogY = frog.getAnchor().getY()           
            if cy1 <= frogY <= cy2 and  cx1 <= frogX <= cx2:
                frog.undraw()
                frog = Frog( frog_point )
                frog.draw( win )
                lives = lives - 1
                banner.setText( "{0:1} hearts left — {1:1} crossing(s)"
                                .format( lives, crossed ) )

        # Move each car in third list, same documention as above
        for car in carsList3:
            dx = 0.1
            dy = 0
            car.move( dx, dy )
            # Add -20, + 20 for flexibility in range of getting touched by car
            cx1, cy1 = car.getP1().getX()-20, car.getP1().getY()-20
            cx2, cy2 = car.getP2().getX()+20, car.getP2().getY()+20
            frogX = frog.getAnchor().getX()
            frogY = frog.getAnchor().getY()           
            if cy1 <= frogY <= cy2 and  cx1 <= frogX <= cx2:
                frog.undraw()
                frog = Frog( frog_point )
                frog.draw( win )
                lives = lives - 1
                banner.setText( "{0:1} hearts left — {1:1} crossing(s)"
                                .format( lives, crossed ) )

        # If frog did not get hit by any cars, it has successfully crossed the gray border
        if frogY <= 160:
            frog.undraw() # if it crosses, return it to original spot as well!
            frog = Frog( frog_point )
            frog.draw( win ) # and draw it again
            crossed = crossed + 1 # this time, banner will + 1 successful crossing
            banner.setText( "{0:1} hearts left — {1:1} crossing(s)"
                                .format( lives, crossed ) )

        # If frog has unsuccessfully tried crossing 3 times/hit 3 times, game over
        if lives == 0:
            banner.setText( "Game over :( Froggy crossed {0:1} times(s)"
                            .format ( crossed ) )
            break # and break the animation loop to end the game
        
    win.getMouse()
    win.close()

main()


