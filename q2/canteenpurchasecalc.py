def total(price, quantity):
    """Calculates and returns the total purchase cost."""
    return price * quantity


def change(payment, total):
    """Calculates and returns the amount of change or shortage."""
    return payment - total


def main():
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity purchased: "))
    payment = float(input("Enter the amount paid: "))
   
    total = total(price, quantity)
    
    balance = change(payment, total)
    
  
    print(f"\nTotal Cost: {total:.2f}")
    
    if balance >= 0:
        print(f"Customer's Change: {balance:.2f}")
    else:
      
        shortage = abs(balance)
        print(f"Insufficient payment! Additional amount needed: {shortage:.2f}")

main()
