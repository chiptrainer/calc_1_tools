import math

def get_function():
    """Display function menu and return selected function"""
    print("\n=== SELECT FUNCTION ===")
    print("1. Polynomial (ax^n + bx^(n-1) + ...)")
    print("2. sin(x)")
    print("3. cos(x)")
    print("4. tan(x)")
    print("5. sec(x) = 1/cos(x)")
    print("6. csc(x) = 1/sin(x)")
    print("7. cot(x) = 1/tan(x)")
    print("8. ln(x)")
    print("9. e^x")
    print("10. sqrt(x)")
    print("11. 1/x")
    print("12. 1/x^2")
    print("13. Rational (P(x)/Q(x))")
    print("14. |x|")
    print("15. Custom expression")
    print("16. Piecewise function")
    
    choice = int(input("Choice: "))
    
    if choice == 1:
        degree = int(input("Polynomial degree: "))
        coeffs = []
        for i in range(degree, -1, -1):
            c = float(input(f"Coeff for x^{i}: "))
            coeffs.append(c)
        return lambda x: sum(coeffs[degree-i] * x**i for i in range(degree+1))
    
    elif choice == 2:
        return lambda x: math.sin(x)
    elif choice == 3:
        return lambda x: math.cos(x)
    elif choice == 4:
        return lambda x: math.tan(x)
    elif choice == 5:
        return lambda x: 1/math.cos(x) if math.cos(x) != 0 else float('inf')
    elif choice == 6:
        return lambda x: 1/math.sin(x) if math.sin(x) != 0 else float('inf')
    elif choice == 7:
        return lambda x: 1/math.tan(x) if math.tan(x) != 0 else float('inf')
    elif choice == 8:
        return lambda x: math.log(x) if x > 0 else float('-inf')
    elif choice == 9:
        return lambda x: math.exp(x)
    elif choice == 10:
        return lambda x: math.sqrt(x) if x >= 0 else float('nan')
    elif choice == 11:
        return lambda x: 1/x if x != 0 else float('inf')
    elif choice == 12:
        return lambda x: 1/(x**2) if x != 0 else float('inf')
    
    elif choice == 13:
        print("Numerator polynomial:")
        n_deg = int(input("Degree: "))
        n_coeffs = []
        for i in range(n_deg, -1, -1):
            c = float(input(f"Coeff for x^{i}: "))
            n_coeffs.append(c)
        
        print("Denominator polynomial:")
        d_deg = int(input("Degree: "))
        d_coeffs = []
        for i in range(d_deg, -1, -1):
            c = float(input(f"Coeff for x^{i}: "))
            d_coeffs.append(c)
        
        def rational(x):
            num = sum(n_coeffs[n_deg-i] * x**i for i in range(n_deg+1))
            den = sum(d_coeffs[d_deg-i] * x**i for i in range(d_deg+1))
            if den == 0:
                return float('inf')
            return num / den
        return rational
    
    elif choice == 14:
        return lambda x: abs(x)
    
    elif choice == 15:
        print("Build expression using:")
        print("x, +, -, *, /, **, sin, cos, tan, log")
        expr_str = input("Expression: ")
        # Create safe evaluation function
        def custom_func(x):
            try:
                # Replace common functions with math module versions
                safe_dict = {
                    'x': x,
                    'sin': math.sin,
                    'cos': math.cos,
                    'tan': math.tan,
                    'log': math.log,
                    'ln': math.log,
                    'exp': math.exp,
                    'sqrt': math.sqrt,
                    'pi': math.pi,
                    'e': math.e
                }
                return eval(expr_str, {"__builtins__": {}}, safe_dict)
            except:
                return float('nan')
        return custom_func
    
    elif choice == 16:
        print("Piecewise function setup:")
        n_pieces = int(input("Number of pieces: "))
        pieces = []
        for i in range(n_pieces):
            print(f"\nPiece {i+1}:")
            print("Condition type:")
            print("1. x < value")
            print("2. x <= value")
            print("3. x > value")
            print("4. x >= value")
            print("5. x == value")
            print("6. value1 < x < value2")
            cond_type = int(input("Type: "))
            
            if cond_type <= 5:
                val = float(input("Value: "))
            else:
                val1 = float(input("Value1: "))
                val2 = float(input("Value2: "))
            
            print("Function for this piece:")
            func = get_simple_function()
            
            if cond_type == 1:
                pieces.append((lambda x, v=val: x < v, func))
            elif cond_type == 2:
                pieces.append((lambda x, v=val: x <= v, func))
            elif cond_type == 3:
                pieces.append((lambda x, v=val: x > v, func))
            elif cond_type == 4:
                pieces.append((lambda x, v=val: x >= v, func))
            elif cond_type == 5:
                pieces.append((lambda x, v=val: x == v, func))
            elif cond_type == 6:
                pieces.append((lambda x, v1=val1, v2=val2: v1 < x < v2, func))
        
        def piecewise(x):
            for condition, func in pieces:
                if condition(x):
                    return func(x)
            return float('nan')
        return piecewise
    
    else:
        return lambda x: x  # Default to identity

def get_simple_function():
    """Get a simple function for piecewise definitions"""
    print("1. Constant")
    print("2. x")
    print("3. x^2")
    print("4. x^3")
    print("5. sin(x)")
    print("6. cos(x)")
    print("7. e^x")
    print("8. ln(x)")
    
    choice = int(input("Choice: "))
    if choice == 1:
        c = float(input("Constant value: "))
        return lambda x: c
    elif choice == 2:
        return lambda x: x
    elif choice == 3:
        return lambda x: x**2
    elif choice == 4:
        return lambda x: x**3
    elif choice == 5:
        return lambda x: math.sin(x)
    elif choice == 6:
        return lambda x: math.cos(x)
    elif choice == 7:
        return lambda x: math.exp(x)
    elif choice == 8:
        return lambda x: math.log(x) if x > 0 else float('-inf')
    else:
        return lambda x: x