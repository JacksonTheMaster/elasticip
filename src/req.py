import os
import requests as rq

urlslug = 'https://api.cloudflare.com/client/v4/zones/Cloudflare-ZONE-ID/dns_records?type=A&name=DEFINITE_A_RECORD.DOMAIN.TLD&type=&page=1&per_page=20&order=type&direction=desc&match=all'


print(urlslug)

bearer = 'Your Cloudflare token'

email='your Cloudflare-registerd email'

headers = {
    'X-Auth-Email': f"{email}",
    'X-Auth-Key': f"{bearer}",
    'Content-Type': 'application/json',
}

response = rq.get(f"{urlslug}", headers=headers)

output = open("/var/lib/elasticip/src/result.yml", "wt")
tmp = (response.content)

output.write(str(tmp))
output.close()
