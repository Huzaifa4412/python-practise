# 1. Extract Domains
emails = [
    "huzaifa@gmail.com",
    "ali@yahoo.com",
    "dev@company.com",
    "test@gmail.com",
    "admin@openai.com",
]

domains = [email.split("@")[1] for email in emails]
# print(domains)

# 2. Word Frequency Counter (Ignore Small Words)
# 📌 Problem: Count the frequency of words in a sentence but skip common words like "the", "is", "a".


text = "The AI agent is a powerful tool and the AI is growing  ~ Simple ai"
stop_words = {"the", "is", "a", "", "~"}

# how to calculate frequency of single word
# word = "Huzaifa  is a good boy"
# print(f"{word.count('good')}")

# simple loop
# for word in text.split(" "):
#     if word not in stop_words:
#         print(f"{word}: {text.lower().count(word.lower())}")

# frequency = {
#     word: text.lower().count(word.lower())
#     for word in text.split(" ")
#     if word not in stop_words
# }
# print(frequency)


# 3. Price Lookup Dictionary

products = [
    ("Laptop", 1200),
    ("Phone", 800),
    ("Mouse", 50),
    ("Keyboard", 150),
    ("Monitor", 400),
]
# ✅ Expected Output:

# {
#     'Laptop': 1200,
#     'Phone': 800,
#     'Mouse': 50,
#     'Keyboard': 150,
#     'Monitor': 400
# }

# lookup = {product for product in products for product_name, price in product}
# print(lookup)

products = [
    ("Laptop", 1200),
    ("Phone", 800),
    ("Mouse", 50),
]

# price_lookup = {name.lower(): price for name, price in products}
# print(price_lookup["phone"])


# 4. Filter Big Spenders - how spend more then $500

spending = {"Huzaifa": 1200, "Ali": 400, "Sara": 900, "John": 200, "Ahmed": 750}
# ✅ Expected Output:


# {
#     'Huzaifa': 1200,
#     'Sara': 900,
#     'Ahmed': 750
# }

# big_spenders = []

# for spender, value in spending.items():
#     if value > 500:
#         big_spenders.append({spender: value})

# print(big_spenders)

big_spenders = [{spender: value} for spender, value in spending.items() if value > 500]
print(big_spenders)


# 5. Flatten & Filter Transactions

transactions = [[120, 305, 450], [200, 125, 600, 333], [75, 90, 180]]
# # 👉 Task: Flatten list banao, sirf even amounts rakho

filtered_transactions = [
    transaction for row in transactions for transaction in row if transaction % 2 == 0
]
print(filtered_transactions)
