import csv

# Data to be written to the CSV file
data_to_write = [
  ['Name', 'Age', 'Grade'],
  ['Alice', 25, 'A'],
  ['Bob', 22, 'B'],
  ['Charlie', 28, 'A+']
]

# Open the CSV file in 'write' mode
with open('data.csv', 'w', newline='') as file:
  # Create a CSV writer object
  csv_writer = csv.writer(file)

  # Write the data to the CSV file
  csv_writer.writerows(data_to_write)