from time import sleep


def repeat_decorator(call_count, start_sleep_time, factor, border_sleep_time):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Кол-во запусков = {call_count}')
            print('Начало рабобты')
            for i in range(1, call_count + 1):
                t = min(start_sleep_time * factor ** (i - 1), border_sleep_time)
                sleep(t)
                result_func = func(*args, **kwargs)
                print(f'Запуск номер {i}. Ожидание: {t} . Результат декорируемой функций = "{result_func}"')
            print('Конец работы')
        return wrapper
    return my_decorator


@repeat_decorator(call_count=4, start_sleep_time=1, factor=3, border_sleep_time=12)
def simple_function():
    return 'Будет сделано, готов вкалывать'


if __name__ == '__main__':
    simple_function()
