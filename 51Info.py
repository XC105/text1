import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import json
# header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#            'cookie': '_uab_collina=159339704124225740207109; __zp__pub__=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1593397041; __g=-; __c=1593398819; __l=r=&l=%2Fwww.zhipin.com%2Fjob_detail%2Fb379a8bc81b1c38b0XZ629-4E1Y~.html%3Fka%3Dsearch_list_jname_1_blank%26lid%3Dnlp-7wDwprGBOhM.search.1&friend_source=0&friend_source=0; __a=76453785.1593397042.1593397042.1593398819.7.2.6.7; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1593401865; __zp_stoken__=1a7baZzA%2BAg8eUzkAaEAgb0MCUihGOSIaN0cmIz9eIH5kPHosI0FoPzlGSR97LgR5Hh89f2YiDDt7NkJVPCJneDFnDy45dzxaJDx7QAsiFF9zeA4kVAF%2BHhBoNgM8TkkyXCZ4ADVWDRg2BUY%3D',
#            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#            'accept-encoding': 'gzip, deflate, br',
#            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#            'cache-control': 'max-age=0',
#            'referer': 'https://www.zhipin.com/wapi/zpAntispam/verify/sliderNew?u=IA%7E%7E&callbackUrl=http%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2Fb379a8bc81b1c38b0XZ629-4E1Y%7E.html%3Fka%3Dsearch_list_jname_1_blank%26lid%3Dnlp-7wDwprGBOhM.search.1&p=IvRP9GS1RWsHTWs1P6k%7E',
#            'upgrade-insecure-requests': '1'}


page = urllib.request.urlopen('https://jobs.51job.com/guangzhou-thq/123369987.html?s=01&t=0')
contents = page.read()

soup = BeautifulSoup(contents,"html.parser")




for tag in soup.find_all('div',class_='cn'): #岗位名称，公司salary

    title = tag.find('h1').get_text()

    salary = tag.find('strong').get_text()

    print(title)
    print(salary)


for tag in soup.find_all('div',class_='jtag'): #公司待遇

    bonus = tag.find('span').get_text()

    print(bonus)


for tag in soup.find_all('p',class_='cname'): #公司名称

    conpanyName = tag.find('a').get_text()

    print(conpanyName)



for tag in soup.find_all('div',class_='tCompany_main'):  #职位信息


    info = tag.find('div', class_='bmsg job_msg inbox').get_text()

    # name  = tag.find('span', class_='bname').get_text()
    # intro= tag.find('div', class_='tmsg inbox').get_text()


    info1 = info.replace("\n","")
    info2 = info1.replace("\xa0","")

    print(info1)


result = []
arr = {}
arr['职位名称'] = title
arr['公司名称'] = conpanyName
arr['薪资'] = salary
arr['待遇'] = bonus
arr['职位信息'] = info2
result.append(arr)

# jsonInfo = json.dumps(result,ensure_ascii=False)



with open("info.json","w",encoding="utf-8") as fp:

    fp.write(str(result))


print('\n')
print(arr)



