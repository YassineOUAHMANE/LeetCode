class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1,num2 = 0,0
        merge = []
        while num1 < len(nums1) and num2 < len(nums2):
            if  nums1[num1] < nums2[num2]:
                merge.append(nums1[num1])
                num1+=1
            else:
                merge.append(nums2[num2])
                num2+=1
        for i in range(num1,len(nums1)):
            merge.append(nums1[i])
        for j in range(num2,len(nums2)):
            merge.append(nums2[j])
        
        if len(merge)%2==0:
            return (merge[(len(merge)//2)] + merge[(len(merge)//2)-1])/2
        else:
            return merge[len(merge)//2]
                
                
                
        