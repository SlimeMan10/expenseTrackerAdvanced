# Categories: food, transport, shopping, entertainment, travel, technology, social
class Tracker:

    # Initialize with a default budget of 1000 (whole number)
    def __init__(self, budget=1000):
        if not isinstance(budget, int) or budget <= 0:
            raise ValueError("Budget must be a positive whole number.")
        self.budget = budget
        self.amount_spent = 0
        self.categories = {
            "food": [],
            "transport": [],
            "shopping": [],
            "entertainment": [],
            "travel": [],
            "technology": []
        }
    
    def sizeOfCategory(self, category):
        return len(self.categories[category])
    
    def remove_expense(self, category, place):
        items = self.categories[category]
        item = items[place]
        cost = item['Cost']
        self.amount_spent -= float(cost)
        del items[place]
        
        
    def printAll(self):
        """Print all expenses in all categories."""
        for category in self.categories:
            print(f"Category: {category.capitalize()}")
            self.printCategory(category)
            print()  # Add spacing between categories

    def printCategory(self, category):
        # Get the list of items for the given category
        items = self.categories[category]
        if not items:
            print("  Nothing in this category.")
        else:
            for i, item in enumerate(items, 1):  # Enumerate for numbering
                if isinstance(item, dict):  # Ensure the item is a dictionary
                    key = item.get("Item", "Unknown")
                    value = item.get("Cost", "Unknown")
                    print(f"  {i}. {key}: ${value}")
                else:
                    print(f"  {i}. Malformed item: {item}")

    def setNewBudget(self, number):
        self.budget = number
        print(f"Budget updated to ${self.budget}")

    def add_expense(self, category, item, price):
        """Add an expense to a category."""
        # Check if expense exceeds budget
        if price + self.amount_spent > self.budget:
            print("Exceeds budget! Cannot add this expense.")
            return

        # Check if category is valid
        if category not in self.categories:
            print(f"Invalid category '{category}'. Please choose a valid category.")
            return

        # Add expense
        self.amount_spent += price
        lowerCaseItem = item.lower()
        self.categories[category].append({"Item": lowerCaseItem, "Cost": price})
        print(f"Added '{item}' (${price}) to category '{category}'.")

    def getBudget(self):
        return self.budget
    
    def getRemainingBudget(self):
        return self.budget - self.amount_spent
    
