#Extracts all DPs in a vcf so that a depth of coverage histogram can be generated in R.

import argparse
parser = argparse.ArgumentParser(description="Pull out all DPs (depths) in a vcf.")
parser.add_argument('-i', type=str, nargs='+', metavar='input_file', required=True, help='Path to the input .vcf file')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name for the output .txt file.')
args = parser.parse_args()

output_file=open(args.o, 'w+')

for file in args.i:
	
	input_file=open(file, 'r')
	input_length=len(input_file.readlines())
	input_file.close
	input_file=open(file, 'r')
	file_line_count=0
	
	while file_line_count<input_length:
		current_line=input_file.readline()
		if ";DP=" in current_line:
			location=current_line.index(";DP=")
			while current_line[location+4] != ";":
				depth = current_line[location+4]
				output_file.write(depth)
				location+=1
			output_file.write("\n")
		file_line_count+=1
	
	input_file.close()

output_file.close()
