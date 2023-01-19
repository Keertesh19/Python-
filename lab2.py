# LAB 2

# TASK 1
str1 = "Hello"
int1 = 21
float1 = 10.5
bool1 = True

print('# TASK 1 \n')
print(type(str1), type(int1), type(float1), type(bool1))
print(f'\n{str1}, I am {int1} years old. My fav number is {float1}. {bool1} equals {+bool1}.\n')

# TASK 2
str1 = "Hello"
str2 = "Python"

print('# TASK 2\n')
print(str1 + "###" + str2 + "       # METHOD 1") # METHOD 1
print("###".join([str1, str2]) + "      # METHOD 2\n") # METHOD 2

# TASK 3
print('# TASK 3\n')
int1 = int(input('Input an integer : '))
int2 = int(input('Input second integer : '))

print(f'\nThe sum of int1 and int2 is {int1 + int2}')

# TASK 4
print('\n# TASK 4\n')
str1 = input("Input some text : ")
int1 = int(input('Input a number : '))

print(f'\nstr1 : {str1}\nnum1 : {int1 + 10}')

# TASK 5

celsius = 15.4
fahrenheit = 1.8 * celsius + 32

print('\n# TASK 5\n')
print(f'Temperature in Celsius : {celsius}\nTemperature in Fahrenheit : {fahrenheit}')
