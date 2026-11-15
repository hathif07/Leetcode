int dfs(struct TreeNode* root, int curr) {
    if (root == NULL)
        return 0;

    curr = (curr << 1) | root->val;

    // If leaf node
    if (root->left == NULL && root->right == NULL)
        return curr;

    return dfs(root->left, curr) + dfs(root->right, curr);
}

int sumRootToLeaf(struct TreeNode* root) {
    return dfs(root, 0);
}