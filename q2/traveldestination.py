destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

print("All destinations:")
for place in destinations:
    print(place)

print("Sliced destinations (index 1 to 3):")
print(destinations[1:4])

search_place = input("Enter a destination to search for: ")
if search_place in destinations:
    print(f"{search_place} exists in the list.")
else:
    print(f"{search_place} does not exist in the list.")

destinations[2] = "Iloilo"

print("Updated destinations:")
print(destinations)
