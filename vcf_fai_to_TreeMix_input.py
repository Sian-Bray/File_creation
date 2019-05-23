#Number of SNPs not distance along contig!
#Creates a TreeMix format file from a .vcf and .fai files.
import argparse
parser = argparse.ArgumentParser(description="Creates a TreeMix input file from a vcf and it's references .fai file.")
parser.add_argument('-v', type=str, metavar='input_vcf', required=True, help='Path to the input .vcf file')
parser.add_argument('-f', type=str, metavar='input_fai', required=True, help='Input .fai file (fasta index file of the VCFs reference).')
parser.add_argument('-k', type=int, metavar='K_in_future_TreeMix', required=True, help='What value of K you will use later in TreeMix.')
parser.add_argument('-d', type=int, metavar='distance', required=True, help='Distance in bp from the end of any contig.')
parser.add_argument('-p', type=str, metavar='populations', required=True, help='List of population names, one population per line.Populations should be in the same order in the vcf.')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='TreeMix format output file.')
args = parser.parse_args()
#Write output file
output_file=open(args.o, 'w+')
#Create population list
pop_file=open(args.p, 'r')
pop_list=pop_file.readlines()
pop_file.close()
for number, group in enumerate(pop_list):
	pop_list[number]=group.replace('\n', '')
	output_file.write(group.replace('\n', '')+' ')
#Open the vcf
vcf=open(args.v, 'r')
vcf_length=len(vcf.readlines())
vcf.close()
vcf=open(args.v, 'r')
#Create lists to append
alt_allele=[]
ref_allele=[]
contig_lines=[]
contig_names=[]
contig_lengths=[]
#Create ordered lists of contigs and contig lenghts
contigs=open(args.f, 'r')
for contig in contigs:
	current_contig=contig.split('\t')
	contig_names.append(current_contig[0])
	contig_lengths.append(current_contig[1])
#Create variables to use
last_contig='LoTs?!'
single_line='\n'
#Create file from vcf
for count, line in enumerate(vcf):
	current_line=line.replace('\n', '').split('\t')
	if len(current_line) <2:
		continue
	elif current_line[0]=="#CHROM":
		name_list=current_line[9:]
	else:
		current_contig=current_line[0]
		#If the contig has changed and we have sites
		if current_contig != last_contig and last_contig != 'LoTs?!':
			to_write=len(contig_lines)-len(contig_lines)%args.k
			if to_write > 0:
				written_line=contig_lines[0:to_write]
				for stuff in written_line:
					output_file.write(stuff)
			contig_lines=[]
			single_line='\n'
			last_contig=current_line[0]
		#If this is continuing the same contig or the first site
		if current_contig == last_contig or last_contig == 'LoTs?!':
			#If you are not too close to the begining or end of the contig
			if int(current_line[1]) >= args.d and int(current_line[1]) <= int(contig_lengths[contig_names.index(current_contig)])-args.d:
				pop_count=0
				last_contig=current_line[0]
				#Work through the line, summing allele counts within populations
				for count1, item1 in enumerate(current_line[9:]):
					individual=name_list[count1]
					current_pop=pop_list[pop_count]
					if individual[:3]==current_pop:
						current_alleles=item1.split(':')
						current_alleles=current_alleles[0].split('/')
						alt=current_alleles.count('1')
						ref=current_alleles.count('0')
						alt_allele.append(alt)
						ref_allele.append(ref)
					#Write the summed allele count to the line if the population has changed or you are at the end of the line
					if individual[:3]!=current_pop or count1+10 == len(current_line):
						single_line=single_line+(str(sum(alt_allele))+','+str(sum(ref_allele))+' ')
						alt_allele=[]
						ref_allele=[]
						pop_count+=1
						#If this was the last item in the line add the line to the list of lines
						if count1+10 == len(current_line):
							contig_lines.append(single_line)
							pop_count=0
							single_line='\n'
						#If this is not the last item, start again
						if count1+10 != len(current_line):
							current_alleles=item1.split(':')
							current_alleles=current_alleles[0].split('/')
							alt=current_alleles.count('1')
							ref=current_alleles.count('0')
							alt_allele.append(alt)
							ref_allele.append(ref)
		#If this is the last line in the vcf
		if count == vcf_length-1:
			to_write=len(contig_lines)-len(contig_lines)%args.k
			if to_write > 0:
				written_line=contig_lines[0:to_write]
				for stuff in written_line:
					output_file.write(stuff)