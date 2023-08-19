'''
Problem := https://leetcode.com/problems/house-robber/
'''

def max_robbery_amt(house,cur_ind):
    if cur_ind>= len(house):
        return 0
    else:
        st_f_hs = house[cur_ind] + max_robbery_amt(house,cur_ind+2)
        skip_f_hs = max_robbery_amt(house,cur_ind+1)
        return max(st_f_hs,skip_f_hs)

houses = [7]
print(max_robbery_amt(houses,0))