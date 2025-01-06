import matplotlib.pyplot as plt
from collections import Counter

# Data
drivers = [
    "BTS7960", "TB6612FNG", "TB6612FNG", "L293D", "L293D", "TB6612FNG", "BTS7960",
    "L298N", "L298N", "TB6612FNG", "BTS7960", "L298N", "TB6612FNG", "TB6612FNG",
    "BTS7960", "L293D", "L298N", "TB6612FNG", "L298N", "L293D", "TB6612FNG",
    "TB6612FNG", "Others", "TB6612FNG", "TB6612FNG", "L298N", "L298N", "L298N",
    "L298N", "BTS7960", "L293D", "TB6612FNG", "TB6612FNG", "L298N", "BTS7960",
    "BTS7960", "BTS7960", "BTS7960", "L293D", "BTS7960", "L293D", "L293D"
]

# Count occurrences of each driver type
driver_counts = Counter(drivers)

# Extract labels and sizes
labels = list(driver_counts.keys())
sizes = list(driver_counts.values())

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Motor Driver Usage Percentage\n (About 100 user survey report)\n") 
plt.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()
