'''
problem := https://leetcode.com/problems/edit-distance/
'''

def find_min_edits(s1,s2,ind1,ind2):
    if ind1==len(s1):
        return len(s2)-ind2
    if ind2==len(s2):
        return len(s1)-ind1
    if s1[ind1] == s2[ind2]:
        return find_min_edits(s1,s2,ind1+1,ind2+1)
    else:
        del_ops = 1+find_min_edits(s1,s2,ind1,ind2+1)
        ins_ops = 1+find_min_edits(s1,s2,ind1+1,ind2)
        reps_ops = 1+find_min_edits(s1,s2,ind1+1,ind2+1)
        return min(del_ops,ins_ops,reps_ops)


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"

    print('Min edits =', find_min_edits(s1=word2,s2=word1,ind1=0,ind2=0))


