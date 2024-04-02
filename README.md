# PF-Assignment-first-
"""
calculate the multiplication ands sum of two numbers given two integer numbers ,return their product only if the product is equal to or than 1000 otherwise return thrir sum
"""
def calculate_product_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
# Example usage:
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = calculate_product_or_sum(num1, num2)
print("Result:", result)
"""
print the sum ofd current num and previous num 
write a program to iterate the firstr 10 numbers and in each iteration print the sum ofd the current and previous numbers 
"""
# Iterate through the first 10 numbers
for i in range(10):
    current_num = i
    if i == 0:
        previous num =0
    else:
        previous_num = i - 1
    sum_of_nums = current_num + previous_num
    # Print the sum
    print("Sum of", current_num, "and", previous_num, "is:", sum_of_nums)
