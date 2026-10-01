room_prices = [2500, 1800, 3200, 2500, 4500, 2100, 3200, 1500]

total_revenue = sum(room_prices)
average_revenue = total_revenue / len(room_prices)

above_avg = []
for each_price in room_prices:
    if each_price > average_revenue:
        above_avg.append(each_price)

# percentage of avg prices
percent_abv_avg = (len(above_avg)/ len(room_prices)) * 100

# values equal to 2500
vals = [price for price in room_prices if price == 2500]


# percentage of prices below average
below_avg = []
for each_price in room_prices:
    if each_price < average_revenue:
        below_avg.append(each_price)

# percentage of prices below average
percent_blw_avg = (len(below_avg)/ len(room_prices)) * 100

# difference from avg
avg_diff = []
for each_price in room_prices:
    avg_diff.append(each_price - average_revenue)

# percent from dif

per_from_diff = []

for each_price in room_prices:
    value = ((each_price - average_revenue) / average_revenue)* 100 
    per_from_diff.append(value)

# displaying the results
print(f"Total revenue: {total_revenue}")
print(f"Average revenue: {average_revenue}")
print(f"Number of prices above average: {len(above_avg)}")
print(f"Percentage of prices above average: {percent_abv_avg:.2f}%")
print(f"Number of prices below average: {len(below_avg)}")
print(f"Percentage of prices below average: {percent_blw_avg:.2f}%")
print(f"prices equal to 2500: {vals}")
print(f"Difference from average for each price: {avg_diff}")
print(f"Difference from percent : {per_from_diff}")
