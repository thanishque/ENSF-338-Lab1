import json
import timeit

def modify_and_reverse(input_file, output_file):

    with open(input_file, 'r') as file:
        data = json.load(file)

    for record in data:
        record['size'] = 35

    with open(output_file, 'w') as file:
        json.dump(data[::-1], file, indent=2)

input_file_path = '/Users/Arnav/Documents/ENSF_338/lab1/large-file.json'  # Replace with the path to your JSON input file
output_file_path = '/Users/Arnav/Documents/ENSF_338/lab1/output.2.3.json'

modify_and_reverse(input_file_path, output_file_path)

for i in range(10):
    time_taken = timeit.timeit(lambda: modify_and_reverse(input_file_path, output_file_path), number=1)
    print(f"Iteration {i + 1}: {time_taken:.6f} seconds")
