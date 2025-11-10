class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        # transforma: a[i] = nums1[i] - nums2[i]
        a = [x - y for x, y in zip(nums1, nums2)]
        n = len(a)
        tmp = [0] * n  # buffer p/ merge

        def sort_count(lo, hi):
            # divide e conquista com mergesort + contagem
            if lo >= hi:
                return 0
            mid = (lo + hi) // 2
            cnt = sort_count(lo, mid) + sort_count(mid + 1, hi)

            # conta pares cruzados: i em [lo..mid], j em [mid+1..hi]
            # condição: a[i] <= a[j] + diff
            i = lo
            for j in range(mid + 1, hi + 1):
                while i <= mid and a[i] <= a[j] + diff:
                    i += 1
                cnt += (i - lo)

            # merge crescente
            i, j, k = lo, mid + 1, lo
            while i <= mid and j <= hi:
                if a[i] <= a[j]:
                    tmp[k] = a[i]; i += 1
                else:
                    tmp[k] = a[j]; j += 1
                k += 1
            while i <= mid:
                tmp[k] = a[i]; i += 1; k += 1
            while j <= hi:
                tmp[k] = a[j]; j += 1; k += 1
            for t in range(lo, hi + 1):
                a[t] = tmp[t]

            return cnt

        return sort_count(0, n - 1)
