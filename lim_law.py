import math
from func_inp import get_function

def compute_limit(f, c, epsilon=1e-7):
    """Compute two-sided limit"""
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
    
    left = compute_one_sided_limit(f, c, True)
    right = compute_one_sided_limit(f, c, False)
    
    if abs(left - right) < epsilon:
        return (left + right) / 2
    else:
        return float('nan')  # DNE

def format_result(val):
    """Format numerical result"""
    if math.isnan(val):
        return "DNE (Does Not Exist)"
    elif math.isinf(val):
        return "infinity" if val > 0 else "-infinity"
    else:
        return f"{val:.6f}"

def limit_laws():
    """Display and demonstrate limit laws"""
    print("\n=== LIMIT LAWS ===")
    print("\nIf lim f(x) = L and lim g(x) = M, then:")
    print("1. Sum: lim[f(x) + g(x)] = L + M")
    print("2. Difference: lim[f(x) - g(x)] = L - M")
    print("3. Product: lim[f(x) * g(x)] = L * M")
    print("4. Quotient: lim[f(x)/g(x)] = L/M (if M != 0)")
    print("5. Power: lim[f(x)^n] = L^n")
    print("6. Root: lim[nth_root(f(x))] = nth_root(L)")
    
    print("\nDemonstration:")
    print("Let's verify with two functions")
    
    f = get_function()
    print("Second function:")
    g = get_function()
    c = float(input("Point to approach: "))
    
    lim_f = compute_limit(f, c)
    lim_g = compute_limit(g, c)
    
    print(f"\nlim(x->{c}) f(x) = {format_result(lim_f)}")
    print(f"lim(x->{c}) g(x) = {format_result(lim_g)}")
    
    if not math.isnan(lim_f) and not math.isnan(lim_g):
        # Verify each law
        sum_func = lambda x: f(x) + g(x)
        lim_sum = compute_limit(sum_func, c)
        print(f"\nSum law: {format_result(lim_sum)} = {format_result(lim_f + lim_g)}")
        
        prod_func = lambda x: f(x) * g(x)
        lim_prod = compute_limit(prod_func, c)
        print(f"Product law: {format_result(lim_prod)} = {format_result(lim_f * lim_g)}")
        
        if abs(lim_g) > 1e-6:
            quot_func = lambda x: f(x) / g(x) if g(x) != 0 else float('nan')
            lim_quot = compute_limit(quot_func, c)
            print(f"Quotient law: {format_result(lim_quot)} = {format_result(lim_f / lim_g)}")

if __name__ == "__main__":
    while True:
        limit_laws()
        input("\nPress Enter to run again...")