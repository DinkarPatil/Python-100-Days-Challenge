from prettytable import PrettyTable

table = PrettyTable()

# Calling an method

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Calling an attribute
# table.align = "r"

print(table)