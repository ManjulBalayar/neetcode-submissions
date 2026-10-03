class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in seen:
                idx1 = seen[diff] + 1
                idx2 = i + 1
                return [idx1, idx2]

            seen[num] = i