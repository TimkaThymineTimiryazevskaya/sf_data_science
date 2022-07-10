import numpy as np
number = np.random.randint(1,101)
count = 0
predict_number = 50
while predict_number != number:
    count += 1

    if predict_number > number:
        predict_number = predict_number//2

    elif predict_number < number:
        predict_number = predict_number//2 + predict_number

print(f"Вы угадали число! Это число = {number}, за {count} попыток")