class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        freq={0:1}
        count=0
        prefix=0
        n=len(a)
        for i in range(n):
            prefix+=a[i]
            p=prefix-k
            if p in freq:
                count+=freq[p]
            freq[prefix]=freq.get(prefix,0)+1
        return count


              