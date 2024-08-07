class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #
        #need a low, and high as pointers
        #this calculate index numbers
        low = 0
        high = len(nums) - 1

        #low is incremented or high is decrimented but they'll meet
        while low <= high:

            #calculate middle index value, use floor division 
            middle = low + ((high - low) // 2)
            #first comparison, is target the middle value?
            if nums[middle] == target:
                return middle
            #if the target more than index's value at middle
            elif nums[middle] < target:
                #change the low to be one index above the middle and redo
                low = middle + 1
            #is the target more than the index value at middle 
            elif nums[middle] > target:
                #decrease the high index value by one and redo
                high = middle - 1
            else:
                return middle
        
        
        #default is -1
        return -1
