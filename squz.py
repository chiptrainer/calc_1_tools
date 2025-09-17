import math

def squeeze_theorem():
    """Demonstrate squeeze theorem"""
    print("\n=== SQUEEZE THEOREM ===")
    print("If g(x) <= f(x) <= h(x) near x=c")
    print("and lim g(x) = lim h(x) = L")
    print("then lim f(x) = L")
    
    print("\nExample: Find lim(x->0) x²sin(1/x)")
    print("\nWe know: -1 <= sin(1/x) <= 1")
    print("So: -x² <= x²sin(1/x) <= x²")
    
    print("\nLet's verify numerically:")
    x_vals = [0.1, 0.01, 0.001, 0.0001]
    print("\nx       | -x²      | x²sin(1/x) | x²")
    print("-" * 45)
    
    for x in x_vals:
        lower = -x**2
        try:
            middle = x**2 * math.sin(1/x)
        except:
            middle = 0
        upper = x**2
        print(f"{x:7.4f} | {lower:8.6f} | {middle:10.6f} | {upper:8.6f}")
    
    print("\nAs x->0: both -x² and x² approach 0")
    print("Therefore: lim(x->0) x²sin(1/x) = 0")

if __name__ == "__main__":
    while True:
        squeeze_theorem()
        input("\nPress Enter to run again...")