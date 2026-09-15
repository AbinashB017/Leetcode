class Solution {
public:
    vector<int>nse(vector<int>& arr){
        stack<int>st;
        int n=arr.size();
        vector<int>ns(n);
        for(int i=n-1;i>=0;i--){
            while(!st.empty() && arr[i]<=arr[st.top()])st.pop();
            if(st.empty())ns[i]=n;
            else ns[i]=st.top();
            st.push(i);
        }
        return ns;
    }
    vector<int>pse(vector<int>& arr){
        stack<int>st;
        int n=arr.size();
        vector<int>ps(n);
        for(int i=0;i<n;i++){
            while(!st.empty() && arr[i]<arr[st.top()])st.pop();
            if(st.empty())ps[i]=-1;
            else ps[i]=st.top();
            st.push(i);

        }
        return ps;

    }
    int largestRectangleArea(vector<int>& heights) {
        int maxi=INT_MIN;
        int n=heights.size();
        vector<int>nsee=nse(heights);
        vector<int>psee=pse(heights);
        for(int i=0;i<n;i++){
            maxi=max(maxi,heights[i]*(nsee[i]-psee[i]-1));
        }
        return maxi;
    }
};