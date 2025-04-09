"""
@author: vena
"""


def divide(a, b):
    """
    This function divides a by b when b != 0
    """
    c = 0
    try:
        c = float(a)/float(b)
    except ZeroDivisionError:
        print("Can't divide by 0.")
    except ValueError:
        print("Can't divide non-numeric inputs.")
    except:
        print("Can't divide inputs.")
    return c

def divide3(a, b):
    if b == 0:
         raise ZeroDivisionError("You messed up")
    c = float(a)/float(b)

# This following function is very important.
# We want a float to be entered rather than an int and that is why we do this
# We could have done this method using try and except 
# This way is to easily differentiate between int and float 
def getAge():
    original_age = input("Please enter your age using decimals: ")
    age = float(original_age)
    if '.' not in original_age:
        raise TypeError("You entered an integer. Please use decimals. ")
    if age <= 0:
        raise ValueError("You entered a negative age. ")
    return "You are " + str(age) + " years young! "

if __name__ == "__main__":
    '''
    divide(5,0)
    print(divide(4, 2))
    divide3(5, 0) # Specifically to throw this one
    '''
    # The point is once we catch the error we can throw any error we want to throw
    
    print(getAge())