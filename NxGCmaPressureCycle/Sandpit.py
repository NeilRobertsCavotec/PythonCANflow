import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Replace with the path to your CSV file
file_path = r"C:\Users\Neil.Roberts\Documents\MyVS.PyStuff\NxGCmaPressureCycle\NxGCmaPressureCycle.csv"

# Reading the .csv CAN captured file.
data_frame = pd.read_csv(file_path)

# Get the values of the CAN message columns B1.1 and B2.1 for the first 500 rows
b0_1_values = data_frame['B0.1'][:1500]
b1_1_values = data_frame['B1.1'][:1500]
b2_1_values = data_frame['B2.1'][:1500]
b3_1_values = data_frame['B3.1'][:1500]
b4_1_values = data_frame['B4.1'][:1500]
b5_1_values = data_frame['B5.1'][:1500]
b6_1_values = data_frame['B6.1'][:1500]
b7_1_values = data_frame['B7.1'][:1500]

'''
# MessageIndex Bit positions.
bit_positions_b0_1 = [0, 1, 2, 3, 4, 5]
'''


# Device Index

bit_positions_b0_1 = [6, 7]
bit_positions_b1_1 = [0, 1, 2]

'''
bit_positions_b2_1 = [0, 1]
bit_positions_b3_1 = [0, 1]
bit_positions_b4_1 = [0, 1]
bit_positions_b5_1 = [0, 1]
bit_positions_b6_1 = [0, 1]
bit_positions_b7_1 = [0, 1]
Message Index.
bit_positions_b2 = [4, 5, 6, 7]
bit_positions_b3 = [0, 1, 2, 3, 4, 5, 6, 7]

'''

# Flow Demand
'''
bit_positions_b0_1 = [0, 1]
bit_positions_b1_1 = [0, 1]
bit_positions_b2_1 = [0, 1]
bit_positions_b3_1 = [0, 1]
bit_positions_b4_1 = [0, 1]
bit_positions_b5_1 = [0, 1]
bit_positions_b6_1 = [0, 1]
bit_positions_b7_1 = [0, 1]

'''

# Workport
'''
bit_positions_b0_1 = [0, 1]
bit_positions_b1_1 = [0, 1]
bit_positions_b2_1 = [0, 1]
bit_positions_b3_1 = [0, 1]
bit_positions_b4_1 = [0, 1]
bit_positions_b5_1 = [0, 1]
bit_positions_b6_1 = [0, 1]
bit_positions_b7_1 = [0, 1]

'''

# Flow Direction
'''
bit_positions_b0_1 = [0, 1]
bit_positions_b1_1 = [0, 1]
bit_positions_b2_1 = [0, 1]
bit_positions_b3_1 = [0, 1]
bit_positions_b4_1 = [0, 1]
bit_positions_b5_1 = [0, 1]
bit_positions_b6_1 = [0, 1]
bit_positions_b7_1 = [0, 1]

'''

# Load Sense
'''
bit_positions_b0_1 = [0, 1]
bit_positions_b1_1 = [0, 1]
bit_positions_b2_1 = [0, 1]
bit_positions_b3_1 = [0, 1]
bit_positions_b4_1 = [0, 1]
bit_positions_b5_1 = [0, 1]
bit_positions_b6_1 = [0, 1]
bit_positions_b7_1 = [0, 1]

'''

# Extract specific bits and calculate combined values
combined_values = []

# DeviceIndex
for b1, b2 in zip(b1_1_values, b2_1_values):
    combined_value = ((b1 >> bit_positions_b0_1[0]) & 1) + (((b1 >> bit_positions_b1_1[1]) & 1) * 2) + \
                     ((b2 >> bit_positions_b0_1[0]) & 1) + (((b2 >> bit_positions_b1_1[1]) & 1) * 2)
    combined_values.append(combined_value)

# Smooth the combined values using a windowed average
window_size = 10
smoothed_combined_values = np.convolve(combined_values, np.ones(window_size) / window_size, mode='same')

# Plot the smoothed combined values
plt.figure(figsize=(10, 6))
plt.plot(range(1500), smoothed_combined_values, label='Combined Values', linewidth=2)
plt.xlabel('Index')
plt.ylabel('Combined Smoothed Value')
plt.title('NxG CMA CAN Message')
plt.legend()
plt.grid(True)
plt.show()
