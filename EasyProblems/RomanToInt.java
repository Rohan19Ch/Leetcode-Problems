package EasyProblems;

/**
 * LeetCode Problem 13: Roman to Integer
 * 
 * Problem Description:
 * Given a roman numeral, convert it to an integer.
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
 * 
 * Symbol       Value
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 * 
 * For example, 2 is written as II in Roman numeral, just two ones added together.
 * 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
 * 
 * Roman numerals are usually written largest to smallest from left to right. However, the numeral for four 
 * is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract 
 * it making four. The same principle applies to the number nine, which is written as IX.
 * 
 * Time Complexity: O(n) where n is the length of the string
 * Space Complexity: O(1) - only using constant extra space
 * 
 * Examples:
 * Input: s = "III"
 * Output: 3
 * 
 * Input: s = "LVIII"
 * Output: 58 (L = 50, V= 5, III = 3)
 * 
 * Input: s = "MCMXC"
 * Output: 1994 (M = 1000, CM = 900, XC = 90)
 */

class RomanToInt {
    
    public int romanToInt(String s) {
        int result = 0;
        int prevValue = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int currentValue = getValue(s.charAt(i));
            
            if (currentValue > prevValue) {
                result += currentValue - 2 * prevValue;
            } else {
                result += currentValue;
            }
            
            prevValue = currentValue;
        }
        
        return result;
    }
    
    private int getValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
    
    public int romanToIntAlternative(String s) {
        int result = 0;
        int prevValue = 0;
        
        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = getValue(s.charAt(i));
            
            if (currentValue < prevValue) {
                result -= currentValue;
            } else {
                result += currentValue;
            }
            
            prevValue = currentValue;
        }
        
        return result;
    }

    public static void main(String[] args) {
        RomanToInt romanToInt = new RomanToInt();
        
        System.out.println("III = " + romanToInt.romanToInt("III"));
        System.out.println("IV = " + romanToInt.romanToInt("IV"));
        System.out.println("IX = " + romanToInt.romanToInt("IX"));
        System.out.println("LVIII = " + romanToInt.romanToInt("LVIII"));
        System.out.println("MCMXC = " + romanToInt.romanToInt("MCMXC"));
        
        System.out.println("\nAlternative solution:");
        System.out.println("III = " + romanToInt.romanToIntAlternative("III"));
        System.out.println("IV = " + romanToInt.romanToIntAlternative("IV"));
        System.out.println("MCMXC = " + romanToInt.romanToIntAlternative("MCMXC"));
    }
}