package MediumProblems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class LetterCombinationsOfAPhoneNumber {

    public  List<String> answer = new ArrayList<>();

    public List<String> letterCombinations(String digits) {

        if (digits.length() == 0) {
            return answer;
        }

        HashMap<String, List<String>> numToAlpha = new HashMap<>();

        numToAlpha.put("2", Arrays.asList("a", "b", "c"));
        numToAlpha.put("3", Arrays.asList("d", "e", "f"));
        numToAlpha.put("5", Arrays.asList("j", "k", "l"));
        numToAlpha.put("6", Arrays.asList("m", "n", "o"));
        numToAlpha.put("4", Arrays.asList("g", "h", "i"));
        numToAlpha.put("7", Arrays.asList("p", "q", "r", "s"));
        numToAlpha.put("8", Arrays.asList("t", "u", "v"));
        numToAlpha.put("9", Arrays.asList("w", "x", "y", "z"));


        return answer;
    }

}
