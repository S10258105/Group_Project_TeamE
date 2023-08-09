# Import the Path class from the pathlib module
from pathlib import Path

# Import the csv module for handling CSV files
import csv

def profitloss_function():
    """
    - Function calculates net profit deficits for each day with a deficit. 
      In cases where there are no deficit days, it calculates the highest net profit surplus.
    - No parameters required
    - Function reads data from Profit_and_Loss.csv file
    """

    # Creates the file path to the "Profit_and_Loss.csv" file located in the "csv_reports"
    # directory relative to the current working directory.
    # Assign to variable fp_read
    fp_read = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"

    # Creates the file path to the "summary_report.txt" file located in the
    # current working directory
    # Assign to variable fp_write
    fp_write = Path.cwd()/"summary_report.txt"

    # read the Profit_and_Loss.csv file with UTF-8 encoding
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # creates a csv.reader object named reader that reads data from the opened file
        reader = csv.reader(file)

        # Skip header (first row of the CSV file)
        next(reader)

        # Creates an empty lists to store the day number and net profit
        net_profit=[]

        # Loop iterates over each row of data in the reader object
        # Variable row represents a single row of data from the CSV file
        for row in reader:
       
        # Get the day and net profit values and append them to net_profit list
            net_profit.append([row[0], row[4]])

    # Creates an empty list called deficit_days_list.
    # List will store the indices of days where there is a profit deficit.
    deficit_days_list = []

    # Initialize a variable highest_surplus to keep track of the highest net profit surplus
    highest_surplus = 0

    # Initialize an empty string variable named output to store the summary report generated
    # based on net profit deficits or the highest net profit surplus
    output = ""

    # Loop will iterate over the range of days (from day 1 to the total number of days)
    # in the net_profit list.
    for day in range(1, len(net_profit)):
   
    # Retrieves the net profit amount on the current day from the net_profit list and
    # assign to current_profit variable
    # The net profit amount is stored in the second column (index 1) of each day's data list
    # int() function to convert profit amount from string to integer
        current_profit = int(net_profit[day][1])

    # Retrieves the net profit amount on the previous day from the net_profit list and
    # assign to previous_profit variable
    # int() function to convert profit amount from string to integer
        previous_profit = int(net_profit[day-1][1])

    # Checks if the net profit amount on the current day is less than the
    # net profit amount on the previous day.
        if current_profit < previous_profit:
 
    # If there is a net profit deficit, the current day's index (day) is added to
    # the deficit_days_list list to keep track of the days with deficits.
            deficit_days_list.append(day)

    # Calculates the deficit by subtracting the current day's net profit amount from
    # the previous day's net profit.
    # Assign to deficit variable
            deficit = previous_profit - current_profit

    # Retrieves the day number of the current deficit day from the net_profit list
    # The day number is stored in the first column (index 0) of each day's data list
    # int() function to convert day number from string to integer
    # Assign to deficit_day variable
            deficit_day = int(net_profit[day][0])

    # Appends a formatted string stating the deficit day and its
    # corresponding deficit amount in USD to the output variable.
            output += (f"\n[PROFIT DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}")

    # Checks if the net profit on the current day is more than or equal to the
    # net profit on the previous day.
        else:

            # If so, calculate the surplus by subtracting the previous day's net profit from the 
            # current day's net profit
            surplus = current_profit - previous_profit

            # Check if the surplus amount is higher than the current highest surplus amount
            if surplus > highest_surplus:
            
            # highest_surplus variable will store the new updated highest surplus amount
                highest_surplus = surplus

            # surplus_day will store the day with the highest surplus
            # The day number is stored in the first column (index 0) of each day's data list
            # int() function to convert day number from string to integer
                surplus_day = int(net_profit[day][0]) 
    
    # If the deficit_days_list list is empty, the following code will be executed.
    if not deficit_days_list:
    
    # Appends a formatted string that indicates that all the net profit on each
    # day is higher than the previous day to the output variable.
        output += (f"\n[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    # Appends a formatted string stating the highest surplus day and the amount of the highest
    # net profit surplus in USD to the output variable.
        output += (f"\n[HIGHEST NET PROFIT SURPLUS] DAY: {surplus_day}, AMOUNT: USD{highest_surplus}")
   
    # Open the "summary_report.txt" file in "append" mode for writing with UTF-8 encoding
    with fp_write.open(mode="a", encoding="UTF-8") as summary_file:
       
        # Write the contents of the 'output' variable to the file
        summary_file.write(output)

    # Function returns the final output variable, which contains either the summary report
    # of net profit deficits or the highest net profit surplus
    return output
 
 