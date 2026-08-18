def class_average(*scores):
    if len(scores) == 0:
        print(0)
    else:
        total = 0
        for s in scores:
            total += s
        print(total / len(scores))

class_average(80, 90, 70)
class_average(55, 60, 65, 70, 75)
class_average()