class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_ang = {}

        for index, elem in enumerate(strs):
            anagr_of_elem = {}

            for character in elem:
                if anagr_of_elem.get(character, False):
                    anagr_of_elem[character] += 1
                else:
                    anagr_of_elem[character] = 1
            hashed_dict = frozenset(anagr_of_elem.items())
            if hash_ang.get(hashed_dict, False):
                hash_ang[hashed_dict].append(elem)
            else:
                hash_ang[hashed_dict] = [elem]
        
        return hash_ang.values()