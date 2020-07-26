#coding:utf8
import requests
import re
domains = set() # 域名去重列表，默认为空
domain = 'http://xqctk.jtys.sz.gov.cn' # 请求网址的域名
html = requests.get(domain).text
s = re.findall(r'http[^\/]{1,2}//([^(\/| |")]+)', html)
print(set(s))
# from lxml import etree
# from urllib.parse import urlparse
# tree = etree.HTML(html)
#
# def match_link(links):
#     for link in links:
#         if not re.match(r'(//|http|https).*', link):
#             continue
#         if str(link).startswith('//'):
#             link = domain+link
#         res = urlparse(link)
#         domains.add(res.netloc)
#
# href_links = tree.xpath('//@href')
# match_link(href_links)
# src_link = tree.xpath('//@src')
# match_link(src_link)
# print(domains)
# print('*'*100)