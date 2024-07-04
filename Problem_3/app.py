def count_words_in_file(filename: str) -> int:
    with open(filename, "r") as f:
        words = f.read().split()
    return len(words)

print(count_words_in_file("sample.txt"))
