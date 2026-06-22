class Solution:
    def twoSum(self, a: List[int], k: int) -> List[int]:
       freq={}
       
       for i in range(len(a)):
         if k-a[i] in freq:
            return [freq[k-a[i]], i]
            
         freq[a[i]]=i
      
