import random
from Bio import SeqIO

if __name__ == '__main__':
    # to always generate the same random sequence
    seed = 0
    random.seed(seed)

    numreads = 5000
    meanread =  100
    stddread =    5

    record = SeqIO.read("slice.fasta", "fasta")
    last = len(record) - 1

    reads = []

    for i in range(numreads):
        start = random.randint(0, last)
        # read length normally distibuted with mean 100, stddev 5
        readlen = int(random.gauss(meanread, stddread))
        # make sure we don't slice past the end
        if start + readlen > last:
            stop = last
        else:
            stop = start+readlen

        read = record[start:stop]
        read.description += " fragment %s:%s" % (start, stop)
        reads.append(read)

    SeqIO.write(reads, "reads.fasta", "fasta")
