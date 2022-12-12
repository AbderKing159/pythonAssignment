# after you clone the repo you will see this matrix.

matrix = [
    [True, 34, 5, 'School'],
    ['book', 'mosh', 'arc', 'photo'],
    [8, 23, 20, 11, 37, 55, 17],
    [-1, 'Mani']
]

# PART 1
onlyStrings = False
for item in matrix:
    if type(item) == list:
        onlyStrings = True
    for j in item:
        if type(j) != str:
            onlyStrings = False
            break
    if onlyStrings:
      for j in item:
        print(j.upper())


# PART 2
onlyInt = False
for i in matrix:
    if type(i) == list:
        onlyInt = True
    for a in i :
        if type(a) != int:
            onlyInt = False
            break
    if onlyInt:
        for a in reversed(i):
            isPrime = True
            for h in range(2, a//2):
                if a%h == 0:
                    isPrime= False
                    break
            if isPrime == True:
                print(a)




# You should write a program that do: 
# 1- Find the list that contains ALL STRING and print them on the console on capital letters. 
# For example program will not do anything with first and second array. but the 3rd array contains ALL STRING.
# If an array contains string but there are other data types in array, your program will ignore it.
# So the program will print BOOK MOSH ARC PHOTO
# 2- Find the list that all of its elements are numbers.
# Then print the prime numbers that exists in the list in reverse order.
# During the test I will change the order of matrix. So your program should be able to find the proper array smartly.
# Your prgram should be smart to find the list that contain all strings and all numbers.