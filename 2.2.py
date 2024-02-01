def count_consonants(word):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    return sum(1 for char in word if char in consonants)

def average_consonants_per_word(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    words = [word for line in lines for word in line.split()]

    total_consonants = 0
    total_words = len(words)

    for word in words:
        total_consonants += count_consonants(word)

    if total_words == 0:
        return 0  # Avoid division by zero

    average_consonants = total_consonants / total_words
    return average_consonants

file_path = '/Users/Arnav/Documents/ENSF_338/lab1/pg2701.txt' 
result = average_consonants_per_word(file_path)
print(f"The average number of consonants per word is: {result}")

