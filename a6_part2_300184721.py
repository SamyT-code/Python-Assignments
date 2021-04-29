class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    'class that represents a 2D (axis-parallel) rectangle that a user can draw on a computer screen'

    def __init__(self,bottom_left, top_right, color):
        '''(Rectangle, Point, Point, str)-> None
        Preconditions: first Point (passed to the constructor, i.e. __init__) will always have smaller than
        or equal x coordinate than the x coordinate of the second Point and smaller than or equal y coordinate
        than the y coordinate of the second Point'''
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color


    def get_bottom_left(self):
        '''(Rectangle)-> Point'''
        return self.bottom_left

    def get_top_right(self):
        '''(Rectangle)-> Point'''
        return self.top_right

    def get_color(self):
        '''(Rectangle)-> str'''
        return self.color

    def reset_color(self, color):
        '''(Rectangle)-> None'''
        self.color = color

    def get_perimeter(self):
        '''(Rectangle)-> number
        returns the perimeter of the rectangle'''
        x2 = self.get_top_right().x
        x1 = self.get_bottom_left().x
        y2 = self.get_top_right().y
        y1 = self.get_bottom_left().y
        return 2*(abs(x2 - x1)) + 2*(abs(y2-y1))

    def get_area(self):
        '''(Rectangle)-> number
        returns the area of the rectangle'''
        x2 = self.get_top_right().x
        x1 = self.get_bottom_left().x
        y2 = self.get_top_right().y
        y1 = self.get_bottom_left().y
        base = x2-x1
        hauteur = y2-y1
        return abs(base * hauteur)

    def move(self, dx, dy):
        '''(Rectangle, number, number)->number
        Displaces the top and bottom points'''
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)        
        

    def intersects(self, other):
        '''(Rectangle)->bool
        Returns True if 2 rectangles intersect with each other, False otherwise'''
        if (other.bottom_left.x <= self.top_right.x and other.top_right.x >= self.bottom_left.x and other.top_right.y >= self.bottom_left.y and other.bottom_left.y <= self.top_right.y) == True:
            return True
        else:
            return False

    def contains(self, px, py):
        '''(Rectangle)->bool
        Returns True if a point is in the rectange, false otherwise'''
        if (self.top_right.y >= py and self.bottom_left.x <= px and self.top_right.x >= px and self.bottom_left.y <= py) == True:
            return True
        return False
    
    ### 3 methods to override pythons object methods

    def __str__(self):
        '''(Rectangle)->str
        returns nice string representation'''
        return 'I am a ' + str(self.color) + ' rectangle with bottom left corner at ' + str(self.bottom_left) + ' and top right corner at ' + str(self.top_right) + '.'

    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation of the rectangle'''
        return 'Rectangle(' + str(self.bottom_left) + ',' + str(self.top_right) + ",'" + str(self.color) + "')"

    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have the same coordinates'''
        return self.bottom_left == other.bottom_left and self.top_right == other.top_right and self.color == other.color
        
    
    ### 3 methods to override pythons object methods

    

    

class Canvas:
    'class that represents a collection of Rectangles'

    def __init__(self):
        '''(Canvas)->None
        Creates an empty list'''
        self.list = []

    def __len__(self):
        '''(Canvas)->number
        Returns the amount of recangles inside canvas'''
        return len(self.list)

    def __repr__(self):
        '''(Canvas)->str
        Prints the Canvas in a nice way'''
        return 'Canvas(' + str(self.list) + ')'
        

    def add_one_rectangle(self, rectangle):
        '''(Canvas, Rectangle)->Canvas
        Add rectangles to the Canvas'''
        self.list.append(rectangle)


    def count_same_color(self, color):
        '''(Rectangle, str)->int
        return the amount of times a certain color is present in the canvas'''
        counter = 0
        for rectangle in self.list:
            if rectangle.color == color:
                counter = counter + 1
        return counter

    def total_perimeter(self):
        '''(Canvas)->int
        Returns the total perimeter of the rectangles'''
        counter = 0
        for rectangle in self.list:
            counter = counter + rectangle.get_perimeter()
        return counter

    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle
        Returns an all encompassing rectangle (which is by default red)'''
        min_x_bottom = []
        min_y_bottom = []
        max_x_top = []
        max_y_top = []
        for rectangle in self.list:
            min_x_bottom.append(rectangle.bottom_left.x)
            min_y_bottom.append(rectangle.bottom_left.y)
            max_x_top.append(rectangle.top_right.x)
            max_y_top.append(rectangle.top_right.y)
        min_x = min(min_x_bottom)
        min_y = min(min_y_bottom)
        max_x = max(max_x_top)
        max_y = max(max_y_top)
        return Rectangle(Point(min_x,min_y), Point(max_x, max_y), 'red')

    def common_point(self):
        '''(Canvas)->bool
        Returns True if a point is inside all the Reactangles, false otherwise'''
        for rectangleA in self.list:
            for rectangleB in self.list:
                if rectangleA.intersects(rectangleB):
                    pass
                else:
                    return False
        return True
            
        













