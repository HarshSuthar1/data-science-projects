from collections import Counter

def mean(x):
    return sum(x)/len(x)

def median(x):
    sorted_x = sorted(x)
    if len(x)%2==1:
        return sorted_x[len(x)//2]
    else:
        return (sorted_x[len(x)//2] + sorted_x[(len(x)//2)-1]) / 2

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

length = int(input("Enter how many numbers u want: "))

data = []

print("Enter data: ")

for i in range(length):
    data.append(int(input("")))

choice = int(input('''1. Mean
2. Median
3. Mode\n'''))

if choice == 1:
    print(mean(data))
if choice == 2:
    print(median(data))
if choice == 3:
    print(mode(data))