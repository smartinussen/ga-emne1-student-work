import encodings

from pathlib import Path as P

print(f"Current dir is: {P.cwd()}")


data_dir = P("../data") # alternativt p("..") / "data"
prices = data_dir / "prices.txt"

print(data_dir.exists())
print(prices.exists())
####
with open(prices, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
#####
read_prices = []
with open(prices, "r", encoding="utf-8") as file:
    for line in file:
        price = float(line.strip())
        read_prices.append(price)

print(read_prices)
print(sorted(read_prices))
print(sum(read_prices))
print(min(read_prices))
print(max(read_prices))

report = data_dir / "price_report.txt"

# Replace existing content
with open(report, "w", encoding="utf-8") as file:
    file.write("First line\n")

# Append to to file
with open(report, "a", encoding="utf-8") as file:
    file.write("Second line\n")

report_lines = [
    "Item: Epler",
    "Amount: 20",
    "Price: 96.50"
]

with open(report, "w", encoding="utf-8") as file:
    for line in report_lines:
        file.write(line + "\n")

with open(report, "a", encoding="utf-8") as file:
    file.write("HUSK: Hør med alle om de skal ha noe")
