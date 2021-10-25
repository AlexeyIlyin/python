import time

class TrafficLight:
    color = {'red': 7, 'yellow' : 2, 'green' : 5}

    def running (self, iter):
        i = 0
        while i < iter:
            for col, time_col in TrafficLight.color.items():
                print(col, time_col, 'сек.')
                time.sleep(int(time_col))
            i += 1

sv = TrafficLight()
sv.running(5)








