import urllib.request
import re
import os
import sys
from bs4 import BeautifulSoup
import time
import datetime

def key_word_setter():
    key_word = input("\n请输入你需要搜索的关键词：").strip().replace(" ", "+")
    return key_word


def path_maker(key_word):
    os.mkdir(key_word)                                                 
    os.chdir(key_word)



def url_setter(key_word):
    url_origin = "http://searchen.chinadaily.com.cn/search?query=%s"  % key_word
    url = "".join(url_origin)
    return url



def url_to_soup(url):                                             
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read()   
    soup = BeautifulSoup(html, "html.parser")
    print ("\n正在打开：",url)        
    return soup


def times_finder(soup):
    times_list_origin = list(soup.find_all(style="width:300px; float:left;text-align:left;color:#999999"))
    times_list = []
    for each_time_loop in times_list_origin:
        each_time = each_time_loop.text.strip()[:10].split(".")
        times_list.append((int(each_time[0]), int(each_time[1]), int(each_time[2])))        
    return times_list




def titles_finder(soup):
    titles_list_origin = list(soup.find_all(href=re.compile("http://www.bjreview.com/"), target="_blank",style="font-size:16px; font-weight:bold"))
    titles_list = []
    for each_title_loop in titles_list_origin:
        titles_list.append(each_title_loop.text) 
    return titles_list


def each_filename_maker(each_title):     
    article_filename_revised = ""                                     
    for each_char in each_title:
        if each_char.isdigit() or each_char.isalpha() or each_char.isspace():
            article_filename_revised += each_char      
    each_filename = article_filename_revised
    return each_filename



def links_finder(soup):
    links_list_origin = soup.find_all(href=re.compile("http://www.bjreview.com/"), target="_blank",style="font-size:16px; font-weight:bold")
    links_list = []
    for each_link_loop in links_list_origin:
        links_list.append(each_link_loop["href"])
    return links_list


def listfile_maker(title_list, links_list):       
    with open("Article List.txt", "w") as f:                              
        for abel in range(len(title_list)):
            content = "\n\n标题："+ title_list[abel] + "\n链接："+ links_list[abel]
            f.write(content)

def content_writer(soup_each_link, each_filename, each_title, each_link, each_time):
    article_content = []
    article_content.append(each_title)
    article_content.append("\n")                                     
    article_content.append(str(each_time))
    article_content.append("\n")
    article_content.append(each_link)                                
    article_filename = each_filename + ".txt"                           
                      
    for each_para in soup_each_link.find_all("p"):
        article_content.append("\n")
        article_content.append(each_para.text)                       
        article_content.append("\n\n")
        with open(article_filename, 'w+',encoding='utf-8') as file:  
            file.writelines(article_content)
 
 



def main():
    print("\n本爬虫为了爬取北京周报上的文章而设计，可以输入关键词然后将搜到的文章下载下来。")
    key_word = key_word_setter()              
    start_date_origin = (input("\n请输入寻找的起始年月日（如“2010,12,24”）："))
    end_date_origin = (input("\n请输入寻找的终止年月日（如“2010,12,24”）："))
    
    regulation = re.compile(r"\d{4}[,]\d{1,2}[,]\d{1,2}")

    if regulation.fullmatch(start_date_origin) and regulation.fullmatch(end_date_origin):
        pass
    else:
        print("\n您的输入有误，请重启软件。3秒后软件关闭。\n")
        time.sleep(3)
        sys.exit(0)
        
    
    start_date_list = start_date_origin.split(",")
    start_date = tuple([int(each_number) for each_number in start_date_list])
  

    
    end_date_list = end_date_origin.split(",")
    end_date = tuple([int(each_number) for each_number in end_date_list])
      
    
    if end_date < start_date:        
        start_date, end_date = end_date, start_date

        
    try:
        path_maker(key_word)                  
    except OSError:
        print("\n目标文件夹名字存在重复，请删掉相关文件夹再试。3秒后软件关闭。\n")
        time.sleep(3)
        sys.exit(0)
            
    url = url_setter(key_word)                
    soup = url_to_soup(url)                   
    times_list = times_finder(soup)           
    titles_list = titles_finder(soup)          
    links_list = links_finder(soup)             
        
    im_time = (2017,2,17)

    info = [{"title": titles_list[x], "link": links_list[x], "time":times_list[x]} for x in range(len(titles_list))]
    newinfo = list(filter(lambda y: (y["time"] < im_time) and (start_date <= y["time"] <= end_date), info))
     
    if len(newinfo) < len(info):
        print("\n在所有爬取的文章中，某些文章不满足下载条件。")

    

    real_title_list = [(each["title"]) for each in newinfo]
    real_link_list = [(each["link"]) for each in newinfo]

    listfile_maker(real_title_list, real_link_list)

    try:
        path_maker(key_word)                  
    except OSError:
        print("\n目标文件夹名字存在重复，请删掉相关文件夹再试。3秒后软件关闭。\n")
        time.sleep(3)
        sys.exit(0)

 

                
    for each in range(len(newinfo)):
        time.sleep(1)
        each_title = newinfo[each]["title"]
        each_link = newinfo[each]["link"]
        each_time = newinfo[each]["time"]
        soup_each_link = url_to_soup(each_link)
        each_filename = each_filename_maker(each_title)
        content_writer(soup_each_link, each_filename,each_title, each_link, each_time)
    print("\n网页中拥有关键词%s的文章已经抓取完毕，共%s篇，3秒后软件关闭。\n" %(key_word,len(newinfo)))                  
    time.sleep(3)
    sys.exit(0)

        
if __name__ == "__main__":
    main()
    input()


   







