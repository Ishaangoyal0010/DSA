class Solution(object):
    def lemonadeChange(self, bills):
        my_dict = {5: 0, 10: 0, 20: 0}
        for i in range(len(bills)):
            if bills[i]==5:
                my_dict[5]+=1
            if bills[i]==10:
                if my_dict[5]>0:
                    my_dict[5]-=1
                    my_dict[bills[i]]+=1
                else:
                    return False

            if bills[i]==20:
                if my_dict[5]>0 and my_dict[10]>0:
                    my_dict[10]-=1
                    my_dict[5]-=1
                elif my_dict[5]>2:
                    my_dict[5]-=3
                else:
                    return False
        return True
        