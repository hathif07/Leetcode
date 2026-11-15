#include <stdio.h>

int countBinarySubstrings(char *s) {
    int prev = 0, curr = 1;
    int result = 0;

    for (int i = 1; s[i] != '\0'; i++) {
        if (s[i] == s[i - 1]) {
            curr++;
        } else {
            result += (prev < curr) ? prev : curr;
            prev = curr;
            curr = 1;
        }
    }

    result += (prev < curr) ? prev : curr;

    return result;
}