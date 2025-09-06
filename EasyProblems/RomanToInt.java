package EasyProblems;

/**
 * LeetCode Problem 13: Roman to Integer
 * 
 * Problem Description:
 * Given a roman numeral, convert it to an integer.
 * 
 * Time Complexity: O(n) where n is the length of the string
 * Space Complexity: O(1) - only using constant extra space
 */


import java.util.HashMap;

class RomanToInt {
    public int romanToInt(String s) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("I", 1);
        map.put("V", 5);
        map.put("X", 10);
        map.put("L", 50);
        map.put("C", 100);
        map.put("D", 500);
        map.put("M", 1000);

        int res = 0;
        int pre = 0;
        for (int i = 0; i < s.length(); i++) {
            int curr = map.get(String.valueOf(s.charAt(i)));
            if (curr > pre) {
                res += curr - 2 * pre;
            } else {
                res += curr;
            }
            pre = curr;
        }
        return res;
    }


    public static void main(String[] args) {
        RomanToInt romanToInt = new RomanToInt();
        System.out.println(romanToInt.romanToInt("III"));
        System.out.println(romanToInt.romanToInt("IV"));
        System.out.println(romanToInt.romanToInt("IX"));
    }
}