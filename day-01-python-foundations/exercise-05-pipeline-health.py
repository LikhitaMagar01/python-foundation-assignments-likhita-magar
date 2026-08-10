"""
Exercise 5: Pipeline Health Status
Student: Likhita
Day: 1
"""

# function definition
def check_pipeline(rows_loaded, rows_failed, runtime_minutes):
    # calculations
    total_rows = rows_loaded + rows_failed
    failure_rate = (rows_failed / total_rows) * 100

    if failure_rate <= 2 and runtime_minutes <= 20:
        pipeline_status = "Healthy"
    elif failure_rate <= 5:
        pipeline_status = "Warning"
    else:
        pipeline_status = "Critical"

    # output
    print(f"Inputs: Loaded={rows_loaded}, Failed={rows_failed}, Runtime={runtime_minutes} min")
    print(f"-> Failure Rate: {failure_rate:.2f}%")
    print(f"-> Pipeline Status: {pipeline_status}\n")

# function calls
print("test 1")
check_pipeline(rows_loaded=9800, rows_failed=200, runtime_minutes=18)

print("test 2")
check_pipeline(rows_loaded=9500, rows_failed=500, runtime_minutes=15)

print("test 3")
check_pipeline(rows_loaded=9900, rows_failed=100, runtime_minutes=30)

print("It shouldn't be considered healthy as for SLA both runtime and ")

