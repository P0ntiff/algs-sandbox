package primitives;
/**
     * Given an integer represented as a string under base b1, convert it to base b2 and return it as a string.

    Input-Output

    Example 1

    Input: ("12", 10, 2)
    Output: "1100"
    Explanation: We are converting "12" which is under base 10 (decimal) to base 2 (binary)
    Constraints

    2 <= b1 <= 36
    2 <= b2 <= 36
    For base 2 to base 10 use digits 0-9 to represent digits
    For base 11 to base 36 use alphabet characters A-Z to represent digits (case insensitive)
 * 
 */
public class ChangingBase {
    public static void main(String[] args) {
        // System.out.println("Numeric value of A in base 16 is " + Character.digit('A', 16));
        // System.out.println("Numeric value of 8 in base 8 is " + Character.digit('8', 8));
        // System.out.println("Numeric value of B in base 12 is " + Character.digit('B', 12));
        System.out.println("Input: ('12', 10, 2)");
        System.out.println("Output: " + change_base("12", 10, 2));
    
        System.out.println("Input: ('154', 10, 12)");
        System.out.println("Output: " + change_base("154", 10, 12));
    
    }

    public static String change_base(String input, int b1, int b2) {
        boolean isNegative = input.startsWith("-");
        // convert to intermediary integer (take digit of 1/A/B and convert it to 1/10/12)
        int maxPower = input.length() - 1;
        int startIndex = isNegative ? 1 : 0;

        int inputAsInteger = 0;
        for (int i = startIndex; i < input.length(); i++) {
            char digit = input.charAt(i);
            int placeValue = Character.digit(digit, b1);
            inputAsInteger += placeValue * Math.pow(b1, maxPower - i);
        }

        // build output by constructing one digit at a time, prepend each digit and reduce the integer piece by piece
        StringBuilder output = new StringBuilder();
        while (inputAsInteger > 0) {
            int remainder = (int) inputAsInteger % b2;
            inputAsInteger /= b2;

            output.insert(0, Character.forDigit(remainder, b2));
        }

        if (isNegative) {
            output.insert(0, '-');
        }

        return output.toString();
    }
}