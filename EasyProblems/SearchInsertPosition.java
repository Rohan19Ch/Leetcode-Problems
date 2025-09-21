class Solution {
    public int lengthOfLastWord(String s) {

        s = s.trim();

        int index = s.length() - 1;

        while(index >= 0) {
            if(s.charAt(index) == ' ') {
                return s.length() - index;
            }

            index--;
        }

        if(index == -1) {
            return s.length();
        }

        return 0;

    }
}