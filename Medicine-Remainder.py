import datetime
import time

print("Medicine Reminder System")

# File to store medicines
file = open("medicines.txt", "a")

n = int(input("How many medicines do you want to add? "))

for i in range(n):
    name = input("Enter medicine name: ")
    med_time = input("Enter time (HH:MM): ")

    file.write(name + "," + med_time + "\n")

file.close()

# Read medicines from file
medicines = []

file = open("medicines.txt", "r")

for line in file:
    name, med_time = line.strip().split(",")
    medicines.append((name, med_time))

file.close()

print("\nReminder started...")

while True:
    now = datetime.datetime.now().strftime("%H:%M")

    for med in medicines:
        if now == med[1]:
            print("\nReminder: Time to take", med[0])

    time.sleep(60)