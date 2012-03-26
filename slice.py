from Bio import SeqIO

if __name__ == '__main__':
    start = 896878
    size =   50000

    record = SeqIO.read("NC_010278.gb", "genbank")

    slice = record[start:start+size]
    slice.description = "%s bases starting at position %s" % (size, start)

    SeqIO.write(slice, "slice.fasta", "fasta")
