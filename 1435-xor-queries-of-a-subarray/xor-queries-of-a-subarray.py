class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre = [0]*n
        pre[0] = arr[0]
        for i in range(1, n):
            pre[i] = pre[i-1] ^ arr[i]

        ans = []
        for l, r in queries:
            if l==0:
                ans.append(pre[r])
            else:
                ans.append(pre[r] ^ pre[l-1])

        return ans    