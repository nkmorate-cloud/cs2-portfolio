# Function to compute the verage of the three scores
def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

# This is to determine the performance category based on the average
def get_performance(average):
    if 85 <= average <= 100:
        return "Mastery"
    elif 70 <= average < 85:
        return "Developing"
    else:
        return "Needs Review"

# Function to check if the student meets the eligibility criteria
def is_eligible(average, completed_tasks):
    if average >= 85 and completed_tasks >= 3:
        return True
    else:
        return False

score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
completed_tasks = int(input("Completed Tasks: "))

avg = calculate_average(score1, score2, score3)
perf_category = get_performance(avg)
eligibility = is_eligible(avg, completed_tasks)

print(f"\nAverage: {avg:.2f}")
print(f"Performance: {perf_category}")
print(f"Eligible for Challenge: {eligibility}")


#    calculate_average() returns a float (numerical average).
#    get_performance() returns a string ("Mastery", "Developing", or "Needs Review").
#    is_eligible() returns a Boolean (True or False).

# In the main program, calculate_average() computes the average and sends it back using the 'return' statement. That returned value is stored in a variable (e.g., 'avg'), which is then passed inside the parentheses as an argument when calling get_performance(avg).

# The is_eligible() function will return False because both conditions (average >= 85 AND completed_tasks >= 3) must be True for the student to be eligible.

# Using 'return' sends the data back to the program so it can be stored in variables and reused in other functions. If the function only printed the result, the value would just appear on the screen and could not be used for further calculations or logic.
