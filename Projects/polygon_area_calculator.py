class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            self.picture = ("*" * self.width + "\n") * self.height
            return self.picture

    def get_amount_inside(self, othr):
        wfit = int(self.width/othr.width)
        hfit = int(self.height/othr.height)
        
        if wfit == 0 or hfit == 0:
            return 0
        else: return (wfit * hfit)



class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)
