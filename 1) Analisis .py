# ---------------------------------------------
# مثال های تحلیل پیچیدگی زمانی
# ---------------------------------------------

# مثال حلقه تو در تو
# F(n) ≈ 3n^2

def example_nested(n):
    for i in range(n):
        for j in range(n):
            print(i)
            print(j)
            print(i + j)

# مثال سری مثلثی
# F(n) = n(n+1)/2

def triangular_loop(n):
    for i in range(n):
        for j in range(i, n):
            k = i + j
            print(k)

# مثال لگاریتمی
# F(n) = log2(n)

def logarithmic_example(n):
    while n > 1:
        n = n // 2

# مثال گام دار
# F(n) ≈ n/3

def stepped_loop(n):
    for i in range(0, n + 3, 3):
        t = 2 * i
        l = t + 5

# فیبوناچی بازگشتی

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# مثال تابع بازگشتی ترکیبی

def recursive_test(a, b):
    if a > b:
        return a * b
    return recursive_test(a, b - 2) + recursive_test(a - 1, b - 3) + 6
