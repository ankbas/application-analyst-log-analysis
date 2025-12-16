import pandas as pd

data = pd.read_csv("app_logs.csv")

total_events = len(data)
error_count = data[data["status"] == "error"].shape[0]
avg_response = data["response_time"].mean()

print("Application Usage Summary")
print("-------------------------")
print(f"Total Events: {total_events}")
print(f"Errors Found: {error_count}")
print(f"Average Response Time: {avg_response:.2f} ms")
