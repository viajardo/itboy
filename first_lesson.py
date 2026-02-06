# first_lesson.py
# Simple business script to calculate Net Profit after tax for a list of sales figures.
# Detailed comments explain each variable, list, and the loop logic.

# tax_rate: the percentage of each sale taken as tax (decimal form).
# Example: 0.18 means 18% tax.
from typing import List

tax_rate: float = 0.18

# sales: a list of individual sale amounts (floats).
# Each element represents revenue from one transaction (or day, product, etc).
# Example values are included; change these to match your own data.
sales: List[float] = [1200.00, 800.00, 300.00]

# total_sales: accumulator variable to hold the running total of all sales.
# Start at 0.0 because before processing the list we haven't added anything.
total_sales: float = 0.0

# total_tax: accumulator variable to hold the running total of tax computed for each sale.
# We compute tax per sale and add it to this accumulator so we can see the total tax.
total_tax: float = 0.0

# Loop through each sale in the sales list.
# The loop reads the list from left to right. For each 'sale' value:
#  - We add it to the running total_sales.
#  - We calculate the tax for that single sale (sale * tax_rate).
#  - We add that per-sale tax to the running total_tax.
for sale in sales:
    # 'sale' is a single number from the list (for example, 1200.0).
    # Add the current sale to the running total of sales.
    total_sales += sale  # same as: total_sales = total_sales + sale

    # Calculate tax for this single sale.
    # Multiplying each sale by tax_rate gives tax owed for this sale.
tax_for_sale = sale * tax_rate

    # Add the per-sale tax to the running total tax.
    total_tax += tax_for_sale  # same as: total_tax = total_tax + tax_for_sale

    # (Optional) You could print per-sale details inside the loop to inspect flow:
    # print(f"Processed sale={{sale:.2f}}, tax_for_sale={{tax_for_sale:.2f}}, running_total_sales={{total_sales:.2f}}")

# After the loop completes:
# total_sales now holds the sum of all sales in the list.
# total_tax now holds the sum of tax calculated for each sale.
# Net profit after tax: what remains after paying tax on the total sales.
# Here we define net_profit = total_sales - total_tax
net_profit: float = total_sales - total_tax

# Print summary results, formatted to two decimal places for clarity and aligned columns for readability.
print("Business Summary:")
print(f"  Total sales:      ${{total_sales:10.2f}}")
print(f"  Total tax:        ${{total_tax:10.2f}}  (tax rate = {{tax_rate:.1%}})")
print(f"  Net profit (after tax): ${{net_profit:10.2f}}")

# Notes and learning points:
# - Using accumulators (total_sales and total_tax) is a common pattern:
#   you initialize at 0 and update them inside a loop.
# - We compute tax per-sale and accumulate it. Doing per-sale tax can be important
#   if different sales had different tax rules or rounding per transaction was needed.
#   For a simple flat tax, you could also compute tax once as total_sales * tax_rate.
# - The loop variable 'sale' does not change the original list; it is just the current value.
# - Negative values in sales (like returns or refunds) reduce total_sales and therefore reduce tax and net profit accordingly.

# Quiz (one logic-based question):
# Suppose sales = [1200.00, 800.00, -200.00] and tax_rate = 0.18.
# Walk through how the loop changes total_sales and total_tax step-by-step and then compute the final net_profit.
# When you run the script, paste the printed output here and your answer to the quiz question — I'll check your reasoning and correct any misconceptions.