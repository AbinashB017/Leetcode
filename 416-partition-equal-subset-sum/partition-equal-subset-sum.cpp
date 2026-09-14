class Solution {
    int solve(int index,int target,vector<int>& nums,vector<vector<int>>& dp){
        if(index==0)return nums[index]==target;
        if(target==0)return true;
        if(dp[index][target]!=-1)return dp[index][target];
        int take=false;
        if(nums[index]<=target){
            take=solve(index-1,target-nums[index],nums,dp);
        }
        int nottake=solve(index-1,target,nums,dp);
        return dp[index][target]=(take||nottake);
    }
public:
    bool canPartition(vector<int>& nums) {
        int n=nums.size();
        int sum=0;
        for(auto it:nums){
            sum+=it;
        }
        if(sum%2==1)return false;
        int target=sum/2;
        vector<vector<int>>dp(n,vector<int>(target+1,-1));
        return solve(n-1,target,nums,dp);
        
    }
};