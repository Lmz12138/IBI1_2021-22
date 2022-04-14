f1 = open('C:/Users/lenovo/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r').readlines()#需要整理的文件
f2 = open('2.fasta','w')#整理之后的文件
for i in f1:
	if i.startswith('>'):
		f2.write('\n'+i)
	else:
		f2.write(i.strip("\n"))
Gene = open('C:/Users/lenovo/IBI_2021-22/IBI1_2021-22/Practical8/2.fasta')
Gene_list = []
for line in Gene:
	Gene_list.append(line)
Gene.close()
seq = ''.join(Gene_list)
print(seq)
import re
regular_expression =  '(?<=gene:)[A-Z0-9]*(?<!_mRNA)'
#print(re.findall(regular_expression,seq))
name = re.findall(regular_expression,seq)
regular_expression2 = '(?<=A)[A-Z]{10,}'
#print(re.findall(regular_expression2,seq))
only_seq = re.findall(regular_expression2,seq)
dict1 = dict(zip(name,only_seq))
only_seq2 = []
n = 0
#print(len(only_seq))
for i in only_seq:
	if "GAATTC" in i:
		only_seq2.append(i)
print(len(only_seq2))
seq_len = []
for i in only_seq2[0:2464]:
	seq_len.append(len(i) + 1)
print(seq_len)
name1 = input("please type the gene name:")
length = input("please type the length of gene:")
length = int(length)
f3 = open('cut_genes.fa','w')
if name1 in name:
	flag1 = True
if length in seq_len:
	flag2 = True
if flag1 and flag2 == True:
	print('A' + f'{dict1[name1]}')
	f3.write('A'+ f'{dict1[name1]}'+"\n")
else:
	print("this gene can not be found")