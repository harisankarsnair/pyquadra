import streamlit as st
from math import sqrt
def print_factor(x):
    list = []
    for i in range(1,x+1):
        if x % i == 0:
            list.append(i)

    return list


def pairOfNum(b, c):
    a = 1
    d = b * b - 4 * a * c

    sqrt_val = sqrt(abs(d))

    if (d > 0):
        x = -b + sqrt_val
        y = -b - sqrt_val

        root1 = (x) // (2 * a)
        root2 = (y) // (2 * a)

        if (root1 + root2 == -1 * b
                and root1 * root2 == c):
           num = st.write("The pair of numbers are ",int(root1), " and ",int(root2))
           return num
        else:
            return st.write("No such pair of numbers exist.")

    elif(d == 0):
        root = -b // (2 * a)
        if (root + root == -1 * b and root * root == c):
            return st.write("The pair of numbers are ",root, " and ",root)
        else:
            return st.write("No such pair of numbers exist.")

    else:
        return st.write("No such pair of numbers exist.")

st.sidebar.title('Options')
option = st.sidebar.radio('Select an option',('Home','find the factor of a no:','find the pair of no:s from the sum and product'))

# OPTION 1 - Home page

if option == 'Home':
    st.title("All in one Maths app")
    st.subheader("App to do almost all the calculations in Maths.")

# OPTION 2 - factors of a no:

if option == 'find the factor of a no:':
    st.title("Find the factor of a number")
    num = st.number_input("Insert the number:",max_value=10000)

    st.write("The factors of ",num," are",print_factor(num))

# OPTION 3 - Pair of numbers

if option == 'find the pair of no:s from the sum and product':
    st.title("Find the pair of numbers from the sum and product given ")
    sum = st.number_input("Enter the sum")
    product = st.number_input("Enter the product")
    pairOfNum(-sum, product)
    

