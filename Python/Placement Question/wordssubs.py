class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        words2dic={}
        ans=[]
        for i in words2:
            for j in i:
                words2dic[j]=words2dic.get(j,0)+1
        for i in words1:
            tempdic={}
            for j in i:
                tempdic[j]=tempdic.get(j,0)+1
            flag=True
            for j in words2dic.keys():
                if(words2dic[j]>tempdic.get(j,0)):
                    flag=False
            if flag:
                ans.append(i)
        return ans
s=Solution()
s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","o"])