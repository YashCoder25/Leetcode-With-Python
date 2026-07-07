class Solution:
    def heapify(self,arr,n,i):
        largest = i
        left =  2 * i + 1
        right = 2 * i + 2   


        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)

        return nums        