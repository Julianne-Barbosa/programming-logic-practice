seconds = int(input())

hours = 0
minutes = 0

if seconds>=3600:
    hours = seconds // 3600
    seconds = seconds % 3600

if seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60

print(f'{hours}:{minutes}:{seconds}')