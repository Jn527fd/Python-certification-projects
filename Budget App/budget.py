class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if amount <= self.get_balance():
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return sum(item["amount"] for item in self.ledger)

  def transfer(self, amount, budget_category):
    if amount <= self.get_balance():
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  def __str__(self):
    #> right aligned, ^ center aligned
    #.2f contains two decimal points
    #[:23] first 23 characters
    title = f"{self.category:*^30}\n"
    items = ""
    for item in self.ledger:
      items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
    total = f"Total: {self.get_balance():.2f}"
    return title + items + total


def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  spendings = []
  total_amount = 0

  # Calculate percentage spent for each category
  for category in categories:
    total_amount += sum(item["amount"] for item in category.ledger
                        if item["amount"] < 0)

    spending_per_category = sum(item["amount"] for item in category.ledger
                                if item["amount"] < 0)

    spendings.append(spending_per_category)

  # print(spendings)
  # print(total_amount)

  for i, spending in enumerate(spendings):
    percentage = (spending / total_amount) * 100
    spendings[i] = int((percentage // 10) * 10)

  print(spendings)

  # Create the main body of the chart
  for i in range(100, -1, -10):
    chart += f"{i:3}| "
    for spending in spendings:
      chart += "o  " if spending >= i else "   "
    chart += "\n"

  # Add a horizontal line below the main body
  chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

  # Add category names below the horizontal line
  max_len = max(len(category.category) for category in categories)
  for i in range(max_len):
    chart += "     "
    for category in categories:
      chart += category.category[i] if i < len(category.category) else " "
      chart += "  "
    if i < max_len - 1:
      chart += "\n"
    else:
      chart += ""
  
  return chart


# Example usage:
# categories = [Category("Food"), Category("Clothing"), Category("Entertainment")]
# print(create_spend_chart(categories))
