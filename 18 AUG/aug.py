class shape:
    def __init__(self) -> None:
        pass

class circle(shape):
    def __init__(self) -> None:
        super().__init__()
        # self.radius = float(input("Enter the Radius:"))
        self.a=int(input("Enter First Number:"))
        self.b=int(input("Enter Second Number:"))
    def claculat_area(self):
        # print("Area of Circle: ",3.14*self.radius*self.radius)
        print("Sum Of Two Number: ",self.a+self.b)


# class rectangle(shape):
#     def __init__(self) -> None:
#         super().__init__()
#         self.width = float(input("Enter the width:"))
#         self.height = float(input("Enter the height:"))
#     def claculat_area(self):
#         print("Area of Rectangle: ",self.width*self.height) 

def main():
    print("Choose a shape (circle/rectangle)")
    s = input("Enter your choice: ")
    match s:
        case 'circle':
            c1 = circle()
            c1.claculat_area()
        # case 'rectangle':
        #     r1 = rectangle()
        #     r1.claculat_area()
        case _:
            print("Invalid Choice")

main()