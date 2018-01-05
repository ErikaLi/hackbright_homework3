MELON_COST = 1.00

def find_underpaid_overpaid_customers(melon_cost, quantity, customer_paid, customer_name):
    """Calculate cost of melons and determine who has underpaid."""
    customer_expected = quantity * melon_cost
    if customer_expected != customer_paid:
        print customer_name, "paid {:.2f}, expected {:.2f}".format(
            customer_paid, customer_expected)

# create a variable and assign a path to the file
path = "/home/user/Desktop/underpaid-customers/customer-orders.txt"
# open the file
order_file = open(path)

# iterates over lines in file
for line in order_file:
    # for each line, remove new line
    line = line.rstrip()
    # for each line. split by |
    words = line.split("|")
    # get the full name at index 1
    customer_name = words[1]
    # get number of melons and payment amount and turn the string into float
    quantity = float(words[2])
    customer_paid = float(words[3])
    # call the function to see if customer is underpaid or overpaid
    find_underpaid_overpaid_customers(MELON_COST, quantity, customer_paid, customer_name)

order_file.close()

