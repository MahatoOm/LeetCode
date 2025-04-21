import java.util.Scanner;
class Solution {
    public boolean checkPerfectNumber(int num) {
        // Write your code here

        // int start = 2;
        Scanner input = new Scanner(System.in);
        // System.out.print("Enter a maximum number >> ");
        int end = num;
        int total = 0;
      
            
        for (int st = 1 ; st < end; st ++){
        if ( end % st == 0){
                total += st;
            }
        }
        // if (total == end){
        // System.out.println("The number " + total + " is perfect");
        // return True ;
        // }
        
        

    return (total == end) ;

    }
}
    