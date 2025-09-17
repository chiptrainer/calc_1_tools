import math
from func_inp import get_function
from limits import compute_one_sided_limit, compute_limit_infinity, format_result

def find_asymptotes():
    """Find vertical and horizontal asymptotes"""
    print("\n=== ASYMPTOTE FINDER ===")
    print("Works best with rational functions")
    f = get_function()
    
    print("\n1. Find vertical asymptotes")
    print("2. Find horizontal asymptotes")
    print("3. Find both")
    
    choice = int(input("Choice: "))
    
    if choice in [1, 3]:
        print("\n--- Vertical Asymptotes ---")
        print("Checking common points...")
        # Check common points and zeros of denominator
        test_points = []
        for x in range(-10, 11):
            test_points.append(x)
        
        vas = []
        for x in test_points:
            try:
                # Check if limit approaches infinity
                left_lim = compute_one_sided_limit(f, x, True)
                right_lim = compute_one_sided_limit(f, x, False)
                
                if math.isinf(left_lim) or math.isinf(right_lim):
                    vas.append(x)
                    print(f"Vertical asymptote at x = {x}")
            except:
                pass
        
        if not vas:
            print("No vertical asymptotes found in [-10, 10]")
            print("(May exist outside this range)")
    
    if choice in [2, 3]:
        print("\n--- Horizontal Asymptotes ---")
        pos_inf = compute_limit_infinity(f, True)
        neg_inf = compute_limit_infinity(f, False)
        
        print(f"As x -> +inf: y -> {format_result(pos_inf)}")
        print(f"As x -> -inf: y -> {format_result(neg_inf)}")
        
        if not math.isnan(pos_inf) and not math.isinf(pos_inf):
            print(f"Horizontal asymptote: y = {pos_inf:.6f}")
        if not math.isnan(neg_inf) and not math.isinf(neg_inf) and abs(neg_inf - pos_inf) > 1e-6:
            print(f"Horizontal asymptote: y = {neg_inf:.6f}")

if __name__ == "__main__":
    while True:
        find_asymptotes()
        input("\nPress Enter to run again...")