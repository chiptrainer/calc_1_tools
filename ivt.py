import math
from func_inp import get_function

def bisection_method(f, a, b, target, tol=1e-6):
    """Find where f(x) = target using bisection"""
    g = lambda x: f(x) - target
    
    for _ in range(100):  # Max iterations
        c = (a + b) / 2
        try:
            gc = g(c)
            if abs(gc) < tol:
                return c
            
            ga = g(a)
            if ga * gc < 0:
                b = c
            else:
                a = c
                
            if abs(b - a) < tol:
                return c
        except:
            return None
    return None

def ivt_demo():
    """Demonstrate Intermediate Value Theorem"""
    print("\n=== INTERMEDIATE VALUE THEOREM ===")
    print("If f is continuous on [a,b] and")
    print("N is between f(a) and f(b),")
    print("then there exists c in (a,b) where f(c)=N")
    
    f = get_function()
    a = float(input("\nInterval start (a): "))
    b = float(input("Interval end (b): "))
    
    try:
        fa = f(a)
        fb = f(b)
        print(f"\nf({a}) = {fa:.6f}")
        print(f"f({b}) = {fb:.6f}")
        
        if fa < fb:
            N = float(input(f"\nFind root for N in [{fa:.2f}, {fb:.2f}]: "))
            if fa <= N <= fb:
                # Use bisection method
                c = bisection_method(f, a, b, N)
                if c is not None:
                    print(f"\nFound: f({c:.6f}) = {f(c):.6f}")
                    print(f"(Target was N = {N})")
            else:
                print(f"N must be between {fa} and {fb}")
        else:
            N = float(input(f"\nFind root for N in [{fb:.2f}, {fa:.2f}]: "))
            if fb <= N <= fa:
                c = bisection_method(f, a, b, N)
                if c is not None:
                    print(f"\nFound: f({c:.6f}) = {f(c):.6f}")
                    print(f"(Target was N = {N})")
            else:
                print(f"N must be between {fb} and {fa}")
    except:
        print("Error evaluating function")

if __name__ == "__main__":
    while True:
        ivt_demo()
        input("\nPress Enter to run again...")