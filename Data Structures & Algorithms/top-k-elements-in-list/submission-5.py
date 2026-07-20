class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elem_freq = {}

        for elem in nums:
            elem_freq[elem] = elem_freq.get(elem, 0) + 1
        
        print(elem_freq)

        freq_by_elem = {}

        for key, value in elem_freq.items():
            if freq_by_elem.get(value, False):
                freq_by_elem[value].extend([key])
            else:
                freq_by_elem[value] = [key]
        
        print(freq_by_elem)

        answ = []

        for n in range(len(nums), 0, -1):
            if freq_by_elem.get(n, False):
                answ.extend(freq_by_elem[n])

            if len(answ)==k:
                return answ
            