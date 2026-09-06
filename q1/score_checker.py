score = int(input("Enter student score: "))
if score < 0 or score > 100:
  print("Invalid score.")
  exit()
if 90 <= score <= 100:
    print("Outstanding")
elif 80 <= score <= 89:
    print("Very Satisfactory")
elif 75 <= score <= 79:
    print("Satisfactory")
else:
    print("Needs Improvement")
