class Solution:
    def get_trap_water(self, height) -> int:
        sum_value = 0
        first_value = height[0]
        print(height)
        for i in range(1,len(height)):
            sum_value = sum_value + (first_value - height[i])
            print('sum'+str(sum_value))
        print(sum_value)
        return sum_value
    
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        count = 0
        
        
        total = 0
        def get_ans(height, length):
            max_value = height[0]
            trap_water = [height[0]]
        
            start_index = 0
            nonlocal total
            
            for i in range(1,length):
                if height[i]  >= max_value and len(trap_water) >= 2 :
                    print(trap_water)
                    total = total + self.get_trap_water(trap_water[:])
                    start_index = i
                    max_value = height[i]
                    trap_water = [height[i]]
                    
                elif i+1 == length and len(trap_water) > 2 :
                    rev_list = list(reversed(trap_water[:]))[:]
                    start_index = i
                    max_value = height[i]
                    trap_water = []
                    get_ans(rev_list, len(rev_list))
                    
                elif height[i]  >= max_value:
                    start_index = i
                    max_value = height[i]
                    trap_water = [height[i]]
                else:
                    trap_water.append(height[i])
                    
            if len(trap_water) > 3:
                get_ans(trap_water[1:], len(trap_water[1:]))
            
        get_ans(height, len(height))
        
        return total