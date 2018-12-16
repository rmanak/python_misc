def optimal_change(change, coins={1, 5, 10, 25}):
    """
    Not efficient recursive call for optimal change problem
    """
    if change in coins:
        return 1, [change]

    counts = list()
    outcomes = list()
    which_coin = list()

    for coin in coins:
       if change > coin:
            a, b = optimal_change(change-coin, coins=coins)
            count = a+1
            counts.append(count)
            outcomes.append(b)
            which_coin.append(coin)

    min_count = min(counts)
    min_index = counts.index(min_count)
    best_outcome = outcomes[min_index]
    best_coin = which_coin[min_index]

    return min_count, best_outcome + [best_coin]

for x in [1, 11, 23, 27]:
    print(x, optimal_change(x))

print(optimal_change(42, coins={1, 10, 20, 21}))

def optimal_change2(change, known_ones, coins={1, 5, 10, 25}):
    """
    Not efficient recursive call for optimal change problem with
    caching
    """
    if change in known_ones:
        return known_ones[change]

    if change in coins:
        known_ones[change] = (1, [change])
        return (1, [change])

    counts = list()
    outcomes = list()
    which_coin = list()

    for coin in coins:
       if change > coin:
            a, b = optimal_change2(change-coin, known_ones, coins=coins)
            count = a+1
            counts.append(count)
            outcomes.append(b)
            which_coin.append(coin)

    min_count = min(counts)
    min_index = counts.index(min_count)
    best_outcome = outcomes[min_index]
    best_coin = which_coin[min_index]

    known_ones[change] = (min_count, best_outcome + [best_coin])
    return min_count, best_outcome + [best_coin]

print(optimal_change2(63, known_ones=dict(), coins={1,2,5,10,20,21}))

def optimal_change3(change, coins={1,2,5, 10, 25}):
    """
    dynamic programming approach to optimal change
    """
    optimals = dict()
    if change < min(coins):
        raise ValueError("change must be greater than min")
    optimals[min(coins)] = 1, [min(coins)]
    optimals[0] = 0, []
    for next_val in range(min(coins)+1, change+1):
        potentials = list()
        associate_coins = list()
        previous_coins = list()
        for coin in coins:
            x = optimals.get(next_val - coin)
            if x is not None:
                a, b = x
                potentials.append(1+a)
                associate_coins.append(coin)
                previous_coins.append(b)
        best_val = min(potentials)
        best_index = potentials.index(best_val)
        optimals[next_val] = best_val, previous_coins[best_index] + [associate_coins[best_index]]
    return optimals

print(optimal_change3(63, coins={1,2,5,10,20,21}).get(63))


