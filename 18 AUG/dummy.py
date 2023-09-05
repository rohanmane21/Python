import aug
def main():
    print("Choose a shape (circle/rectangle)")
    s = input("Enter your choice: ")
    match s:
        case 'circle':
            c1 = aug.circle()
            c1.claculat_area()
        case 'rectangle':
            r1 = aug.rectangle()
            r1.claculat_area()
        case _:
            print("Invalid Choice")

main()