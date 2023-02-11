from collections import deque

food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))

mountains_with_difficulty = ("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)
conquered_peaks = []

day = 0
while True:
    if not food or not stamina or len(mountains_with_difficulty) == len(conquered_peaks):
        break

    daily_food = food.pop()
    daily_stamina = stamina.popleft()
    daily_energy = daily_food + daily_stamina
    current_peak_needed_energy = mountains_with_difficulty[day][1]

    if daily_energy >= current_peak_needed_energy:
        current_peak_name = mountains_with_difficulty[day][0]
        conquered_peaks.append(current_peak_name)
        day += 1
    else:
        if day > 0:
            day -= 1

if len(mountains_with_difficulty) == len(conquered_peaks):
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
    print("\n".join(conquered_peaks))
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')





