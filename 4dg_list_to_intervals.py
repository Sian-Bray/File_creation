#Converts a list of 4-fold degenrate sites (tab deliminated file with two columns: Chromosome and position) into a .intervals file that can be used by GATK

import argparse
parser = argparse.ArgumentParser(description="Sums all DPs (depths) in a vcf.")
parser.add_argument('-i', type=str,  metavar='input_file', required=True, help='Path to the input .txt file')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name for the output .interval file.')
args = parser.parse_args()

input_file=open(args.i, 'r')
input_length=len(input_file.readlines())
input_file.close

input_file=open(args.i, 'r')
file_line_count=0
output_file=open(args.o, 'w+')

while input_length > file_line_count :
	current_line=input_file.readline()
	current_line=current_line.replace('\n', '')
	split_line=current_line.split('\t')
	end_point=int(split_line[1])
	end_point=end_point+1
	current_line=current_line.replace('\t', ':')
	output_line=current_line+'-'+str(end_point)
	output_file.write(output_line+'\n')
	file_line_count+=1

output_file.close