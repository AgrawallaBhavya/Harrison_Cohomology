#divisibility check in dimensions 4 and 5
#first form the 18 x 24 matrix
from math import factorial, perm
def get_permutations(elements):
#creates a dictionary mapping permutations of the input to their dictionary number
    perms_dict = {}
    if len(elements) == 1:
        perms_dict[elements] = 0
    else:
        for i in range(len(elements)):
            temp_list = list(elements)
            temp_list.pop(i)
            temp_dict = get_permutations(tuple(temp_list))
            for perms in temp_dict.keys():
                perms_dict[(elements[i], ) + perms] = i*factorial(len(elements) - 1) + temp_dict[perms]
    return perms_dict
def get_repeated_perms(elements):
    a = elements[0]
    b = elements[1]
    c = elements[3]
    answer = {}
    answer[(a,b,b,c)] = 0
    answer[(a,b,c,b)] = 1
    answer[(a,c,b,b)] = 2
    answer[(b,a,b,c)] = 3
    answer[(b,a,c,b)] = 4
    answer[(b,b,a,c)] = 5
    answer[(b,b,c,a)] = 6
    answer[(b,c,a,b)] = 7
    answer[(b,c,b,a)] = 8
    answer[(c,a,b,b)] = 9
    answer[(c,b,a,b)] = 10
    answer[(c,b,b,a)] = 11
    return answer
'''
my_perms = {}
four_perms = get_permutations((1,2,3,4))
for perms in four_perms.keys():
    my_perms[(1,) + perms] = four_perms[perms]
small_perms = get_repeated_perms((1,1,3,4))
small_perms_2 = get_repeated_perms((1,1,2,4))
small_perms_3 = get_repeated_perms((1,1,2,3))
for x in small_perms:
    my_perms[(2,) + x] = small_perms[x] + 24
for y in small_perms_2:
    my_perms[(3,) + y] = small_perms_2[y] + 36
for z in small_perms_3:
    my_perms[(4,) + z] = small_perms_3[z] + 48
'''
'''
my_perms = {}
perms_1 = get_repeated_perms((1,2,2,3))
for x in perms_1.keys():
    my_perms[(1,) + x] = perms_1[x]
my_perms[(2,1,1,2,3)] = 12
my_perms[(2,1,1,3,2)] = 13
my_perms[(2,1,2,1,3)] = 14
my_perms[(2,1,2,3,1)] = 15
my_perms[(2,1,3,1,2)] = 16
my_perms[(2,1,3,2,1)] = 17
my_perms[(2,2,1,1,3)] = 18
my_perms[(2,2,1,3,1)] = 19
my_perms[(2,2,3,1,1)] = 20
my_perms[(2,3,1,1,2)] = 21
my_perms[(2,3,1,2,1)] = 22
my_perms[(2,3,2,1,1)] = 23
my_perms[(3,1,1,2,2)] = 24
my_perms[(3,1,2,1,2)] = 25
my_perms[(3,1,2,2,1)] = 26
my_perms[(3,2,1,1,2)] = 27
my_perms[(3,2,1,2,1)] = 28
my_perms[(3,2,2,1,1)] = 29
'''
my_perms = {}
my_perms[(1,1,1,2,2)] = 0
my_perms[(1,1,2,1,2)] = 1
my_perms[(1,1,2,2,1)] = 2
my_perms[(1,2,1,1,2)] = 3
my_perms[(1,2,1,2,1)] = 4
my_perms[(1,2,2,1,1)] = 5
my_perms[(2,1,1,1,2)] = 6
my_perms[(2,1,1,2,1)] = 7
my_perms[(2,1,2,1,1)] = 8
my_perms[(2,2,1,1,1)] = 9
all_perms = list(my_perms.keys())
#new_conditions = [(1,) + x for x in get_permutations((2,3,4,5)).keys()] + [(2,) + x for x in get_permutations((1,3,4,5)).keys()]
#new_conditions += [(3,) + x for x in get_permutations((1,2,4,5)).keys()] + [(4,) + x for x in get_permutations((1,2,3,5)).keys()]
#new_conditions += [(5,) + x for x in get_permutations((1,2,3,4)).keys()]
'''
new_conditions = [(1,2) + x for x in get_permutations((3,4,5)).keys()] +[(1,3,2,4,5),(1,3,2,5,4),(1,3,4,2,5),(1,3,5,2,4),(1,4,2,3,5)]
new_conditions += [(1,4,3,2,5)] + [(2,1) + x for x in get_permutations((3,4,5)).keys()] 
new_conditions += [(2,3,1) + x for x in get_permutations((4,5)).keys()] + [(2,4,1,3,5)]
new_conditions += [(3,1) + x for x in get_permutations((2,4,5)).keys()] + [(3,4,1,2,5)]
new_conditions += [(4,1,2,3,5), (4,1,2,5,3), (4,1,3,2,5), (4,1,3,5,2), (4,1,5,2,3)]
new_conditions += [(5,1,2,3,4), (5,1,3,2,4), (5,1,4,2,3)]
'''
'''
new_conditions = [(1,1) + x for x in get_permutations((2,3,4)).keys()] + [(1,2,1,3,4), (1,2,1,4,3)] + [(1,3,1,2,4)]
new_conditions += [(2,1,1,3,4), (2,1,1,4,3), (2,1,3,1,4)] + [(2,3,1,1,4)]
new_conditions += [(3,1,1,2,4), (3,1,1,4,2), (3,1,2,1,4)]
new_conditions += [(4,1,1,2,3), (4,1,2,1,3)]
#new_conditions += [(3,) + x for x in get_repeated_perms((1,1,2,4)).keys()] + [(4,) + x for x in get_repeated_perms((1,1,2,3)).keys()]
'''
#new_conditions = [(1,1,2,2,3), (1,1,2,3,2), (1,1,3,2,2), (1,2,1,2,3), (1,2,1,3,2)]
#new_conditions += [(2,1,1,2,3), (2,1,1,3,2), (2,1,2,1,3), (3,1,1,2,2), (3,1,2,1,2)]
#ew_conditions = [(1,1,1,2,3), (1,1,1,3,2), (1,1,2,1,3), (1,2,1,1,3), (2,1,1,1,3), (3,1,1,1,2)]
new_conditions = [(1,1,1,2,2), (1,1,2,1,2), (1,2,1,1,2), (2,1,1,1,2)]
matrix = []
for j in range(10 + len(new_conditions)):
    matrix.append([0 for x in range(10)])
