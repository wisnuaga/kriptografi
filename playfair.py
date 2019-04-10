def remove_same_char(text):
    text = text.upper()
    text = text.replace("J", "I")

    result = " "
    for i in text:
        if(i) not in result:
            result += i

    return result.strip()

def make_alfabet():
    return [chr(i) for i in range(65, 91)]

def input_key_to_matrix(matrix, key):
    key = remove_same_char(key)

    j = 0
    for i in range(len(key)):
        matrix.append(key[i])


def input_alfa_to_matrix(matrix):
    alfabet = make_alfabet()
    alfabet.remove("J")

    j = 0
    for i in range(25):
        if alfabet[j] not in matrix:
            matrix.append(alfabet[j])
        j = j + 1

def make_matrix_2d(matrix, key):
    result = [[], [], [], [], []]

    k = 0
    for i in range(5):
        for j in range(5):
            result[i].append(matrix[k])
            k = k + 1

    return result

def make_matrix_key(key):
    matrix = []
    input_key_to_matrix(matrix, key)
    input_alfa_to_matrix(matrix)
    return make_matrix_2d(matrix, key)

key = "bangsat jahat"

# print (make_matrix_key(key))

