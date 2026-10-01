room_prices = [2500, 1800, 3200, 2500, 4500, 2100, 3200, 1500]

# total revenue 
total_revenue = sum(room_prices)
# average revenue
average_revenue = total_revenue / len(room_prices)
# maximum revenue
max_revenue = max(room_prices)
# minimum revenue
min_revenue = min(room_prices)
# no of revenue with revenue greater than 2500
revenue_greater_than_2500 = []
for room_price in room_prices:
    if room_price > 2500:
        revenue_greater_than_2500.append(room_price)
print(revenue_greater_than_2500)
# no of revenue with revenue exactly 2500
revenue_exactly_2500 = []
for room_price in room_prices:
    if room_price == 2500:
        revenue_exactly_2500.append(room_price)
print(revenue_exactly_2500)
# no of revenue with revenue less than 2500
revenue_less_than_2500 = []
for room_price in room_prices:
    if room_price < 2500:
        revenue_less_than_2500.append(room_price)
print(revenue_less_than_2500)

premium_revenue = revenue_greater_than_2500

# Increment by 10% for premium revenue
increased_prices = []
for each_price in premium_revenue:
    increased_prices.append(each_price * 1.10)


# finding duplicates in the list
room_prices = [2500, 1800, 3200, 2500, 4500, 2100, 3200, 1500]

not_duplicates = []
for each_price in room_prices:
    if each_price not in not_duplicates:
        not_duplicates.append(each_price)
print(not_duplicates)

new_room_prices = [price for price in room_prices if room_prices.count(price) == 1]

