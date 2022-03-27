import random
Gene = {"TTT": "Phe","TCT": "Ser","TAT": "Tyr","TGT": "Cys","TTC": "Phe","TCC": "Ser",
	"TAC": "Tyr","TGC": "Cys", "TTA": "Leu","TCA": "Ser","TAA": "stop", "TGA": "stop",
	"TTG": "Leu","TCG": "Ser", "TAG": "stop","TGG": "Trp","CTT": "Leu","CCT": "Pro","CAT": "His",
	"CGT": "Arg","CTC": "Leu","CCC": "Pro","CAC": "His","CGC": "Arg","CTA": "Leu","CCA": "Pro",
	"CAA": "GIn","CGA": "Arg","CTG": "Leu","CCG": "Pro","CAG": "Gln","CGG": "Arg","ATT": "Lle",
	"ACT": "Thr","AAT": "Asn","AGT": "Ser","ATC": "lle","ACC": "Thr","AAC": "Asn","AGC": "Ser",
	"ATA": "lle","ACA": "Thr","AAA": "Lys","AGA": "Arg","ATG": "Met","ACG": "Thr","AAG": "Lys",
	"AGG": "Arg","GTT": "Val","GCT": "Ala","GAT": "Asp","GGT": "Gly","GTC": "Val","GCC": "Ala",
	"GAC": "Asp","GGC": "Gly","GTA": "Val","GCA": "Ala","GAA": "Glu","GGA": "Gly","GTG": "Val","GCG": "Ala",
	"GAG": "Glu","GGG": "Gly"}#set the dic
print(Gene["GCG"])#test the dic
base = ["A", "C", "G", "T"]
switch = 1
Gene_to_test = []
while switch <= 21:
	result = random.choice(base)
	switch += 1
	print(result)
	Gene_to_test.append(result)
print(Gene_to_test)#生成一个基因
Seq1 = Gene_to_test[:]
sequences = ''.join(map(str, Gene_to_test))
print(f"the sequences is AUG{sequences}TAA")
n = random.randint(0, 2)#随机生成突变个数
print(n)
i = 1 #随机生成一个突变位点
while i <= n:
	result2 = random.choice(base)
	i += 1
	i1 = random.randint(0, 20)
	print(i1)
	Gene_to_test[i1] = f'{result2}'
	print(result2)# #
Seq2 = Gene_to_test[:]
sequences2 = ''.join(map(str,Gene_to_test))
print(f"the mutated gene is AUG{sequences2}TAA")#生成突变基因
def compare(list1, list2):#对两个基因进行比较
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
					print(f"the mutation position is {i + 3}")
				else:
					print(f"the mutation position is {i + 3}")
compare(sequences,sequences2)
Amino_acid = []
Amino_acid2 = []
def aa_detector(s,Amino_acid):
	i2 = 0
	while i2 < len(s):
		first_base = s[i2:i2 + 3]
		aa = str(first_base)
		print(Gene[aa])
		i2 += 3
		Amino_acid.append(Gene[aa])
aa_detector(sequences,Amino_acid)
print(Amino_acid)
aa_detector(sequences2,Amino_acid2)
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
compare_aa(Amino_acid,Amino_acid2)
