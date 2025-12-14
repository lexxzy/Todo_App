Date = input("Enter the date (YYYY-MM-DD): ")
Mood = input("How are you feeling today from 1 to 10?" )
Note = input("Write your journal entry: ")
with open(f"journal/{Date}.txt", "w") as file:
     file.writelines(f"Mood: {Mood}\n")
     file.writelines(f"Note: {Note}\n")