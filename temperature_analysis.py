Task 1: Find Maximum and Minimum

temperatures = [28, 32, 35, 29, 31, 27, 30]

highest = temperatures[0]
lowest = temperatures[0]
for temp in temperatures:
  if temp > highest:
    highest = temp
  if temp < lowest:
      lowest = temp
print("the highest temperature is:", highest, "°C")
print("the lowest temperature is:", lowest, "°C")

Task 2: Count Hot Days

temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_days = 0
for temp in temperatures:
  if temp <= 30:
    continue
  hot_days += 1
print("the hot days (>30°C):", hot_days)


Task 3: Alert System

temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0

for day, temp in enumerate(temperatures, start=1):

    if temp >= 40:
        print("Hot Days before alert:", hot_days)
        print("Alert! Extreme temperature 40°C detected on Day", day)
        break

    if temp > 30:
        hot_days += 1
