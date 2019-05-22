#Generate an intervals list containing the position of genes only
#input is a .gtf file output is a four column .bed file
#use the search term 'gene' or 'exon' to take the whole transcript or exons only respectively
import argparse
parser = argparse.ArgumentParser(description="Generate a .bed file containing the position of genes only from a .gtf file.")
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
position_count=0

while file_line_count <input_length:
	current_line=input_file.readline()
	if args.s+"\t" in current_line:
		interesting_line=current_line.split('\t')
		output_file.write(interesting_line[0]+'\t'+interesting_line[3]+'\t'+interesting_line[4]+'\t'+'pos_'+str(position_count)+'\n')
		position_count+=1
	file_line_count+=1