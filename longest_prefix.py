class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""
        first_word = strs[0]
        for charIdx in range(len(first_word)): #helps us pick the character we are looking at
            for wordIndex in range(1, len(strs)): #helps us pick the word we are looking at
                if len(strs[wordIndex]) <= charIdx:
                    return common_prefix
                if strs[wordIndex][charIdx] != first_word[charIdx]: #if chars done match then return the common prefix
                    return common_prefix
            common_prefix += first_word[charIdx]
        return common_prefix
    
def main():
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))

if __name__ == "__main__":
    main()