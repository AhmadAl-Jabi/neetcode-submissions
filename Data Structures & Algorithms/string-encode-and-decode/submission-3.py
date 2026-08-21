class Solution:

    def encode(self, strs: List[str]) -> str:
        # Need a delimiter and the length of each string

        encoded = ""

        for item in strs:
            # example: "3#cat4#cars"
            encoded += str(len(item)) + "#" + item
        
        return(encoded)

    def decode(self, s: str) -> List[str]:

        new_arr = []

        # Honestly not that bad but you need to view the problem with a certain perspective
        # Basically think that you should start at the beginning (which will be a number) and keep walking
        # Until you hit a "#". That now signifies the end of the number. Now take the entire string after the sharp of length number
        # Shift your pointers to the end of the string you just took. Rinse and repeat
        
        i = 0
        j = 0

        while i < len(s):
            
            while s[j] != "#":
                j += 1
            
            leng = int(s[i:j])
            i = j + leng + 1
            new_arr.append(s[j+1:i])
            j=i

        return new_arr

