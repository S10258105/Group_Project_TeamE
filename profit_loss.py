from pathlib import Path
import csv

def profitloss_function():
    """
    - Function calculates either net profit deficit or highest net profit surplus
    - No parameters required

    """

    # creates the file path to the "Profit_and_Loiss.csv" file located in the "csv_reports"
    # directory relative to the current working directory.
    file_read = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"

    # creates the file path to the "summary_report.txt" file located in the
    # current working directory
    fp_write = Path.cwd()/"summary_report.txt"

    # read the Profit_and_Loss.csv file with UTF-8 encoding
    with file_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # creates a csv.reader object named reader that reads data from the opened file
        reader = csv.reader(file)

        # skip header (first row of the CSV file)
        next(reader)

        # create an empty lists to store the day numvber and net profit
        net_profit=[]

        # loop iterates over each row of data in the reader object
        # variable row represents a single row of data from the CSV file
        for row in reader:
       
        # get the day and net profit values and append them to cash_on_hand list
            net_profit.append([row[0], row[4]])

    # creates an empty list called deficit_days.
    # list will store the indices of days where there is a profit deficit.
    deficit_days = []

    # loop will iterate over the range of days (from day 1 to the total number of days)
    # in the net_profit list.
    for day in range(1, len(net_profit)):
   
    # Retrieves the net profit amount on the current day from the net_profit list and
    # assign to current_profit variable
    # The net profit amount is stored in the second column (index 1) of each row (day)
    # int() function to convert profit amount from string to integer
        current_profit = int(net_profit[day][1])

    # Retrieves the net profit amount on the previous day from the net_profit list and
    # assign to previouos_profit variable
    # int() function to convert profit amount from string to integer
        previous_profit = int(net_profit[day-1][1])

    # Checks if the net profit amount on the current day is less than or equal to the
    # net profit amount on the previous day.
        if current_profit <= previous_profit:
 
    # If there is a net profit deficit, the current day's index (day) is added to
    # the deficit_days list to keep track of the days with deficits.
            deficit_days.append(day)

    # Initializes an empty string output to store the summary report generated
    # based on the deficit days or the highest net profit surplus.
    output = ""

    # Checks if the deficit_days list is not empty.
    # If it contains deficit days, the code below will be executed.
    if deficit_days:

    # loop will iterate over each day's index in the deficit_days list.
        for day in deficit_days:    

    # Retrieves the profit amount on the current day from the neet_profit list and
    # assign to current_profit variable
    # The profit amount is stored in the second column (index 1) of each row (day)
    # int() function to convert profit amount from string to integer
            current_profit = int(net_profit[day][1])

    # Retrieves the profit amount on the previous day from the net_profit list and
    # assign to previouos_profit variable
    # int() function to convert profit amount from string to integer
            previous_profit = int(net_profit[day-1][1])

    # Calculates the deficit by subtracting the current day's net profit amount from
    # the previous day's net profit.
            deficit = previous_profit - current_profit

    # Retrieves the day number of the current deficit day from the net_profit list
    # The day number is stored in the first column (index 0) of each row (day).
    # int() function to convert day number from string to integer
            deficit_day = int(net_profit[day][0])

    # Appends a formatted string representing the deficit day and its
    # corresponding deficit amount to the output string.
    # The formatted string includes the deficit day number and the deficit amount in USD.
            output += (f"\n[PROFIT DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}")

    #  If the deficit_days list is empty, the following code will be executed.
    else:

    # Initializes variables max_profit and max_day to store the maximum net profit amount
    # and the day number corresponding to the highest profit surplus.
    # The initial values are set to the net profit amount and day number of the first entry
    # in the net_profit list.
        max_profit = float(net_profit[0][1])
        max_day = net_profit[0][0]

    # loop will iterate over each nested list in the net_profit list.
    # variable day represents a nested list that contains the day number and net profit value
        for day in net_profit:

    # Retrieves the net profit amount on the current day from the net_profit list
    # profit amount is stored in the second element (index 1) of the current day's data (nested list)
    # float() function converts profit amount from string to a float.
            profit = float(day[1])

    # Checks if the profit amount on the current day (profit) is greater than the
    # current maximum profit (max_profit).
            if profit > max_profit:

    # If so, max_profit variable will store the new maximum profit amount
                max_profit = profit

    # max_day variable will store the day number associated with the new
    # maximum profit value.
    # day number is stored in the first element (index 0) of the nested list.
                max_day = int(day[0])

    # Calculates the day number of the day before the highest net profit surplus (previous_day).
    # Initialize previous_day_profit to store the net profit amount on the day before
    # the highest net profit surplus.      
        previous_day = int(max_day) - 1
        previous_day_profit = 0

    # loop will iterate over each day's data in the net_profit list.
        for day in net_profit:

    # Checks if the day number of the current day matches previous_day
            if int(day[0]) == previous_day:

    # If a match is found, it updates previous_day_profit with the cash amount on the
    # day before the highest profit surplus.
                previous_day_profit = float(day[1])

    # Once the day before the highest profit surplus is found, its cash amount will be
    # stored in previous_day_profit
    # the loop is exited early using the break statement.
                break
   
    # Calculates the net profit surplus by subtracting the net profit amount on the day before the
    # highest net profit surplus from the highest net profit amount.
        surplus = max_profit - previous_day_profit

    # Appends a string to the output that indicates all the net profits amounts on each
    # day are higher than the previous day.
        output += (f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    # Appends a formatted string representing the day and the amount of the highest
    # net profit surplus to the output.
        output += (f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}")

    # Open the "summary_report.txt" file in "append" mode for writing with UTF-8 encoding
    with fp_write.open(mode="a", encoding="UTF-8") as summary_file:
       
        # Write the contents of the 'output' variable to the file
        summary_file.write(output)

    # function returns the final output string, which contains either the summary report
    # of net profit deficits or the highest net profit surplus
    return output