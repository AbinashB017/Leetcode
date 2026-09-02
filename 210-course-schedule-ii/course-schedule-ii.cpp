class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& prerequisites) {
        vector<vector<int>>adj(n);
        vector<int>indegree(n,0);
        queue<int>q;
        for(auto it :  prerequisites){
            int course=it[0];
            int prereq=it[1];
            adj[prereq].push_back(course);
            indegree[course]++;
        }

        for(int i=0;i<n;i++){
            if(indegree[i]==0){
                q.push(i);
            }
        }
        vector<int>topo;
        while(!q.empty()){
            int node=q.front();
            q.pop();
            topo.push_back(node);
            for(auto it:adj[node]){
                indegree[it]--;
                if(indegree[it]==0){
                    q.push(it);
                }
            }
        }
        if(topo.size()==n)return topo;
        return {};
    }
};