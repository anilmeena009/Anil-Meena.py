# # Input number
# num = int(input("Enter a number: "))

# original_num = num

# # Get last digit
# last_digit = num % 10

# # Find first digit using while loop
# while num >=10:
#     num = num // 10
# first_digit = num

# # Sum of first and last digit
# # sum_digits = first_digit + last_digit

# print("First digit:", first_digit)
# print("Last digit:", last_digit)
# # print("Sum of first and last digit:", sum_digits)




# n=int(input("enter the number"))
# sum=0
# i=1
# # for i in range(1,n):
# while(i<=n):
#      sum+=i
#      i+=1
#      print(sum)


# n=int(input("Enter a number: "))
# tab=0
# for i in range(1,11):
#         tab=n*i
#         print(f" {tab}")


# n=int(input("Enter a number: "))
# tab=0
# for i in range(1,11):
#         tab=n*i
#         print(f" {tab}")
# else:
#     print("done!")


# digits=int(input("Enter a number: "))
# count=0
# while digits > 0:
#     count += 1
#     digits //= 10
# print("The number of digits is:", count)


# digits = int(input("Enter a number: "))
# count = 0
# for i in range(1, digits):
#     if digits % 10 == 0:
#         count += 1  
# print("The number of digits is:", count)


# remove duplicate from list
# my_list = [1, 2, 3, 4, 5, 1, 2, 3]
# def remove_duplicates(lst):
#     return list(set(lst))
# result = remove_duplicates(my_list)
# print("List after removing duplicates:", result)

# Write a function that flattens a nested list (e.g., [[1,2],[3,[4,5]],6]
# def flatten(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flat_list.extend(flatten(item))  # Recursively flatten the sublist
#         else:
#             flat_list.append(item)
#     return flat_list
# nested_list = [[1, 2], [3, [4, 5]], 6]
# flatte = flatten(nested_list)  
# print(flatte)

# Rotate a list to the right by k steps (e.g., [1,2,3,4,5], k=2 → [4,5,1,2,3]).
# def rotate_list(lst, k):
#     k = k % len(lst)
#     return lst[-k:] + lst[:-k]
# lst = [1, 2, 3, 4, 5]
# k = 2
# rotated_list = rotate_list(lst, k)
# print(rotated_list)


# Find all pairs in a list whose sum is equal to a target number.
# def find_pairs(list, target):
#     pairs = []
#     seen = set()
#     for i in list:
#         j = target -i
#         if j in seen:
#             pairs.append((j,i))
#         seen.add(i)
#     return pairs
# list = [1, 2, 3, 4, 5, 6]
# target = 7 
# pair = find_pairs(list, target)
# print(target,pair)


# Given a list of tuples like [('a',1), ('b',2), ('a',3)], write a function to group values by key into a dictionary.
# def group_by_key(tuples_list):
#     grouped_dict = {}
#     for key, value in tuples_list:
#         if key not in grouped_dict:
#             grouped_dict[key] = []
#         grouped_dict[key].append(value)
#     return grouped_dict
# tuples_list = [('a', 1), ('b', 2), ('a', 3)]
# grouped_dict = group_by_key(tuples_list)   
# print(grouped_dict)


# Merge two dictionaries. If a key appears in both, sum their values.
# def merge_dictionaries(dict1, dict2):
#     merged_dict = dict1.copy()
#     for key, value in dict2.items():
#         if key in merged_dict:
#             merged_dict[key] += value 
#         else:
#             merged_dict[key] = value
#     return merged_dict
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged_dict = merge_dictionaries(dict1, dict2)
# print(merged_dict)


# Write a function that takes a list of tuples and returns a tuple with the max sum of its elements.
# def max_sum_tuple(tuples_list):
#     max_sum = float('-inf')
#     max_tuple = ()
#     for tup in tuples_list:
#         current_sum = sum(tup)
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_tuple = tup
#     return max_tuple
# tuples_list = [(1, 2), (3, 4), (5, 6)]
# max_tuple = max_sum_tuple(tuples_list)
# print(max_tuple)

# Sort a dictionary by its values in descending order.
# def sort_dict_by_value(d):
#     return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# d = {'a': 3, 'b': 1, 'c': 2}
# sorted_dict = sort_dict_by_value(d)
# print(sorted_dict)

# Write a function to invert a dictionary: {1: 'a', 2: 'b'} → {'a': 1, 'b': 2}.
# def invert_dict(d):
#     inverted_dict = {}
#     for key, value in d.items():
#         inverted_dict[value] = key
#     return inverted_dict
# d = {1: 'a', 2: 'b', 3: 'c'}
# inverted_dict = invert_dict(d)
# print(inverted_dict)

# # Use lambda to square each number in a list.
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)


# Use filter and lambda to get all even numbers from a list.
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

#  Given a list of names, use map to convert each name to Title Case.
# names = ['john', 'jane', 'doe']
# title_case_names = list(map(lambda x: x.title(), names))
# print(title_case_names)


# # Use a function with argument and parameter to find the product of all numbers in a list.
# def product_of_list(numbers):
#     product = 1
#     for number in numbers:
#         product *= number
#     return product
# numbers = [1, 2, 3, 4, 5]
# result = product_of_list(numbers)
# print(result)

# # Use map() and lambda to combine two lists element-wise into sums.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# sums = list(map(lambda x, y: x + y, list1, list2))
# print(sums)


