import math
#Quadratic equation

b = float ( input ( "Enter value of b: "))
a = float ( input ( "Enter value of a: "))
c = float ( input ( "Enter value of c: "))
under_root = pow ( b, 2 ) - (4*a*c)
if ( under_root < 0 ):
    print ( "Imaginary value")
else:
    x = ( -b + math.sqrt( under_root )) / ( 2*a)
    print ( f"{x}" )

    x2 = ( -b - math.sqrt( under_root )) / ( 2*a)
    print ( ".2f" x )

