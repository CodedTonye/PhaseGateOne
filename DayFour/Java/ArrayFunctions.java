import java.util.Arrays;

public class TargetArray {

    public static int[] elementChecker(int[] array, int target) {
        
        int[] numbers = new int[2]; 
        target = 6;
       
        for (int count = 0; count <= array.length; count++) {
          
            for(int index = count + 1; index < array.length; index++) {
                if(array[count]  + array[index] == target) {
                    numbers[0] = array[count];     
                    numbers[1] = array[index];
                }
            }
        }
         return numbers;
    } 
    
    
    public static int[] elementCheckerTwo(int[] array, int target) {
        
        int[] number = new int[2]; 
        target = 12;
       
        for (int count = 0; count <= array.length; count++) {
          
            for(int index = count + 1; index < array.length; index++) {
                if(array[count]  + array[index] == target) {
                    number[0] = array[count];     
                    number[1] = array[index];
                }
            }
        }
         return number;
    } 
    
    
    public static int[] eliminateDuplicate(int[] array) {
        
        int[] arrayNumbers = {9, 5, 1, 9, 4, 5, 1, 7}; 
       
            for (int count = 0; count <= array.length; count++){
                for (int index = count + 1; index < array.length; index++){
                    if (array[count]!= -1 && array[count] == array[index]){
                        array[index] = -1;
                    }
                }
            }
            
            return arrayNumbers;
    }
    
    
    public static int[] getHighestAndLowest(int[] array) {
        
        int[] arrayNumber = {14, 9, 6, 5, 8, 10}; 
        
        int highest = arrayNumber[0];
        int lowest = arrayNumber[0];
       
            for (int count = 0; count <= array.length; count++){
                for (int index = count + 1; index < array.length; index++){
                    if (arrayNumber[1] > highest) {
                        highest = arrayNumber[1];  
                    }
                    else if (arrayNumber[2] > highest) {
                        highest = arrayNumber[2];
                    }
                    else if (arrayNumber[3] > highest) {
                        highest = arrayNumber[3];
                    }
                    else if (arrayNumber[4] > highest) {
                        highest = arrayNumber[4];
                    }
                    else if (arrayNumber[5] > highest) {
                        highest = arrayNumber[5];
                    }
                 }
            }
            
            
            return arrayNumber;
    }
}




















