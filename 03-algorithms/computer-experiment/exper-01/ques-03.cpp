#include <iostream>
#include <vector>

using namespace std;

vector<bool> used;
vector<int> current_perm;
int total_count = 0;

void dfs(int n)
{
    // 一组排列执行完毕
    if (current_perm.size() == (size_t)n)
    {
        total_count++;
        for (int i = 0; i < n; i++)
        {
            cout << current_perm[i] << (i == n - 1 ? "" : " ");
        }
        cout << endl;
        return;
    }

    for (int i = 1; i <= n; i++)
    {
        if (!used[i])
        {
            used[i] = true;
            current_perm.push_back(i);
            dfs(n);
            used[i] = false;
            current_perm.pop_back();
        }
    }
}

int main()
{
    int n = 5;
    used.resize(n + 1);
    dfs(n);
    cout << "count=" << total_count << endl;
    return 0;
}