#include <iostream>
#include <vector>
using namespace std;
class Node {
public:
    int pt;
    int child;
    int dsum;
    int ans;
    vector<int> Road;
    vector<int> Dir;
    vector<int> Res;
};
Node Nd[200005];
int vis[200005];

int dfs1(int nd, int pt){
    int i, size, res;
    Nd[nd].pt = pt;
    Nd[nd].child = 0;
    size = Nd[nd].Road.size();
    for (i = 0; i < size; i++) {
        if( Nd[nd].Road[i] != pt ){
            Nd[nd].child += 1;
            Nd[nd].Res[i] = dfs1(Nd[nd].Road[i], nd);
        }
    }
    res = 0;
    for (i = 0; i < size; i++) {
        if( Nd[nd].Road[i] != pt ){
            res += Nd[nd].Res[i] + Nd[nd].Dir[i];
        }
    }
    Nd[nd].dsum = res;
    return res;
}

void dfs2(int nd, int pt, int uans, int dr){
    int i, size;
    size = Nd[nd].Road.size();
    if (pt == 0) {
        Nd[nd].ans = Nd[nd].dsum;
    } else {
        if(dr == 0)
            Nd[nd].ans = uans + 1;
        else
            Nd[nd].ans = uans - 1;
    }
    for (i = 0; i < size; i++) {
        if( Nd[nd].Road[i] != pt ){
            dfs2(Nd[nd].Road[i], nd, Nd[nd].ans, Nd[nd].Dir[i]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, i, ans, t1, t2;
    cin >> n;
    for (i = 0; i < n - 1;i++){
        cin >> t1 >> t2;
        Nd[t1].Road.push_back(t2);
        Nd[t1].Dir.push_back(0);
        Nd[t1].Res.push_back(0);
        Nd[t2].Road.push_back(t1);
        Nd[t2].Dir.push_back(1);
        Nd[t2].Res.push_back(0);
    }
    dfs1(1, 0);
    dfs2(1, 0, 0, 0);
    ans = 10000000;
    for (i = 1; i <= n; i++) {
        ans = min(ans, Nd[i].ans);
        // cout << Nd[i].ans << "weight" << '\n';
    }
    cout << ans << '\n';
    for (i = 1; i <= n; i++) {
        if (i > 1) cout << " ";
        if (ans == Nd[i].ans) cout << i;
        // cout << Nd[i].ans << "weight" << '\n';
    }
    cout << '\n';
}