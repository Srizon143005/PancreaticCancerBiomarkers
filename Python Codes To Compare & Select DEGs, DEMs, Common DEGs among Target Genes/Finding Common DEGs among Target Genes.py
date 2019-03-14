import pandas

df1 = pandas.read_csv('GSE15471-Upregulated.csv')
df2 = pandas.read_csv('GSE16515-Upregulated.csv')
df3 = pandas.read_csv('GSE28735-Upregulated.csv')

a = []
aa = []
b = []
c = []
common = []

for i in range(0, len(df1)):
    a.append(df1['Gene.symbol'][i])
    aa.append(df1['Gene'][i])

for i in range(0, len(df2)):
    b.append(df2['Gene.symbol'][i])
    
for i in range(0, len(df3)):
    c.append(df3['Gene.symbol'][i])





print('Total A: ' + str(len(df1)))
print('Total B: ' + str(len(df2)))
print('Total C: ' + str(len(df3)))

tmp = 0
stack = []
for i in a:
    if i in b:
        if i not in c:
            if i not in stack:
                stack.append(i)
                tmp = tmp+1
print('A intersection B, not in C: ' + str(tmp))


tmp = 0
stack = []
for i in a:
    if str(i)!='nan':
        if i in c:
            if i not in b:
                if i not in stack:
                    stack.append(i)
                    tmp = tmp+1
print('A intersection C, not in B: ' + str(tmp))

tmp = 0
stack = []
for i in b:
    if str(i)!='nan':
        if i in c:
            if i not in a:
                if i not in stack:
                    stack.append(i)
                    tmp = tmp+1
print('B intersection C, not in A: ' + str(tmp))





upCommon = 0
for i in c:
    if str(i)!='nan':
        if i in a:
            if i in b:
                if i not in common:
                    common.append(i)
                    upCommon=upCommon+1

print(upCommon)






filename = 'Upregulated-Common-Genes-Pval-logFC.csv'
log = open(filename, 'w')

log.write('Gene-symbol,GSE15471-Adj-Pval,GSE15471-logFC,GSE16515-Adj-Pval,GSE16515-logFC,GSE28735-Adj-Pval,GSE28735-logFC\n')
for i in common:
    log.write(str(i) + ',')
    for j in range(0,len(df1)):
        if str(df1['Gene.symbol'][j])==str(i):
            log.write(str(df1['P.adjusted.BH'][j]) + ',' + str(df1['logFC'][j]) + ',')
            break
    
    for j in range(0,len(df2)):
        if str(df2['Gene.symbol'][j])==str(i):
            log.write(str(df2['P.adjusted.BH'][j]) + ',' + str(df2['logFC'][j]) + ',')
            break
    
    for j in range(0,len(df3)):
        if str(df3['Gene.symbol'][j])==str(i):
            log.write(str(df3['P.adjusted.BH'][j]) + ',' + str(df3['logFC'][j]))
            break
    
    log.write('\n')

log.close()
    







df1 = pandas.read_csv('GSE15471-Downregulated.csv')
df2 = pandas.read_csv('GSE16515-Downregulated.csv')
df3 = pandas.read_csv('GSE28735-Downregulated.csv')

a = []
b = []
c = []
common2 = []

for i in range(0, len(df1)):
    a.append(df1['Gene.symbol'][i])

for i in range(0, len(df2)):
    b.append(df2['Gene.symbol'][i])
    
for i in range(0, len(df3)):
    c.append(df3['Gene.symbol'][i])



print('Total A: ' + str(len(df1)))
print('Total B: ' + str(len(df2)))
print('Total C: ' + str(len(df3)))

tmp = 0
stack = []
for i in a:
    if i in b:
        if i not in c:
            if i not in stack:
                stack.append(i)
                tmp = tmp+1
print('A intersection B, not in C: ' + str(tmp))


tmp = 0
stack = []
for i in a:
    if str(i)!='nan':
        if i in c:
            if i not in b:
                if i not in stack:
                    stack.append(i)
                    tmp = tmp+1
print('A intersection C, not in B: ' + str(tmp))

tmp = 0
stack = []
for i in b:
    if str(i)!='nan':
        if i in c:
            if i not in a:
                if i not in stack:
                    stack.append(i)
                    tmp = tmp+1
print('B intersection C, not in A: ' + str(tmp))




downCommon = 0
for i in c:
    if str(i)!='nan':
        if i in a:
            if i in b:
                if i not in common2:
                    common2.append(i)
                    downCommon=downCommon+1

print(downCommon)




filename = 'Downregulated-Common-Genes-Pval-logFC.csv'
log = open(filename, 'w')

log.write('Gene-symbol,GSE15471-Adj-Pval,GSE15471-logFC,GSE16515-Adj-Pval,GSE16515-logFC,GSE28735-Adj-Pval,GSE28735-logFC\n')
for i in common2:
    log.write(str(i) + ',')
    for j in range(0,len(df1)):
        if str(df1['Gene.symbol'][j])==str(i):
            log.write(str(df1['P.adjusted.BH'][j]) + ',' + str(df1['logFC'][j]) + ',')
            break
    
    for j in range(0,len(df2)):
        if str(df2['Gene.symbol'][j])==str(i):
            log.write(str(df2['P.adjusted.BH'][j]) + ',' + str(df2['logFC'][j]) + ',')
            break
    
    for j in range(0,len(df3)):
        if str(df3['Gene.symbol'][j])==str(i):
            log.write(str(df3['P.adjusted.BH'][j]) + ',' + str(df3['logFC'][j]))
            break
    
    log.write('\n')

log.close()





filename = 'Common Genes.csv'
CommonGenes = open(filename, 'w')

CommonGenes.write('Type,Gene.symbol\n')
for i in common:
    CommonGenes.write('Upregulated,'+str(i)+'\n')
for i in common2:
    CommonGenes.write('Downregulated,'+str(i)+'\n')

CommonGenes.close()





df1 = pandas.read_csv('Target Genes.csv')
tg = []
for i in range(0,len(df1)):
    if df1['Gene.symbol'][i] not in tg:
        tg.append(df1['Gene.symbol'][i])

print(len(tg))

for i in tg:
    if i in common:
        print(i)
    elif i in common2:
        print(i)
        




filename = 'Final Target Genes.csv'
TargetGenes = open(filename, 'w')

TargetGenes.write('Gene.symbol\n')
for i in tg:
    TargetGenes.write(str(i)+'\n')

TargetGenes.close()




