
def split_data_to_array():
    safe = 0
    with open('input.txt', 'r') as file:
        report = []
        for line in file:
            parts = line.split()
            level = []
            for i in parts:
                level.append(int(i))
            if (is_ascending(level) or is_decending(level) or can_be_safe_by_removal(level)):
                    safe += 1
            report.append(level)
    return(report, safe)

def is_ascending (level):
    if (len(level) == 1):
        return True
    if (level[0] >= level[1] or abs(level[0] -level[1]) > 3):
        return False
    return is_ascending(level[1:])

def is_decending (level):
    if (len(level) == 1):
        return True
    if (level[0] <= level[1] or abs(level[0] -level[1]) > 3):
        return False
    return is_decending(level[1:])

def can_be_safe_by_removal(level):
    for i in range(len(level)):
        modified_level = level[:i] + level[i+1:]  # Remove the i-th element
        if is_ascending(modified_level) or is_decending(modified_level):
            return True
    return False

report = []
safe = 0

report, safe = split_data_to_array()



#res, sum = subtract_arrays(first_row, sec_row)
print(f"{safe}")
#print_row(res)
