def register():
    SECTIONS = ["Dahlia", "Rosal", "Ilang Ilang", "Sampaguita"]  
    CLUBS = ["Robotics", "Science", "Mathematics", "Programming"]
    ATTENDANCE = ["Present", "Absent", "Late"]

    name = input("Enter Student Name: ").strip()
    if not name:
        print("Error: Student name is required.")
        exit()

    section = input("Enter Section: ").strip()
    if section not in SECTIONS:
        print("Error: Please choose a valid section.")
        exit()

    club = input("Enter Club Choice: ").strip()
    if club not in CLUBS:
        print("Error: Please choose a valid club.")
        exit()

    email = input("Enter School Email: ").strip()
    if "@" not in email:
        print("Error: Invalid email format. Missing '@'.")
        exit()

    attendance = input("Enter Attendance Status (Present/Absent/Late): ").strip()
    if attendance not in ATTENDANCE:
        print("Error: Invalid attendance status.")
        exit()

    print("\nREGISTRATION ACCEPTED")
    print("---------------------")
    print(f"Student: {name}")
    print(f"Section: {section}")
    print(f"Club: {club}")
    print(f"Email: {email}")
    print(f"Attendance: {attendance}")

register()
