#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class tpl {
   public:
    int b, w, EN;
}; // 트리플로 b: 이전 노드, w: 비용, EN: EdgeNumber
vector<tpl> ED[300005];

long long SL[300005]; // Shortest Length
int ENU[300005]; // 노드마다 자기가 고른 노드
int ELE[300005]; // 고른 엣지의 비용
int Visit[300005]; // finalize 되었는지 확인용

int n, m, u;

class pkt { //패킷을 통해 다익스트라,
   public:
    long long l; // 그전까지 비용
    int w, a, b, EN; //  w: weight, a: 이전노드, b: 다음노드, EN: EdgeNumber
    bool operator < (const pkt& k) const {
        return l > k.l;
    }
}; // < 연산자 재정의를 통해 priority_queue에서 작은게 먼저 나오게 함

priority_queue<pkt> Q;

void Dij(int s) { // s에서 시작
    pkt p, q; // p는 Q에서 꺼낸 패킷, q는 보낼 패킷 
    int i;
    p.l = 0;
    p.w = 0;
    p.a = 0;
    p.b = s;
    p.EN = 0;
    Q.push(p); // S에서 오는 0짜리 패킷 시작
    while (!Q.empty()) {
        p = Q.top();
        Q.pop();
        if (Visit[p.b]) {
            //
            if (p.l == SL[p.b] && p.w < ELE[p.b]) { 
                ELE[p.b] = p.w;
                ENU[p.b] = p.EN;
            }
            // 원래는 이부분이 없음, visit면 shortest라서 작업을 안한다.
            // l의 길이를 보고 w가 같으면 EN을 바꿔줌
            continue;
        }
        Visit[p.b] = 1;
        SL[p.b] = p.l;
        ENU[p.b] = p.EN;
        ELE[p.b] = p.w;
        // 붙어있는 모든 엣지들에 대해 패킷을 만듬
        for (i = 0; i < ED[p.b].size(); i++) {
            q.l = SL[p.b] + ED[p.b][i].w;
            q.w = ED[p.b][i].w;
            q.a = p.b;
            q.b = ED[p.b][i].b;
            q.EN = ED[p.b][i].EN;
            Q.push(q);
        }
    }
};

int main() {
    int i, j, A, B, W;
    long long ans;
    tpl tmp;
    cin >> n >> m;
    for (i = 1; i <= m; i++) {
        cin >> A >> B >> W;
        tmp.b = B, tmp.w = W, tmp.EN = i;
        ED[A].push_back(tmp);
        tmp.b = A, tmp.w = W, tmp.EN = i;
        ED[B].push_back(tmp);
    }
    cin >> u;
    Dij(u);
    ans = 0;
    for (i = 1; i <= n; i++) {
        if (i != u)
            ans += ELE[i];
    }
    cout << ans << '\n';
    for (i = 1; i <= n; i++) {
        if (i != u)
            cout << ENU[i]<< ' ';
    }
    cout << '\n';
    return 0;
}