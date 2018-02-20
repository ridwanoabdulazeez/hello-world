# hello-world


my name is ridwan. i have a huge passion for technology
vowels = {"a", "e", "i", "o", "u"}
# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

settext = " "

textEntered = set(input("please input your enter direction: "))

diff = textEntered.difference(vowels)
final_diff = sorted(diff)

print(final_diff)


textEntered = set(input("please input your enter direction: "))
sets = " "
for test in textEntered:
    if test not in vowels:
        sets += test
        newSet = set(sets)
        print(newSet)
     
