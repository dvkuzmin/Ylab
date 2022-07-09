from time import sleep


class ExpTimeDecorator:
    def __init__(self, call_count: int, start_sleep_time: int, factor: int, border_sleep_time: int):
        self.call_count = call_count
        self.start_sleep_time = start_sleep_time
        self.factor = factor
        self.border_sleep_time = border_sleep_time

    def __call__(self, func):
        def wrapper(number: int):
            print(f"Количество запусков  = {self.call_count}")
            print("Начало работы")
            for n, i in enumerate(range(self.call_count)):
                t = self.start_sleep_time * self.factor ** (n + 1)
                t = t if t <= self.border_sleep_time else self.border_sleep_time
                sleep(t)
                result = func(number)
                print(f"Запуск номер {n+1}. Ожидание: {t} секунд. Результат декорируемой функции = {result}")
            print("Конец работы")
        return wrapper


@ExpTimeDecorator(call_count=3, start_sleep_time=1, factor=2, border_sleep_time=7)
def multiplier(number: int):
    return number * 2


multiplier(3)