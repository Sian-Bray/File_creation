#Converts .gtf file to a .fasta file

import argparse
parser = argparse.ArgumentParser(description="Converts .gtf file to a .fasta file")
parser.add_argument('-i', type=str, metavar='input_file', required=True, help='Path to the input .gtf file')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name for the output .fasta file. The output file will be created in your current directory.')
args = parser.parse_args()

input_file=open(args.i, 'r')
output_file=open(args.o, 'w+')
writing_protein=False
current_protein=''

for count, line in enumerate(input_file):
    if writing_protein==True and '# ' in line:
        if '# end gene ' in line:
            n=len(current_protein)//100
            count1=0
            count2=100
            while count2<=(n*100):
                output_file.write(current_protein[count1:count2]+'\n')
                count1+=100
                count2+=100
            output_file.write(current_protein[count2-100:]+'\n')
            current_protein=''
            writing_protein=False
        else:
            good_line=line.replace('# ', '')
            good_line=good_line.replace('protein sequence = [', '')
            good_line=good_line.replace(']', '')
            good_line=good_line.replace('\n', '')
            current_protein+=good_line
    if writing_protein==False and '# start gene ' in line:
        output_file.write('>'+line.replace('# start gene ', ''))
        writing_protein=True

input_file.close()
output_file.close()
