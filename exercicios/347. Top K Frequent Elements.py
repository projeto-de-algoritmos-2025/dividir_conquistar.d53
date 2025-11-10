from collections import Counter
import random

class Solution:
    def topKFrequent(self, nums, k):
        # conta frequencias
        freq = Counter(nums)
        items = list(freq.items())

        # se k cobre todos
        if k == len(items):
            return [v for v, _ in items]

        # particiona por quickselect
        def partition(l, r, p):
            pv = items[p][1]
            items[p], items[r] = items[r], items[p]
            s = l
            for i in range(l, r):
                if items[i][1] < pv:
                    items[s], items[i] = items[i], items[s]
                    s += 1
            items[r], items[s] = items[s], items[r]
            return s

        # quickselect para achar corte
        def quickselect(l, r, k_smallest):
            while l <= r:
                p = random.randint(l, r)
                p = partition(l, r, p)
                if p == k_smallest:
                    return
                if p < k_smallest:
                    l = p + 1
                else:
                    r = p - 1

        n = len(items)
        quickselect(0, n - 1, n - k)

        # retorna k mais frequentes
        return [v for v, _ in items[n - k:]]
