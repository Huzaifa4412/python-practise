#  1. Capitalize & Filter Names (List Comprehension)
# You have a list of names.
# 👉 Task: Create a list of names starting with "a" (case-insensitive), capitalized.


import re


names = ["ali", "huzaifa", "ahmed", "Sara", "asim", "John", "Anus"]
# ✅ Expected Example: ['Ali', 'Ahmed', 'Asim']

# names = [name.capitalize() for name in names if name.lower().startswith("a")]
# print(names)


# 1. LIST (Basic + if + if-else)
# 👉 Task: From nums, create a list where:

# even → square it

# odd → keep same

nums = [1, 2, 3, 4, 5, 6]
# # ✅ Expected: [1, 4, 3, 16, 5, 36]

# new_nums = [n if n % 2 != 0 else n**2 for n in nums]
# new_nums


#  SET (Unique Filtering)
# 👉 Task: From a sentence, extract unique letters, ignoring vowels.
# ✅ Expected (order doesn’t matter): {'c','m','p','r','h','n','s','k','t','d','f'}

sentence = "Comprehensions make Pythonic code simple and fast"
vowels = "a,e,i,o,u".split(",")
# print(vowels)

unique_consonants = {
    ch.lower() for ch in sentence if ch.isalpha() and ch.lower() not in vowels
}
# print(unique_consonants)

# Extract the letter which only came for the first time

# sentence = "Comprehensions make Pythonic code simple and fast"
# unique_char = {
#     ch.lower() for ch in sentence if ch.isalpha and sentence.lower().count(ch) == 1
# }
# print(unique_char)


# ✅ 1. WORD ANALYSIS (Dict + Set + Filtering)
# 📌 Problem:
# You have a paragraph. You need to:

# Count the frequency of only unique words (appearing once).

# Ignore stop words & punctuation.

# Return as a dictionary.


paragraph = """
AI is transforming the world. The future of AI is automation and intelligence.
AI makes the world smarter.
"""
stop_words = {"the", "is", "of", "and"}
# ✅ Expected Output:

# {
#     'transforming': 1,
#     'future': 1,
#     'automation': 1,
#     'intelligence': 1,
#     'makes': 1,
#     'smarter': 1
# }
# (Notice "ai" & "world" are not included because they repeat)

# Extract clean words (lowercase & no punctuation)
words = re.findall(r"[a-zA-Z]+", paragraph.lower())

unique_words = {
    word: words.count(word)
    for word in set(words)
    if words.count(word) == 1 and word not in stop_words
}

# print(unique_words)


# 2. PRODUCT DATA CLEANING (Nested + Dict + If-Else)
# 📌 Problem:
# You have a list of product data. You need to:

# Convert it to a dictionary {product_name: final_price}.

# If in_stock == False, ignore the product.

# Apply 10% discount if price > 1000 else 5%.

# Make all product names lowercase.

products = [
    ("Laptop", 1200, True),
    ("Phone", 800, True),
    ("Monitor", 1500, False),
    ("Mouse", 50, True),
    ("Tablet", 1100, True),
]
# ✅ Expected Output:


# {
#     'laptop': 1080.0,   # 10% off
#     'phone': 760.0,     # 5% off
#     'mouse': 47.5,      # 5% off
#     'tablet': 990.0     # 10% off
# }
filtered_products = {
    name.lower(): (value * 0.90 if value > 1000 else value * 0.95)
    for name, value, stock in products
    if stock
}
print(filtered_products)
