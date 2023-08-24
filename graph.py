import matplotlib.pyplot as plt

x1 = [2, 4, 5, 7]
y1= [2, 3, 6, 7]

plt.plot(x1, y1, label = "Line 1", color = "green", linestyle = "dashed", 
         linewidth = "3", marker = "o",
            markerfacecolor = 'blue',
           markersize = 12)
plt.xlim(1,8)
plt.ylim(1,8)

x2 = [1, 2, 3, 4]
y2= [1, 2, 3, 4]

plt.plot(x2, y2, color = "purple", linestyle = "dotted", 
         linewidth = "3", marker = "o",
           label = "Line 2", markerfacecolor = 'pink',
           markersize = 12)


plt.xlim(1,8)
plt.ylim(1,8)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Graph - 2 Lines")
plt.legend()
plt.show()