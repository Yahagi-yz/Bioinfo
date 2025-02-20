
def parse_fasta(file_path):
    seq = ""
    seq_header = ""
    sequences = {}
    DNA = 'ATGCURYSWKMBDHVN'
    with open(file_path , 'r') as f:
        for line in f:
            if line.startswith(">"):
                if seq:
                    if seq_header in sequences.keys():
                        print("There is duplication key:{seq_header}")
                    else:
                        sequences[seq_header] = seq.upper()
                        seq = ""
                seq_header = line.removeprefix(">").rstrip().split()[0]
            else:
                seq += line.strip()
        sequences[seq_header] = seq
    sequences_new = {}
    error = {}
    for key in sequences.keys():
        seq_tmp = sequences[key]
        seq_new = ""
        error_count = 0
        for i in seq_tmp:
            if i in DNA:
                seq_new += i
            else:
                error_count += 1
        sequences_new[key] = seq_new
        error[key] = error_count
    return sequences_new,error
file = "E:/Working/Python/01.learning/Daily/Day1/Test1.fasta"
result,num_error = parse_fasta(file)
print(result,num_error)

import math
def calculate_gc_distribution(fasta_dict):
    
    gc_dis_count = {}
    for key in fasta_dict.keys():
        gc = (fasta_dict[key].upper().count("G")+ \
        fasta_dict[key].upper().count("C"))/len(fasta_dict[key])*10
        gc_percent = math.floor(gc)
        grads = f'{gc_percent*10}-{gc_percent*10+10}%'
        if grads not in gc_dis_count.keys():
            gc_dis_count[grads] = 0
        gc_dis_count[grads] += 1
    return gc_dis_count
GC_distribution = calculate_gc_distribution(result)
print(GC_distribution)
    
