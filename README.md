# Entropy Calculator

Written in Python, this calculates the information entropy and maximum entropy of a given string or file.

## How does it work?

This is a pretty simple calculator which just uses the negative sum of all the probabilities of the chars in a given string multiplied with the logarithm to the base two of the probabilities. The probabilities of the chars are calculated simply by counting the occurrence divided by the total number of chars.

Mathematically speaking this is `-sum(p*log(p))` with p being the probability of a char occurring. The maximum entropy calculation is explained below.

## What is it good for?

Well that is basically up to you. Entropy functions are used in Computer Science mainly for calculation of compression potential or in cryptography. But you are free to use this for whatever you want. I wrote it as preparation for one of my exams.

*Warning:* This can only be used for calculating the entropy of strings (by alphabet). There are however other types like coin tosses of fair or unfair coins throws etc. but you're gonna have to write calculators for this on your own - for now.

*Update:* This script now can calculate the maximum entropy now too. This is pretty useful for pre-compression analyses. Maximum entropy is calculated by splitting the alphabet into parts of the same size and calculating the entropy of this, like: `-1 * SIZE_OF_ALPHABET * (DISTINCT_PROBABILITY * log(DISTINCT_PROBABILITY, 2))`.

## Usage

You can run as much calculations as you want in one run of the script. For example use it like this with a simple string (you can skip the quotation marks if you don't have spaces in your string - if you want):

```
entro.py "teststring"
```
or this for a file:

```
entro.py -files test.txt
```

or combine both of them:

```
entro.py "teststring" -files test.txt
```

Both arguments work with as many strings and filepaths as you want. Just separate them using a space like this:

```
entro.py "teststring" "teststring2" teststring3 -files test1.txt -files test2.txt
```

## Command line parameters

### Output Adjustments

`--simple` determines whether the output is explicit like this:

```
---
Content: TEST
Probabilities: {'T': 0.5, 'E': 0.25, 'S': 0.25}
Entropy: 1.5 bits
---
```

or simplistic like this:

```
---
Entropy: 1.5 bits
---
```

`--max` determines whether the output includes the maximum entropy or not, still will show if `--simple` is set:

```
---
Content: TEST
Probabilities: {'T': 0.5, 'E': 0.25, 'S': 0.25}
Entropy: 1.5 bits
Maximum Entropy: 1.584962500721156 bits
---
```

### String Conversion

`--lower` - Converts the input strings to lowercase

`--upper` - Opposite of lower, converts to upper (if both are set only lower will be executed)

`--squash` - Removes all whitespaces from input files (*This only applies to command line inputs if they were surrounded by quotation marks! Otherwise they will get split by the spaces as separate arguments.*)
