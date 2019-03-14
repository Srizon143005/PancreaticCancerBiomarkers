# 1480, 350

import pandas

df = pandas.read_csv('GSE16515-Adjusted-Pvals-All-Methods-T-Test-log.csv')

filename = 'GSE16515-Upregulated.csv'
upregulated = open(filename, 'w')

filename = 'GSE16515-Downregulated.csv'
downregulated = open(filename, 'w')

upregulated.write('Gene,p.value,P.adjusted.BH,logFC,Gene.symbol\n')
downregulated.write('Gene,p.value,P.adjusted.BH,logFC,Gene.symbol\n')

upDEGs = 0
downDEGs = 0
for i in range(0,len(df)):
    if float(df['P.adjusted.BH'][i])<0.01 and float(df['logFC'][i])>1.0:
        upregulated.write(str(df['Gene'][i]))
        upregulated.write(',')
        upregulated.write(str(df['p.value'][i]))
        upregulated.write(',')
        upregulated.write(str(df['P.adjusted.BH'][i]))
        upregulated.write(',')
        upregulated.write(str(df['logFC'][i]))
        upregulated.write(',')
        upregulated.write(str(df['Gene.symbol'][i]))
        upregulated.write('\n')
        upDEGs = upDEGs+1
    elif float(df['P.adjusted.BH'][i])<0.01 and float(df['logFC'][i])<-1.0:
        downregulated.write(str(df['Gene'][i]))
        downregulated.write(',')
        downregulated.write(str(df['p.value'][i]))
        downregulated.write(',')
        downregulated.write(str(df['P.adjusted.BH'][i]))
        downregulated.write(',')
        downregulated.write(str(df['logFC'][i]))
        downregulated.write(',')
        downregulated.write(str(df['Gene.symbol'][i]))
        downregulated.write('\n')
        downDEGs = downDEGs+1

print(upDEGs)
print(downDEGs)

upregulated.close()
downregulated.close()