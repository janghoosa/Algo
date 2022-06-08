#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class tpl {
   public:
    int b, w, tr;
};
vector<tpl> ED[300005];
long long SL[300005];
int Visit[300005];

int n, m, k;
int ans = 0;
class pkt {
   public:
    long long l;
    int w, b, tr;
    bool operator < (const pkt& k) const {
        // l이 같을때 train이 있는 것을 크게 하여 뒤로 보냄
        if (l == k.l && tr == 1 && k.tr == 0){
            return true;
        } else {
            return l > k.l;
        }
        
    }
};

priority_queue<pkt> Q;

void Dij(int s) {
    pkt p, q; 
    int i;
    // 시작은 0번 패킷에서 시작
    p.l = 0;
    p.w = 0;
    p.b = s;
    p.tr = 0;
    Q.push(p);
    while (!Q.empty()) {
        p = Q.top();
        Q.pop();
        if (Visit[p.b]) {
            continue;
        }
        Visit[p.b] = 1;
        // cout << "visit " << p.b << ' ' << p.w << ' ' << p.tr << ' ';
        SL[p.b] = p.l;
        // 방문한 패킷이 트레인이면 ans++
        if (p.tr > 0) {
            ans++;
        }
        // 붙어있는 모든 엣지들에 대해 패킷을 만듬
        for (i = 0; i < ED[p.b].size(); i++) {
            q.l = SL[p.b] + ED[p.b][i].w;
            q.w = ED[p.b][i].w;
            q.b = ED[p.b][i].b;
            q.tr = ED[p.b][i].tr;
            Q.push(q);
        }
    }
};

int main() {
    int i, j, A, B, W;
    tpl tmp;
    cin >> n >> m >> k;
    // EDGE 추가 
    for (i = 1; i <= m; i++) {
        cin >> A >> B >> W;
        tmp.b = B, tmp.w = W, tmp.tr = 0;
        ED[A].push_back(tmp);
    }
    // train 추가
    for (i = 1; i <= k; i++) {
        cin >> A >> W;
        tmp.b = A, tmp.w = W, tmp.tr = 1;
        ED[1].push_back(tmp);
    }
    Dij(1);
    cout << k-ans << '\n';
    return 0;
}