// Longest Path In Directed Graph
// https://www.codingninjas.com/codestudio/problems/longest-path-in-directed-graph_1172157

int Visited[10005];
vector<int> D;
vector<pair<int, int>> E[10005];

void dfs(int nd){
    int i;
    Visited[nd] = 1;
    for(i=0;i<E[nd].size();i++){
        if(Visited[E[nd][i].first] == 0){
            dfs(E[nd][i].first);            
        }
        if(D[E[nd][i].first] != -1){
            D[nd] = max(D[nd],D[E[nd][i].first] + E[nd][i].second);
        }
    }
};


vector<int> findMaxDistances(int n, int src, vector<vector<int>> &edges) {
	/*
        Parameters of this function are -:
        'n': Number of nodes in given directed graph.
        'src': Source node.
        'edges': list of all edges, such that the 'ith edge is a 
                 directed edge from 'edges[i][0]' to 'edges[i][1]' and have weight 'edges[i][2]'. 
    */

    // Write your code here.
    int i, j;
    D.clear(); 
    for (i=0;i<n;i++){
        Visited[i] = 0;
        D.push_back(-1);
        E[i].clear();
    }
    for (j=0;j<edges.size();j++){
        E[edges[j][1]].push_back(make_pair(edges[j][0],edges[j][2]));
    }
    D[src] = 0;
    for (i=0;i<n;i++){
        if(Visited[i]==0){
            dfs(i);
        }
    }
    return D;
}