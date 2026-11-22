
DAYS_IN_WEEK: int = 7

day: int = int(input("Day: "))

days_to_wait: int = int(input("Days to wait: "))

# Calculate delivery day
delivery_day: int = day + days_to_wait

# Check if delivery day exceeds 7
if delivery_day > DAYS_IN_WEEK:
    delivery_day -= DAYS_IN_WEEK

print("Delivery day:", delivery_day)

assert 1 <= delivery_day <= DAYS_IN_WEEK
