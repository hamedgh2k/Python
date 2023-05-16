def prime(x):
    z = 0
    for i in range(1, x + 1):
        if x % i == 0:
            z += 1
    if z == 2:
        return True
    else:
        return False
# x must be an integer and if the number was prime it return True otherwise it return False
