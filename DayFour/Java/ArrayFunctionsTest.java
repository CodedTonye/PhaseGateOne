import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;


public class TargetArrayTest{

	@Test
	public void testThatTheAdditonOfTwoNumbersGives6(){
		int[] numbers = {8, 6, 12, 4, -2};
		int target = 6;
		
		
		int[] actual = TargetArray.elementChecker(numbers, target);

		
		int[] expected = {8, -2};
		assertArrayEquals(actual, expected);
	}
	
	
	@Test
	public void testThatTheAdditonOfTwoNumbersGives12(){
		int[] numbers = {1, 2, 5, 7, 6, 8, 9};
		int target = 12;
		
		
		int[] actual = TargetArray.elementChecker(numbers, target);

		
		int[] expected = {5, 7};
		assertArrayEquals(actual, expected);
	}
	
	
	@Test
	public void testThatDuplicateNumbersAreEliminated(){
		int[] arrayNumbers = {9, 5, 1, 9, 4, 5, 1, 7};
		
		int[] actual = TargetArray.eliminateDuplicate(arrayNumbers);

		int[] expected = {9, 5, 1, 4, 7};
		assertArrayEquals(actual, expected);
	}
}
