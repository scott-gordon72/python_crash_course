def make_sandwich(*items):
    """Make a sandwich"""
    print("Making a sandwich")
    print("Items:")
    for item in items:
        print(f"- {item}")

# Make three sandwiches with different items.
make_sandwich('ham', 'cheese', 'bacon')
make_sandwich('tuna', 'lettuce', 'tomato', 'onion')
make_sandwich('roast beef', 'au jus', 'hot mustard')

