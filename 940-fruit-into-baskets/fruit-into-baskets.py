class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        maxi = 0
        my_dict = {}
        for right in range(len(fruits)):
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1 
            while len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
            maxi = max(maxi, right-left+1)
        return maxi