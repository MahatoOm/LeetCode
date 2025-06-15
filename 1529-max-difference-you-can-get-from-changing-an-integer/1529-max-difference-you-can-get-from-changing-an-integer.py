class Solution:
    def maxDiff(self, num: int) -> int:

        lst = list(str(num))
        if len(lst) == 1:
            return 8

        if len(set(lst)) == 1:
            return  int("".join(['8'] * len(lst)))
  
        x_a = '-1'
        y_a = '-1'
        x_b = '-1'
        y_b = '-1'
      
        b_should_not_be_one = False
        for i in range(len(lst)):
            if i == 0: 
                if lst[i] != '1' :          
                    x_b = (lst[i])
                    y_b = '1'
                else:
                    b_should_not_be_one = True

                
            if lst[i] != '9' and x_a == '-1':
                x_a = (lst[i])
                y_a = '9'
            if lst[i] != '0' and i != 0  and x_b == '-1':
                if b_should_not_be_one and lst[i] == '1':
                    continue
                x_b = (lst[i])
                y_b = '0'


            if (x_a != '-1') and (y_a != '-1') and  (x_b != '-1') and (y_b != '-1'):
                break

        # x = [element for element in lst if element != x_a else y_a ]
        # y = [element for element in lst if element != x_b else y_b ]
        x = ''
        y = ''
        for i, element in enumerate(lst):

            if element == x_a :
                x += (y_a )
            else:
                x += (element)

            if element == x_b  :
                y += (y_b )
            else:
                y += (element )

        return int(x) - int(y)

