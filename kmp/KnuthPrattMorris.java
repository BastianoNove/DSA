import java.util.ArrayList;
import java.util.Arrays;

class KnuthPrattMorris {
    public static void main(String args[]) {
        KnuthPrattMorris test = new KnuthPrattMorris();
        String pattern = "abba";
        String text = "abbababbabbbabbaaaaabbabbbabbabbbabbbba";
        System.out.println("Pattern:");
        System.out.println(pattern);
        System.out.println("Text:");
        System.out.println(text);
        ArrayList<Integer> matches = test.kpm_matcher(text, pattern);
        for(Integer start: matches) {
            System.out.println("Found match starting at index: " + start);
        }
    }

    public int[] failure_function(String pattern) {
        int m = pattern.length();
        int[] pi = new int[m];
        pi[0] = 0;
        int k = 0;
        for( int q = 1; q < m; q++) {
            while (k > 0 && pattern.charAt(k) != pattern.charAt(q)) {
                k = pi[k];
            }
            if (pattern.charAt(k) == pattern.charAt(q)) {
                k = k + 1;
            }
            pi[q] = k;
        }
        System.out.println("pi is " + Arrays.toString(pi));
        return pi;
    }

    public ArrayList<Integer> kpm_matcher(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int[] pi = failure_function(pattern);
        int q = 0;
        ArrayList<Integer> matches = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            while (q > 0 && pattern.charAt(q) != text.charAt(i)) {
                q = pi[q];
            }
            if (pattern.charAt(q) == text.charAt(i)) {
                q = q + 1;
            }
            if (q == m) {
                matches.add(i-(m-1));
                q = pi[q-1];
            }
        }
        return matches;
    }
}
