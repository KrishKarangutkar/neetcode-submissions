class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        lenth = len(check)
        for str in strs:
            while True:
                if check == str:
                    break
                elif check in str:
                    break
                elif len(check) == 0:
                    return ""
                else:
                    check = check[0:lenth-1]
                    lenth -= 1
        return check