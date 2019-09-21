from string import punctuation


def is_tachycardic(w):
    str = "tachycardic"
    removable = punctuation + " "
    w = w.strip(removable)  # remove all leading/trailing spaces & punctuation
    w = w.lower()  # make all letters lowercase
    result = w == str
    print(result)
    return result


def user_interface():
    word = input("Enter a word: ")
    is_tachycardic(word)
    return

if __name__ == "__main__":
    user_interface()
