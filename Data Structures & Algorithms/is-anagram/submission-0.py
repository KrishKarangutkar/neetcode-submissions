class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        s_str = "".join(s_list)
        t_str = "".join(t_list)
        if s_str == t_str:
            return True
        else:
            return False
