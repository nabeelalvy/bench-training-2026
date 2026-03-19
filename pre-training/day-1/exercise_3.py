# ======================
# Loops
# ======================


def print_table(multiplier: int):
    print("+----+----+-----+")
    for num in range(1,11):
        print(f"| {multiplier:>2} x {num:>2} = {multiplier * num:>3} |")
    print("+----+----+-----+")

while True:
    try:
        multiplier = int(input("Give me a number between 1 and 12, I will generate it's table: "))
        if 1 <= multiplier <= 12:
            print_table(multiplier)
            break
        else:
            print("Please Try Again!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

print(f"\nNow printing all tables between 1 and 12")
for num in range(1,13):
    print_table(num)


