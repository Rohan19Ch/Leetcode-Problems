package EasyProblems;

public class NeedleInHaystack {
    public static int strStr(String haystack, String needle) {

        if(!haystack.contains(needle)) {
            return -1;
        }

        int initial = 0;
        int later = needle.length() - 1;
        String substring;

        while(later < haystack.length()) {

            substring = haystack.substring(initial, later+1);

            if(substring.equals(needle)) {
                return initial;
            }

            initial++;
            later++;

        }

        return -1;
    }

    public  static void main(String args[]) {
        System.out.println(strStr("sadbutsad", "sad"));
    }
}
