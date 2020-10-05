import math


# Calculates the entropy of a given string
# Returns the entropy and an alphabet with the calculated probabilities
def calculateEntropy(input_string):
    alphabet, alphabet_size, entropy = {}, len(input_string), 0

    for char in input_string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1

    for char in alphabet:
        alphabet[char] = alphabet[char] / alphabet_size
        entropy -= alphabet[char] * math.log(alphabet[char], 2)

    max_entropy = - len(alphabet) * (1 / len(alphabet) * math.log(1 / len(alphabet), 2))
    return entropy, alphabet, max_entropy


# Calculates the entropy of a given string
# Returns only the entropy in bits as this is the minimal function
def calculateEntropyMin(input_string):
    alphabet, alphabet_size, entropy = {}, len(input_string), 0

    for char in input_string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1

    for char in alphabet:
        i = alphabet[char] / alphabet_size
        entropy -= i * math.log(i, 2)
    return entropy


# Outputs a given entropy including the original text and the alphabet with probabilities
def printEntropy(original_string, entropy_value, alphabet_dict, simple_bool, max_value):
    print('---')
    if not simple_bool:
        print('Content: ' + original_string)
        print('Probabilities: ' + str(alphabet_dict))
    print('Entropy: ' + str(entropy_value) + ' bits')
    if max_value:
        print('Maximum Entropy: ' + str(max_value) + ' bits')
    print('---')


# Reads a file by a given path
def readEntropyFile(path_string):
    f = open(path_string, 'r')
    content = f.read().replace('\n', ' ')
    f.close()
    return content.strip()
