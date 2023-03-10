import matplotlib.pyplot as plt

plt.bar(
    ["США", "Китай", "Япония", "Великобритания"],
    [39, 38, 27, 22],
    color=["b", "r", "y", "g"],
)

plt.xlabel("Страна", fontsize="small", color="midnightblue")
plt.ylabel("Количество", fontsize="small", color="midnightblue")
plt.title("Золотые медали: Летняя олимпиада Токио 2020", fontsize=15)
plt.show()