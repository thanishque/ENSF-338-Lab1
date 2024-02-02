import timeit

def count_vowels(word):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in word if char in vowels)

def average_vowels_per_word(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    words = [word for line in lines for word in line.split()]

    total_vowels = 0
    total_words = len(words)

    for word in words:
        total_vowels += count_vowels(word)

    if total_words == 0:
        return 0  # Avoid division by zero

    average_vowels = total_vowels / total_words
    return average_vowels


file_path = '/Users/Arnav/Documents/ENSF_338/lab1/pg2701.txt'  

for i in range(100):
    time_taken = timeit.timeit(lambda: average_vowels_per_word(file_path), number=1)
    print(f"Iteration {i + 1}: {time_taken:.6f} seconds")
