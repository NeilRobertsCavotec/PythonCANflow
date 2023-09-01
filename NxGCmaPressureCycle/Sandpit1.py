import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Replace with the path to your CSV file
file_path = r"C:\Users\Neil.Roberts\Documents\MyVS.PyStuff\NxGCmaPressureCycle\NxGCmaPressureCycle.csv"

# Reading the .csv CAN captured file.
data_frame = pd.read_csv(file_path)

# Get the values of the CAN message columns B1.1 and B2.1 for the first 500 rows
b1_1_values = data_frame['B1.1'][:500]
b2_1_values = data_frame['B2.1'][:500]

# Bit positions for B1.1 and B2.1
bit_positions_b1_1 = [0, 1]
bit_positions_b2_1 = [0, 1]

# Extract specific bits and calculate combined values
combined_values = []

for b1, b2 in zip(b1_1_values, b2_1_values):
    combined_value = ((b1 >> bit_positions_b1_1[0]) & 1) + (((b1 >> bit_positions_b1_1[1]) & 1) * 2) + \
                     ((b2 >> bit_positions_b2_1[0]) & 1) + (((b2 >> bit_positions_b2_1[1]) & 1) * 2)
    combined_values.append(combined_value)

# Smooth the combined values using a windowed average
window_size = 10
smoothed_combined_values = np.convolve(combined_values, np.ones(window_size) / window_size, mode='same')

# Create a subplot with two plots: one for column plot and one for smooth line plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Column plot Message Index
ax1.bar(range(500), combined_values, label='Combined Values', color='blue', alpha=0.7)
ax1.set_ylabel('Combined Value')
ax1.set_title('NxG CMA DeviceIndex')
ax1.grid(True)
ax1.legend()

# Smooth line plot Pressure Flow requests
ax2.plot(range(500), smoothed_combined_values, label='Smoothed Values', color='red', linewidth=2)
ax2.set_xlabel('Index')
ax2.set_ylabel('Smoothed Value')
ax2.set_title('NxG Flow Demend')
ax2.grid(True)
ax2.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
