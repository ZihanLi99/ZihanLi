# Author: Zihan Li
# Date: 2020/2/26
# Description: a generator function named count_seq that doesn't take any parameters 
#              and generates a sequence that starts 

def count_seq():
    cur = '2'
    # set first digit
    yield int(cur)
    # yield first digit
    while True:
        newseq = ''
        start = 0
        # use an number to store the index of digit start
        for i in range(len(cur)):
            if cur[start] != cur[i]:
            # find until different than start
                length = i - start
                # calculate length
                newseq += '{}{}'.format(length, cur[start])
                start = i
                # reset start index to current i
        if start < len(cur):
            length = len(cur) - start
            # calculate length
            newseq += '{}{}'.format(length, cur[start])
        cur = newseq
        # update new sequence
        yield int(cur)
