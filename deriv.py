import math
from func_inp import get_function

def instantaneous_roc():
    """Estimate instantaneous rate of change"""
    print("\n=== INSTANTANEOUS ROC ===")
    print("(Derivative approximation)")
    f = get_function()
    c = float(input("Point c: "))
    
    # Use progressively smaller h values
    h_values = [0.1, 0.01, 0.001, 0.0001]
    print("\nApproaching from both sides:")
    print("h value    | Left deriv | Right deriv | Average")
    print("-" * 50)
    
    for h in h_values:
        try:
            left = (f(c) - f(c - h)) / h
            right = (f(c + h) - f(c)) / h
            avg = (left + right) / 2
            print(f"{h:10.4f} | {left:10.6f} | {right:11.6f} | {avg:10.6f}")
        except:
            print(f"{h:10.4f} | Error")
    
    # Final estimate with very small h
    h = 0.00001
    try:
        deriv = (f(c + h) - f(c - h)) / (2 * h)
        print(f"\nBest estimate: {deriv:.6f}")
        print("(This is the slope of the tangent line)")
    except:
        print("\nCannot compute at this point")

if __name__ == "__main__":
    while True:
        instantaneous_roc()
        input("\nPress Enter to run again...")