# The program receives a list of integers between 0 - 9 (including edges) which its length is 9,
# The program returns the missing integer example: missing_num([0,1,2,3,4,6,7,8,9]) returns the integer 5
# The time complexity of the Program is O(9log(9)) and the memory complexity is O(9) when the list is not sorted

def missing_num_rec(num_list, sta, fin):
    if fin - sta == 1 and num_list[fin] - num_list[sta] > 1:  # end of recursion
        return num_list[fin] - 1
    mid = int(sta + (fin - sta) / 2)
    if num_list[fin] - num_list[mid] > fin - mid:  # checks left side
        return missing_num_rec(num_list, mid, fin)
    else:  # checks right side
        return missing_num_rec(num_list, sta, mid)


def missing_num(num_list):
    sort_list = sorted(num_list)
    last = len(num_list) - 1
    if sort_list[last] - sort_list[0] == last:  # if all integers between the end and last integer exists returns 0 or 9
        if num_list[0] == 0:
            return 9
        else:
            return 0

    return missing_num_rec(sort_list, 0, len(num_list) - 1)


ls = [0, 5, 7, 9, 8, 1, 3, 2, 4]
print(f"The list is: \n  {ls}")
print(f"The missing integer is:\n {missing_num(ls)}")

