class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        max_area = 0
        high = len(heights) -1

        while low<high:
            width = high-low
            height = min(heights[low], heights[high])
            max_area = max(max_area,width*height)

            if heights[low] < heights[high]:
                low+=1
            else:
                high-=1

        return max_area
            
        