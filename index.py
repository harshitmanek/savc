<<<<<<< HEAD

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
    side=raw_input("Enter side: ")
    volume=s*s*s*1.0
    print volume
def cube_surface_area():
    side=raw_input("Enter side: ")
    surfacearea=6.0*s*s
    print surfacearea

=======
<<<<<<< HEAD
def main():
    pass
def cube_volume():
    pass
def cube_surface_area():
    pass
def cuboid_volume():
    pass
def cuboid_surface_area():
    pass

=======
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
>>>>>>> 89bfc225f00fade9d65058131d4ae401710f9eeb
>>>>>>> 89966e17325755565318d18053893e95ed68c12f
