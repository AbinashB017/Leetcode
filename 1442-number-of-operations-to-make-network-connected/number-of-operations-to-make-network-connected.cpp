class DisjointSet{
public:
vector<int>parent,size;
    DisjointSet(int n){
        size.resize(n+1);
        parent.resize(n+1);
        for(int i=0;i<=n;i++){
            parent[i]=i;
            size[i]=1;
        }
    }
    int findultparent(int node){
        if(parent[node]==node)return node;
        return parent[node]=findultparent(parent[node]);
    }

    void unionbysize(int u,int v){
        int ult_u=findultparent(u);
        int ult_v=findultparent(v);
        if(ult_u==ult_v)return;
        if(size[ult_u]>size[ult_v]){
            parent[ult_v]=ult_u;
            size[ult_u]+=size[ult_v];
        }
        else{
            parent[ult_u]=ult_v;
            size[ult_v]+=size[ult_u];
        }
    }

};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        DisjointSet ds(n);
        int extra=0;
        for(auto it : connections){
            int a=it[0];
            int b=it[1];
            if(ds.findultparent(a)==ds.findultparent(b)){
                extra++;
            }
            else{
                ds.unionbysize(a,b);
            }
        }
        int nc=0;
        for(int i=0;i<n;i++){
            if(ds.parent[i]==i){
                nc+=1;
            }
        }
        int ans=nc-1;
        if(extra>=ans)return ans;
        return -1;
    }
};