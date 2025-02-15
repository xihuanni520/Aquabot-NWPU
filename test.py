import matplotlib.pyplot as plt
plt.bar(["传统ROV", "本作品"], [500, 350], color=["red", "green"])
plt.ylabel("能耗 (W)")
plt.savefig("power_consumption.png")