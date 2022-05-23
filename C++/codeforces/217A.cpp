#include <iostream>
#include <vector>
using namespace std;

vector<int> E[1000];

int V[1000];
int X[1000], Y[1000];

void dfs(int nd){
    int i, s;
    s = E[nd].size();
    for (i = 0; i < s;i++){
        if(V[E[nd][i]]==0){
            V[E[nd][i]] = 1;
            dfs(E[nd][i]);
        }
    }
}

int main(){
    int i, j, n, ans;
    cin >> n;
    for (i = 0; i < n;i++){
        cin >> X[i] >> Y[i];
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (X[i] == X[j] ||Y[i]==Y[j]){
                E[i].push_back(j);
                E[j].push_back(i);
            }
        }
    }
    ans = 0;
    for (i = 0; i < n;i++){
        if(V[i]==0){
            ans++;
            dfs(i);
        }
    }
    ans--;
    cout << ans << '\n';
}