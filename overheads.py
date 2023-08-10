# Import the Path class from the pathlib module
from pathlib import Path

# Import the csv module for handling CSV files
import csv

def overhead_function():
    """
    - Function identifies the highest overhead category 
    - No parameters required
    - Function reads data from Overheads.csv
    """
    # Creates a Path object named file_path.
    # Uses the Path.cwd() method to get the current working directory 
    # Appends the relative path "summary_report.txt" to it
    file_path = Path.cwd()/"summary_report.txt"

    # Creates an empty "summary_report.txt" file 
    file_path.touch()

    # Creates the file path to the "Overheads.csv" file located in the "csv_reports" 
    # directory relative to the current working directory.
    # Assign to variable fp_read
    fp_read = Path.cwd()/"csv_reports"/"Overheads.csv"

    # Creates the file path to the "summary_report.txt" file located in the 
    # current working directory
    # Assign to variable fp_write
    fp_write = Path.cwd()/"summary_report.txt"

    # Read the Overheads.csv file with UTF-8 encoding 
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    # Creates a csv.reader object named reader that reads data from the opened file 
        reader = csv.reader(file)
        
        # Skip header (first row of the CSV file)
        next(reader) 

        # Creates an empty list called Overheads.
        # List will be used to store category name and overheads data from the CSV file
        Overheads=[] 

        # Loop iterates over each row of data in the reader object
        # Variable row represents a single row of data from the CSV file
        for row in reader:

        # Get the category name and overheads data and append them to Overheads list
            Overheads.append([row[0],row[1]])
    
    # Initializes an empty string variable named output. 
    # Variable will store the generated summary report.
    output = ""

    # Retrieves the overhead value from the first nested list in Overheads list
    # Overhead value is stored in the second element (index 1) of each nested list
    # float() to convert the value from string to float and assign it to the variable max_value.
    max_value = float(Overheads[0][1])

    # Retrieves the category name from the first nested list in the Overheads list 
    # Category name is stored in the first element (index 0) of each nested list 
    # Assign it to the variable max_category.
    max_category = Overheads[0][0]

    # Loop will iterate over each entry (nested list) in the Overheads list
    # Variable category represents a nested list that contains the category name 
    # and the overhead value in each iteration
    for category in Overheads:

        # Retrieves the overhead value from the current category entry (nested list)
        # Overhead value is stored in the second element (index 1) of the category list
        # Float() function is used to convert the value from a string to a float.
        value = float(category[1])

        # checks if the current overhead value (value) is greater than the current 
        # maximum overhead value (max_value)
        if value > max_value:

        # If the current overhead value is greater than the current maximum overhead value, 
        # max_value variable will store the new updated maximum overhead value
            max_value = value

        # max_category variable will store the category name associated with the new 
        # maximum overhead value.
        # Category name is stored in the first element (index 0) of the category list.
            max_category = category[0]
    
    # Appends the formatted string to the output variable
    # The string states  the category name (max_category)  and the corresponding overhead 
    # value (max_value) in percentage
    output += (f"[HIGHEST OVERHEAD] {max_category}: {max_value}%")
    
    # Opens the "summary_report.txt" file in "write" mode with UTF-8 encoding
    with fp_write.open(mode="w", encoding="UTF-8") as summary_file:

        #  Writes the content of the output variable to the "summary_report.txt" file
        summary_file.write(output)
    
    # Function returns the output variable that contains the highest overhead category 
    # and its corresponding overhead value
    return output