class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 3, 4]
        #[2*3*4,1*3*4, 1*2*4, 1*2*3]
        #right = [2*3*4 ,3*4 , 4, empty]
        #left = [empty, 1, 1*2, 1*2*3]
        rightProduct = 1
        rightArr = [1] *len(nums)
        leftProduct = 1
        leftArr = []
        res = []

        for i in range(len(nums)):
            rightArr[len(nums)- 1-i] = (rightProduct)
            rightProduct *= nums[len(nums)- 1-i]
            leftArr.append(leftProduct)
            leftProduct *= nums[i]
            reversed(rightArr)

        for i in range(len(nums)):
            res.append(leftArr[i]*rightArr[i])
        return res
