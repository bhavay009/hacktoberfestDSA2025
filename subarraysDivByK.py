class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        heap={0:1}

        for i in nums:
            prefix+=i
            sum=prefix%k

            if sum in heap:
                count+=heap[sum]

            else:
                count+=0

            if sum in heap:
                heap[sum]+=1

            else:
                heap[sum]=1

        return count                        
        
