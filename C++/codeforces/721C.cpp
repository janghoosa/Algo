// 10번에서 오류남... 왜?

#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

class tpl {
   public:
    int a, b, w;
}; // 트리플로 b: 이전 노드, w: 비용, EN: EdgeNumber

vector<tpl> G[5005];
int dp[5005][5005];
int ne[5005][5005];
int visit[5005];

int n, m, T;

void dfs(int nd) {
    int i, j;
    tpl to;
    if (visit[nd]) {
        return;
    }
    visit[nd] = 1;
    for (i = 0; i < G[nd].size();i++){
        to = G[nd][i];
        dfs(to.b);
        for (j = 2; j <= n;j++){
            if(dp[to.b][j-1]+to.w < dp[nd][j]){
                dp[nd][j] = dp[to.b][j - 1] + G[nd][i].w;
                ne[nd][j] = to.b;
            }
        }
    }
}

int main() {
    int A, B, t, i, ans, rt;
    tpl tmp;
    cin >> n >> m >> T;
    for(i=1;i<=n;i++)
        G[i].clear();
    for (i = 0; i < m; i++) {
        cin >> A >> B >> t;
        tmp.b = B;
        tmp.w = t;
        tmp.a = A;
        G[A].push_back(tmp);
    };
    memset(dp, 1000000005, sizeof(dp));
    memset(visit, 0, sizeof(visit));
    visit[n] = 1;
    dp[n][1] = 0;
    dfs(1);
    for (i = n;;i--){
        if(dp[1][i]<=T){
            ans = i;
            break;
        }
    }
    cout << ans << '\n';
    rt=1;
    cout << rt << ' ';
    while (rt != n) {
        rt=ne[rt][ans--];
        cout << rt << ' ';
    }
    cout << '\n';
    return 0;
}