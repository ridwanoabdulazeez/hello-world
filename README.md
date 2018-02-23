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
     
# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  --------------------



with open("C:\\Users\\Kingsgate\\Downloads\\sampple.txt", 'a') as rid:
    
    for i in range(1,13):
        for j in range(1,13):
            print("{:>3} times {} is {}".format(j, i, i*j))
        print("-"*40)
print(file=rid)
