import math
import random


def random_number(number1, number2):
    random.seed(3)
    numbers = []
    for num in range(10):
        numbers.append(random.randint(number1, number2))
    return numbers

print(random_number(1, 50), end=" ")


def length_in_list(number):
    count = 0
    for counter in number:
        count += 1
    return count


names = ["Glory", "Chi-Chi", "Melody", "Fantasy"]
length = length_in_list(names)
print(length)


def even_numbers(numbers):
    total = 0
    for counter in numbers:
        if counter % 2 == 0:
            total += counter
    return total


digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = even_numbers(digit)
print(number)


def odd_Numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total


#digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#number = odd_Numbers(digit)
#print(number)


def multiply(number):
    total = 1
    for index in range(0, length_in_list(number), 3):
        total *= number[index]

    return total


#digit =[1,2,3,4,5,6,7,8,9,10]
#esther = multiply(digit)
#print(esther)

def average(numbers):
    for counter in numbers:
        counter = counter / length_in_list(numbers)
        return counter


#number = [10,10,10,10,10]
#digit = average(number)
#print(digit)

def largest(digit):
    max = digit[0]
    for count in range(length_in_list(digit)):
        if digit[count] > max:
            max = digit[count]
    return max


#digit = [4,3,56,34,2]
#print(largest(digit))


def smallest(digit):
    max = digit[0]
    for count in range(length_in_list(digit)):
        if digit[count] < max:
            max = digit[count]
    return max


#digit = [4,3,56,34,2]
#print(smallest(digit))

def count_numbers(words):
    count = 0
    for word in words:
        if length_in_list(word) > 2 and word[0] == word[-1]:
            count += 1
    return count


#print(count_numbers(['esther','girl','3453','beauty']))


def sequence(esther):
    digit = esther[:]
    print(digit + esther)
    duplicate = digit + esther
    select = set(duplicate)
    print(select)


#esther = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#max = sequence(esther)
#print(max)


def third_element(number):
    total = 0
    for digit in range(1, 10, 3):
        total += digit
    return total


#numbers = [1,2,3,4,5,6,7,8,9,10]
#print(third_element(numbers))


def first_middle_last(number, middle_number=0):
    total_sum = 0

    for digit in range(0, length_in_list(number)):
        result = length_in_list(number) / 2
        result_ = math.floor(result)
        middle_number = number[result_]
        total_sum = number[0] + middle_number + number[-1]
        return total_sum


#print(first_middle_last([2, 9, 5, 7, 6]))


def sum_collection(numbers):
    total = 0
    sum_set = {}
    for number in numbers:
        total += number
        sum_set = total
    return sum_set


#print(sum_collection({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
