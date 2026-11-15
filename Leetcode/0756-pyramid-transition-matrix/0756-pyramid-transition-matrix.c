#include <stdbool.h>
#include <string.h>

#define MAX 256

// transition map: pair (A,B) -> possible top blocks
char trans[26][26][MAX];
int transCount[26][26];

bool dfs(char *row, int len) {
    if (len == 1)
        return true;

    char next[MAX];

    bool build(int idx) {
        if (idx == len - 1) {
            next[idx] = '\0';
            return dfs(next, len - 1);
        }

        int a = row[idx] - 'A';
        int b = row[idx + 1] - 'A';

        for (int i = 0; i < transCount[a][b]; i++) {
            next[idx] = trans[a][b][i];
            if (build(idx + 1))
                return true;
        }
        return false;
    }

    return build(0);
}

bool pyramidTransition(char* bottom, char** allowed, int allowedSize) {
    memset(transCount, 0, sizeof(transCount));

    // build allowed transitions
    for (int i = 0; i < allowedSize; i++) {
        int a = allowed[i][0] - 'A';
        int b = allowed[i][1] - 'A';
        char c = allowed[i][2];
        trans[a][b][transCount[a][b]++] = c;
    }

    return dfs(bottom, strlen(bottom));
}