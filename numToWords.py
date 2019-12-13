def numToWords(num):
    under20 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    above100 = {
        100: 'Hundred',
        1000:'Thousand', 
        1000000:'Million', 
        1000000000:'Billion',
        1000000000000:'Trillion'
    }
    
    if num < 20:
        return under20[num]

    if num < 100:
        return tens[(int)(num/10)] + ' ' + under20[num%10]
    
    epoch = 1
    for key in above100.keys():
        if key<=num and key>epoch:
            epoch = key

    return numToWords((int)(num/epoch)) + ' ' + above100[epoch] + ' ' + numToWords(num%epoch)