import math

def trig_values():
    """Display common trig values"""
    print("\n=== COMMON TRIG VALUES ===")
    print("\nAngle | sin | cos | tan")
    print("-" * 35)
    
    angles = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2,
              2*math.pi/3, 3*math.pi/4, 5*math.pi/6, math.pi,
              3*math.pi/2, 2*math.pi]
    
    angle_names = ["0", "pi/6", "pi/4", "pi/3", "pi/2",
                   "2pi/3", "3pi/4", "5pi/6", "pi",
                   "3pi/2", "2pi"]
    
    for angle, name in zip(angles, angle_names):
        s = math.sin(angle)
        c = math.cos(angle)
        try:
            t = math.tan(angle)
            print(f"{name:6} | {s:4.2f} | {c:4.2f} | {t:5.2f}")
        except:
            print(f"{name:6} | {s:4.2f} | {c:4.2f} | undef")

if __name__ == "__main__":
    while True:
        trig_values()
        input("\nPress Enter to run again...")