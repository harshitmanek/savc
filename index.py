

def main():
    print "**************MENU*******************"
    print "1]VOLUME OF CUBE"
    print "2]SURFACE AREA OF CUBE"
    print "3]VOLUME OF CUBOID"
    print "4]SURFACE AREA OF CUBOID"
    e=int(raw_input("\n\t\tenter your choice:"))
    if(e==1):
        cube_volume()
    elif(e==2):
        cube_surface_area()
    elif(e==3):
        cuboid_volume()
    else:
        cuboid_surface_area() 


def cube_volume():
    s=int(raw_input("Enter side: "))
    volume=s*s*s*1.0
    print volume
def cube_surface_area():
    s=int(raw_input("Enter side: "))
    surfacearea=6.0*s*s
    print surfacearea
def cuboid_surface_area():
    length=float(raw_input("enter the length"))
    breadth=float(raw_input("enter the breadth"))
    height=float(raw_input("enter the height"))
    area=2*(length*breadth + breadth*height + length*height)
    print area
def cuboid_volume():
    length=float(raw_input("enter the length"))
    breadth=float(raw_input("enter the breadth"))
    height=float(raw_input("enter the height"))
    volume=length*breadth*height
    print volume
main()
