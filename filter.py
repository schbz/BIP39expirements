target = input(' which file would you like to filter?  ')
output = input(' what should I call the output txt file?  ')

bipwords = []
with open('BIP39english.txt', 'r') as f:
    for line in f:
        bipwords.append(line[:-1])
        
otherwords = []
with open(target, 'r') as f:
    for line in f:
        if not ' ' in line.strip():
            otherwords.append(line.strip())
        
bipclipped = []
for x in bipwords:
    bipclipped.append(x[:4])
        
dif = [x for x in otherwords if (x[:4] or x[:3]) not in bipclipped]

##print(dif)
print(len(dif), ' words were not used in BIP39')

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
        ##else:
        ##    print(num)
    return final_list


print(len(Remove(dif)), ' words after removing duplicates')


with open(output, 'a') as f:
    for x in Remove(dif):
        print(x , file=f)
        
print('word list saved as: '+ output)

