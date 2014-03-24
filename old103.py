import time
START = time.time()
SIZE = 7
LIM = 255 #We know that the answer is less than this. {20,31,38,39,40,42,45}
MIN_LIM = 230 # Since we have 7 numbers, need at least 2^7 = 128 different numbers

#test_lst = [20,31,38,39,40,42,45]#[11,18,19,20,22,25]
#test_lst = [11,17,20,22,23,24]
test_lst = [11,18,19,20,22,25]
vals = set([0])
done_set = set()
for i in test_lst:
    new_set = set()
    for j in vals:
        new_set.add(i+j)
        if j <= sum(test_lst)/2:
            done_set.add(j)
    for j in new_set:
        vals.add(j)
for i in new_set:
    if i <= sum(test_lst)/2:
        done_set.add(i)

print sorted(done_set), len(sorted(done_set))
print "Time Taken:", time.time() - START


"""
For MIN_LIM, I'm guessing that you need to increase the size by at least 2x what it was before. Reason for this is such: you can't make the numbers more dense than they were before or else you could have done better before. As such, you need at least 2x as many numbers at a dencsity <= the density of size = n-1

This is the optimal n=6 set.
[0, 11, 18, 19, 20, 22, 25, 29, 30, 31, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 82, 84, 85, 86, 90, 93, 95, 96, 97, 104, 115] 64

This is the non optimal n=6 generated by the rule.
[0, 11, 17, 20, 22, 23, 24, 28, 31, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 82, 83, 84, 86, 89, 93, 94, 95, 97, 100, 106, 117] 64


This is the non-optimal n=7 set made from the rule.
[0, 20, 31, 38, 39, 40, 42, 45, 51, 58, 59, 60, 62, 65, 69, 70, 71, 73, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 89, 90, 91, 93, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 162, 164, 165, 166, 168, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 182, 184, 185, 186, 190, 193, 195, 196, 197, 204, 210, 213, 215, 216, 217, 224, 235, 255] 128



"""
