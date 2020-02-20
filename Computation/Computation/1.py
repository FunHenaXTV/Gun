from computation import fast_tanh
x1 = 443
y1 = 357
length = 295

tg = (250-y1)/x1
print(tg)
x = (length**2/(1+tg**2))**0.5
y = tg * x

print(y)

print(fast_tanh(x1, y1, length))
