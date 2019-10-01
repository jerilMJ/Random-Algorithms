'''

    This algorithm takes 2 whole numbers as input and outputs the
    smallest number from the set of permutations of number 1 that is
    greater than number 2.
    The set of permutations of number 1 are found recursively.

    Input:
    ------
    Two space separated whole numbers.

    Output:
    -------
    As mentioned above.

    eg: Input : 234 340
        Output: 342

    Explanation: Among the permutations of 234, ( 234, 243, 324, 342, 423, 432 )
        342, 423 and 432 are greater than the second number 340. So the smallest
        of the bunch (342) is the required output.

'''

given_set = []  # Set to store given digits
permutations_set = []

# Function to find all permutations of given set and store them in permutations set
# This is done recursively
def permutations(g_set, index, size):
    if index == size:
        perm = g_set[:]
        for i in range(size):
            perm[i] *= 1*(10**i)
        permutations_set.append(sum(perm))
    else:
        for i in range(index, size):
            temp = g_set[i]
            g_set[i] = g_set[index]
            g_set[index] = temp

            permutations(g_set, index + 1, size)    # Recursive call

            temp = g_set[i]
            g_set[i] = g_set[index]
            g_set[index] = temp


n1, n2 = input().split(' ')
list1 = list(n1)
list1 = list(map(int, list1))   # Separate each digits of number 1

permutations(list1, 0, len(list1))  # Find permutation of digits of number 1

filtered = filter(lambda x: x > int(n2), permutations_set)  # Filtering numbers < number 2
filtered = sorted(filtered) # After sorting, first item will be smallest

try:
    print(filtered[0])
except IndexError:
    print('No larger numbers')
