def total(price, quantity):
    """Calculates and returns the total purchase cost."""
    return price * quantity


def change(payment, total):
    """Calculates and returns the amount of change or shortage."""
    return payment - total


def total(price, quantity):
    """Calculates and returns the total purchase cost."""
    return price * quantity


def change(payment, total):
    """Calculates and returns the amount of change or shortage."""
    return payment - total


def totalprice(price, quantity):
    """Calculates and returns the total purchase cost."""
    return price * quantity


def totalchange(payment, total):
    """Calculates and returns the amount of change or shortage."""
    return payment - total


def main():
  
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity purchased: "))
    payment = float(input("Enter the amount paid: "))
    
   
    totalprice = total(price, quantity)
    
    balance = change(payment, totalprice)
    
    print(f"\nTotal Cost: {totalprice:.2f}")
    
    if balance >= 0:
        print(f"Customer's Change: {balance:.2f}")
    else:
        shortage = abs(balance)
        print(f"Insufficient payment! Additional amount needed: {shortage:.2f}")

main()

