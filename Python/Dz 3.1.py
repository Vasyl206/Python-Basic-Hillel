seconds = int(input("Введіть число від 0 і до 8640000: "))

minut, sec = divmod(seconds, 60)
hour, minut = divmod(minut, 60)
day, hour = divmod(hour, 24)

if day % 10 == 1 and day % 100 != 11:
    day_str = f"{day} день"
elif 2 <= day % 10 <= 4 and (day % 100 < 10 or day % 100 >= 20):
    day_str = f"{day} дні"
else:
    day_str = f"{day} днів"

print(f"{day_str} {hour:02}:{minut:02}:{sec:02}")