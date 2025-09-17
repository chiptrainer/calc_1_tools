def interval_notation_help():
    """Display interval notation guide"""
    print("\n=== INTERVAL NOTATION GUIDE ===")
    print("\nNotation | Meaning")
    print("-" * 30)
    print("[a, b]   | a <= x <= b (closed)")
    print("(a, b)   | a < x < b (open)")
    print("[a, b)   | a <= x < b")
    print("(a, b]   | a < x <= b")
    print("(-inf, b] | x <= b")
    print("(a, inf) | x > a")
    print("(-inf, inf) | all real numbers")
    
    print("\nExamples:")
    print("[2, 5]: includes 2 and 5")
    print("(2, 5): excludes 2 and 5")
    print("[0, inf): x >= 0")
    
    print("\nUnion notation:")
    print("(-inf, 2) U (2, inf): all x except 2")
    print("[1, 3] U [5, 7]: 1<=x<=3 or 5<=x<=7")

if __name__ == "__main__":
    while True:
        interval_notation_help()
        input("\nPress Enter to run again...")