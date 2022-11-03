def hcf(num1, num2):
    l = [num1, num2]
    greater_num = max(l)
    lesser_num = min(l)
    
    while True:
        q = greater_num % lesser_num 
        if q == 0:
            return lesser_num
        else:
            greater_num = lesser_num
            lesser_num = q
            
if hcf(3, 20) == 1:
    print("Co-Prime Numbers")
else:
    print("Not Co-Prime Numbers")