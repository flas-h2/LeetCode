class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.string = s
        words = []
        for word in self.string.split():
            if word.isalpha():
                words.append(word)
        length = len(words[-1])
        return length
        

solution = Solution()
solution.lengthOfLastWord("   fly me   to   the moon  ")

        