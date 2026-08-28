class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output_arr = []


        def dfs(open_count, close_count, curr_string):

            if open_count + close_count == n * 2:
                output_arr.append(curr_string)
                return
            
            # need open_count to be >= close_count at all times for valid answer
            # can always append a open bracket as long as it's < n
            if open_count < n:
                dfs(open_count + 1, close_count, curr_string + "(")
            
            if close_count < open_count:
                dfs(open_count, close_count + 1, curr_string + ")")

            
        dfs(0,0,"")
        return output_arr

        