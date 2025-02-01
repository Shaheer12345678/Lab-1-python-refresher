import timeit

def pow2(n):
    return 2 ** n

def for_loop_pow2_1000():
    results = []
    for i in range(1001):
        results.append(pow2(i))
    return results

def list_comp_pow2_1000():
    return [pow2(n) for n in range(1001)]

# Part 1
elapsed_time = timeit.timeit(lambda: pow2(10000), number=10000)
print(f"Elapsed time for 10000 calls of pow2(10000): {elapsed_time}")

# Part 2
elapsed_time = timeit.timeit(lambda: for_loop_pow2_1000(), number=1000)
print(f"Elapsed time for for_loop_pow2_1000: {elapsed_time}")

# Part 3
elapsed_time = timeit.timeit(lambda: list_comp_pow2_1000(), number=1000)
print(f"Elapsed time for list_comp_pow2_1000: {elapsed_time}")
