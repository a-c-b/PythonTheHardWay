from fractions import Fraction	
from decimal import Decimal


furst = raw_input ("\nFirst fraction ") # a variable
sknd = raw_input("Second Fraction? ") #b variable

dec_furst = float(Fraction(furst))
dec_sknd = float(Fraction(sknd))

a = float(dec_furst)+float(dec_sknd)
b = float(dec_furst)-float(dec_sknd)

# get the fractional values of the decimal results
d = Fraction(Decimal(a - int(a)))
e = Fraction(Decimal(b - int(b)))

print a; print b;  print "Fractions added: ",d; print "Fractions subtracted: ", e

