import random
import time as tm 

def is_sorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            return False
    return True

def bozosort(numbers):
    while not is_sorted(numbers):
        index_1, index_2 = random.randint(0, len(numbers)-1), random.randint(0, len(numbers)-1)
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

if __name__ == "__main__":
    two = [15, 5]
    three = [15, 5, 14]
    four = [15, 5, 14, 1]
    five = [15, 5, 14, 1, -6]
    six = [15, 5, 14, 1, -6, 26]
    seven = [15, 5, 14, 1, -6, 26, -100]
    eight = [15, 5, 14, 1, -6, 26, -100, 0] 
    nine = [15, 5, 14, 1, -6, 26, -100, 0, 99]
    ten = [15, 5, 14, 1, -6, 26, -100, 0, 99, 28931]
    
    t1 = tm.time()
    bozosort(two)
    print '\nResult for Two:'
    print ' '.join([str(i) for i in two])
    t2 = tm.time()
    print 'took ', t2 - t1, ' seconds'
    print '--------'

    t3 = tm.time()
    bozosort(three)
    print '\nResult for Three:'
    print ' '.join([str(i) for i in three])
    t4 = tm.time()
    print 'took ', t4 - t3, ' seconds'
    print '--------'


    t5 = tm.time()
    bozosort(four)
    print '\nResult for Four:'
    print ' '.join([str(i) for i in four])
    t6 = tm.time()
    print 'took ', t6 - t5, ' seconds'
    print '--------'

    t7 = tm.time()
    bozosort(five)
    print '\nResult for Five:'
    print ' '.join([str(i) for i in five])
    t8 = tm.time()
    print 'took ', t8 - t7, ' seconds'
    print '--------'

    t9 = tm.time()
    bozosort(six)
    print '\nResult for Six:'
    print ' '.join([str(i) for i in six])
    t10 = tm.time()
    print 'took ', t10 - t9, ' seconds'
    print '--------'

    t11 = tm.time()
    bozosort(seven)
    print '\nResult for Seven:'
    print ' '.join([str(i) for i in seven])
    t12 = tm.time()
    print 'took ', t12 - t11, ' seconds'
    print '--------'

    t13 = tm.time()
    bozosort(eight)
    print '\nResult for Eight:'
    print ' '.join([str(i) for i in eight])
    t14 = tm.time()
    print 'took ', t14 - t13, ' seconds'
    print '--------'

    t15 = tm.time()
    bozosort(nine)
    print '\nResult for Nine:'
    print ' '.join([str(i) for i in nine])
    t16 = tm.time()
    print 'took ', t16 - t15, ' seconds'
    print '--------'

    t17 = tm.time()
    bozosort(ten)
    print '\nResult for Ten:'
    print ' '.join([str(i) for i in ten])
    t18 = tm.time()
    print 'took ', t18 - t17, ' seconds'
    print '--------'




