#include <math.h>
int countMajoritySubarrays(int* nums, int numsSize, int target) {
    int count=0;
    for(int i=0; i<numsSize; i++){
        int targetc=0;
        int totalc=0;
        for(int j=i; j<numsSize; j++){
            totalc++;
            if(nums[j]==target){
                targetc++;
            }
            if(targetc>totalc/2){
                count++;
            }
        }
    }
    
    return count;
}