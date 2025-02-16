class Solution:
    def constructDistancedSequence(self, target_number: int) -> List[int]:
     
        # Initialize the result sequence with size 2*n - 1 filled with 0s
        result_sequence = [0] * (target_number * 2 - 1)

        # Keep track of which numbers are already placed in the sequence
        is_number_used = [False] * (target_number + 1)

        # Start recursive backtracking to construct the sequence
        self.find_lexicographically_largest_sequence(
            0, result_sequence, is_number_used, target_number
        )

        return result_sequence

    # Recursive function to generate the desired sequence
    def find_lexicographically_largest_sequence(
        self, current_index, result_sequence, is_number_used, target_number
    ):
        # If we have filled all positions, return true indicating success
        if current_index == len(result_sequence):
            return True

        # If the current position is already filled, move to the next index
        if result_sequence[current_index] != 0:
            return self.find_lexicographically_largest_sequence(
                current_index + 1,
                result_sequence,
                is_number_used,
                target_number,
            )

        # Attempt to place numbers from targetNumber to 1 for a
        # lexicographically largest result
        for number_to_place in range(target_number, 0, -1):
            if is_number_used[number_to_place]:
                continue

            is_number_used[number_to_place] = True
            result_sequence[current_index] = number_to_place

            # If placing number 1, move to the next index directly
            if number_to_place == 1:
                if self.find_lexicographically_largest_sequence(
                    current_index + 1,
                    result_sequence,
                    is_number_used,
                    target_number,
                ):
                    return True
            # Place larger numbers at two positions if valid
            elif (
                current_index + number_to_place < len(result_sequence)
                and result_sequence[current_index + number_to_place] == 0
            ):
                result_sequence[current_index + number_to_place] = (
                    number_to_place
                )

                if self.find_lexicographically_largest_sequence(
                    current_index + 1,
                    result_sequence,
                    is_number_used,
                    target_number,
                ):
                    return True

                # Undo the placement for backtracking
                result_sequence[current_index + number_to_place] = 0

            # Undo current placement and mark the number as unused
            result_sequence[current_index] = 0
            is_number_used[number_to_place] = False

        return False





        # total_items = (2 * n) -1
        # if total_items == 1:
        #     return [1]
        # a =[0] * total_items

        # start_value = n
        # i = 0
        # j = n
        # while start_value > 0:
        #     a[i] = start_value
        #     if start_value == 1:
        #         a[j] = n-1
        #         a[j+n-1] = n-1
        #         break
        #     if start_value == 2:
        #         a[i+1] = n-1
        #         a[i+n] = n-1
        #         a[j] = start_value
        #         break
            
        #     a[j] = start_value
        #     i+=1
        #     j-=1
        #     start_value -= 2


        # start_value = n-3
        # last_i = total_items - 1
        # last_j = last_i - start_value
        # while start_value > 0:

        #     a[last_i] = start_value
        #     if start_value == 1:
        #         break
            
        #     a[last_j] = start_value
        #     if start_value ==2 :
        #         break
        #     last_i -= 1
        #     last_j += 1
        #     start_value -=2

        # return a