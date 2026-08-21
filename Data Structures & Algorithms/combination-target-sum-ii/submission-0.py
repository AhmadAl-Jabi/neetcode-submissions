class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Need to sort the array so that any dupes are next to each other
        # And then you can basically choose to include or skip. If you skip then you while loop and iterate
        # Until you don't see the item anymore

        res = []
        candidates.sort()

        def dfs(idx, path, cur):

            # Base case
            if cur == target:
                res.append(path.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if cur + candidates[i] > target:
                    break # Basically we went overboard here
                
                path.append(candidates[i])
                dfs(i+1,path,cur + candidates[i])
                path.pop() # This is what allows us to explore other paths afterwards
            
        dfs(0,[],0)
        return res

            