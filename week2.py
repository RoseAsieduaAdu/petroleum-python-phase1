# Lesson 2 - If Statements and Loops 
# Well Health Checker 


# Single well data
well_name = "Rose-1"
oil_rate = 850
water_rate = 520


# calculate water cut
total_fluid = oil_rate + water_rate
water_cut = (water_rate / total_fluid) * 100
water_cut = round(water_cut, 2)


print("well:", well_name)
print("water cut:", water_cut, "%")


# check well health
if water_cut > 70:
    print("STATUS: CRITICAL - Well needs immediate attention")
elif water_cut > 50:
    print("STATUS: WARNING - Water cut is getting high")
elif water_cut > 30:
    print("STATUS: Monitor- keep an eye on this well")
else: 
    print("STATUS: GOOD - Well is performing fine")
    

# Multiple wells data
wells = [
    ["Rose-1",  850, 520],
    ["Rose-2",  600,  800],
    ["Rose-3",  1200, 180],
    ["Rose-4",  300,  900],
    ["Rose-5",  950,  400],
]


print("")
print("=== FIELD PRODUCTION REPORT ===")
print("")


# Loop through every well
for well in wells:


    # Extract data 
    name       = well[0]
    oil         = well[1]
    water       = well[2]


    # Calcualte water cut 
    total     = oil + water
    wcut      =round((water/total)*100,2)


    # Check status
    if wcut > 70:
        status = "CRITICAL"
    elif wcut > 50:
        status = "WARNING"
    elif wcut > 30:
        status = "MONITOR"
    else: 
        status = "GOOD"


        # Print results
    print("Well:", name, "Water Cut", wcut, "% | Status:", status)
    if status == "CRITICAL":
        print("   ⚠ ACTION REQUIRED:", name, "must be reviewed immediately")