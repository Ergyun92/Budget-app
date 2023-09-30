class Category:
    def __init__(self, category_name):
        self.ledger = []
        self.category = category_name
        
        
    def __str__(self):
        category = self.category
        title = category.center(30, '*') + '\n'
        for i in self.ledger:
            title += f"{i['description'][:23].ljust(23)}" + "{:.2f}".format(i['amount']).rjust(7) + "\n"
        total = self.get_balance()
        title += "Total: " + "{:.2f}".format(total)
        return title


    def deposit(self, amount, description=""):
        self.ledger.append({'amount': (amount), 'description': (description)})


    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -(amount), 'description': (description)})
            return True
        return False


    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance


    def transfer(self, amount, transfer_to):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {transfer_to.category}")
            transfer_to.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False


    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    name = []
    budget = []
    percentage = []

    for category in categories:
        total = 0
        for i in category.ledger:
            if i['amount'] < 0:
                total -= i['amount']
        budget.append(round(total, 2))
        name.append(category.category)

    for amount in budget:
        tot_spent = sum(budget)
        percentage.append(round(amount / tot_spent, 2) * 100)

    spend_chart = 'Percentage spent by category' + '\n'
    labels = range(100, -10, -10)

    for label in labels:
        spend_chart += str(label).rjust(3) + "| "
        for percent in percentage:
            if percent >= label:
                spend_chart += 'o  '
            else:
                spend_chart += '   '
        spend_chart += '\n'

    spend_chart += "    ----" + ("---" * (len(name) - 1))
    spend_chart += '\n     '

    spacing = 0
    for n in name:
        if spacing < len(n):
            spacing = len(n)

    for i in range(spacing):
        for n in name:
            if len(n) > i:
                spend_chart += n[i] + '  '
            else:
                spend_chart += '   '
        if i < spacing - 1:
            spend_chart += '\n     '

    return (spend_chart)