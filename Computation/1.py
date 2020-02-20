from computation import fast_tanh
x1 = 571.5
y1 = 361.1
length = 103.5

tg = (250-y1)/x1
print('afsdd')
x = (length**2/(1+tg**2))**0.5
y = tg * x

print(x, y)

print(fast_tanh(x1, y1, length))
