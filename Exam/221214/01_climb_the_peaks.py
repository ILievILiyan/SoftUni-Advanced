from collections import deque

food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))

mountains_with_difficulty = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

peaks_queue = deque(x for x in mountains_with_difficulty.items())
conquered_peaks = []

while peaks_queue and stamina and food:
    current_peak = peaks_queue.popleft()

    daily_food = food.pop()
    daily_stamina = stamina.popleft()
    daily_energy = daily_food + daily_stamina

    if daily_energy >= current_peak[1]:
        current_peak_name = current_peak[0]
        conquered_peaks.append(current_peak_name)
    else:
        peaks_queue.appendleft(current_peak)

    if not peaks_queue:
        print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
    elif not food or not stamina:
        print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print(f"Conquered peaks:", *conquered_peaks, sep="\n")
