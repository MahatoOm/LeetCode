class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        # count_s = defaultdict(int)

        # for data in set(s):
        #     count_s[data] = s.count(data)
        # print(count_s)
        left = 0
        right = n- 1
        res = []
        visites = set()
        def check_condition(l , r, last_occur):
            # right_idx = last_occur

            while l <= last_occur :
                data = s[l]

                right_idx = s.rfind(data)
                if right_idx > last_occur :
                    last_occur = right_idx

                l+=1
            return last_occur



        while left <= right:

            if s.find(s[left]) == s.rfind(s[left]):
                res.append(1)
                left += 1  
            else:  
                val = check_condition(left + 1, right, s.rfind(s[left]))
                res.append(val - left + 1)
                left = val + 1


        return res

