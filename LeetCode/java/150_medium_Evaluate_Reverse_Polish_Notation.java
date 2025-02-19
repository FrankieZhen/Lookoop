/**
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 */

// 2018-7-28
// 150. Evaluate Reverse Polish Notation
class 150_medium_Evaluate_Reverse_Polish_Notation {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int fir,sec;
        String token,thir,result;
        int lens = tokens.length;
        for (int i = 0; i <  lens; i++) {
            token = tokens[i];
            switch (token) {
                case "+":
                    sec = stack.pop();
                    fir = stack.pop();
                    result = Integer.parseInt(fir) + Integer.parseInt(sec);
                    thir = Integer.toString(result);
                    stack.push(thir);
                    break;
                case "-":
                    sec = stack.pop();
                    fir = stack.pop();
                    result = Integer.parseInt(fir) - Integer.parseInt(sec);
                    thir = Integer.toString(result);
                    stack.push(thir);
                    break;
                case "*":
                    sec = stack.pop();
                    fir = stack.pop();
                    result = Integer.parseInt(fir) * Integer.parseInt(sec);
                    thir = Integer.toString(result);
                    stack.push(thir);
                    break;
                case "/":
                    sec = stack.pop();
                    fir = stack.pop();
                    result = Integer.parseInt(fir) / Integer.parseInt(sec);
                    thir = Integer.toString(result);
                    stack.push(thir);
                    break;
                default:
                    stack.push(token);
                    break;
            }
        }
        thir = stack.pop();
        return Integer.parseInt(thir);
    }
}