int minMoves(int* nums, int numsSize) {
    int count=0;
    int l=0;
    for(int i=0; i<numsSize; i++){
        if(nums[i]>l){
            l=nums[i];
        }
    }
    for(int i=0; i<numsSize; i++){
        count=count+(l-nums[i]);
    }

    return count;
}