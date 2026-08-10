class Solution:

    def encode(self, strs: List[str]) -> str:

        #I'm thinking we paste the string and then its length at the end
        #But we need a way to know if it's the length or if the string originally had the number
        #If we just prefix every single string with a number and then a random character
        #We can know exactly how many to read after the character (if it's just number then it's vague if 5 or 53 e.g.)
        encoded_str = ""

        for string in strs:
            encoded_str += (str(len(string)) + "*" + string)
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_arr = []

        # ex: "5*hello2*OK"

        i, j = 0, 0

        while i < len(s):
            # when j reaches * we basically take the number from [i:j]
            while s[j] != "*":
                j += 1
            
            
            num = int(s[i:j])
            print(num)

            decoded_arr.append(s[j+1: j + 1 + num])

            # set i to the end of the string
            i = j + num + 1
            j = j + num + 1
        
        return decoded_arr



