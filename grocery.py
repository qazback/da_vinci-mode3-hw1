def grocery_list():
    items = {}

    try:
        while True:
            item = input().lower()
            items[item] = items.get(item, 0) + 1
    except EOFError:
        pass

    sorted_items = sorted(items.items(), key=lambda x: x[0])
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    grocery_list()
