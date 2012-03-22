from Bio import SeqIO

if __name__ == '__main__':
    start = 896878
    size =   50000

    record = SeqIO.read("slice.fasta", "fasta")

    slice = record[start:start+size]
    slice.description = "%s bases starting at position %s" % (size, start)

    SeqIO.write(slice, "slice.fasta", "fasta")
