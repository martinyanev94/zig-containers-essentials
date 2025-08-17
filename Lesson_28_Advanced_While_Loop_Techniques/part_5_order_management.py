def get_order_details():
    order_id = input("Enter order ID: ")
    amount = float(input("Enter order amount: "))
    return order_id, amount

orders = []
while True:
    details = get_order_details()
    orders.append(details)
    more = input("Would you like to add another order? (y/n): ")
    if more.lower() != 'y':
        break

print("Order Summary:")
for order in orders:
    print(f"Order ID: {order[0]}, Amount: ${order[1]:.2f}")
