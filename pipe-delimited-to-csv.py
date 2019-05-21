import csv
import sys
import os

# Convert comma-delimited CSV files to pipe-delimited files
# Usage: Drag-and-drop CSV file over script to convert it.

inputPath = sys.argv[1]
outputPath = os.path.dirname(inputPath) + "/output.csv"

# https://stackoverflow.com/a/27553098/3357935
print("Converting delimiter from pipes '|' to commas ','...")
with open(inputPath) as inputFile:
	with open(outputPath, 'w', newline='') as outputFile:
		reader = csv.DictReader(inputFile, delimiter='|')
		writer = csv.DictWriter(outputFile, reader.fieldnames, delimiter=',')
		writer.writeheader()
		writer.writerows(reader)
print("Conversion complete.")
