
import random

print('Rolling Dice ... 🎲')

dice = {1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6:'6️⃣', 7: '7️⃣'}
number = random.randint(1, 7)
print(dice[number])