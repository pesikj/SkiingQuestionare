import pandas
import matplotlib.pyplot as plt
table = pandas.read_excel("Dotazník-pro-instruktory-Odpovědi.xlsx", skiprows=1)
partial_satisfaction_table = table[["Dílčí spokojenost 1", "Dílčí spokojenost 2", "Dílčí spokojenost 3"]]
fig, ax = plt.subplots()
labels = ["Spokojenost\ns informovaností", "Spokojenost\ns průběhem", "Spokonenost\ns instruktory"]
bp = ax.boxplot(partial_satisfaction_table, labels=labels, vert=0, patch_artist=True)

colors = ['pink', 'lightblue', 'lightgreen']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
ax.set_xlim(0, 10)
ax.set_title("Přehled dílčích výsledků spokojenosti")
fig.subplots_adjust(left=0.20)
plt.show()

fig, ax = plt.subplots()

first_group_table = table.loc[:, "Informace ke kurzu": "Informace od lyžařské školy"]
bp = ax.boxplot(first_group_table, labels=first_group_table.columns, vert=0, patch_artist=True)
colors = ['pink', 'lightblue', 'lightgreen', "gold","violet", "coral", "paleturquoise", "wheat"]
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
ax.set_xlim(0, 10)
ax.set_title("Přehled dílčích výsledků spokojenosti")
fig.subplots_adjust(left=0.3)
plt.show()