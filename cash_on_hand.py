# Import the Path class from the pathlib module
from pathlib import Path

# Import the csv module for handling CSV files
import csv

def coh_function():
    """
    - Function calculates cash deficits for each day with a deficit. 
      In cases where there are no deficit days, it calculates the highest cash surplus.
    - No parameters required
    - Function reads data from Cash_on_Hand.csv file
    """
   
    # Creates the file path to the "Cash_on_Hand.csv" file located in the "csv_reports"
    # directory relative to the current working directory.
    # Assign to variable fp_read
    fp_read = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

    # Creates the file path to the "summary_report.txt" file located in the
    # current working directory
    # Assign to variable fp_write
    fp_write = Path.cwd()/"summary_report.txt"

    # Reads the Cash_on_Hand.csv file with UTF-8 encoding
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:  
        # Creates a csv.reader object named reader that reads data from the opened file
        reader = csv.reader(file)
       
    # Skip header (first row of the CSV file)
        next(reader)

    # create an empty lists to store the day number and cash on hand records
        cash_on_hand=[]

        # Loop iterates over each row of data in the reader object
        # Variable row represents a single row of data from the CSV file
        for row in reader:

    # Get the day and cash on hand data and append them to cash_on_hand list
            cash_on_hand.append([row[0],row[1]])
   
    # Creates an empty list called deficit_days_list.
    # List will store the indices of days where there is a cash deficit.
    deficit_days_list = []

    # Initialize a variable highest_surplus to keep track of the highest cash surplus
    highest_surplus = 0

    # Initializes an empty string variable named output to store the summary report generated
    # based on the cash deficits or the highest cash surplus.
    output = ""

    # Loop will iterate over the range of days (from day 1 to the total number of days)
    # in the cash_on_hand list.
    for day in range(1, len(cash_on_hand)):

    # Retrieves the cash amount on the current day from the cash_on_hand list and
    # assign to current_cash variable
    # The cash amount is stored in the second column (index 1) of each day's data list
    # int() function to convert cash amount from string to integer
        current_cash = int(cash_on_hand[day][1])

    # Retrieves the cash amount on the previous day from the cash_on_hand list and
    # assign to previous_cash variable
    # int() function to convert cash amount from string to integer
        previous_cash = int(cash_on_hand[day-1][1])
        
    # Checks if the cash amount on the current day is less than the
    # cash amount on the previous day.
        if current_cash < previous_cash:

    # If there is a cash deficit, the current day's index (day) is added to
    # the deficit_days_list list to keep track of the days with deficits.
            deficit_days_list.append(day)

    # Calculates the deficit by subtracting the current day's cash amount from
    # the previous day's cash amount.
    # Assign to deficit variable
            deficit = previous_cash - current_cash

    # Retrieves the day number of the current deficit day from the cash_on_hand list
    # The day number is stored in the first column (index 0) of each day's data list
    # int() function to convert day number from string to integer
    # Assign to deficit_day variable
            deficit_day = int(cash_on_hand[day][0])

    # Appends a formatted string stating the deficit day and its
    # corresponding deficit amount in USD to the output variable.
            output += (f"\n[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}")

    # Checks if the cash amount on the current day is more than or equal to the
    # cash amount on the previous day.
        else:

            # If so, calculate the surplus by subtracting the previous day's cash amount from the 
            # current day's cash amount
            # Assign to variable surplus
            surplus = current_cash - previous_cash

            # Check if the surplus amount is higher than the current highest surplus amount
            if surplus > highest_surplus:
            
            # highest_surplus will store the new updated highest surplus amount
                highest_surplus = surplus

            # surplus_day will store the day with the highest surplus
            # The day number is stored in the first column (index 0) of each day's data list
            # int() function to convert day number from string to integer
                surplus_day = int(cash_on_hand[day][0]) 
    
    # If the deficit_days_list list is empty, the following code will be executed.
    if not deficit_days_list:
    
    # Appends a formatted string that indicates that all the cash amounts on each
    # day are higher than the previous day to the output variable.
        output += (f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    # Appends a formatted string stating the highest surplus day and the amount of the highest
    # cash surplus in USD to the output variable.
        output += (f"\n[HIGHEST CASH SURPLUS] DAY: {surplus_day}, AMOUNT: USD{highest_surplus}")
   
    # Open the "summary_report.txt" file in "append" mode for writing with UTF-8 encoding
    with fp_write.open(mode="a", encoding="UTF-8") as summary_file:
       
        # Write the contents of the 'output' variable to the file
        summary_file.write(output)

    # Function returns the final output variable, which contains either the summary report
    # of cash deficits or the highest cash surplus
    return output