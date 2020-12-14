import math

def PythagoreanTriple(a):
    a = set(a)
    a = list(a)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            c = math.sqrt((a[i] * a[i]) + (a[j] * a[j]))
            if c in a:
                result = True
                return result
            else:
                result = False
    return result

def testingSamples():
    print("Testing Triples")
    sample1 = [1,3,6,2,5,1,4]
    sample2 = [1,7,6,2,5,1,4]
    sample3 = [1,13,6,2,5,14,12,5]
    sample4 = [11,7,6,2,5,1,8]

    assert(PythagoreanTriple(sample1) == True)
    assert(PythagoreanTriple(sample2) == False )
    assert(PythagoreanTriple(sample3) == True)
    assert(PythagoreanTriple(sample4) == False)
    
    print("Passed Successfully")
    
testingSamples()