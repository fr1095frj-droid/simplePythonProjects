import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

rolls = [random.randrange(1, 3) for _ in range(100)]
values, frequencies = np.unique(rolls, return_counts=True)

title = f'Flip coin fro {len(rolls)} times'

axes = sns.barplot(x=values, y=frequencies)

axes.set_title(title)

sns.set_style('whitegrid')

axes.set(xlabel='Roll', ylabel='Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.2%}'
    axes.text(text_x, text_y, text, ha='center', va='bottom')

plt.show()

