#include <iostream>
#include <vector>

class DisjointSet
{
private:
    std::vector<int> parent;
    std::vector<int> rank;

public:
    DisjointSet(int n)
    {
        // 初始化, 每个元素作为一个单独的集合
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++)
        {
            parent[i] = i;
        }
    }

    int find(int x)
    {
        // 将查找路径上的结点直接连接到根结点
        if (parent[x] != x)
        {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // 合并两个元素所在集合, 按秩合并
    void unionSets(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);

        if (rank[rootX] < rank[rootY])
        {
            parent[rootX] = rootY;
        }
        else if (rank[rootY] < rank[rootX])
        {
            parent[rootY] = rootX;
        }
        else
        {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }

    void printState(int n)
    {
        std::cout << "current state: ";
        for (int i = 0; i < n; i++)
        {
            std::cout << parent[i] << " ";
        }
        std::cout << std::endl;
    }
};

int main()
{
    int n = 10;
    DisjointSet ds(n);

    std::cout << "original: " << std::endl;
    ds.printState(n);

    ds.unionSets(1, 2);
    ds.unionSets(3, 4);
    ds.unionSets(1, 3);
    ds.printState(n);

    ds.find(4);
    ds.printState(n);
}