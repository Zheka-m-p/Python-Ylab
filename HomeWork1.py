from math import prod
from itertools import combinations


def domain_name(url):
    s = url.split('://')
    if 'http' in s[0]:
        ans = s[1].split('.')
    else:
        ans = s[0].split('.')
    if ans[0] != 'www':
        return ans[0]
    else:
        return ans[1]


def int32_to_ip(int32):
    ip_1 = int32 // 256**3
    ip_2 = int32 % 256**3 // 256**2
    ip_3 = int32 % 256**3 % 256**2 // 256
    ip_4 = int32 % 256**3 % 256**2 % 256
    ipv4 = map(str, [ip_1, ip_2, ip_3, ip_4])
    return '.'.join(ipv4)


def zeros(n):
  x = n//5
  return x+zeros(x) if x else 0


def bananas(s):
    res = []
    for c in combinations(range(len(s)), len(s)-6):
        x = list(s)
        for i in c:
            x[i] = '-'
        x = ''.join(x)
        if x.replace('-', '') == 'banana':
            res.append(x)
    return set(res)


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
