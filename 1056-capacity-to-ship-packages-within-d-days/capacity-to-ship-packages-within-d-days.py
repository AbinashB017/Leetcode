class Solution:
    def reqdays(self, weights, capacity):
        days =1
        load =0
        for i in range(len(weights)):
            if load + weights[i] > capacity:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = float("inf")
        while low <= high:
            mid = int(low + (high - low) / 2)
            daysneeded = self.reqdays(weights, mid)
            if daysneeded <= days:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans
