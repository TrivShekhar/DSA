class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        temp = self.trie
        ind = 0 
        while word[ind] in temp and ind<len(word)-1:
            temp = temp[word[ind]]
            ind+=1
        
        if ind==len(word)-1 :
            if word[ind] in temp:
                temp[word[ind]]["isWord"]=True
            else:
                temp[word[ind]] ={}  
                temp[word[ind]]["isWord"]=True
            return
        while ind<len(word)-1:
            temp[word[ind]]={word[ind+1]:{}}
            temp[word[ind]]["isWord"]=False
            temp = temp[word[ind]]
            ind+=1
        temp[word[ind]]["isWord"]=True




class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie =  Trie()
        ans = []
        for word in words:
            trie.insert(word)
        def helper(trie, word, r,c):
            if r>=0 and c>=0 and r<len(words) and c<len(words[0]):
                if "isWord" in trie and trie["isWord"]:
                    ans.append(word)
                    return
                elif words[r][c] not in trie:
                    return
                else:
                    print(r,c)
                    if c+1<len(words[0]) and r<len(words):
                        helper(trie[words[r][c]],word+words[r][c+1],r,c+1)
                    if r+1<len(words)  and c<len(words[0]): 
                        helper(trie[words[r][c]],word+words[r+1][c],r+1,c)
                    if c>0:
                        helper(trie[words[r][c]],word+words[r][c-1],r,c-1)
                    if r>0:
                        helper(trie[words[r][c]],word+words[r-1][c],r-1,c)
        helper(trie.trie,"",0,0)
        return ans
