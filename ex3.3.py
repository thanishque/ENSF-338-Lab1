import json
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def modify_and_reverse(input_file, output_file, num_records=None):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if num_records is not None:
        data = data[:num_records]

    for record in data:
        record['size'] = 35

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data[::-1], file, indent=2)


def measure_processing_time():
    num_records = 1000
    iterations = 1000
    times = []

    for _ in range(iterations):
        time_taken = timeit.timeit(
            lambda: modify_and_reverse(input_file_path, output_file_path, num_records), number=1)
        times.append(time_taken)

    return times


input_file_path = 'C:\\Users\\deboj\\OneDrive\\Desktop\\ENSF_338\\Lab_1\\ENSF-338-Lab1\\large-file.json'
output_file_path = 'C:\\Users\\deboj\\OneDrive\\Desktop\\ENSF_338\\Lab_1\\ENSF-338-Lab1\\output.2.3.json'

record_counts = [1000, 2000, 5000, 10000]

avg_times = []

for num_records in record_counts:
    total_time = 0
    iterations = 100

    for _ in range(iterations):
        time_taken = timeit.timeit(lambda: modify_and_reverse(
            input_file_path, output_file_path, num_records), number=1)
        total_time += time_taken

    average_time = total_time / iterations
    avg_times.append(average_time)
    print(
        f"Avg. time for processing {num_records} records (100 iterations): {average_time:.6f} seconds")

slope, intercept, r_value, p_value, std_err = linregress(
    avg_times, record_counts)
line = slope * np.array(avg_times) + intercept

print(f"Slope: {slope}, Intercept: {intercept}, R-squared: {r_value**2}")

# Measure processing time
measurement_times = measure_processing_time()

# Plot histogram
plt.hist(measurement_times, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Processing Times for 1000 Records (1000 iterations)')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.show()
