import random
Gene = {"TTT": "Phe","TCT": "Ser","TAT": "Tyr","TGT": "Cys","TTC": "Phe","TCC": "Ser",
	"TAC": "Tyr","TGC": "Cys", "TTA": "Leu","TCA": "Ser","TAA": "stop", "TGA": "stop",
	"TTG": "Leu","TCG": "Ser", "TAG": "stop","TGG": "Trp","CTT": "Leu","CCT": "Pro","CAT": "His",
	"CGT": "Arg","CTC": "Leu","CCC": "Pro","CAC": "His","CGC": "Arg","CTA": "Leu","CCA": "Pro",
	"CAA": "GIn","CGA": "Arg","CTG": "Leu","CCG": "Pro","CAG": "GIn","CGG": "Arg","ATT": "lle",
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
n = random.randint(0, 2)
print(n)
i = 1
while i <= n:
	result2 = random.choice(base)
	i += 1
	i1 = random.randint(0, 20)
	print(i1)
	Gene_to_test[i1] = f'{result2}'
	print(result2)
Seq2 = Gene_to_test[:]
sequences2 = ''.join(map(str,Gene_to_test))
print(f"the mutated gene is AUG{sequences2}TAA")
def compare(list1, list2):
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
				print(f"the mutation positon is {position + 3}")
compare(sequences,sequences2)