for s in range(len(all_perms)):
    current = all_perms[s]
    reversedd = (current[4], current[3], current[2], current[1], current[0])
    matrix[s][my_perms[current]] += 1
    matrix[s][my_perms[reversedd]] += -1
for s in range(len(new_conditions)):
    current = new_conditions[s]
    more_1 = (current[1], current[0], current[2], current[3], current[4])
    more_2 = (current[1], current[2], current[0], current[3], current[4])
    more_3 = (current[1], current[2], current[3], current[0], current[4])
    more_4 = (current[1], current[2], current[3], current[4], current[0])
    my_list = (current, more_1, more_2, more_3, more_4)
    matrix[10 +s][my_perms[my_list[0]]] += 1
    matrix[10 +s][my_perms[my_list[1]]] += -1
    matrix[10 +s][my_perms[my_list[2]]] += 1
    matrix[10+s ] [my_perms[my_list[3]]] += -1
    matrix[10 + s][my_perms[my_list[4]]] += 1
def exchange(matrix, u, v, j):
    for k in range(j):
        matrix[u][k] = matrix[u][k] + matrix[v][k]
        matrix[v][k] = matrix[u][k] - matrix[v][k]
        matrix[u][k] = matrix[u][k] - matrix[v][k]
def reduce(matrix, row_1, col, row_2, j):
    a = matrix[row_1][col]
    b = matrix[row_2][col]/a
    #subtract a multiple of row_1 from row_2 to make the row_2 entry in col = 0
    for k in range(j):
        matrix[row_2][k] = matrix[row_2][k] - b*matrix[row_1][k]

rank = 0
for i in range(10):
        reduce_bool = False
        for s in range(i, len(matrix)):
            if matrix[s][i] == 0:
                continue
            else:
                reduce_bool = True
                rank += 1
                if not i == s:
                  exchange(matrix, s, i, 10)
                break
        if reduce_bool:
            for j in range(len(matrix)):
                if not matrix[j][i] == 0 and not j == i:
                  reduce(matrix, i, i, j, 10)

print(rank)
