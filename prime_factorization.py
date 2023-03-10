# Выведите разложение натурального числа n > 1 на простые множители.
# Простые множители должны быть упорядочены по возрастанию и разделены пробелами.
def prime_factorization(a):
    ans = []
    d = 2
    while d <= a:
        if a % d == 0:
            ans.append(d)
            a = a/d
        else:
            d += 1
    return ans


print(*prime_factorization(int(input())))
