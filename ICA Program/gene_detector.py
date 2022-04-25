import random

Gene = {"TTT": "Phe", "TCT": "Ser", "TAT": "Tyr", "TGT": "Cys", "TTC": "Phe", "TCC": "Ser",
		"TAC": "Tyr", "TGC": "Cys", "TTA": "Leu", "TCA": "Ser", "TAA": "stop", "TGA": "stop",
		"TTG": "Leu", "TCG": "Ser", "TAG": "stop", "TGG": "Trp", "CTT": "Leu", "CCT": "Pro", "CAT": "His",
		"CGT": "Arg", "CTC": "Leu", "CCC": "Pro", "CAC": "His", "CGC": "Arg", "CTA": "Leu", "CCA": "Pro",
		"CAA": "GIn", "CGA": "Arg", "CTG": "Leu", "CCG": "Pro", "CAG": "Gln", "CGG": "Arg", "ATT": "Lle",
		"ACT": "Thr", "AAT": "Asn", "AGT": "Ser", "ATC": "lle", "ACC": "Thr", "AAC": "Asn", "AGC": "Ser",
		"ATA": "lle", "ACA": "Thr", "AAA": "Lys", "AGA": "Arg", "ATG": "Met", "ACG": "Thr", "AAG": "Lys",
		"AGG": "Arg", "GTT": "Val", "GCT": "Ala", "GAT": "Asp", "GGT": "Gly", "GTC": "Val", "GCC": "Ala",
		"GAC": "Asp", "GGC": "Gly", "GTA": "Val", "GCA": "Ala", "GAA": "Glu", "GGA": "Gly", "GTG": "Val", "GCG": "Ala",
		"GAG": "Glu", "GGG": "Gly"}  # set the dic
print(Gene["GCG"])  # test the dic
base = ["A", "C", "G", "T"]
switch = 1
Gene_to_test1 = []
while switch <= 21:
	result = random.choice(base)
	switch += 1
	print(result)
	Gene_to_test1.append(result)
print(Gene_to_test1)  # 生成一个基因
sequences = ''.join(map(str, Gene_to_test1))
print(f"the sequences is AUG{sequences}TAA")
n = random.randint(0, 2)  # 随机生成突变个数
print(n)
i = 1  # 随机生成一个突变位点
while i <= n:
	result2 = random.choice(base)
	i += 1
	i1 = random.randint(0, 20)
	print(i1)
	Gene_to_test1[i1] = f'{result2}'
	print(result2)
sequences2 = ''.join(map(str, Gene_to_test1))
print(f"the mutated gene is AUG{sequences2}TAA")  # 生成突变基因


def compare(list1, list2):  # 对两个基因进行比较
	error = []
	error_index = []
	if len(list1) == len(list2):
		for i in range(0, len(list1)):
			if list1[i] == list2[i]:
				print("they are equal")
			else:
				error.append(list1[i])
				error.append(list2[i])
				error_index.append(i)
				print(f"the {error[0]} mutated to {error[1]}")
				position = ''.join(map(str, error_index))
				position = int(position)
				position = position + 3
				position = str(position)
				if len(position) < 3:
					print(f"the mutation position is {i + 4}")
				else:
					print(f"the mutation position is {i + 4}")


compare(sequences, sequences2)
Amino_acid = []
Amino_acid2 = []


def aa_detector(s, Amino_acid):
	i2 = 0
	while i2 < len(s):
		first_base = s[i2:i2 + 3]
		aa = str(first_base)
		print(Gene[aa])
		i2 += 3
		Amino_acid.append(Gene[aa])


aa_detector(sequences, Amino_acid)
print(Amino_acid)
aa_detector(sequences2, Amino_acid2)
print(Amino_acid2)


def compare_aa(list1, list2):
	error = []
	error_index = []
	if len(list1) == len(list2):
		for i in range(0, len(list1)):
			if list1[i] == list2[i]:
				print("they are equal")
			else:
				error.append(list1[i])
				error.append(list2[i])
				error_index.append(i)
				print(f"the amino acid changed from {error[0]} to {error[1]}")


compare_aa(Amino_acid, Amino_acid2)
# function 2
syn = []
nonsyn = []
result3 = random.choice(base)
i2 = random.randint(0, 20)
Gene_to_test1[i2] = f'{result3}'
sequences3 = ''.join(map(str, Gene_to_test1))
print(sequences3)
i3 = 0
n = 0
while i3 < 7:
	slide1 = sequences2[n:n + 3]
	slide2 = sequences3[n:n + 3]
	if slide1 == slide2:
		syn.append(slide1)
	else:
		if Gene[f'{slide1}'] == Gene[f'{slide2}']:
			syn.append(f'{slide1}')
		else:
			nonsyn.append(f'{slide1},{slide2}')
	i3 = i3 + 1
	n = n + 3
print(syn)
print(nonsyn)
# function3
stop_codon = ['TAA', 'TAG', 'TGA']


def codon_calculator(seq):
	codon = []
	import re
	codon.append(re.findall('TA(C|T)', seq))
	codon.append(re.findall('T(C|T)A', seq))
	codon.append(re.findall('[ACG]AA', seq))
	codon.append(re.findall('[ACG]AG', seq))
	codon.append(re.findall('T[CGT]G', seq))
	codon.append(re.findall('[ACG]GA', seq))
	codon.append(re.findall('TG[CGT]', seq))
	result4 = len(codon) / (4 ** 21)
	print(f'the point is {result4}')


codon_calculator(sequences2)
# function4
codon_num = len(nonsyn) / 4 ** 21
def possible_compare(seq):
	n = 0
	i = 0
	counter = 0
	while n < 21:
		slide = seq[n:n + 3]
		if i == 3:
			i = 0
		if slide[i] == "A":
			slide_new = slide.replace('A', 'G', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
			else:
				counter = counter + 1
		if slide[i] == "C":
			slide_new = slide.replace('C', 'T', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
		if slide[i] == 'G':
			slide_new = slide.replace('G', 'A', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
			else:
				counter = counter + 1
		if slide[i] == 'T':
			slide_new = slide.replace('T', 'C', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
			else:
				counter = counter + 1
		i = i + 1
		if i % 3 == 0:
			n = n + 3
	print(f'the point of this seq is {counter/4**21}')
	if counter/4**21 > codon_num:
		print('the possibility of transversion mutations is bigger than amino acid changes that would results from all possible single transition mutations')
	else:
		print('the possibility of transversion mutations is bigger than amino acid changes that would results from all possible single transition mutations')
possible_compare(sequences2)
