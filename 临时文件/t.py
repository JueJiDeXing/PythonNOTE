import sys
from collections import defaultdict
from math import sqrt
from functools import lru_cache
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().strip()
inf = float("inf")


def Eratisthenes(N):
    primes = []
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    for i in range(2, N):
        if is_prime[i]: primes.append(i)
        for j in range(i * i, N, i):
            is_prime[j] = False
    return primes, is_prime


primes, _ = Eratisthenes(10 ** 4 + 5)


def dijkstra(g, start):
    h = [(0, start)]
    dis = defaultdict(lambda: inf)
    dis[start] = 0
    while h:
        d, u = heappop(h)
        if dis[u] < d: continue
        for v, w in g[u]:
            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                heappush(h, (dis[v], v))
    return dis


def solve():
    n, a, b = map(int, input().split())
    nums = list(map(int, input().split()))
    g = defaultdict(list)

    def f(x):
        res = 0
        for j in range(len(primes)):
            if x <= 1: break
            while x % primes[j] == 0:
                res += primes[j]
                x //= primes[j]
        if x > 1: res += x
        return res % n + 1

    for i, x in enumerate(nums, 1):
        fx = f(x)
        g[i].append([n + fx + 1, 1])  # i -> 虚拟点
        g[n + fx + 1].append([i, 0])  # 虚拟点 -> i
        g[i].append([fx, 1])  # i -> fx
        g[fx].append([i, 1])  # fx -> i
    dis = dijkstra(g, a)
    print(-1 if dis[b] == inf else dis[b])


solve()
