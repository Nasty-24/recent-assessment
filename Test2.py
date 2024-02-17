class Colors:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
class Number(Colors):
    def __init__(self,roman,irabic):
        super().__init__(roman,irabic)
        self.roman = roman
        self.irabic = irabic
class Shapes(Colors):
    def __init__(self,circle,square,triangle):
        super().__init__(circle,square,triangle)
        self.circle = circle
        self.square = square
        self.triangle = triangle

numb1 = Number("RT",234)
numb2 = Number("ry",34)
print(numb1.red,numb1.green,numb1.blue)
print(numb1.red,numb1.green,numb1.blue)
print(numb1)
print(numb2)

