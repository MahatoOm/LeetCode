import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        stack = []  # stack to hold characters
        heap = []   # min-heap to find the smallest character before *

        # map from character to indices in the stack (for quick delete)
        import collections
        pos_map = collections.defaultdict(list)

        for ch in s:
            if ch == '*':
                # Remove the smallest character from the stack
                while heap:
                    smallest_char = heapq.heappop(heap)
                    if pos_map[smallest_char]:  # if any available to delete
                        idx = pos_map[smallest_char].pop()
                        stack[idx] = ''  # mark as removed
                        break
            else:
                # add to stack and record position
                pos_map[ch].append(len(stack))
                heapq.heappush(heap, ch)
                stack.append(ch)

        return ''.join([ch for ch in stack if ch != ''])
