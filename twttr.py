def main():
    text=input("text: ")
    print(shorten(text))
def shorten(word):
    new_text=""
    vowels=["a","e","i","o","u"]
    for i in range(len(word)):
        if word[i].lower() not in vowels:
            new_text+=word[i]
    return new_text
if __name__ == "__main__":
    main()
