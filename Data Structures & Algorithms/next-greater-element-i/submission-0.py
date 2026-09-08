class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for idx, i in enumerate(nums1):
            found = False
            for j in range(len(nums2)):
                if nums2[j] == i:
                    found = True
                if found and nums2[j] > i:
                    out.append(nums2[j])
                    break
            if len(out) < idx+1:
                out.append(-1)
        return out