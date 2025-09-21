package MediumProblems;

public class LongestPalindromicSubstring {

    public static String longestPalindrome(String s) {

        if(s.length() <= 1) {
            return s;
        }

        int iterator = 0;
        int stringLength = s.length();

        String longestPalindromeYet = "";
        String currentPalindrome = "";

        // Odd length palindromes
        while(iterator < stringLength - 1) {

            //Odd length considerations
            int left = iterator;
            int right = iterator;

            while(left >= 0 && right < stringLength && s.charAt(left) == s.charAt(right)) {


                left--;
                right++;
            }

            currentPalindrome = s.substring(left+1, right);

            if(currentPalindrome.length() > longestPalindromeYet.length()) {
                longestPalindromeYet = currentPalindrome;
            }

            //Even length considerations
            left = iterator;
            right = iterator+1;

            while(left >= 0 && right < stringLength && s.charAt(left) == s.charAt(right)) {


                left--;
                right++;
            }

            currentPalindrome = s.substring(left+1, right);

            if(currentPalindrome.length() > longestPalindromeYet.length()) {
                longestPalindromeYet = currentPalindrome;
            }

            iterator++;

        }


        if(longestPalindromeYet == "") {
            return s.substring(0,1);
        }

        return longestPalindromeYet;

    }

    public static void main(String args[]) {
        System.out.println(longestPalindrome(""));
    }


}
