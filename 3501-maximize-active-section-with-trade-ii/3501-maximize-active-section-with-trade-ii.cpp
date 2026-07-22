class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();
        vector<int> rtype, rstart, rend;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            rtype.push_back(s[i]-'0');
            rstart.push_back(i);
            rend.push_back(j-1);
            i = j;
        }
        int m = rtype.size();
        vector<long long> length(m);
        for (int k = 0; k < m; k++) length[k] = rend[k]-rstart[k]+1;

        long long totalOnes = 0;
        for (int k = 0; k < m; k++) if (rtype[k]==1) totalOnes += length[k];

        const long long NEG = LLONG_MIN/2;
        vector<long long> A(m, NEG);
        for (int p = 1; p+1 < m; p++)
            if (rtype[p]==1) A[p] = length[p-1] + length[p+1];

        int LOG = 1;
        while ((1<<LOG) < max(m,1)) LOG++;
        LOG++;
        vector<vector<long long>> sp(LOG, vector<long long>(m, NEG));
        if (m>0) sp[0] = A;
        for (int e = 1; e < LOG; e++) {
            int half = 1<<(e-1);
            for (int idx = 0; idx + (1<<e) <= m; idx++)
                sp[e][idx] = max(sp[e-1][idx], sp[e-1][idx+half]);
        }
        vector<int> logT(m+1,0);
        for (int k = 2; k <= m; k++) logT[k] = logT[k/2]+1;

        auto queryMax = [&](int l, int r) -> long long {
            if (l > r || l < 0 || r >= m) return NEG;
            int k = logT[r-l+1];
            return max(sp[k][l], sp[k][r-(1<<k)+1]);
        };

        auto findRun = [&](int pos) -> int {
            int lo=0, hi=m-1, ans=0;
            while (lo<=hi){
                int mid=(lo+hi)/2;
                if (rstart[mid]<=pos){ans=mid; lo=mid+1;}
                else hi=mid-1;
            }
            return ans;
        };

        vector<int> result;
        result.reserve(queries.size());
        for (auto &q : queries) {
            int l=q[0], r=q[1];
            int i=findRun(l), j=findRun(r);
            long long gain = 0;
            if (!(i==j || j==i+1)) {
                int lo=i+1, hi=j-1;
                if (lo==hi) {
                    if (rtype[lo]==1) {
                        long long lc = rend[i]-l+1;
                        long long rc = r-rstart[j]+1;
                        gain = lc+rc;
                    }
                } else {
                    long long mid = queryMax(lo+1, hi-1);
                    long long leftVal = NEG, rightVal = NEG;
                    if (rtype[lo]==1) {
                        long long lc = rend[i]-l+1;
                        leftVal = lc + length[lo+1];
                    }
                    if (rtype[hi]==1) {
                        long long rc = r-rstart[j]+1;
                        rightVal = length[hi-1] + rc;
                    }
                    long long best = max({mid, leftVal, rightVal});
                    gain = (best <= NEG/2) ? 0 : best;
                }
            }
            result.push_back((int)(totalOnes + gain));
        }
        return result;
    }
};