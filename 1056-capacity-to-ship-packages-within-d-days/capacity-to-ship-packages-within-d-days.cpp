class Solution {
public:
    int numdays(vector<int>& weights,int capacity){
        int day=1;
        int load=0;
        for(int i=0;i<weights.size();i++){
            if(load+weights[i]>capacity){
                day++;
                load=weights[i];
            }
            else{
                load+=weights[i];
            }
            
        }
        return day;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int n=weights.size();
        int low=*max_element(weights.begin(),weights.end());
        int sum=0;
        int ans=INT_MAX;
        for(auto it:weights){
            sum+=it;
        }
        int high=sum;
        while(low<=high){
            int mid=low+(high-low)/2;
            int nodays=numdays(weights,mid);
            if(nodays<=days){
                ans=min(ans,mid);
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return ans;
    }
};