from functools import reduce

def process_matrix(matrix):
    if matrix == []: 
        return []
    elif is_numerical_matrix(matrix): 
        return _process_matrix(matrix)
    else:
        raise ValueError('Only works on numerical matrices')

def _process_matrix(matrix):
    processed_matrix = []
   
    for i, column in enumerate(matrix):
        processed_list = []
        for j in range(len(column)): 
            new_value = process_elements(i, j, matrix)
            processed_list.append(new_value)

        processed_matrix.append(processed_list)

    return processed_matrix

def process_elements(matrix_index, list_index, elements):

    vertical_indices = get_neighbours_indices(list_index, elements[matrix_index])
    
    neighbor_list = get_other_neighbors_list(list_index, elements)
    horizontal_indices = get_neighbours_indices(matrix_index, neighbor_list)

    vertical_values = get_neighbor_values(vertical_indices, elements[matrix_index])
    vertical_values.append(elements[matrix_index][list_index])
    horizontal_values = get_neighbor_values(horizontal_indices, neighbor_list)

    values = vertical_values + horizontal_values
    average = get_average(values)

    return average

def get_neighbours_indices(index, elements):

    indices = []

    indices.append(index + 1)
    indices.append(index - 1)
 
    indices = list(filter(lambda x : x >= 0 and x < len(elements), indices))
   
    return indices

def get_other_neighbors_list(index, elements):
    neighbors = []
    for column in elements:
        neighbors.append(column[index])

    return neighbors

def get_neighbor_values(indices, elements):
    values = []
    for index in indices:
        values.append(elements[index])
    return values

def get_average(values):
    return reduce(lambda a, b : a + b, values, 0) / len(values)


def is_numerical_matrix(matrix):
    return is_list_of_lists(matrix) and is_same_length(matrix) and is_all_numbers(matrix)

def is_same_length(matrix):
    it = iter(matrix)
    the_len = len(next(it))
    return all(len(l) == the_len for l in it)
        
def is_list_of_lists(matrix):
    return all(isinstance(element, list) for element in matrix)        

def is_all_numbers(matrix):
    val = None
    for lst in matrix:
        if all(type(element) in (int, float) for element in lst):
            val = True
        else:
            val = False
            break
    return val

matrix = [[2,3,4], [4,7,9], [5,1,8],[6,4,2]]
print(process_matrix(matrix))