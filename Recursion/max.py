"""
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

ให้เขียน Recursive หาค่า Max ของ Inpu
"""

def maxi(nums):
    # base case
    if len(nums) == 1:
        return nums[0]
    
    # recursive case
    most = maxi(nums[1:])
    return nums[0] if nums[0] > most else most

n = list(map(int, input('Enter Input : ').split()))
print(f'Max : {maxi(n)}')