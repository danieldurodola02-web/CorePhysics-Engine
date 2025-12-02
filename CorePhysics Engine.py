import math
# MAIN MENU

def main_menu():
    while True:
        print("\nWELCOME TO COREPHYSICS ENGINE")
        print("1. Motion Solver (SUVAT)")
        print("2. Electricity & Power")
        print("3. Optics")
        print("4. Gravity & Forces")
        print("5. Exit")

        try:
            choice=int(input("Choose a module:"))
        except ValueError:
            print("Invalid input. Enter a number from 1 to 5.")
            continue
        if choice==1:
            suvat_menu()
        elif choice==2:
            electricity_menu()
        elif choice==3:
            optics_menu()
        elif choice==4:
            forces_menu()
        elif choice==5:
            print("\nExiting the Engine. Goodbye")
            break
        else:
            print("Choose a valid option (1-5).")

# SUVAT (Motion) MODULE 
def suvat_menu():
    while True:
        print("\n---Motion Solver (SUVAT)---")
        print("1. Find Final Velocity (v)")
        print("2. Find Displacement (s)")
        print("3. Find Acceleration (a)")
        print("4. Find Time (t)")
        print("5. Back to Main Menu")
        
        try:
            choice=int(input("Choose an option:"))
        except ValueError:
            print("Invalid input. Choose 1-5.")
            continue

        if choice==1:
            final_velocity()
        elif choice==2:
            displacement()
        elif choice==3:
            acceleration()
        elif choice==4:
            time_solver()
        elif choice==5:
            break
        else:
            print("Choose a valid option (1-5). ")
def final_velocity():
    print("\n---Final Velocity (v = u +at)---")
    u = float(input("Enter initial velocity u(m/s):"))
    a = float(input("Enter acceleration a (m/s²):"))
    t = float(input("Enter time t (s):"))
    v = u + (a*t)
    print(f"Final Velocity = {v} m/s")

def displacement():
    print("\n---Displacement (s = ut + ½at²)---")
    u = float(input("Enter initial velocity u(m/s):"))
    t = float(input("Enter time t (s):"))
    a = float(input("Enter acceleration a (m/s²):"))
    s = (u*t)+(0.5*(a*(t**2)))
    print(f"Displacement = {s} m")
     
def acceleration():
    print("\n---Acceleration ((v-u)/t)---")
    v = float(input("Enter final velocity v(m/s):"))
    u = float(input("Enter initial velocity u(m/s):"))
    t = float(input("Enter time t(s):"))
    if t == 0:
        print("Time cannot be zero.")
        return
              
    a = (v-u)/t
    print(f"Acceleration = {a} m/s²")

def time_solver():
    print("\n---Time Solver ((v-u)/a)---")
    v = float(input("Enter final velocity v(m/s):"))
    u = float(input("Enter initail velocity u(m/s):"))
    a = float(input("Enter acceleration a(m/s²):"))
    if a==0:
     print("Acceleration cannot be zero.")
     return
    t = (v-u)/a
    print(f"Time = {t} seconds")

# ELECTRICITY MODULE
def electricity_menu():
    while True:
        print("\n---Electricity & Power---")
        print("1. Ohm's Law (V = IR)")
        print("2. Electrical Power (P = VI)")
        print("3. Back")

        try:
            choice=int(input("Choose:"))
        except ValueError:
            print("Invalid input.")
            continue

        if choice==1:
            ohms_law()
        elif choice==2:
            power_calc()
        elif choice==3:
            break
        else:
            print("choose between 1-3.")

def ohms_law():
     print("\n---Ohm's Law (V=IR)---")
     I = float(input("Enter current I (A):"))
     R = float(input("Enter resistance R (Ω):"))
     V = I * R
     print(f"Voltage = {V} V")

def power_calc():
     print("\n---Power Calculation (P=VI)---")
     V = float(input("Enter voltage V (V):"))
     I = float(input("Enter current I (A):"))
     P = V * I
     print(f"Power = {P} W")

# OPTICS MODULE
def optics_menu():
    while True:
        print("\n---Optics---")
        print("1. Lens Formula (1/f = 1/v + 1/u)")
        print("2. Back")

        try:
            choice=int(input("choose:"))
        except ValueError:
            continue

        if choice==1:
              lens_formula()
        elif choice==2:
              break
def lens_formula():
    print("\n---Lens Formula---")
    u = float(input("Enter object distance u(m):"))
    v = float(input("Enter image distance v(m):"))
    if u==0 or v==0:
        print("u and v cannot be zero")
        return
    f = 1/((1/v)+(1/u))
    print(f"Focal Length = {f} m")

#FORCES AND GRAVITY MODULE
def forces_menu():
     while True:
        print("\n---Gravity And Forces---")
        print("1. Weight (W=mg)")
        print("2. Universal Gravitation")
        print("3. Back")

        try:
            choice=int(input("Choose:"))
        except ValueError:
            continue

        if choice==1:
            weight_calc()
        elif choice==2:
            gravitation()
        elif choice==3:
            break

def weight_calc():
    print("\n---Weight W=mg---")
    m = float(input("Enter Mass:"))
    g = 9.8
    W = m * g
    print(f"Weight = {W} N")

def gravitation():
    print("\n---Newton's Law of Gravitation---")
    G = 6.674e-11
    m1 = float(input("Enter mass 1 (kg):"))
    m2 = float(input("Enter mass 2 (kg):"))
    r = float(input("Enter distance r (m):"))

    if r==0:
        print("Distance cannot be zero")
        return
    F = G * (m1 * m2) / (r ** 2)
    print(f"Gravitational Force = {F} N")

#RUN PROGRAM

main_menu()



