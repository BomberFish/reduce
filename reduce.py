# Program requires gcd function from math library
from math import gcd
# For showing full error logs
import traceback


def handleError(e):
    # Simple error handler
    # Prints message & traceback to stdout and exits
    print(e, "Exiting...")
    print("Full error log:")
    traceback.print_tb()
    exit(1)

try:
    # Ask user for numerator and convert to int
    n = int(input("Type in an integer numerator: "))
except:
    # Throw error if not integer
    handleError("Numerator must be an integer.")
try:
    # Ask user for numerator and convert to int
    d = int(input("Type in an integer denominator: "))
except:
    # Throw error if not integer
    handleError("Denominator must be an integer. Exiting...")

# Makes fraction have proper form
if d < 0:
    n = n*-1
    d = d*-1

# Print numerator and denominator as unsimplified fraction
if d == 0:
    frac = "undefined"
else:
    frac = str(n) + " / " + str(d)
print("Your fraction is " + frac)

# Finds greatest common divisor of numerator and denominator
gcf = gcd(n, d)

# Divides numerator and denominator by the gcd
n_simplified = n / gcf
d_simplified = d / gcf

if d_simplified == 0:
    # If denominator is 0
    frac_simplified = "undefined"
elif d_simplified == 1:
    # If fraction ends up being equal to a whole number
    # Must be converted to int since python is quirky like that
    frac_simplified = str(int(n_simplified))
elif n_simplified == 0:
    # If numerator is 0, fraction is equal to 0
    frac_simplified = "0"
else:
    # If fraction is already properly formatted
    # Formats numerator and denominator into fraction as string
    # Also has to be converted to int
    frac_simplified = str(int(n_simplified)) + " / " + str(int(d_simplified))

# Print numerator and denominator as simplified fraction
print("The reduced fraction is " + frac_simplified)

# Checks if frac_simplified is the same as frac
if frac_simplified == frac:
    # Tells user fraction is already simplified
    print("This fraction cannot be further reduced.")