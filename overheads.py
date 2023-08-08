from pathlib import Path
import csv

def overhead_function():
    """
    - Function calculates the highest overhead
    - No parameters required

    """
    # creates a Path object named file_path.
    # uses the Path.cwd() method to get the current working directory 
    # appends the relative path "summary_report.txt" to it
    file_path = Path.cwd()/"summary_report.txt"

    #  creates an empty "summary_report.txt" file 
    file_path.touch()

    # creates the file path to the "Overheads.csv" file located in the "csv_reports" 
    # directory relative to the current working directory.
    fp_read = Path.cwd()/"csv_reports"/"Overheads.csv"

    # creates the file path to the "summary_report.txt" file located in the 
    # current working directory
    fp_write = Path.cwd()/"summary_report.txt"

    # read the Overheads.csv file with UTF-8 encoding 
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    # creates a csv.reader object named reader that reads data from the opened file 
        reader = csv.reader(file)
        
        # skip header (first row of the CSV file)
        next(reader) 

        # creates an empty list called Overheads.
        # list will be used to store category name and overheads data from the CSV file
        Overheads=[] 

        # loop iterates over each row of data in the reader object
        # variable row represents a single row of data from the CSV file
        for row in reader:

        # get the category name and overheads data and append them to Overheads list
            Overheads.append([row[0],row[1]])
    
    # initializes an empty string variable named output. 
    # variable will store the generated summary report.
    output = ""

    # retrieves the overhead value from the first nested list in Overheads list
    # overhead value is stored in the second element (index 1) of each nested list
    # converts the value from string to float and assign it to the variable max_value.
    max_value = float(Overheads[0][1])

    # retrieves the category name from the first nested list in the Overheads list 
    # category name is stored in the first element (index 0) of each nested list 
    # assigns it to the variable max_category.
    max_category = Overheads[0][0]

    # loop will iterate over each entry (nested list) in the Overheads list
    # variable category represents a nested list that contains the category name 
    # and the overhead value in each iteration
    for category in Overheads:

        # retrieves the overhead value from the current category entry (nested list)
        # overhead value is stored in the second element (index 1) of the category list
        # float() function is used to convert the value from a string to a float.
        value = float(category[1])

        # checks if the current overhead value (value) is greater than the current 
        # maximum overhead value (max_value)
        if value > max_value:

        # If the current overhead value is greater than the current maximum overhead value, 
        # max_value variable will store the new maximum overhead value
            max_value = value

        # max_category variable will store the category name associated with the new 
        # maximum overhead value.
        # category name is stored in the first element (index 0) of the category list.
            max_category = category[0]
    
    # appends the formatted string to the output variable
    # The string represents the highest overheads and includes the category name (max_category) 
    # and the corresponding overhead value (max_value)
    output += (f"[HIGHEST OVERHEADS] {max_category}: {max_value}%")
    
    # opens the "summary_report.txt" file in "write" mode with UTF-8 encoding
    with fp_write.open(mode="w", encoding="UTF-8") as summary_file:

        #  writes the content of the output variable to the "summary_report.txt" file
        summary_file.write(output)
    
    # function returns the output variable that contains the highest overhead category 
    # and its corresponding overhead value
    return output