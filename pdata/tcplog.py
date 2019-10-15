import pandas as pd
import GeoIP

gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

f=open('test.txt','r')


lines=f.readlines()
lines=[x.strip('\r').strip('\n') for x in lines]
q=len(lines)//14
p_dict={'ip': [], 
        'domain': [], 
        'port': [],
        'program': [],
        'geo': []
        }
for x in range(q):
    ip=(lines[(14*x)+4].split()[-1]) #ip
    domain=(lines[(14*x)+5].split()[-1]) #domain
    port=(lines[(14*x)+7].split()[-1]) #puerto
    program=(lines[(14*x)+9].split()[-1]) #program
    if ip =='0.0.0.0':
        break
    if domain ==':':
        domain = 'no_domain'

    geo = gi.country_name_by_addr(ip)

    print(x)
    print(ip) #ip
    print(domain) #domain
    print(port) #puerto
    print(program) #program
    print(geo)

    p_dict['ip'].append(ip)
    p_dict['domain'].append(domain)
    p_dict['port'].append(port)
    p_dict['program'].append(program)
    p_dict['geo'].append(geo)

df = pd.DataFrame(p_dict)
df.to_csv('proccesed.csv', sep='\t')
# writer = pd.ExcelWriter('proccesed.xls')
# df.to_excel(writer, sheet_name='Sheet1')

