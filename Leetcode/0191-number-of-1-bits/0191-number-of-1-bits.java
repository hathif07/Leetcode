class Solution {
    public int hammingWeight(int n) {
        String nb=Integer.toBinaryString(n);
        int count=0;
        n=nb.length();
        for(int i=0; i<n;i++){
            if(nb.charAt(i)=='1'){
                count++;
            }
        }
        return count;
    }
}