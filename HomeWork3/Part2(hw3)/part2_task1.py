def cache_func(func):
    cache = {}

    def decorator(*args, **kwargs):
        nonlocal cache
        if args not in cache:
            result = func(*args, **kwargs)
            cache[args] = result
            return result   # , 'Добавляем в кэш'
        else:
            return cache[args]   # , 'Берём из кэша'

    return decorator


@cache_func
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    print(multiplier(10))
    print(multiplier(12))
    print(multiplier(10))
