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

        # We'll probably need an i and j, where one is at the beginning of new word and the other is at the end, and then 
        # we make one equal the other at the end and move forward. i can be at the beginning

        # Here we don't know in advance how long to loop so resort to while loop

        #So plan is that one pointer walks till it sees a # --> Thinking it should be i?
        #Then we store s[pointer -1] and know the length
        #Then the other pointer tps to the pointer and it walks that far (+1 cuz of slicing)
        #Rinse and repeat until we reach the end of the string basically

        # ex: "1000#bob20000#$#@$12#Jim"

        i = 0
        j = 0

        while i < len(s):
            
            while s[j] != "#":
                j += 1
            
            leng = int(s[i:j])
            i = j + leng + 1
            new_arr.append(s[j+1:i])
            j=i

            '''
            if (s[i]) == "#":
                # Store the number before the "#"
                leng = int(s[i-1])

                j = i + 1

                for _ in range(leng):
                    j += 1
                
                new_arr.append(s[i + 1:j])

            i += 1
            '''

        return new_arr

