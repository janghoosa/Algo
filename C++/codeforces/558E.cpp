#include <iostream>
using namespace std;

int n, q, m, L, R, K;

class Node {
   public:
    int cnt, lazy;
    int Left, Right;
};
char A[100005];
Node T[26][400000];

int build(int c, int nd, int lf, int rg) {
    int mid, lr, rr;
    T[c][nd].Left = lf;
    T[c][nd].Right = rg;
    if (lf == rg) {
        if (A[lf] - 'a' == c)
            T[c][nd].cnt = 1;
        else
            T[c][nd].cnt = 0;
        T[c][nd].lazy = -1;
    } else {
        mid = (lf + rg) / 2;
        lr = build(c, nd * 2, lf, mid);
        rr = build(c, nd * 2 + 1, mid + 1, rg);
        T[c][nd].cnt = lr + rr;
        T[c][nd].lazy = -1;
    }
    return T[c][nd].cnt;
}

void pushdown(int c, int nd) {
    if (T[c][nd].lazy == 1) {
        T[c][nd * 2].lazy = 1;
        T[c][nd * 2 + 1].lazy = 1;
        T[c][nd * 2].cnt = T[c][nd * 2].Right - T[c][nd * 2].Left + 1;
        T[c][nd * 2 + 1].cnt = T[c][nd * 2 + 1].Right - T[c][nd * 2 + 1].Left + 1;
    } else if (T[c][nd].lazy == 0) {
        T[c][nd * 2].lazy = 0;
        T[c][nd * 2 + 1].lazy = 0;
        T[c][nd * 2].cnt = 0;
        T[c][nd * 2 + 1].cnt = 0;
    } else {
        ;
    }
    T[c][nd].lazy = -1;
}

void pushup(int c, int nd) {
    T[c][nd].cnt = T[c][nd * 2].cnt + T[c][nd * 2 + 1].cnt;
}

void update(int c, int nd, int lf, int rg, int v) {
    if (lf <= T[c][nd].Left && rg >= T[c][nd].Right) {
        T[c][nd].lazy = v;
        if (v == 1)
            T[c][nd].cnt = T[c][nd].Right - T[c][nd].Left + 1;
        else
            T[c][nd].cnt = 0;
    } else {
        int mid = (T[c][nd].Left + T[c][nd].Right) / 2;
        pushdown(c, nd);
        if (rg <= mid) {
            update(c, nd * 2, lf, rg, v);
        } else if (lf > mid) {
            update(c, nd * 2 + 1, lf, rg, v);
        } else {
            update(c, nd * 2, lf, rg, v);
            update(c, nd * 2 + 1, lf, rg, v);
        }
        pushup(c, nd);
    }
}

int query(int c, int nd, int lf, int rg) {
    int mid, lr, rr;
    if (lf <= T[c][nd].Left && rg >= T[c][nd].Right) {
        return T[c][nd].cnt;
    } 
    else {
        pushdown(c, nd);
        pushup(c, nd);
        mid = (T[c][nd].Left + T[c][nd].Right) / 2;
        if (rg <= mid) {
            return lr = query(c, nd * 2, lf, rg);
        } else if (lf > mid) {
            return rr = query(c, nd * 2 + 1, lf, rg);
        } else {
            lr = query(c, nd * 2, lf, rg);
            rr = query(c, nd * 2 + 1, lf, rg);
            return lr + rr;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i, j, c, cur;
    int cnts[26];
    cin >> n >> q;
    cin >> (A+1);
    for (c = 0; c < 26; c++)
        build(c, 1, 1, n);
    // for (c = 0; c < 26;c++){
    //     cout << (char)(c + 'a') << ' ' <<  query(c, 1, 1, n) << '\n';
    // }
    // for (i = 1; i <= n; i++) {
    //     for (c = 0; c < 26; c++) {
    //         if (query(c, 1, i, i) == 1)
    //             cout << (char)(c + 'a');
    //     }
    // }
    // cout << '\n';
    for (i = 1; i <= q; i++) {
        cin >> L >> R >> K;
        if (K == 1) {
            for (c = 0; c < 26; c++) {
                cnts[c] = query(c, 1, L, R);
                update(c, 1, L, R, 0);
            }
            for (cur = L, c = 0; c < 26; c++) {
                if (cnts[c] > 0) update(c, 1, cur, cur + cnts[c] - 1, 1);
                cur += cnts[c];
            }
        } else {
            for (cur = 0, c = 0; c < 26; c++) {
                cnts[c] = query(c, 1, L, R);
                update(c, 1, L, R, 0);
            }
            for (cur = L, c = 25; c >= 0; c--) {
                if (cnts[c] > 0) update(c, 1, cur, cur + cnts[c] - 1, 1);
                cur += cnts[c];
            }
        }
    }
    for (i = 1; i <= n; i++) {
        for (cur = L, c = 0; c < 26; c++) {
            if (query(c, 1, i, i) == 1)
                cout << (char)(c + 'a');
        }
    }
    cout << '\n';
    return 0;
}