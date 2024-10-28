from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemy_count = 100
        day_count = 0
        print(f'{self.name}, на нас напали!')
        while enemy_count > 0:
            enemy_count -= self.power
            day_count += 1
            print(f'{self.name} сражается {day_count} дней, осталось {enemy_count} воинов' + '\n')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!' + '\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")



# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     def __init__(self, name, counter, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.counter = counter
#         self.delay = delay
#
#     def timer(self, name, counter, delay):
#         while counter:
#             time.sleep(delay)
#             print(f'{name} {time.ctime(time.time())}')
#             counter -= 1
#
#     def run(self):
#         print(f'Поток {self.name} запущен')
#         self.timer(self.name, self.counter, self.delay)
#         print(f'Поток {self.name} заверщен')
#
#
# thread1 = MyThread('thread1', 5, 1)
# thread2 = MyThread('thread2', 3, 0.5)
# thread1.start()
# thread2.start()