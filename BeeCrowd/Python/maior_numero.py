import math

valores = [int(x) for x in input().split(' ')]
a, b, c = valores

maior_ab=(a+b+abs(a-b))/2
maior_c=(maior_ab+c+abs(maior_ab-c))/2

print("%d eh o maior" %maior_c)
