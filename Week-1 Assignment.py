# Databricks notebook source
# DBTITLE 1,Q1
# Q1 
# Swap two variables without using an extra variable
first_num = 10
second_num = 20

first_num, second_num = second_num, first_num

print("After swapping without using extra variable:")
print("first_num =", first_num)
print("second_num =", second_num)

# Swap two variables using an extra variable
first_num = 10
second_num = 20

temp = first_num
first_num = second_num
second_num = temp

print("After swapping using extra variable:")
print("first_num =", first_num)
print("second_num =", second_num)

# COMMAND ----------

# DBTITLE 1,Q2
# MAGIC %md
# MAGIC #Q2
# MAGIC list - ordered - changeable - allow duplicate values
# MAGIC 
# MAGIC tuple - ordered - unchangeable - allow duplicate values
# MAGIC 
# MAGIC dictionary - ordered - changeable - does not allow duplicate values - dict
# MAGIC 
# MAGIC set - unordered - unchangeable - unindexed
# MAGIC 
# MAGIC string - ordered - mutable - str

# COMMAND ----------

# DBTITLE 1,Q3
def count_because(s):
    # Convert the string to lowercase to make the comparison case-insensitive
    s = s.lower()
    
    # Split the string into words and count the number of times 'because' occurs
    count = 0
    for word in s.split():
        if word == 'because':
            count += 1
    
    return count
input1 = 'You cannot end a sentence with because because because is a conjunction.'
output1 = count_because(input1)
print(output1)  
input2 = 'You cannot end a sentence with Because because Because is a conjunction.'
output2 = count_because(input2)
print(output2)

# COMMAND ----------

# DBTITLE 1,Q4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(is_prime, numbers))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = filter_primes(numbers)
print(primes)

# COMMAND ----------

# DBTITLE 1,Q5
[(word[0],word[-1]) for word in "Farmer jack realized that big yellow quilts were expensive".split()]

# COMMAND ----------

# MAGIC %md
# MAGIC #Q6
# MAGIC Answer: b) __str__(), __add__()

# COMMAND ----------

# DBTITLE 1,Q7
input_string = 'You	cannot	end	a	sentence	with	because	Because	because	is	a	conjunction.'

# Split the sentence into words
words = input_string.split()

# Create an empty list
word_list = []

# Iterate over each word
for word in words:
    # Check if the word starts with second letter of English alphabet
    if word[0].lower() == 'b':
        # Append the word to the list if it is not already present
        if word not in word_list:
            word_list.append(word)

# Print the output
print(*word_list, sep='\n')

# COMMAND ----------

# DBTITLE 1,Q8
def isRightTriangle(a, b, c): 
  
    # Calculate the square of the sides 
    a_square = a * a
    b_square = b * b
    c_square = c * c
  
    # Calculate the square of the largest side 
    c_square = max(a_square, b_square, c_square) 
  
    # Compare and return result 
    if (c_square == a_square + b_square): 
        return True
    else: 
        return False 
  
# Driver code 
a = 3
b = 4
c = 5
print(isRightTriangle(a, b, c))

# COMMAND ----------

# DBTITLE 1,Q9
def two_sum(nums, target): 
    # create a for loop that iterates through each element in nums list
    for i in range(len(nums)): 
        # create another for loop that iterates through each element in nums list
        for j in range(i + 1, len(nums)):  
            # if the sum of two elements equals the target
            if nums[i] + nums[j] == target: 
                # return the indices of the two elements
                return [i, j] 
  
# test cases 
nums = [2, 7, 11, 15] 
target = 9
print(two_sum(nums, target)) # [0, 1]

# COMMAND ----------

# DBTITLE 1,Q10
def big_diff(arr):
  min = arr[0]
  max = arr[0]
  for i in range(len(arr)):
    if arr[i] < min:
      min = arr[i]
    elif arr[i] > max:
      max = arr[i]
  return max - min

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))

#The logic of this code is to loop through the array and compare the elements of the array with the min and max variables. The min variable is initially set to the first element of the array and the max variable is initially set to the first element of the array. Then, for each element in the array, if it is less than the min variable, then it becomes the new min variable, and if it is greater than the max variable, then it becomes the new max variable. Finally, the difference between the max and min variable is returned.

# COMMAND ----------


