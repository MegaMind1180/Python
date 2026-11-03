import sys


def main():
    print("=== Inventory System Analysis ===")
    inventory = {}

    args = sys.argv[1:]
    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":", 1)
        name, qty_str = parts[0], parts[1]

        try:
            qty = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        if qty < 0:
            print(f"Error - invalid quantity for '{name}'")
            continue

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        inventory[name] = qty

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for name, qty in inventory.items():
        pct = (qty / total_qty) * 100
        print(f"Item {name} represents {pct:.1f}%")

    most_item = None
    most_qty = -1
    least_item = None
    least_qty = float("inf")

    for name, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_item = name
        if qty < least_qty:
            least_qty = qty
            least_item = name

    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
