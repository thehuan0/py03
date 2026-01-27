#!/usr/bin/env python3
"""
This module manages player inventories using nested dictionaries.
It demonstrates inventory transactions, value calculations, and analytics.
"""


def ft_inventory_system() -> None:
    """
    Manage and analyze player inventory systems.

    Features:
    - Nested dictionary structure for inventory data
    - Item transactions between players
    - Inventory value and category calculations
    - Analytics for richest player and rare items
    """
    print("=== Player Inventory System ===\n")
    inventories = {
        'alice': {
            'sword': {
                'qty': 1, 'type': 'weapon', 'rty': 'rare', 'value': 500},
            'potion': {
                'qty': 5, 'type': 'consumable', 'rty': 'common', 'value': 50},
            'shield': {
                'qty': 1, 'type': 'armor', 'rty': 'common', 'value': 200}
        },
        'bob': {
            'potion': {
                'qty': 0, 'type': 'consumable', 'rty': 'common', 'value': 50},
            'magic_ring': {
                'qty': 1, 'type': 'accesory', 'rty': 'rare', 'value': 400}
        }}

    print("=== Alice's Inventory ===")
    inventory_value = 0
    item_count = 0
    categories = dict()

    for item, info in inventories['alice'].items():
        item_total = info['qty'] * info['value']
        inventory_value += item_total
        item_count += info['qty']

        cat = info['type']
        categories[cat] = categories.get(cat, 0) + info['qty']

        print(
            f"{item} ({info['type']}, {info['rty']}): "
            f"{info['qty']}x @ {info['value']} gold each = {item_total} gold"
        )

    print(f"Inventory value: {inventory_value} gold")
    print(f"Item count: {item_count} items")

    print("Categories:", end=" ")
    for cat, count in categories.items():
        print(f"{cat}({count})", end=", ")
    print("\n")

    print("=== Transaction: Alice gives Bob 2 potions ===")
    if inventories['alice']['potion']['qty'] >= 2:
        inventories['alice']['potion']['qty'] -= 2
        inventories['bob']['potion']['qty'] += 2
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("\n=== Updated Inventories ===")
    print("Alice potions:", inventories['alice']['potion']['qty'])
    print("Bob potions:", inventories['bob']['potion']['qty'])

    print("\n=== Inventory Analytics ===")
    richest_player = ""
    richest_value = 0

    most_items_player = ""
    most_items = 0

    rare_items = dict()

    for player, inventory in inventories.items():
        total_value = 0
        total_items = 0

        for item, info in inventory.items():
            total_value += info['qty'] * info['value']
            total_items += info['qty']

            if info['rty'] == 'rare':
                rare_items[item] = rare_items.get(item, 0) + info['qty']

        if total_value > richest_value:
            richest_value = total_value
            richest_player = player

        if total_items > most_items:
            most_items = total_items
            most_items_player = player

    print(
        f"Most valuable player: "
        f"{richest_player.capitalize()} ({richest_value} gold)"
    )
    print(f"Most items: {most_items_player.capitalize()} ({most_items} items)")

    print("Rarest items:", end=" ")
    for item in rare_items.keys():
        print(item, end=", ")
    print()


if __name__ == "__main__":
    ft_inventory_system()
