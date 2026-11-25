class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0 
       

        if target not in nums:
            return -1

        while high>=low:
            mid = (high+low)//2
            if nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
            else:
                return mid

        
        print(mid)
                