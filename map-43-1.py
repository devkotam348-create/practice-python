##write a pythonn script to find number of vowels in each of the string in a given list of strings. Use map function.

f = ['mahendra', 'devkota', 'rajendra', 'vowel']
print( list(map(lambda x: sum(ch in 'aeiou' for ch in x), f)))