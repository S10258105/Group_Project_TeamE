from pathlib import Path
import csv

def coh_function():
    """
    - Function calculates either cash deficit or highest cash surplus
    - No parameters required

    """
   
    # creates the file path to the "Cash_on_Hand.csv" file located in the "csv_reports"
    # directory relative to the current working directory.
    fp_read = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

    # creates the file path to the "summary_report.txt" file located in the
    # current working directory
    fp_write = Path.cwd()/"summary_report.txt"

    # read the Cash_on_Hand.csv file with UTF-8 encoding
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:  
        # creates a csv.reader object named reader that reads data from the opened file
        reader = csv.reader(file)
       
    # skip header (first row of the CSV file)
        next(reader)

    # create an empty lists to store the day number and cash on hand records
        cash_on_hand=[]

        # loop iterates over each row of data in the reader object
        # variable row represents a single row of data from the CSV file
        for row in reader:

    # get the day and cash on hand data and append them to cash_on_hand list
            cash_on_hand.append([row[0],row[1]])
   
    # creates an empty list called deficit_days.
    # list will store the indices of days where there is a cash deficit.
    deficit_days = []

    # loop will iterate over the range of days (from day 1 to the total number of days)
    # in the cash_on_hand list.
    for day in range(1, len(cash_on_hand)):

    # Retrieves the cash amount on the current day from the cash_on_hand list and
    # assign to current_cash variable
    # The cash amount is stored in the second column (index 1) of each row (day)
    # int() function to convert cash amount from string to integer
        current_cash = int(cash_on_hand[day][1])

    # Retrieves the cash amount on the previous day from the cash_on_hand list and
    # assign to previouos_cash variable
    # int() function to convert cash amount from string to integer
        previous_cash = int(cash_on_hand[day-1][1])

    # Checks if the cash amount on the current day is less than or equal to the
    # cash amount on the previous day.
        if current_cash <= previous_cash:

    # If there is a cash deficit, the current day's index (day) is added to
    # the deficit_days list to keep track of the days with deficits.
            deficit_days.append(day)
   
    # Initializes an empty string output to store the summary report generated
    # based on the deficit days or the highest cash surplus.
    output = ""

    # Checks if the deficit_days list is not empty.
    # If it contains deficit days, the code below will be executed.
    if deficit_days:

    # loop will iterate over each day's index in the deficit_days list.
        for day in deficit_days:

    # Retrieves the cash amount on the current day from the cash_on_hand list and
    # assign to current_cash variable
    # The cash amount is stored in the second column (index 1) of each row (day)
    # int() function to convert cash amount from string to integer
            current_cash = int(cash_on_hand[day][1])
   
    # Retrieves the cash amount on the previous day from the cash_on_hand list and
    # assign to previouos_cash variable
    # int() function to convert cash amount from string to integer
            previous_cash = int(cash_on_hand[day-1][1])

    # Calculates the deficit by subtracting the current day's cash amount from
    # the previous day's cash amount.
            deficit = previous_cash - current_cash

    # Retrieves the day number of the current deficit day from the cash_on_hand list
    # The day number is stored in the first column (index 0) of each row (day).
    # int() function to convert day number from string to integer
            deficit_day = int(cash_on_hand[day][0])

    # Appends a formatted string representing the deficit day and its
    # corresponding deficit amount to the output string.
    # The formatted string includes the deficit day number and the deficit amount in USD.
            output += (f"\n[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}")

    #  If the deficit_days list is empty, the following code will be executed.
    else:

    # Initializes variables max_cash and max_day to store the maximum cash amount
    # and the day number corresponding to the highest cash surplus.
    # The initial values are set to the cash amount and day number of the first entry
    # in the cash_on_hand list.
        max_cash = float(cash_on_hand[0][1])
        max_day = cash_on_hand[0][0]
   
    # loop will iterate over each nested list in the cash_on_hand list.
    # variable day represents a nested list that contains the day number and cash on hand value
        for day in cash_on_hand:

    # Retrieves the cash amount on the current day from the cash_on_hand list
    # cash amount is stored in the second element (index 1) of the current day's data (nested list)
    # float() function converts cash amount from string to a float.
            cash = float(day[1])

    # Checks if the cash amount on the current day (cash) is greater than the
    # current maximum cash (max_cash).
            if cash > max_cash:

    # If so, max_cash variable will store the new maximum cash amount
                max_cash = cash

    # max_day variable will store the day number associated with the new
    # maximum cash value.
    # day number is stored in the first element (index 0) of the nested list.
                max_day = day[0]

    # Calculates the day number of the day before the highest cash surplus (previous_day).
    # Initialize previous_day_cash to store the cash amount on the day before
    # the highest cash surplus.
        previous_day = int(max_day) - 1
        previous_day_cash = 0
   
    # loop will iterate over each day's data in the cash_on_hand list.
        for day in cash_on_hand:

    # Checks if the day number of the current day matches previous_day
            if int(day[0]) == previous_day:

    # If a match is found, it updates previous_day_cash with the cash amount on the
    # day before the highest cash surplus.
                previous_day_cash = float(day[1])

    # Once the day before the highest cash surplus is found, its cash amount will be
    # stored in previous_day_cash
    # the loop is exited early using the break statement.
                break

    # Calculates the cash surplus by subtracting the cash amount on the day before the
    # highest cash surplus from the highest cash amount.
        surplus = max_cash - previous_day_cash

    # Appends a string to the output that indicates all the cash amounts on each
    # day are higher than the previous day.
        output += (f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    # Appends a formatted string representing the day and the amount of the highest
    # cash surplus to the output.
        output += (f"[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}")
   
    # Open the "summary_report.txt" file in "append" mode for writing with UTF-8 encoding
    with fp_write.open(mode="a", encoding="UTF-8") as summary_file:
       
        # Write the contents of the 'output' variable to the file
        summary_file.write(output)

    # function returns the final output string, which contains either the summary report
    # of cash deficits or the highest cash surplus
    return output