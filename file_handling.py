favorite_quote = input("enter favorite quote")

file_to_save_favorite_quote = input("enter file to save favorite quote and end it with an extention")

open(file_to_save_favorite_quote,"x")

with open(file_to_save_favorite_quote,"a") as f:
    f.write(favorite_quote)

with open(file_to_save_favorite_quote) as f:
    print(f.read())