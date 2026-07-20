class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for el in strs:
            encoded_str+= f'{len(el)}卐{el}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s:
            len_of_sub_str = ''
            decoded_str = []

            index = 0
            while True:
                symbol = s[index]

                if symbol == '卐':
                    len_for_element = int(len_of_sub_str)
                    decoded_str.append(s[index+1:index+1+len_for_element])
                    index = index+1+len_for_element
                    len_of_sub_str = ''

                else:
                    len_of_sub_str+=symbol
                    index += 1
                
                if index >= len(s):
                    break
            return decoded_str
        else:
            return []