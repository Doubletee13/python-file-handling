import os

favorite_quote = input("enter favorite quote: ")

while True:
    file_to_save_favorite_quote = input("enter file to save favorite quote and end it with a '.txt' extention: ")
    root, extention = os.path.splitext(file_to_save_favorite_quote)
    if extention == "":
        print("must end with an extention")
    elif extention != ".txt":
        print(f"{file_to_save_favorite_quote} must end with a .txt extention")
    else:
        open(root+extention,"x")
        with open(file_to_save_favorite_quote,"a") as f:
            f.write(favorite_quote)

        with open(file_to_save_favorite_quote) as f:
            print(f.read())
        break

 


