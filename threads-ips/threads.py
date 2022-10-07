from threading import Thread
import time

def super_truck(speed, pilot):
    track = 0
    while track <= 100:
        track+=speed
        time.sleep(0.5)
        print('Pilot: {} Km: {}\n'.format(pilot, track))
        
t_truck1 = Thread(target=super_truck, args=[1, 'Mateus'])
t_truck2 = Thread(target=super_truck, args=[2, 'John'])

t_truck1.start()
t_truck2.start()