import sys

if __name__=="__main__":
    width = int(sys.argv[1])
    num = float(sys.argv[2])

    m_flag = num < 0
    a_num  = abs(num)

    if width % 2 != 0:
        print "can not convert this value." 
        exit()

    if 2 ** (width/2) < a_num:
        print "can not convert this value." 
        exit()

    
    bits = [0] * width

    for i in range(1,width):
        j = width/2-i

        v = 2.0 ** (j - 1)

        if a_num - v >= 0:
            bits[i] = 1
            a_num -= v

    error = a_num
    if m_flag:
        for i in range(width):
            bits[i] = 1 - bits[i]

        c = 1
        for i in range(width)[::-1]:
            if c == 0:
                break
            if bits[i]==1:
                bits[i]=0
            else:
                bits[i]=1
                c = 0

    print "%db'%s"%(width,"".join(map(str,bits)))
    print "ABS ERROR = %e" %  a_num


