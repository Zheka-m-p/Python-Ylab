from math import prod


def count_find_num(primesL, limit):
    p = prod(primesL)
    if p > limit:
        return []
    else:
        count = 0
        minim = min(primesL)  # минимальное из простых чисел, вдруг там не в порядке возрастания даны
        while minim * p <= limit:
            count += 1
            p = minim * p
        p = prod(primesL)
        ans = [p]
        maxim = p  # максимальное значение, если нет чисел, удовлетворящих усовию кроме чисел из произведения списка
        count_ans = 1
        for i in range(count):
            ans1 = []
            for j in ans:
                for k in primesL:
                    if k * j <= limit:
                        ans1.append(k * j)
            ans = list(set(ans1))
            count_ans += len(ans)
            maxim = max(maxim, max(ans))
    return [count_ans, maxim]
