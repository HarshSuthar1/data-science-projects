string = input("Enter string: ")

def length(x):
    count = 0
    for i in x:
        count+=1
    return count

def is_vowel(x):
    return True if x[0] in "aeiouAIOUE" else False

def reversed_string(x):
    return x[::-1]

print(length(string))
print(is_vowel(string))
print(reversed_string(string))

