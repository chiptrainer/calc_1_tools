import math
from func_inp import get_function

def aroc():
    """Calculate Average Rate of Change"""
    print("\n=== AVERAGE RATE OF CHANGE ===")
    f = get_function()
    a = float(input("Start point (a): "))
    b = float(input("End point (b): "))
    
    try:
        fa = f(a)
        fb = f(b)
        if b - a == 0:
            print("Error: a and b must be different")
            return
        
        avg_roc = (fb - fa) / (b - a)
        print(f"\nf({a}) = {fa:.6f}")
        print(f"f({b}) = {fb:.6f}")
        print(f"AROC = {avg_roc:.6f}")
        print(f"\nThis is the slope of the secant line")
        print(f"from ({a}, {fa:.4f}) to ({b}, {fb:.4f})")
    except:
        print("Error calculating AROC")

if __name__ == "__main__":
    while True:
        aroc()
        input("\nPress Enter to run again...")