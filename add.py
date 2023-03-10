class vector :
    
    def __init__(self , x , y) :
        
        self.x = x 
        self.y = y
    
    def __add__(self, other):
        
        return vector(self.x + other.x, self.y + other.y)

v1 = vector(1 , 2)
v2 = vector(2 , 3)
v3 = v1 + v2

print(v3.x, v3.y)