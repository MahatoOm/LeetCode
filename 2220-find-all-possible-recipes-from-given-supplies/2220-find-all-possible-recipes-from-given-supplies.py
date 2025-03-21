class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        def check_conditions(recipes , ingredient, n , supplies_dict ):
            nonlocal res 
            not_completed_dict = {}
            count = 0

            for i in range(n):
                check = True
                for ind in ingredient[i]:
                    if  ind not in  supplies_dict:
                        check = False
                        if recipes[i] not in not_completed_dict:
                            not_completed_dict[recipes[i]] = [ind]
                        else:
                            not_completed_dict[recipes[i]].append(ind)

                if check:
                    
                    res.append(recipes[i])
                    supplies_dict[recipes[i]] = True
            return not_completed_dict
        supplies_dict = {item : True for item in supplies}
        n = len(recipes)
        res = []
        not_completed_dict = check_conditions(recipes, ingredients, len(recipes) , supplies_dict)
        new = len(not_completed_dict)

        # print(supplies_dict)

        while new< n:
            org = len(not_completed_dict)
            not_completed_dict = check_conditions(list(not_completed_dict.keys()), list(not_completed_dict.values()),len(not_completed_dict) , supplies_dict)
            # print(ret)
            n = org
            new = len(not_completed_dict)
            


        

        return res