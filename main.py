# imports the three modules named cash_on_hand, profit_loss, and overheads
import cash_on_hand, profit_loss, overheads

def main():
    """
    - Function executes all 3 functions in the three modules
    - No parameters required

    """

    # calls the overhead_function() from the overheads module
    # Execute the function to calculate and write the highest overhead to a summary report.
    overheads.overhead_function()

    # calls the coh_function() from the cash_on_hand module
    # Execute the function to calculate and write the cash deficits or highest surplus to summary report
    cash_on_hand.coh_function()

    # calls the profitloss_function() from the profit_loss module
    # Execute the function to calculate and write the net profit deficits or highest surplus to summary report
    profit_loss.profitloss_function()

# initiates the execution of the tasks specified in the overhead_function, 
# coh_function, and profitloss_function
main()