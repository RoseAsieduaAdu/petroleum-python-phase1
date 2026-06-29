# Lesson 2 - If Statements and Loops
# Well Health Checker

# Multiple wells data
wells = [
    ["Rose-1", 850,  520],
    ["Rose-2", 600,  800],
    ["Rose-3", 1200, 180],
    ["Rose-4", 300,  900],
    ["Rose-5", 950,  400],
]

# Field report function
def field_report(wells):

    print("")
    print("=== FIELD PRODUCTION REPORT ===")
    print("")

    # Counters
    total_wells    = 0
    critical_wells = 0

    for well in wells:

        # Extract data
        name  = well[0]
        oil   = well[1]
        water = well[2]

        # Calculate water cut
        total = oil + water
        wcut  = round((water / total) * 100, 2)

        # Check status
        if wcut > 70:
            status = "CRITICAL"
            critical_wells += 1
        elif wcut > 50:
            status = "WARNING"
        elif wcut > 30:
            status = "MONITOR"
        else:
            status = "GOOD"

        # Print well result
        print("Well:", name, "| Water Cut:", wcut, "% | Status:", status)

        if status == "CRITICAL":
            print("   ⚠ ACTION REQUIRED:", name, "must be reviewed immediately")

        total_wells += 1

    # Summary
    print("")
    print("=== SUMMARY ===")
    print("Total Wells Checked:", total_wells)
    print("Critical Wells:", critical_wells)
    print("Wells Performing Fine:", total_wells - critical_wells)

# Run the function
field_report(wells)