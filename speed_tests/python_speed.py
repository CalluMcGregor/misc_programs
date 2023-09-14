import time
start = time.time()

test_size = 100_000
current = 0

while current < test_size:
    current += 1
    print(current)

print(time.time()-start, 'seconds')