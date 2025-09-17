import math
from func_inp import get_function
from limits import compute_limit, compute_one_sided_limit

def check_continuity():
    """Check if function is continuous at a point"""
    print("\n=== CONTINUITY CHECKER ===")
    f = get_function()
    c = float(input("Check continuity at x = "))
    
    print("\nChecking three conditions:")
    
    # Condition 1: f(c) is defined
    try:
        fc = f(c)
        if math.isnan(fc) or math.isinf(fc):
            print("1. f(c) is NOT defined [FAIL]")
            print("   Function is DISCONTINUOUS")
            return
        else:
            print(f"1. f(c) = {fc:.6f} [PASS]")
    except:
        print("1. f(c) is NOT defined [FAIL]")
        print("   Function is DISCONTINUOUS")
        return
    
    # Condition 2: limit exists
    limit = compute_limit(f, c)
    if math.isnan(limit):
        print("2. Limit does NOT exist [FAIL]")
        left = compute_one_sided_limit(f, c, True)
        right = compute_one_sided_limit(f, c, False)
        print(f"   Left limit: {format_result(left)}")
        print(f"   Right limit: {format_result(right)}")
        print("   Function is DISCONTINUOUS")
        return
    else:
        print(f"2. lim(x->{c}) f(x) = {limit:.6f} [PASS]")
    
    # Condition 3: f(c) = limit
    if abs(fc - limit) < 1e-6:
        print(f"3. f(c) = limit [PASS]")
        print("\n   Function is CONTINUOUS at this point!")
    else:
        print(f"3. f(c) != limit [FAIL]")
        print("   Function is DISCONTINUOUS")
        print("   (Removable discontinuity)")

def format_result(val):
    """Format numerical result"""
    if math.isnan(val):
        return "DNE (Does Not Exist)"
    elif math.isinf(val):
        return "infinity" if val > 0 else "-infinity"
    else:
        return f"{val:.6f}"

if __name__ == "__main__":
    while True:
        check_continuity()
        input("\nPress Enter to run again...")