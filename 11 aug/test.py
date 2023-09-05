# class Car:
    
#     cn=input("Enter Name:")
#     cm=int(input("Enter Model"))
# c=Car()
# print(c.cn)
# print(c.cm)

    
class Car:
    def __init__(self,n,m) -> None:
        self.n=n
        self.m=m

    def details(self):
       print("Car Name:",self.n)
       print("\nCar Model",self.m)
c=Car("Honda",222)
c.details()
    
    
