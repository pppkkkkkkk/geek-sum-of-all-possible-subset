#User function Template for python3
class Solution:
    def subsetXORSum(self, arr):
        # code here
        
        list = []
        
        # i = 0
        # while i<len(arr):
        #     j = i+1
        #     while j <= len(arr):
        #         list.append(arr[i:j])
        #         j+=1
        #     i+=1
        def dfs (index, arr, curSub):
            if index >= len(arr):
                list.append(curSub)
                return
            #include index
            newSub = curSub + [arr[index]]
            dfs(index+1, arr, newSub)
            
            #exclude index
            dfs(index+1, arr, curSub)
            
        dfs(0,arr,[])
        # print(list)
        
        total = 0
        for items in list:
            # print(items)
            local = 0
            for item in items:
                local = local^item
            total += local
        return total
            
