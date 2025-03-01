class circle():
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * self.pi 
    
    def circum(self):
        return self.radius * self.pi * 2 
    

r1 = circle(10)

print(r1.radius)
print(r1.area())
print(r1.circum())