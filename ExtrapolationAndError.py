def lagrange_interpolation(x_points, y_points, x):
  
    n = len(x_points)
    total = 0.0

    for i in range(n):
        # Formula L_i(x) BIG π x-xi/xi-xj
        Li = 1.0
        for j in range(n):
            if i != j:
                Li *= (x - x_points[j]) / (x_points[i] - x_points[j])
        total += y_points[i] * Li

    return total

def main():
    #  Ask how many data points
    while True:
        try:
            n = int(input("How many data points (2-5)? "))
            if 2 <= n <= 5:
                break
            else:
                print("Please enter an integer between 2 and 5.")
        except ValueError:
            print("Please enter a valid integer.")

    #  Ask for X1..Xn and Y1..Yn
    x_points = list(range(1, n + 1))  # [1,2] or [1,2,3] or [1,2,3,4] or [1,2,3,4,5]
    y_points = []

    #I'm gonna comment this out for now, since we won't ask for the actual X Values. 
    # Our X Values will always be 1,2,3,4,5 for the sake of simplicity and dealing with non-linear data.

    """
    #  Ask for X1..Xn
    print("\nEnter the x-values:")
    for i in range(n):
        while True:
            try:
                x_val = float(input(f"X{i}: "))
                x_points.append(x_val)
                break
            except ValueError:
                print("Please enter a valid number.")

    """
    
       #  Ask for Y1..Yn
    print("\nEnter the y-values:")
    for i in range(n):
        while True:
            try:
                y_val = float(input(f"Y{i}: "))
                y_points.append(y_val)
                break
            except ValueError:
                print("Please enter a valid number.")

    # Temporary Commented Out Single Input Test Case
    """
    #  Ask for the x where P(x) is needed
    while True:
        try:
            x = float(input("\nEnter the value of x where you want to evaluate P(x): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    #  Compute and print result
    result = lagrange_interpolation(x_points, y_points, x)
    print(f"\nThe estimated value P({x}) is: {result}")
    """
    
    #TEST  2: Using Sequential Indices (1,2,3,4,5) to Try out Test Cases (3-5 Data Points Advance). This works better somehow.
    for j in range (5):
        print(f"\n--- Test Case: Estimating P({5+(j+1)}) ---")
        result = lagrange_interpolation(x_points, y_points, 5+(j+1))
        print(f"\nThe estimated value P({5+(j+1)}) is: {result}")

if __name__ == "__main__":
    main()
    