# # Write a function to check if two lists are anagrams of each other.
# def are_anagrams(list1, list2):
#     return sorted(list1) == sorted(list2)   
# list1 = ['a', 'b', 'c']
# list2 = ['c', 'b', 'a']
# result = are_anagrams(list1, list2)
# print("Are the lists anagrams of each other?", result)

# Count the frequency of each word in a sentence and return a dictionary.
# def word_frequency(sentence):
#     words = sentence.split()
#     frequency = {}
#     for word in words:
#         word = word.lower()  # Normalize to lowercase
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency
# sentence = "Hello world hello"
# frequency_dict = word_frequency(sentence)
# print(frequency_dict)

#  Given a list of dictionaries [{name: "A", age: 25},...], use filter() to get only those with age > 30.
# def filter_by_age(dicts, age_threshold):
#     return list(filter(lambda d: d['age'] > age_threshold, dicts))
# dicts = [{'name': 'A', 'age': 25}, {'name': 'B', 'age': 35}, {'name': 'C', 'age': 30}]
# age_threshold = 30
# filtered_dicts = filter_by_age(dicts, age_threshold)
# print(filtered_dicts)

# Write a function that finds the first non-repeating character in a string.
# def first_non_repeating_char(s):
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     for char in s:
#         if char_count[char] == 1:
#             return char
#     return None
# s = "swiss"
# result = first_non_repeating_char(s)
# print("First non-repeating character:", result if result else "None")


#18. Create a dictionary from two lists, one of keys and one of values.
# def create_dict_from_lists(keys, values):
#     return dict(zip(keys, values))
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# result_dict = create_dict_from_lists(keys, values)
# print("Created dictionary:", result_dict)

#19. Write a function to check if two lists are anagrams of each other.
# def are_anagrams(list1, list2):
#     return sorted(list1) == sorted(list2)
# list1 = ['a', 'b', 'c']
# list2 = ['c', 'b', 'a']
# result = are_anagrams(list1, list2)
# print("Are the lists anagrams of each other?", result)


# Implement a frequency counter using list comprehension and dictionary.
# def frequency_counter(lst):
#     return {item: lst.count(item) for item in set(lst)}
# lst = [1, 2, 2, 3, 3, 3]
# result = frequency_counter(lst)
# print("Frequency counter:", result)


# Case Study: Sales and Inventory Management System
# Objective:
# Design a Python-based system for a retail company that manages inventory, sales, and profit tracking using Object-Oriented Programming. The company wants to:
# Add new products.
# Update stock.
# Record customer purchases.
# Automatically update inventory.
# Calculate total revenue and profit per product.

# Entities & Structure:
# Product: Represents individual items.
# Inventory: Manages the collection of products.
# SalesRecord: Logs each sale and helps compute revenue and profit.
# StoreManager: Interface to interact with all operations.
# class Product:
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock

#     def update_stock(self, quantity):
#         self.stock += quantity

#     def sell(self, quantity):
#         if quantity <= self.stock:
#             self.stock -= quantity
#             return True
#         return False
# class Inventory:
#     def __init__(self):
#         self.products = {}

#     def add_product(self, product):
#         if product.name in self.products:
#             self.products[product.name].update_stock(product.stock)
#         else:
#             self.products[product.name] = product

#     def get_product(self, name):
#         return self.products.get(name, None)
# class SalesRecord:
#     def __init__(self):
#         self.sales = []

#     def record_sale(self, product, quantity):
#         if product.sell(quantity):
#             self.sales.append((product.name, quantity, product.price * quantity))
#             return True
#         return False

#     def total_revenue(self):
#         return sum(sale[2] for sale in self.sales)

#     def profit_per_product(self):
#         profit = {}
#         for sale in self.sales:
#             name, quantity, revenue = sale
#             if name not in profit:
#                 profit[name] = 0
#             profit[name] += revenue
#         return profit
# class StoreManager:
#     def __init__(self):
#         self.inventory = Inventory()
#         self.sales_record = SalesRecord()

#     def add_product(self, name, price, stock):
#         product = Product(name, price, stock)
#         self.inventory.add_product(product)

#     def update_stock(self, name, quantity):
#         product = self.inventory.get_product(name)
#         if product:
#             product.update_stock(quantity)

#     def record_sale(self, name, quantity):
#         product = self.inventory.get_product(name)
#         if product:
#             return self.sales_record.record_sale(product, quantity)
#         return False

#     def total_revenue(self):
#         return self.sales_record.total_revenue()

#     def profit_per_product(self):
#         return self.sales_record.profit_per_product()
# # Example Usage
# if __name__ == "__main__":
#     manager = StoreManager()

#     # Adding products
#     manager.add_product("Laptop", 1000, 10)
#     manager.add_product("Phone", 500, 20)

#     # Updating stock
#     manager.update_stock("Laptop", 5)

#     # Recording sales
#     manager.record_sale("Laptop", 2)
#     manager.record_sale("Phone", 3)

#     # Displaying total revenue and profit per product
#     print("Total Revenue:", manager.total_revenue())
#     print("Profit per Product:", manager.profit_per_product())
    
    
    
# swap two value in list without using def function.
# my_list = [1, 2, 3, 4, 5]
# index1 = 1  # Index of the first element to swap
# index2 = 3  # Index of the second element to swap
# # Swap the elements
# my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
# print("List after swapping:", my_list)


# filter even numbers from a list using lambda function.
# list1=[1,2,3,4,5,6,7,8,9]
# lst=list(filter(lambda x : x%2==0,list1))
# print(lst)