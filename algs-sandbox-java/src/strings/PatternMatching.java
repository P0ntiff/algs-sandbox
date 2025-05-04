package strings;

import java.util.HashMap;

public class PatternMatching {
    //  * Pattern Matching
    //     Given a list of strings and a pattern string, return a list of all of the strings in the provided list that match the pattern of the pattern string.

    //     Input-Output

    //     Example 1

    //     Input: words = ["aa", "bb"], pattern = "cc"
    //     Output: ["aa", "bb"]
    //     Explanation: Both strings repeat letters just as the pattern string does.
    //     Example 2

    //     Input: words = ["aac", "bbc", "bcb", "yzy"], pattern = "ghg"
    //     Output: ["bcb", "yzy"]
    //     Example 3

    //     Input: words = ["aa", "bb"], pattern = "zy"
    //     Output: []

    public static void main(String[] args) {
        String[] words = {"aa", "bb"};
        String pattern = "zy";

        System.out.println(patternMatch(words, pattern));

    }

    private static String[] patternMatch(String[] words, String pattern) {

        HashMap<Character, Character> pToW = new HashMap<>();

        for (String w: words) {

        }


    }



}
