
def print_row(row):
    i = 0
    while(i < len(row)):
        print (f"{row[i]}")
        i +=1

def split_data_to_array():
    with open('input.txt', 'r') as file:
        first_int = []
        sec_int = []

        for line in file:
            parts = line.split()
            first_int.append(int(parts[0]))
            sec_int.append(int(parts[1]))
        return(first_int, sec_int)

def subtract_arrays(first, second):
    i = 0
    res = []
    diff = 0
    sum = 0
    while (i < len(first)):
        diff = first[i] - second[i]
        res.append(abs(diff))
        sum += (abs(diff))
        i += 1
    return res, sum

first_row = []
sec_row = []
res = []
sum = 0

first_row, sec_row = split_data_to_array()

first_row.sort()
sec_row.sort()

res, sum = subtract_arrays(first_row, sec_row)
print(f"SUM:{sum}")
#print_row(res)
