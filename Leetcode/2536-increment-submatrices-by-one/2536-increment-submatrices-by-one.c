/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** rangeAddQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize, int** returnColumnSizes) {
    int **mat=(int**)malloc(n * sizeof(int*));
    *returnColumnSizes=(int*)malloc(n * sizeof(int));
    *returnSize=n;

    for(int i=0; i<n; i++){
        mat[i]=(int*)calloc(n,sizeof(int));
        (*returnColumnSizes)[i]=n;
    }

    for(int a=0; a<queriesSize; a++){
        int r1=queries[a][0];
        int c1=queries[a][1];
        int r2=queries[a][2];
        int c2=queries[a][3];

        for (int r = r1; r <= r2; r++) {
            mat[r][c1] += 1;
            if (c2 + 1 < n) 
                mat[r][c2 + 1] -= 1;
        }
    }

    for (int i = 0; i < n; i++) {
        int running = 0;
        for (int j = 0; j < n; j++) {
            running += mat[i][j];
            mat[i][j] = running;
        }
    }

    return mat;
}