class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n=len(costs)
        freq=[0]*(max(costs)+1)
        count=0
        for cost in costs:
            freq[cost]+=1 
        for j in range(len(freq)):
            if freq[j]>0:
                can_buy=min(freq[j],coins//j)
                coins_spent=can_buy*j
                coins-=coins_spent
                count+=can_buy
        return count

        