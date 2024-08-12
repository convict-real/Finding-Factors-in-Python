import time

N = 4
Factors = []

startTime = time.perf_counter()
for i in range(1, N + 1):
    if N % i == 0:
        Factors.append(i)
endTime = time.perf_counter()

print((endTime - startTime) * 1000)
print(Factors)

