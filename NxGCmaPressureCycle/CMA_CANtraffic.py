import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

# C:\Users\Neil.Roberts\Documents\MyVS.PyStuff\KalmanFilter\ZtPosition.csv
file_path = r"C:\Users\Neil.Roberts\Documents\MyVS.PyStuff\NxGCmaPressureCycle\NxGCmaPressureCycle.csv"  

# Load data from the CSV file
data_frame = pd.read_csv(file_path)

column_name = 'B1' # Replace with the actual column name

# Get the values of the specified column for the first 500 rows
values_to_plot = data_frame[column_name][:10000]

print(data_frame.columns)

# measurements = data_frame[column_name].values
measurements = data_frame[column_name].values

plt.figure(figsize=(10, 6))
plt.plot(range(10000), values_to_plot, label=column_name)
plt.xlabel('Index')
plt.ylabel('bar')
plt.title(f'NxG CMA {column_name} Trafic')
plt.legend()
plt.grid(True)
plt.show()




