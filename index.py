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

