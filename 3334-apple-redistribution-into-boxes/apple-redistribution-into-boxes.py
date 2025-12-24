class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sum1 = sum(apple)
        capacity.sort(reverse=True)
        sum2 = 0
        cnt = 0

        for i in range(len(capacity)):
            sum2 += capacity[i]
            cnt += 1
            if sum2>=sum1:
                break

        return cnt

        