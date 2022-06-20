
from math import factorial


def get_permutations(elements):
#creates a dictionary mapping permutations of the input to their sign
    perms_dict = {}
    if len(elements) == 1:
        perms_dict[elements] = 1
    else:
        for i in range(len(elements)):
            temp_list = list(elements)
            temp_list.pop(i)
            temp_dict = get_permutations(tuple(temp_list))
            for perms in temp_dict.keys():
                perms_dict[(elements[i], ) + perms] = ((-1)**i)*temp_dict[perms]
    return perms_dict

def create_shuffles(elements, i , j):
#given a permutation, create a list of it's i+j shuffles
    shuffles = set()
    if j == 0:
        shuffles.add(elements)
    elif j==1:
        last_element = elements[-1]
        temp_list = list(elements[:-1])
        for s in range(i+j-1):
            temp_list.insert(s, last_element)
            shuffles.add(tuple(temp_list))
            temp_list.pop(s)
        temp_list.append(last_element)
        shuffles.add(tuple(temp_list))
    else:
        last_element = elements[-1]
        second_last_element = elements[-2]
        temp_list = list(elements)
        temp_list.pop(-1)
        temp_elements = tuple(temp_list)
        temp_shuffles = create_shuffles(temp_elements, i, j-1)
        for shuffle in temp_shuffles:
            temp_list = list(shuffle)
            begin_at = shuffle.index(second_last_element)
            for s in range(begin_at + 1, i+j-1):
                temp_list.insert(s, last_element)
                shuffles.add(tuple(temp_list))
                temp_list.pop(s)
            temp_list.append(last_element)
            shuffles.add(tuple(temp_list))
    return shuffles
def exchange(matrix, u, v, n):
    for k in range(factorial(n)):
        matrix[u][k] = matrix[u][k] + matrix[v][k]
        matrix[v][k] = matrix[u][k] - matrix[v][k]
def reduce(matrix, row_1, col, row_2, n, p):
    #subtract a multiple of row_1 from row_2 to make the row_2 entry in col = 0
    ratio = (matrix[row_2][col]*pow(matrix[row_1][col], -1, p))%p
    for k in range(factorial(n)):
        matrix[row_2][k] = (matrix[row_2][k] - ratio*matrix[row_1][k])%p
def get_rank(n, p):
    my_tuple = tuple()
    for i in range(1,n+1):
        my_tuple+=(i, )
    my_dictionary = get_permutations(my_tuple)
    my_iterator = list(my_dictionary.keys())
#create the symmetry conditions matrix
    matrix = []
    for i in range((factorial(n))*int(n/2)):
        matrix.append([0 for j in range(factorial(n))])
    for s in range(factorial(n)):
        my_perm = my_iterator[s]
        for m in range(1, int(n/2) + 1):
            for perm in create_shuffles(my_perm, m, n-m):
                my_value = my_dictionary[my_perm]*my_dictionary[perm]
                matrix[s+ m-1][my_iterator.index(perm)] = my_value
    
#gauss reduce this matrix to get the dimension of the kernel
    rank = 0
    for i in range(factorial(n)):
        reduce_bool = False
        for s in range(i, factorial(n)*int(n/2)):
            if matrix[s][i]%p == 0:
                continue
            else:
                reduce_bool = True
                rank += 1
                if not i == s:
                  exchange(matrix, s, i, n)
                break
        if reduce_bool:
            for j in range(factorial(n)*int(n/2)):
                if not matrix[j][i] == 0 and not j == i:
                  reduce(matrix, i, i, j, n, p)
    return rank
print(get_rank(3,3), get_rank(4,3), get_rank(5,3), get_rank(6,3))

