import time, string
START = time.time()

s = '1'
for j in range(2,21):
    new_s = []
    count = 1
    chars = s[0]
    for i in xrange(1,len(s)):
        if s[i] == s[i-1]:
            count +=1
        else:
            new_s.append(str(count))
            new_s.append(chars)
            count = 1
            chars = s[i]
    new_s.append(str(count))
    new_s.append(chars)

    s = string.join(new_s,'')
    print j, s, len(s)

print "Time Taken:", time.time() - START
