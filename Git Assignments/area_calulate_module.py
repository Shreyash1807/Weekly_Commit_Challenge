import math
def calculate_area(choice):
    match choice:
        case 1:
            r=float(input("Ener Radius : >>>> "))
            area_c=3.14*r*r
            print("Area Of Circul = ",area_c)

        case 2:
            b=float(input("Enter Base : >>>> "))
            h=float(input("Enter Height : >>>> "))
            area_t=0.5*b*h
            print("Area Of Triangle = ",area_t)

        case 3:
            s=float(input("Enter Side : >>>> "))
            area_s=s*s
            print("Area Of squre = ",area_s)

        case 4:
            l=float(input("Enter Length : >>>> "))
            w=float(input("Enter width : >>>> "))
            area_r=l*w
            print("Area Of Rectangle = ",area_r) 

        case _:
            print("Invalid Choice....!!! Try Again..")       