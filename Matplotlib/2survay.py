import matplotlib.pyplot as plt
from collections import Counter

# Data
issues = [
    "Reverse power source connection", "Overcurrent issues", "Reverse power source connection",
    "Overcurrent issues", "Reverse power source connection", "Cost issues", "Cost issues",
    "Breaking problem", "Overcurrent issues", "Reverse power source connection", "Cost issues",
    "Breaking problem", "Cost issues", "Reverse power source connection", "Cost issues",
    "Reverse power source connection", "Overcurrent issues", "Cost issues", "Breaking problem",
    "Reverse power source connection", "Reverse power source connection", "Reverse power source connection",
    "Reverse power source connection", "Overcurrent issues", "Breaking problem", "Reverse power source connection",
    "Breaking problem", "Not enough current", "Breaking problem", "Logic voltage problem",
    "Low current output", "Overcurrent issues", "Reverse power source connection", "Breaking problem",
    "Reverse power source connection", "Reverse power source connection", "Reverse power source connection",
    "Reverse power source connection", "Cost issues", "Overcurrent issues", "Overcurrent issues", "Overcurrent issues"
]

# Count occurrences of each issue
issue_counts = Counter(issues)

# Extract labels and sizes
labels = list(issue_counts.keys())
sizes = list(issue_counts.values())

# Plot pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Common Issues with Motor Driver\n(About 100 user survey review)\n")
plt.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()
