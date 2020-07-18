class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return  Book(self.pages+other.pages)

    def __str__(self):
        return str(self.pages)
b=Book(100)
b1=Book(200)
b2=Book(200)
# print(type(b2))
print(b+b1+b2)
# b3=b+b1
# print (b3+b2)