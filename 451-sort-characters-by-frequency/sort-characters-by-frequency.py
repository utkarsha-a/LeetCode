class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        sorted_char = sorted(freq_map.keys(), key = lambda x : -freq_map[x])
        res = ''.join(char * freq_map[char] for char in sorted_char)
        return res
        