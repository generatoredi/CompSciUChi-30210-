"""
Short Exericses #1
"""


def add_one_and_multiply(a, x):
    """ Add 1 to a, and multiply by x"""

    ### EXERCISE 1 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    r = (a+1)*x

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r

add_one_and_multiply(10, 20)


def out_of_range(x, lb, ub):
    """ Is x outside the range lb to ub (inclusive)?"""

    ### EXERCISE 2 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    
    if x in range(lb,ub+1):
        r=False
    else:
        r=True

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r

out_of_range(10, 3, 10)


def number_string(x):
    """
    Given a number x, produce a string: "POSITIVE", "NEGATIVE", "ZERO"
    (depending on whether the number is positive, negative, or zero)
    """

    ### EXERCISE 3 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable s should contain the value
    # we ask you to compute in this exercise.
    if x>0:
        s="POSITIVE"
    elif x<0:
        s="NEGATIVE"
    else:
        s="ZERO"

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return s


number_string(10)


def num_divisible(lb, ub, p, q):
    """
    How many numbers between lb and ub (inclusive) are divisible by p
    or divisible by q, but not divisible by both p and q.
    """

    ### EXERCISE 4 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n=0
    for a in range(lb,ub+1):
        if (a%p==0 and a%q!=0) or (a%p!=0 and a%q==0):
            n+=1
    
    
    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n

num_divisible(1, 25, 3, 5)



def count_greater_than_val(lst, val):
    """
    Count the number of numbers in the list that are strictly greater than the value of val.
    """

    ### EXERCISE 5 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n=0
    for number in lst:
        if number>val:
            n+=1
    
    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n


count_greater_than_val([1, 10, 11, 2, 12, 13], 10)



def negate_list(lst):
    """
    Produce a *new* list with its values negated
    """

    ### EXERCISE 6 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise
    new_lst=[]
    for number in lst:
        new_lst.append(-1*number)
        

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return new_lst



