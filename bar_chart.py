import matplotlib.pyplot as plt

left= [1, 2, 3, 4, 5]
height= [10, 11, 23, 36, 4]


tick_label = ["one", "two", "three", "four", "five"]
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ["deeppink", "orange"])


plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Bar Chat")
plt.legend()
plt.show()