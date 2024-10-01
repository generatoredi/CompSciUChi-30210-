def f(x):
    '''
    Real valued square function  f(x) == x^2
    '''
    return x*x



a = 0
b = 1
def integrate(n):

    # n: the number of rectangles
    total_area = 0
    width = (b - a) / n
    for i in range(n):
        x = a + i * width
        y = f(x)
        total_area += y * width

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return total_area


print(integrate(1000))