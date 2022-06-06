class Category:
    # Instantiate objects based on categories
    # Instance variable called ledger that is a list
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    # A deposit method: amount and description. If no description, empty string. Append to ledger list {"amount": amount, "description": description}.
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
    
    # A withdraw method: similar to deposit, amount is negative. If not enough funds, nothing added.Return True if the withdrawal took place, False otherwise.
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else: return False
    
    # A get_balance method: returns current balance based on deposits and withdrawals.
    def get_balance(self):
        self.balance = 0
        for transaction in self.ledger:
            self.balance += transaction['amount']
        return self.balance

    # A transfer method: amount and another budget category. Add withdrawal with amount and description "Transfer to [Destination Budget Category]". Add deposit to category with amount and description "Transfer from [Source Budget Category]". If not enough funds, nothing added. Return True if the transfer took place, and False otherwise.
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination.category)
            destination.deposit(amount, "Transfer from " + self.category)
            return True
        else: return False

    # A check_funds method: amount. Returns False if amount is greater than balance and returns True otherwise. This method should be used by the withdraw method and transfer method.
    def check_funds(self, amount):
        if amount > self.get_balance(): return False
        else: return True

    # Printed budget:
        # A title line of 30 characters where the name of the category is centered in a line of * characters.
        # A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
        # A line displaying the category total.

    def __repr__(self):
        # Centered title in * (30 characters total)
        text = self.category.center(30, "*")
        #List of transactions, 23 character description and 7 character right aligned amount
        total = 0
        for transaction in self.ledger:
            description = transaction["description"]
            amount = round(transaction["amount"], 2)
            text += "\n" + "{:<23}".format(description[:23]) + "{:>7}".format("{:.2f}".format(amount))
            total = total + amount
        # Total
        text += "\nTotal: " + str(total)
        return text

# Function create_spend_chart that takes a list of categories and returns a string that is a bar chart.
def create_spend_chart(categories):
    # Spending per category    
    spend = list()
    # Category name
    catnames = list()
    # Total amount per category, extract names
    for cat in categories:
        total = abs(sum([transaction['amount'] for transaction in cat.ledger if transaction['amount']<0]))
        spend.append(total)
        catnames.append(cat.category)
    # Total spending
    total = sum(spend)
    # Convert to percentages
    for i in range(len(spend)):
        spend[i] = spend[i]/total *100

    # Graphic
    # Title
    graphic = "Percentage spent by category\n"
    # Rows of barchart
    for number in reversed(range(0, 110, 10)):
        # Right aligned numbers (3 characters total), followed by separator
        graphic += "{:>3}".format(str(number)) + "| "
        for i in range(len(spend)):
            # If percentage indicated in the row is reached in the category spending, there should be an "o" to build the bar
            if number <= spend[i]:
                graphic += "o  "
            else:
                graphic += "   "
        graphic += "\n"
    # Seprating line extending 2 past the last category
    graphic += "{:>4}".format("") + "-"*((len(categories)*3)+1)
    # Longest category label defines the height of the axis label
    charheight = len(max(catnames, key=len))
    # Add labels to graphic
    for i in range(charheight):
        graphic += "\n" + "{:>5}".format("")
        for name in catnames:
            if i < len(name):
                graphic += name[i] + "  "
            else:
                graphic += "   "
    # Return graphic
    return graphic
