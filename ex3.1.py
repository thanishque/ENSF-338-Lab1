import pandas as pd
import matplotlib.pyplot as plt

# Loading the JSON dataset
url = "https://github.com/ldkteaches-calgary/ensf338W24/blob/main/lab01/songdata.json"
df = pd.read_json(url)

belowNeg8 = df[df['loudness'] < -8]
aboveNeg8 = df[df['loudness'] >= -8]

# Create histograms for the 'tempo' parameter for each group
plt.hist(belowNeg8['tempo'], bins=10, color='yellow', alpha=0.6, label='Below -8')
plt.hist(aboveNeg8['tempo'], bins=10, color='green', alpha=0.6, label='At or Above -8')

plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.title('Distribution of Tempo for Songs with Loudness Below and At or Above -8')

plt.legend()

# Save the histograms as PNG files
plt.savefig('hist1.png')
plt.clf()  

# Create a new histogram for the second group
plt.hist(aboveNeg8['tempo'], bins=20, color='orange', alpha=0.7, label='At or Above -8')

plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.title('Distribution of Tempo for Songs with Loudness At or Above -8')

plt.legend()

# Save the histogram as a PNG file
plt.savefig('hist2.png')
