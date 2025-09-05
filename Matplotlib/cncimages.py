import matplotlib.pyplot as plt

# Data for the graph
original_line_length = [50, 90, 120, 125, 135]
plane_surface = [1, 0, 0, 1, 0]
rough_surface = [2, 6, 7, 4, 5]

# Create the plot
plt.plot(original_line_length, plane_surface, label='Plane Surface')
plt.plot(original_line_length, rough_surface, label='Rough Surface')

# Add labels, title, and legend
plt.title('Missed Path (BE) (Without Error Optimization)')
plt.xlabel('Original Line Length (AB), mm')
plt.ylabel('Missed Path Length (BE), mm')
plt.legend()

# Show the plot
plt.show()
