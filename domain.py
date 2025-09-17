import math
from func_inp import get_function

def domain_finder():
    """Find domain restrictions"""
    print("\n=== DOMAIN FINDER ===")
    print("Common domain restrictions:")
    print("1. ln(x): x > 0")
    print("2. sqrt(x): x >= 0")
    print("3. 1/x: x != 0")
    print("4. tan(x): x != pi/2 + n*pi")
    print("5. sec(x): x != pi/2 + n*pi")
    print("6. csc(x): x != n*pi")
    
    print("\nTest a function's domain:")
    f = get_function()
    
    print("\nTesting points from -10 to 10:")
    undefined = []
    
    for x in range(-10, 11):
        try:
            val = f(x)
            if math.isnan(val) or math.isinf(val):
                undefined.append(x)
        except:
            undefined.append(x)
    
    if undefined:
        print(f"Function undefined at: {undefined}")
    else:
        print("Function defined on entire interval")
    
    # Check special points
    print("\nChecking special points:")
    special = [0, math.pi/2, math.pi, -math.pi/2, -math.pi]
    for x in special:
        try:
            val = f(x)
            if not math.isnan(val) and not math.isinf(val):
                print(f"f({x:.4f}) = {val:.6f}")
            else:
                print(f"f({x:.4f}) = undefined")
        except:
            print(f"f({x:.4f}) = undefined")

if __name__ == "__main__":
    while True:
        domain_finder()
        input("\nPress Enter to run again...")