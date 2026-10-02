class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))

        curr_count = 1
        longest_count = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] - sorted_nums[i] == 1:
                curr_count += 1
            else:
                curr_count = 1

            longest_count = max(longest_count, curr_count)

        return longest_count