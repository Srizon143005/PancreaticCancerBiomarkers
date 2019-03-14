# 14, 2

import pandas

df = pandas.read_csv('GSE41372-Adjusted-Pvals-All-Methods-T-Test.csv')

filename = 'GSE41372-Upregulated.csv'
upregulated = open(filename, 'w')

filename = 'GSE41372-Downregulated.csv'
downregulated = open(filename, 'w')

upregulated.write('microRNA,p.value,P.adjusted.BH,logFC\n')
downregulated.write('microRNA,p.value,P.adjusted.BH,logFC\n')

upDEMs = 0
downDEMs = 0
for i in range(0,len(df)):
    if float(df['P.adjusted.BH'][i])<0.01 and float(df['logFC'][i])>1.0:
        upregulated.write(str(df['Gene'][i]))
        upregulated.write(',')
        upregulated.write(str(df['p.value'][i]))
        upregulated.write(',')
        upregulated.write(str(df['P.adjusted.BH'][i]))
        upregulated.write(',')
        upregulated.write(str(df['logFC'][i]))
        upregulated.write('\n')
        upDEMs = upDEMs+1
    elif float(df['P.adjusted.BH'][i])<0.01 and float(df['logFC'][i])<-1.0:
        downregulated.write(str(df['Gene'][i]))
        downregulated.write(',')
        downregulated.write(str(df['p.value'][i]))
        downregulated.write(',')
        downregulated.write(str(df['P.adjusted.BH'][i]))
        downregulated.write(',')
        downregulated.write(str(df['logFC'][i]))
        downregulated.write('\n')
        downDEMs = downDEMs+1

print(upDEMs)
print(downDEMs)

upregulated.close()
downregulated.close()