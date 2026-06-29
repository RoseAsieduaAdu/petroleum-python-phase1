# oil Production Calculator
# Phase 1 - Week 1


# Well information
well_name = "Rose-1"
field_name = "Tano Basin"


# Production data 
oil_rate = 850        # barrels per day (bopd)
water_rate = 120      # barrels per day (bwpd)
gas_rate = 1200       # standards of cubic feet per day (scfd)
oil_price = 85.50      # USD per barrel


# Calculation
total_fluid= oil_rate + water_rate
water_cut = (water_rate / total_fluid) * 100
daily_revenue = oil_rate * oil_price
monthly_revenue = daily_revenue * 30


# Results 
print("===Well Production Report ===")
print("Well Name:", well_name)
print("Field Name:", field_name)
print("Oil Rate:", oil_rate, "bopd")
print("Water Cut:", round(water_cut, 2), "%")
print("Daily Revenue:$", daily_revenue,)
print("Monthly Revenue: $", monthly_revenue)