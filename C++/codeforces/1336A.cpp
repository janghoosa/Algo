#include <iostream>
#include <vector>
#include <algorithm>
typedef long long ll;
using namespace std;
vector<int> v[200005];
vector<int> route;
int visit[200005];

int dfs(int nd, int depth) {
    int i, to, go = 0, res = 0;
    // cout << "visit" << nd << '\n';
    visit[nd] = 1;
    for (i = 0; i < v[nd].size();i++){
        to = v[nd][i];
        if (visit[to] != 1) {
            res += dfs(to, depth + 1);
            go += 1;
        }
    }
    visit[nd] = 0;
    route.push_back(depth-res);
    if(go == 0){
        return 1;
    }
    return res + 1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i, in1, in2, a, b;
    ll ans = 0;
    cin >> in1 >> in2;
    for (i = 1; i < in1 ;i++){
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    dfs(1, 0);
    sort(route.begin(), route.end());
    for (i = route.size()-1; i >= 0 ;i--){
        // cout << i << " : "  << route[i] << " : " << in2 << '\n';
        ans += route[i];
        in2 -= 1;
        if(in2 == 0){
            break;
        }
    }
    cout << ans << '\n';
}