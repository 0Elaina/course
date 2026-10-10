#include <iostream>
#include <vector>
#include <chrono>
#include <cstdlib>
#include <algorithm>

using namespace std;
using namespace std::chrono;

// 归并排序
void merge(vector<int> &arr, int l, int m, int r)
{
    int n1 = m - l + 1, n2 = r - m;
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1)
        arr[k++] = L[i++];
    while (j < n2)
        arr[k++] = R[j++];
}

void mergeSort(vector<int> &arr, int l, int r)
{
    if (l < r)
    {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

// 快速排序
int partition(vector<int> &arr, int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
    {
        if (arr[j] < pivot)
            swap(arr[++i], arr[j]);
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    vector<int> sizes = {5000, 10000, 100000, 200000, 500000, 1000000};

    for (int n : sizes)
    {
        // 生成随机数组
        vector<int> original(n);
        for (int i = 0; i < n; i++)
            original[i] = rand();

        // 归并排序测试
        vector<int> arr1 = original;
        auto start = high_resolution_clock::now();
        mergeSort(arr1, 0, n - 1);
        auto end = high_resolution_clock::now();
        double mergeTime = duration<double, milli>(end - start).count();

        // 快速排序测试
        vector<int> arr2 = original;
        start = high_resolution_clock::now();
        quickSort(arr2, 0, n - 1);
        end = high_resolution_clock::now();
        double quickTime = duration<double, milli>(end - start).count();

        cout << "size: " << n << endl;
        cout << "mergeTime: " << mergeTime << endl;
        cout << "quickTime: " << quickTime << endl;
        cout << "------------------------" << endl;
    }
    return 0;
}