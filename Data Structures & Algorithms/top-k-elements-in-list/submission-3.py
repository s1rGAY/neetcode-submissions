class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}


        for elem in nums:
            count[elem] = count.get(elem, 0) + 1

        print(count)

        freq = {}

        for num, freque in count.items():
            if freq.get(freque, False):
                freq[freque].append(num)
            else:
                freq[freque] = [num]
        
        answ = []

        for f in range(len(nums), 0, -1):
            if f in freq:
                for num in freq[f]:
                    if k == 0:
                        return answ
                    answ.append(num)
                    k -= 1

        return answ