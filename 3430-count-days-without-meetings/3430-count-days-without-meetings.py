class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        

        # day_calander = [True] *(days+1)
        # print(day_calander)

        meetings = sorted(meetings, key = lambda x: x[0])
        # print(meetings)

        current_day = 1
        idx = 0
        free_days = 0
        
        while current_day < days+1:

            if idx < len(meetings) and ( current_day >= meetings[idx][0] and current_day<=meetings[idx][1]):
                current_day = meetings[idx][1] + 1
                idx += 1
                
            elif idx<len(meetings) and current_day < meetings[idx][0]:
                free_days += meetings[idx][0]-current_day
                current_day = meetings[idx][0]
                
            elif idx<len(meetings) and current_day > meetings[idx][1]:
                idx +=1
            elif idx >= len(meetings):
                diff_days = days - current_day + 1
                free_days += diff_days
                break
            else:
                current_day +=1
                free_days +=1

        


        return free_days