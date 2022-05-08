#include <iostream>
using namespace std;
typedef long long ll;

ll n, m, L, R, V;
ll A[200005];
class Node {
   public:
    ll mn, upd;
    ll Left, Right;
};
Node T[1000000];

ll build(ll nd, ll lf, ll rg) {
    ll mid, lr, rr;
    T[nd].Left = lf;
    T[nd].Right = rg;
    if (lf == rg) {
        T[nd].mn = A[lf];
        T[nd].upd = 0;
    } else {
        mid = (lf + rg) / 2;
        lr = build(nd * 2, lf, mid);
        rr = build(nd * 2 + 1, mid + 1, rg);
        T[nd].mn = min(lr, rr);
        T[nd].upd = 0;
    }
    return T[nd].mn + T[nd].upd;
}

ll query(ll nd, ll lf, ll rg) {
    ll mid, lr, rr;
    if (lf <= T[nd].Left && rg >= T[nd].Right) {
        return T[nd].mn + T[nd].upd;
    } else {
        mid = (T[nd].Left + T[nd].Right) / 2;
        if (rg <= mid) {
            return lr = query(nd * 2, lf, rg) + T[nd].upd;
        } else if (lf > mid) {
            return rr = query(nd * 2 + 1, lf, rg) + T[nd].upd;
        } else {
            lr = query(nd * 2, lf, rg);
            rr = query(nd * 2 + 1, lf, rg);
            return min(lr, rr) + T[nd].upd;
        }
    }
    return T[nd].mn + T[nd].upd;
}

void update(ll nd, ll lf, ll rg, ll v) {
    ll mid;
    if (lf <= T[nd].Left && rg >= T[nd].Right) {
        T[nd].upd += v;
    } else {
        mid = (T[nd].Left + T[nd].Right) / 2;
        if (rg <= mid) {
            update(nd * 2, lf, rg, v);
        } else if (lf > mid) {
            update(nd * 2 + 1, lf, rg, v);
        } else {
            update(nd * 2, lf, rg, v);
            update(nd * 2 + 1, lf, rg, v);
        }
        T[nd].mn = min(T[nd * 2].mn + T[nd * 2].upd, T[nd * 2 + 1].mn + T[nd * 2 + 1].upd);
    }
}

int main() {
    ll i, c, PV, P1, P2;
    cin >> n;
    for (i = 1; i <= n; i++) {
        cin >> c;
        A[i] = c;
    }
    build(1, 1, n);
    cin >> m;
    for (i = 0; i < m; i++) {
        cin >> L >> R;
        L++;
        R++;
        // cout << n << m <<"!!!" << L << R << '\n';
        char c = getchar();
        if (c == '\n') {
            if (L <= R) {
                PV = query(1, L, R);
            } else {
                P1 = query(1, L, n);
                P2 = query(1, 1, R);
                PV = min(P1, P2);
            }
            cout << PV << '\n';
        } else {
            cin >> V;
            if (L <= R) {
                update(1, L, R, V);
            } else {
                update(1, L, n, V);
                update(1, 1, R, V);
            }
        }
    }
}