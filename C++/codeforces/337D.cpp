#include <iostream>
#include <vector>
using namespace std;
vector<int> v[100005];
int inf[100005];
int Vis[100005];
int Dis[100005][3];

void dfs(int nd, int dis, int times) {
    // cout << nd << "  " << dis  << "  "<< times << '\n';
    int i, res;
    Vis[nd] = 1;
    Dis[nd][times] = dis;
    for (i = 0; i < v[nd].size(); i++) {
        int go = v[nd][i];
        if (Vis[go] != 1) {
            dfs(go, dis + 1, times);
        }
    }
    Vis[nd] = 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, d;
    int i, t1, t2, ans;
    cin >> n >> m >> d;
    for (i = 0; i < m; i++) {
        cin >> t1;
        inf[t1] = 1;
    }
    for (i = 1; i < n; i++) {
        cin >> t1 >> t2;
        v[t1].push_back(t2);
        v[t2].push_back(t1);
    }
    dfs(1, 0, 0);
    t1 = 0;
    for (i = 1; i <= n; i++) {
        if (inf[i] && (Dis[t1][0] <= Dis[i][0])) {
            t1 = i;
        };
    }
    dfs(t1, 0, 1);
    t2 = 0;
    for (i = 1; i <= n; i++) {
        if (inf[i] && (Dis[t2][1] <= Dis[i][1])) {
            t2 = i;
        };
    }
    dfs(t2, 0, 2);
    ans = 0;
    for (i = 1; i <= n; i++) {
        // cout << i  << "  :  " << Dis[i][1] << "  :  " << Dis[i][2] << '\n';
        if ((Dis[i][1] <= d) && (Dis[i][2] <= d)) {
            
            ans++;
        }
    }
    cout << ans << '\n';
}