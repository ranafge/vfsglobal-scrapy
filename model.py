import requests

headers = {
    'authority': 'lift-api.vfsglobal.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'clientsource': 'Vs1UBljs00Vo9FPitaY52WWwwCCDtZA7axWhCrzmPUjN0tC1ve2nTZe117b6dxPvaNvnL9FkkzP3By1oLYNeoCyAqO/wXQSTiLV7dyR35fzK2zpOSkkEMp1e/ej6r8qv5EWlauD0BS7hfm1TSRNccqm8JplMYmmHSnUn3t74xio=',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'route': 'bgd/en/ita',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

data = 'username=ranafge@gmail.com&password=cksxYTLkokwBqjv3ior7dHkQFBciiNSXjl0jTPXlNYWkV3aAuDPxzOSKCzKjpzMiYINKULOQ/oCuhXwzRQrhMESrm38hAqHRkDFjial1ZPMoyAX1HJfzm9owc1y+z+6yXGqdArB5mgEGkMvfhMBZlZNrnTQwIwWOYYbsbShYOvY=&missioncode=ita&countrycode=bgd&captcha_version=cloudflare-v1&captcha_api_key=0.xGp8IUG5hmg4SgHi33PrkjR-bXvJ7XBjGzwRDd3ywQ0Jsbt8HHtI-xFjWYPZmKhjOE7YzHbArxQHbuhmgLvDhQoHuvt-MmBTacPjAxHN19m5JUrCMJBoC6dVkOs4JQoOk7-KbVe994l089EV51mAX-8B4-DpqFzWg5XreJSj1ldcvnNe7rEZLatxNobPpz4nFpnrIecAEQNdAQWTv5M8uYEk-l_ZXgOBRmLUf91qXyaHaveXfTH4kTXsm52LRa3d-JQHGkkv1LxijbibOPPzj5DCZNruDd2AsOnLhlf1syW-0dWdEvaD411zYa6MzhIrSvR51yU8N3bGENLHCavJfc1Hh391PfbTyPtPiUAZyI6-jOXdLaLkGT8jUY9Rvv-nEp2a6SrHXli7P8fjleCj2IU56sQCSSs8lM-VYV6GhWwTv_3kXCVbTKHsewRSNTGP.cz2GNk2bOB_Io4Arlahvpg.8759472d04f5e85a97fa38a14c8caa54662b2429d27c30d52529f50ddddb2fe2'

response = requests.post('https://lift-api.vfsglobal.com/user/login', headers=headers, data=data)


headers = {
    'authority': 'd2ab400qlgxn2g.cloudfront.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-request-headers': 'authorization,x-contentful-user-agent',
    'access-control-request-method': 'GET',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

params = {
    'content_type': 'dyanmicFormSchema',
    'fields.locale': 'ita > bgd&ita&vfs',
    'limit': '1',
}

response = requests.options(
    'https://d2ab400qlgxn2g.cloudfront.net/dev/spaces/xxg4p8gt3sg6/environments/master/entries',
    params=params,
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'X-Contentful-User-Agent': 'sdk contentful.js/8.5.8; platform browser; os Windows;',
    'Authorization': 'Bearer 5-eABDj_OU_DJAXxsU2tXGFDk6yozcQbKbNnV-6rS8M',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://visa.vfsglobal.com/',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'content_type': 'dyanmicFormSchema',
    'fields.locale': 'ita > bgd&ita&vfs',
    'limit': '1',
}

response = requests.get(
    'https://d2ab400qlgxn2g.cloudfront.net/dev/spaces/xxg4p8gt3sg6/environments/master/entries',
    params=params,
    headers=headers,
)


headers = {
    'authority': 'd2ab400qlgxn2g.cloudfront.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-request-headers': 'authorization,x-contentful-user-agent',
    'access-control-request-method': 'GET',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

params = {
    'content_type': 'travelInsurance',
    'fields.isoCode': 'ita',
}

response = requests.options(
    'https://d2ab400qlgxn2g.cloudfront.net/dev/spaces/xxg4p8gt3sg6/environments/master/entries',
    params=params,
    headers=headers,
)


headers = {
    'authority': 'd2ab400qlgxn2g.cloudfront.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-request-headers': 'authorization,x-contentful-user-agent',
    'access-control-request-method': 'GET',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

params = {
    'content_type': 'countryNewsflash',
    'fields.locale': 'ita > bgd > en&ita > en&en',
    'order': '-sys.updatedAt',
}

response = requests.options(
    'https://d2ab400qlgxn2g.cloudfront.net/dev/spaces/xxg4p8gt3sg6/environments/master/entries',
    params=params,
    headers=headers,
)


headers = {
    'authority': 'd2ab400qlgxn2g.cloudfront.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer 5-eABDj_OU_DJAXxsU2tXGFDk6yozcQbKbNnV-6rS8M',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-contentful-user-agent': 'sdk contentful.js/8.5.8; platform browser; os Windows;',
}

params = {
    'content_type': 'travelInsurance',
    'fields.isoCode': 'ita',
}

response = requests.get(
    'https://d2ab400qlgxn2g.cloudfront.net/dev/spaces/xxg4p8gt3sg6/environments/master/entries',
    params=params,
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'X-Contentful-User-Agent': 'sdk contentful.js/8.5.8; platform browser; os Windows;',
    'Authorization': 'Bearer 5-eABDj_OU_DJAXxsU2tXGFDk6yozcQbKbNnV-6rS8M',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://visa.vfsglobal.com/',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'content_type': 'countryNewsflash',
    'fields.locale': 'ita > bgd > en&ita > en&en',
    'order': '-sys.updatedAt',
}

response = requests.get(
    'https://d2ab400qlgxn2g.cloudfront.net/dev/spaces/xxg4p8gt3sg6/environments/master/entries',
    params=params,
    headers=headers,
)


headers = {
    'authority': 'lift-api.vfsglobal.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'route': 'bgd/en/ita',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

response = requests.get('https://lift-api.vfsglobal.com/configuration/fields/ita/bgd', headers=headers)


headers = {
    'authority': 'lift-api.vfsglobal.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorize': 'EAAAAKEmJcnHKfrDs0cD9MzWLlkOE0ZpRyvDJhi0gkw6cMuo2hcBi57R4okt7EQY1/UNiTPBMpvvDCLslrZryp0Sn/8E3pypNI141HOWhUYdaRf8mKCTwbV/dsgrRTeJije7ufTQH16HIpj4hVwM/GMqAPCh0QFGIXRCy2exwcHggQJNqEfaxlu5ryyR98Je1F22kiTVvZIt8CEg7kYUzNYfYMOx0wIGSkEEPLklXeZwu2cqRm185tJS4rs72FDgnNOhhE5w6m0xSbhDhoCo8S5a7uheOGhMGfug6NaVUPkxxLHFPPaxWCqmk6BemxiNWst7+Xy5KZ5J+65jRlNfBtvLAbyMPitCLuULGD8oBxFbC1qtosm0ZInmz1mktUTHkbNDQdd0YA9KAb29id6ZkHOAT7NuIQQmMcGL7b2+U5zwXwsZD78l7GkjT+PVcSDKC7w9JBBVzWmeGK4TKcWnpuettDN/ut8nuedmRb/TQqdLiw91gKfBFXeKxRq3hakj11wDeb/rqAPR7Eovrkh48zyJjTMqmjHkPsuqOi9K5/aL4s1t',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'route': 'bgd/en/ita',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

json_data = {
    'countryCode': 'bgd',
    'missionCode': 'ita',
    'loginUser': 'ranafge@gmail.com',
    'languageCode': 'en-US',
}

response = requests.post('https://lift-api.vfsglobal.com/appointment/application', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"countryCode":"bgd","missionCode":"ita","loginUser":"ranafge@gmail.com","languageCode":"en-US"}'
#response = requests.post('https://lift-api.vfsglobal.com/appointment/application', headers=headers, data=data)


cookies = {
    '__Secure-3PSID': 'g.a000hAjj2mkKgZvXCZln3UfVBaZbX0-WVGq6DhIteCZOglPLic3ZZMhrV5ue97PkskSgvjj_EAACgYKAZsSAQASFQHGX2MiO-cdR0uazHUBhB3elO2TThoVAUF8yKqO8L2KtqWH3pFrXF6lC0Qr0076',
    '__Secure-3PAPISID': '7Ls2RfL1LMJvBvGP/Aaj_I9FCtT3HDgMVf',
    'NID': '512=HVikv2m25CTtka4GwGuXqu1cTf78eu5RT47me2jZhtefvS8jqD8PqhTdXv7VSiSOiMBfLqcIDca9waLZOLXqt7jQ7oLJobU1v834-LblLBVVPFDnZHK40cuPtFNKV5sLPaNk_kbRzjORbruRTJFNGwWkXWCL4TWSoI3CJfzJe64CkTsEt76YE3MK-M_effPX2vlLjE5_HELa-OWVw41KxLJttlzg93WBPloxOlpM0Qm44uxORC0f6CR9CKo-oynIf4qLsJYXifJ1p2mWq7hK6-YKmTibNdoCws0wWc_HeTSB9BvDys9fHTiUUnKBpDxlJVIfPXKsDY3z87e0wJ0TriCf58hw-TU1pDgUxns4ryDVivsbwyyeb-5UajgMQ6pELzjvhBWTMg3KGkWzkhc_aPfJkA',
    '1P_JAR': '2024-03-16-13',
    '__Secure-3PSIDTS': 'sidts-CjIBYfD7Z-8pkPBLVu6r8hYapX0IVdSZ2urajZu8VEa3DzlaJDt6eGe5GVxJvlMl9cG-BhAA',
    '__Secure-3PSIDCC': 'AKEyXzWvDlCwQ4-C_4uD8PBTSkWMdiqbygVcNS_-bu-q7JkkJwHp0YdH84M9L7loewkz54jCFg',
}

headers = {
    'authority': 'analytics.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'content-length': '0',
    # 'cookie': '__Secure-3PSID=g.a000hAjj2mkKgZvXCZln3UfVBaZbX0-WVGq6DhIteCZOglPLic3ZZMhrV5ue97PkskSgvjj_EAACgYKAZsSAQASFQHGX2MiO-cdR0uazHUBhB3elO2TThoVAUF8yKqO8L2KtqWH3pFrXF6lC0Qr0076; __Secure-3PAPISID=7Ls2RfL1LMJvBvGP/Aaj_I9FCtT3HDgMVf; NID=512=HVikv2m25CTtka4GwGuXqu1cTf78eu5RT47me2jZhtefvS8jqD8PqhTdXv7VSiSOiMBfLqcIDca9waLZOLXqt7jQ7oLJobU1v834-LblLBVVPFDnZHK40cuPtFNKV5sLPaNk_kbRzjORbruRTJFNGwWkXWCL4TWSoI3CJfzJe64CkTsEt76YE3MK-M_effPX2vlLjE5_HELa-OWVw41KxLJttlzg93WBPloxOlpM0Qm44uxORC0f6CR9CKo-oynIf4qLsJYXifJ1p2mWq7hK6-YKmTibNdoCws0wWc_HeTSB9BvDys9fHTiUUnKBpDxlJVIfPXKsDY3z87e0wJ0TriCf58hw-TU1pDgUxns4ryDVivsbwyyeb-5UajgMQ6pELzjvhBWTMg3KGkWzkhc_aPfJkA; 1P_JAR=2024-03-16-13; __Secure-3PSIDTS=sidts-CjIBYfD7Z-8pkPBLVu6r8hYapX0IVdSZ2urajZu8VEa3DzlaJDt6eGe5GVxJvlMl9cG-BhAA; __Secure-3PSIDCC=AKEyXzWvDlCwQ4-C_4uD8PBTSkWMdiqbygVcNS_-bu-q7JkkJwHp0YdH84M9L7loewkz54jCFg',
    'origin': 'https://visa.vfsglobal.com',
    'referer': 'https://visa.vfsglobal.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-client-data': 'CJG2yQEIpbbJAQipncoBCMTmygEIlqHLAQic/swBCIWgzQEY9snNARjSgs4B',
}

response = requests.post(
    'https://analytics.google.com/g/collect?v=2&tid=G-Z8LKRKHHG4&gtm=45je43d0v9138104707za200&_p=1710597308419&gcd=13l3l3l3l1&npa=0&dma=0&cid=815795067.1710164184&ul=en-us&sr=1920x1080&uaa=x86&uab=64&uafvl=Chromium%3B122.0.6261.129%7CNot(A%253ABrand%3B24.0.0.0%7CGoogle%2520Chrome%3B122.0.6261.129&uamb=0&uam=&uap=Windows&uapv=14.0.0&uaw=0&are=1&pae=1&pscdl=noapi&_eu=AEA&_s=2&dl=https%3A%2F%2Fvisa.vfsglobal.com%2Fbgd%2Fen%2Fita%2Fdashboard&dr=https%3A%2F%2Fvisa.vfsglobal.com%2Fbgd%2Fen%2Fita%2Flogin&sid=1710596853&sct=4&seg=1&dt=Dashboard%20%7C%20VFS%20Global&en=page_view&_et=11772&tfd=29836',
    cookies=cookies,
    headers=headers,
)


print(response)