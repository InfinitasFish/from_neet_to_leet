from __future__ import annotations


# O(m * nlog(n)), bad
class SolutionSlow:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        ann_tps = {}
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            ann_tps[word] = ann_tps.get(word, []) + [strs[i]]

        return [g for g in ann_tps.values()]


# O(m * n)
class SolutionFast:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a hashmap of chars count keys and str values
        map = {}
        for s in strs:
            encoded_word = [0] * 26
            for char in s:
                encoded_word[ord(char) - ord('a')] += 1

            if tuple(encoded_word) in map:
                map[tuple(encoded_word)].append(s)
            else:
                map[tuple(encoded_word)] = [s]

        return list(map.values())


print(SolutionFast().groupAnagrams(["act","pots","tops","cat","stop","hat"]))

