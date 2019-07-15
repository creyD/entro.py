import math

# Calculates the entropy of a given string
# Returns the entropy and an alphabet with the calculated probabilities
def calculateEntropy(input_string):
    alphabet, alphabet_size, entropy = {}, 0, 0

    for char in input_string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
        alphabet_size += 1

    for char in alphabet:
        alphabet[char] = alphabet[char] / alphabet_size
        entropy -= alphabet[char] * math.log(alphabet[char], 2)

    return entropy, alphabet


# Calculates the entropy of a given string
# Returns only the entropy in bits as this is the minimal function
def calculateEntropyMin(input_string):
    alphabet, alphabet_size, entropy = {}, 0, 0

    for char in input_string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
        alphabet_size += 1

    for char in alphabet:
        i = alphabet[char] / alphabet_size
        entropy -= i * math.log(i, 2)

    return entropy
