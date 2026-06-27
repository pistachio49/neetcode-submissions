class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            alph = [0] * 26

            for ch in word:
                alph[ord(ch) - 97] += 1

            new = ""
            for ind, val in enumerate(alph):
                if val:
                    new += f"{chr(ind+97)}{val}"

            d[new].append(word)

        # print(d.values())
        return list(d.values())