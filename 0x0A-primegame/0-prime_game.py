#!/usr/bin/python3

'''The Prime game module.
'''


def isWinner(x, nums):
    '''Outputs the winner of a prime game session with `x` rounds.
    '''
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes within the range of numbers in nums
    num = max(nums)
    primes = [True for _ in range(1, num + 1, 1)]
    primes[0] = False
    for numx, is_prime in enumerate(primes, 1):
        if numx == 1 or not is_prime:
            continue
        for j in range(numx + numx, num + 1, numx):
            primes[j - 1] = False
    # Here, we filter the number of primes less than num in nums for each round
    for _, num in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: num])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
