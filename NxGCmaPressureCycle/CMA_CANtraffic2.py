import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Replace with the path to your CSV file
file_path = r"C:\Users\Neil.Roberts\Documents\MyVS.PyStuff\NxGCmaPressureCycle\NxGCmaPressureCycle.csv"

# Load data from the CSV file
data_frame = pd.read_csv(file_path)

# Get the values of columns B0 and B1 for the first 500 rows
b0_values = data_frame['B0'][:500]
b1_values = data_frame['B1'][:500]

# Convert hex values to binary
def hex_to_binary(hex_str):
    return format(int(hex_str, 16), '08b')  # Convert to 8-digit binary representation

binary_b0_values = b0_values.apply(hex_to_binary)
binary_b1_values = b1_values.apply(hex_to_binary)

# Extract specific bits from binary values
bit_position_b0 = 1
bit_position_b1 = 2

selected_bits_b0 = binary_b0_values.apply(lambda x: int(x[bit_position_b0]))
selected_bits_b1 = binary_b1_values.apply(lambda x: int(x[bit_position_b1]))

# Combine selected bits
combined_decimal_values = selected_bits_b0 + selected_bits_b1

# Smooth the combined decimal values using a windowed average
window_size = 10
smoothed_decimal_values = np.convolve(combined_decimal_values, np.ones(window_size)/window_size, mode='same')

# Plot the smoothed decimal values
plt.figure(figsize=(10, 6))
plt.plot(range(500), smoothed_decimal_values, label='MessageIndex', linewidth=2)
plt.xlabel('Index')
plt.ylabel('Decimal Value')
plt.title('NxG CMA Can MessageData')
plt.legend()
plt.grid(True)
plt.show()
