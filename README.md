# Entropy Calculator

Written in Python, this calculates the information entropy of a given string or file.

## How does this work?

This is a pretty simple calculator which just uses the negative sum of all the probabilities of the chars in a given string multiplied with the logarithm to the base two of the probabilities. The probabilities of the chars are calculated simply by counting the occurrence divided by the total number of chars.

Mathematically speaking this is -sum(p*log(p)) with p being the probability of a char occurring.

## What is it good for?

Well that is basically up to you. Entropy functions are used in Computer Science mainly for calculation of compression potential or in cryptography. But you are free to use this for whatever you want. I wrote it as preparation for one of my exams.

*Warning:* This can only be used for calculating the entropy of strings (by alphabet). There are however other types like coin tosses of fair or unfair coins (...), but you're gonna have to write calculators for this on your own - for now.

## Usage
You can run as much calculations as you want in one run of the script.
```
calc_entro.py teststring
```
or

```
calc_entro.py -files test.txt
```

or combine both of them

```
calc_entro.py teststring -files test.txt
```

Both arguments work with as many strings and filepaths as you want. Just separate them using a space like this:

```
calc_entro.py teststring teststring2 teststring3 -files test1.txt -files test2.txt
```

## Command line parameters

### Output Adjustments
`--simple` determines whether the output is explicit like this:

```
---
Content: TEST
Probabilities: {'T': 0.5, 'E': 0.25, 'S': 0.25}
Entropy: 1.5
---
```

or simplistic like this:

```
---
Entropy: 1.5
---
```

### String conversion
`--lower` - Converts the input strings to lowercase
`--upper` - Opposite of lower, converts to upper (if both are set only lower will be executed)
`--squash` - Removes all whitespaces from input files (*This doesn't apply to input strings as they will be separated by spaces anyways!*)
