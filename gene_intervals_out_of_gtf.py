#Generate an intervals list containing the position of genes only
#input is a .gtf file output is a .intervals file that can be funneled into GATK
#use the search term 'gene' or 'exon' to take the whole transcript or exons only respectively
import argparse
parser = argparse.ArgumentParser(description="Generate an intervals list containing the position of genes only from a .gtf file.")
parser.add_argument('-i', type=str,  metavar='input_file', required=True, help='Path to the input .gtf file')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name for the output .interval file.')
parser.add_argument('-s', type=str, metavar='search_word', required=True, help='Either "transcript" to select the whole transcript or "exon" to select exons only.')
args = parser.parse_args()

input_file=open(args.i, 'r')
input_length=len(input_file.readlines())
input_file.close

input_file=open(args.i, 'r')
file_line_count=0
output_file=open(args.o, 'w+')

while file_line_count <input_length:
	current_line=input_file.readline()
	if args.s+"\t" in current_line:
		interesting_line=current_line.split('\t')
		output_file.write(interesting_line[0]+':'+interesting_line[3]+'-'+interesting_line[4]+'\n')
	file_line_count+=1