class Circle:
   def __init__(self,radius):
      self.radius=radius
   def area(self):
      return 3.14*self.radius*self.radius
class Rectangle:
   def __init__(self,length,breadth):
      self.length=length
      self.breadth=breadth
   def area(self):
      return self.length*self.breadth
radius=float(input("Enter the number:"))
length=float(input("Enter the number:"))
breadth=float(input("Enter the number:"))
circle=Circle(radius)
rectangle=Rectangle(length,breadth)
print("Area of Circle:",circle.area())

print("Area of Rectangle:",rectangle.area())


