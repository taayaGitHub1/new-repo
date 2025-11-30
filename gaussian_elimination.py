def gaussian_elimination():
    import numpy as np

    n = int(input("Enter the dimension of the system of equations: "))
    
    # Input the coefficients matrix
    a = np.zeros((n, n))
    b = np.zeros(n)

    print("Enter the coefficients row-wise:")
    for i in range(n):
        for j in range(n):
            a[i][j] = float(input(f"a[{i+1}][{j+1}]: "))
    
    print("Enter the RHS vector:")
    for i in range(n):
        b[i] = float(input(f"b[{i+1}]: "))
    
    # Gaussian Elimination
    for k in range(n - 1):
        pivot = a[k][k]
        if abs(pivot) < 1e-6:
            print("Method failed: Zero pivot encountered.")
            return
        
        for i in range(k + 1, n):
            term = a[i][k] / pivot
            for j in range(n):
                a[i][j] -= a[k][j] * term
            b[i] -= b[k] * term
    
    # Back substitution
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum_ = sum(a[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - sum_) / a[i][i]
    
    print("\nSolution:")
    for i in range(n):
        print(f"x{i + 1} = {x[i]:.6f}")


# Run the function
gaussian_elimination()
