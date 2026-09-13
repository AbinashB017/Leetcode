class Solution {
    void dfs(int row,int col,vector<vector<char>>& board,vector<vector<int>>& vis){
        int m=board.size();
        int n=board[0].size();
        vis[row][col]=1;
        int dr[]={-1,0,1,0};
        int dc[]={0,1,0,-1};
        for(int i=0;i<4;i++){
            int nr=row+dr[i];
            int nc=col+dc[i];
            if((nr>=0 && nr<m)&& (nc>=0 && nc<n) && (board[nr][nc]=='O') && (vis[nr][nc]!=1)){
                dfs(nr,nc,board,vis);
            }
        }
    }
public:
    void solve(vector<vector<char>>& board) {
        int m=board.size();
        int n=board[0].size();
        vector<vector<int>>vis(m,vector<int>(n));
        for(int i=0;i<n;i++){
            if(board[0][i]=='O' && vis[0][i]!=1){
                dfs(0,i,board,vis);
            }
            if(board[m-1][i]=='O' && vis[m-1][i]!=1){
                dfs(m-1,i,board,vis);
            }
        }
        for(int i=0;i<m;i++){
            if(board[i][0]=='O' && vis[i][0]!=1){
                dfs(i,0,board,vis);
            }
            if(board[i][n-1]=='O' && vis[i][n-1]!=1){
                dfs(i,n-1,board,vis);
            }
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]=='O' && !vis[i][j]){
                    board[i][j]='X';
                }
            }
        }
    }
};