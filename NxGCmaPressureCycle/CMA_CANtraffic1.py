import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

# Replace with the path to your CSV file
file_path = r"C:\Users\Neil.Roberts\Documents\MyVS.PyStuff\NxGCmaPressureCycle\NxGCmaPressureCycle.csv"

# Load data from the CSV file
data_frame = pd.read_csv(file_path)

# Get the values of columns B0 and B1 for the first 500 rows
b0_values = data_frame['B0'][:7742]
b1_values = data_frame['B1'][:7742]

# Convert hex values to decimal
def hex_to_decimal(hex_str):
    return int(hex_str, 16)

decimal_b0_values = b0_values.apply(hex_to_decimal)
decimal_b1_values = b1_values.apply(hex_to_decimal)

# Create an array for x values (row indices)
x_values = np.arange(7742)

# Plot decimal values of B0 and B1
plt.figure(figsize=(10, 6))
plt.plot(x_values, decimal_b0_values, label='B0', linewidth=2)
plt.plot(x_values, decimal_b1_values, label='B1', linewidth=2)
plt.xlabel('Index')
plt.ylabel('Decimal Value')
plt.title('Decimal Values of B0 and B1')
plt.legend()
plt.grid(True)
plt.show()
