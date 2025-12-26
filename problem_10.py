def sum_of_primes(limit: int) -> int:
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, limit, i):
                sieve[multiple] = False

    return sum(i for i, is_prime in enumerate(sieve) if is_prime)


print(sum_of_primes(2_000_000))
