def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = len(get_num_of_char(file_contents))
    char_pops = char_count(file_contents)
    print(f"There are {num_words} words in this book!")
    print()
    print()
    for c in char_pops:
        print(f"There are {char_pops[c]} iterations of the character {c} in this book!")
    
def get_num_of_char(text):
    words = text.split()
    return words

def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()
