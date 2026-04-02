class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        db = {}

        for i, word in enumerate(strs):
            temp = ''.join(sorted(word))
            
            if temp in db:
                db[temp].append(word)
            else:
                db[temp] = [word]
        
        output = []
        for key, value in db.items():
            output.append(value)
        
        return output