'''Follow these steps:
1. Create a file called alternative.py
2. Write a program that prompts the user to enter a string and makes each
alternate character into an uppercase character and each other alternate
character a lowercase character.
e.g. The string “Hello World” would become “HeLlO WoRlD”

Now, try starting with the same string but making each alternative word
lowercase and uppercase.
e.g. The string “I am learning to code” would become “i AM learning TO code”
.
Tip: Using the split() and join() methods will help you here.
'''

sentence = "Hello World"

final_string = ""

for i in range(len(sentence)):
    if i % 2 == 0:
        final_string += sentence[i].upper()
    else:
        final_string += sentence[i].lower()

print(final_string)

sentence2 = "I am learning to code"
words = sentence2.split()
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()
final_string2 = " ".join(words)
print(final_string2)