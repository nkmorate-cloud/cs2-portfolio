def show_table(number):
    for i in range(1, 11): 
        result = number * i
        print(f"{number} x {i} = {result}") 
# this part is where i is used as a placeholder to loop variables

user = int(input("Enter a number: "))

# call the function and pass the inputed number as an argument 
show_table(user)
