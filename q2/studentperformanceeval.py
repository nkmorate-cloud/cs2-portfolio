def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


def get_performance(average):
    if 85 <= average <= 100:
        return "Mastery"
    elif 70 <= average < 85:
        return "Developing"
    else:
        return "Needs Review"


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

