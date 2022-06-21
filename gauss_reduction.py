
from math import factorial, perm


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
def exchange(matrix, u, v, j):
    for k in range(j):
        matrix[u][k] = matrix[u][k] + matrix[v][k]
        matrix[v][k] = matrix[u][k] - matrix[v][k]
def reduce(matrix, row_1, col, row_2, j, p):
    #subtract a multiple of row_1 from row_2 to make the row_2 entry in col = 0
    ratio = (matrix[row_2][col]*pow(matrix[row_1][col], -1, p))%p
    for k in range(j):
        matrix[row_2][k] = (matrix[row_2][k] - ratio*matrix[row_1][k])%p 
def get_cocycle(n, p):
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
            for permi in create_shuffles(my_perm, m, n-m):
                my_value = my_dictionary[my_perm]*my_dictionary[permi]
                matrix[s*int(n/2) + m-1][my_iterator.index(permi)] = my_value
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
                  exchange(matrix, s, i, factorial(n))
                break
        if reduce_bool:
            for j in range(factorial(n)*int(n/2)):
                if not matrix[j][i] == 0 and not j == i:
                  reduce(matrix, i, i, j, factorial(n), p)
    return factorial(n) - rank

def get_cohomology(n,p):
    matrix = []
    for i in range(factorial(n) + factorial(n-1)*(int((n-1)/2))*int((n*(n-1))/2)):
        matrix.append([0 for j in range(int((n*(n-1))/2)*factorial(n-1))])
    my_tuple = tuple([i for i in range(1, n)])
    my_dictionary = get_permutations(my_tuple)
    my_iterator = list(my_dictionary.keys())
    def my_map(permutation, ind_1, n, my_iterator):
        i_1 = permutation[ind_1]
        i_2 = permutation[ind_1 + 1]
        my_min = min([i_1, i_2])
        my_max = max([i_1, i_2])
        new_perm = tuple()
        for j in range(n):
            if (not j == ind_1) and (not j == ind_1 + 1):
                if permutation[j] < my_min:
                    new_perm += (permutation[j] + 1, )
                elif my_min < permutation[j] < my_max:
                    new_perm += (permutation[j], )
                elif permutation[j] > my_max:
                    new_perm += (permutation[j] - 1, )
            elif j == ind_1:
                new_perm += (1, )
            else:
                continue
        tuples = []
        for i in range(1,n+1):
            for j in range(i+1, n+1):
                tuples.append((i,j))
        k = my_iterator.index(new_perm)
        s = tuples.index((my_min, my_max))
        return (s*factorial(n-1)) + k
    my_tuple_1 = tuple([i for i in range(1, n+1)])
    my_iterator_1 = list(get_permutations(my_tuple_1).keys())
    for i in range(factorial(n)):
        temp_perm = my_iterator_1[i]
        for s in range(n-1):
            my_index = my_map(temp_perm, s, n, my_iterator)
            matrix[i][my_index] = (-1)**s
    matrix_1 = []
    for i in range((factorial(n-1))*int((n-1)/2)):
        matrix_1.append([0 for j in range(factorial(n-1))])
    for s in range(factorial(n-1)):
        my_perm = my_iterator[s]
        for m in range(1, int((n-1)/2) + 1):
            for permi in create_shuffles(my_perm, m, n-1-m):
                my_value = my_dictionary[my_perm]*my_dictionary[permi]
                matrix_1[s*int((n-1)/2)+ m-1][my_iterator.index(permi)] = my_value
    for x in range(int((n*(n-1))/2)):
        for s in range(factorial(n-1)*int((n-1)/2)):
            for k in range(factorial(n-1)):
                matrix[factorial(n) + x*factorial(n-1)*int((n-1)/2) + s][x*factorial(n-1) + k] = matrix_1[s][k]
    
    rank = 0
    for i in range(int((n*(n-1))/2)*factorial(n-1)):
        reduce_bool = False
        for s in range(i, factorial(n) + factorial(n-1)*int((n-1)/2)*int((n*(n-1))/2)):
            if matrix[s][i]%p == 0:
                continue
            else:
                reduce_bool = True
                rank += 1
                if not i == s:
                  exchange(matrix, s, i, int((n*(n-1))/2)*factorial(n-1))
                break
        if reduce_bool:
            for j in range(factorial(n) + factorial(n-1)*int((n-1)/2)*int((n*(n-1))/2)):
                if not matrix[j][i] == 0 and not j == i:
                  reduce(matrix, i, i, j, int((n*(n-1))/2)*factorial(n-1), p)
    return get_cocycle(n,p) - (get_cocycle(n-1, p)*int((n*(n-1))/2) - (int((n*(n-1))/2)*factorial(n-1) - rank))
print(get_cohomology(6,3))





    


