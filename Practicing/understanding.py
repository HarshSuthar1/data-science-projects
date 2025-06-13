print("Enter the number of topic which u want to understand: ")
print("1 for string-method")
print("2 for list-method")
print("3 for tuple-method")

def string_exp():
    print('''A string is a sequence of characters. Python treats anything inside quotes as a string. This includes letters, numbers, and symbols. Python has no character data type so single character is a string of length 1.


Code: 
    s = "GfG"
    print(s[1]) # access 2nd char
    s1 = s + s[0] # update
    print(s1) # print

Output:
    f
    GfGG
In this example, s holds the value "GfG" and is defined as a string.''')

def list_exp():
    print('''In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.
List can contain duplicate items.
List in Python are Mutable. Hence, we can modify, replace or delete the items.
List are ordered. It maintain the order of elements based on how they are added.
Accessing items in List can be done directly using their position (index), starting from 0.

Example :
    # Creating a Python list with different data types
    a = [10, 20, "GfG", 40, True]
    print(a)
    # Accessing elements using indexing
    print(a[0])  # 10
    print(a[1])  # 20
    print(a[2])  # "GfG"
    print(a[3])  # 40
    print(a[4])  # True
    # Checking types of elements
    print(type(a[2]))  # str
    print(type(a[4]))  # bool

Explanation:
    The list contains a mix of integers (10, 20, 40), a string ("GfG") and a boolean (True).
    The list is printed and individual elements are accessed using their indexes (starting from 0).
    type(a[2]) confirms "GfG" is a str.
    type(a[4]) confirms True is a bool.''')


def tuple_exp():
    print('''A tuple in Python is an immutable ordered collection of elements. Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable). Tuples can hold elements of different data types. The main characteristics of tuples are being ordered , heterogeneous and immutable.

Creating a Tuple
A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items and they can be of different data types.

Example:
    # Creating an empty Tuple
    tup = ()
    print(tup)
    # Using String
    tup = ('Geeks', 'For')
    print(tup)
    # Using List
    li = [1, 2, 4, 5, 6]
    print(tuple(li))
    # Using Built-in Function
    tup = tuple('Geeks')
    print(tup)

Output:
    ()
    ('Geeks', 'For')
    (1, 2, 4, 5, 6)
    ('G', 'e', 'e', 'k', 's')
''')


choice = int(input("choice: "))
if choice == 1:
    string_exp()
elif choice == 2:
    list_exp()
elif choice == 3:
    tuple_exp()
else:
    print("Enter a valid choice. ")