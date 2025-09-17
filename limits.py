import math
from func_inp import get_function

def format_result(val):
    """Format numerical result"""
    if math.isnan(val):
        return "DNE (Does Not Exist)"
    elif math.isinf(val):
        return "infinity" if val > 0 else "-infinity"
    else:
        return f"{val:.6f}"

def compute_one_sided_limit(f, c, from_left, epsilon=1e-7):
    """Compute one-sided limit"""
    h_values = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    results = []
    
    for h in h_values:
        try:
            if from_left:
                val = f(c - h)
            else:
                val = f(c + h)
            results.append(val)
        except:
            return float('nan')
    
    # Check convergence
    if len(results) >= 2:
        if abs(results[-1]) > 1e6:
            return float('inf') if results[-1] > 0 else float('-inf')
        if abs(results[-1] - results[-2]) < epsilon:
            return results[-1]
    
    return results[-1] if results else float('nan')

def compute_limit(f, c, epsilon=1e-7):
    """Compute two-sided limit"""
    left = compute_one_sided_limit(f, c, True)
    right = compute_one_sided_limit(f, c, False)
    
    if abs(left - right) < epsilon:
        return (left + right) / 2
    else:
        return float('nan')  # DNE

def compute_limit_infinity(f, positive=True):
    """Compute limit at infinity"""
    x_values = [10, 100, 1000, 10000, 100000]
    if not positive:
        x_values = [-x for x in x_values]
    
    results = []
    for x in x_values:
        try:
            results.append(f(x))
        except:
            return float('nan')
    
    # Check for convergence
    if len(results) >= 2:
        if abs(results[-1] - results[-2]) < 1e-6:
            return results[-1]
        elif abs(results[-1]) > abs(results[-2]) * 10:
            return float('inf') if results[-1] > 0 else float('-inf')
    
    return results[-1] if results else float('nan')

def limit_calculator():
    """Calculate limits numerically"""
    print("\n=== LIMIT CALCULATOR ===")
    f = get_function()
    
    print("\n1. Limit as x -> c")
    print("2. Limit as x -> infinity")
    print("3. Limit as x -> -infinity")
    print("4. One-sided limit (left)")
    print("5. One-sided limit (right)")
    
    limit_type = int(input("Type: "))
    
    if limit_type == 1:
        c = float(input("Approach point c: "))
        result = compute_limit(f, c)
        print(f"\nlim(x->{c}) f(x) = {format_result(result)}")
        
    elif limit_type == 2:
        result = compute_limit_infinity(f, positive=True)
        print(f"\nlim(x->inf) f(x) = {format_result(result)}")
        
    elif limit_type == 3:
        result = compute_limit_infinity(f, positive=False)
        print(f"\nlim(x->-inf) f(x) = {format_result(result)}")
        
    elif limit_type == 4:
        c = float(input("Approach point c: "))
        result = compute_one_sided_limit(f, c, from_left=True)
        print(f"\nlim(x->{c}-) f(x) = {format_result(result)}")
        
    elif limit_type == 5:
        c = float(input("Approach point c: "))
        result = compute_one_sided_limit(f, c, from_left=False)
        print(f"\nlim(x->{c}+) f(x) = {format_result(result)}")

if __name__ == "__main__":
    while True:
        limit_calculator()
        input("\nPress Enter to run again...")