# creat class point 
class Point:
    
    def __init__(self, x=0 , y=0 ):
        self.__x = x
        self.__y = y
# getter for x
    def get_x(self) :  
        return self.__x
# getter for y
    def get_y(self) :
        return  self.__y
# setter for x
    def set_x(self,x) :
        self.__x = x
    def set_y(self,y) :
        self.__y = y

# Method to calculate the Euclidean distance between this point and another point
    def Distance(self,p):
        d = ((p.get_x() - self.__x)**2 + (p.get_y()**2 - self.__y)**2)**0.5
        return d
    # Method to calculate the Euclidean norm of this point
    def norm (self) :
        return ((self.__x)**2 + (self.__y)**2)**0.5
    