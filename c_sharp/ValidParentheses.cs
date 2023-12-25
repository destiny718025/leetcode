public class Solution {
    public bool IsValid(string s) {
        var k = new Stack<char>();

        foreach(char c in s) {
            if (c == '(') {
                k.Push(')');
                continue;
            }

            if (c == '{') {
                k.Push('}');
                continue;
            }

            if (c == '[') {
                k.Push(']');
                continue;
            }

            if (k.Count == 0 || k.Pop() != c) {
                return false;
            }
        }

        return k.Count == 0;
    }
}