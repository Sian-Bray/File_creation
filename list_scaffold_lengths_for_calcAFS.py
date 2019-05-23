#Creates a list of scaffold lengths as input for ScanTools (https://github.com/pmonnahan/ScanTools)

import argparse
parser = argparse.ArgumentParser(description='Lists scaffold lengths for calcAFS.py (line 16) in ScanTools')
parser.add_argument('-ref', type=str, metavar='reference_fai_path', required=True, help='Path to the reference .fai index file')
args = parser.parse_args()

#create output file
output_file=open("scaffold_lengths.txt", 'w+')
input_file=open(args.ref, "r")

scaffold_lengths=[]

for count, line in enumerate(input_file):
	split_line=line.split('\t')
	scaffold_lengths.append(split_line[1])

number_of_scaffolds=len(scaffold_lengths)-1

output_file.write("[")
for count1, item in enumerate(scaffold_lengths):
	if count1 < number_of_scaffolds:
		output_file.write(str(scaffold_lengths[count1])+", ")
	if count1 == number_of_scaffolds:
		output_file.write(str(scaffold_lengths[count1])+"]")