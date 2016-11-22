def generatejson():
    import requests, bs4
    f=open('linksoutput.txt','r')
    web_link_all=[]
    for line in f:
        line=line.rstrip()
        web_link_all.append(line)

    i=1  #UNIQUE ID OF THE DOC ADDED
    text_file = open("cranfield-data.json", "w")
    text_file.write("{")
    text_file.write("\n")
    for web_link in web_link_all:
        try:
            t=web_link  #TITLE OF THE FILE ADDED
            res = requests.get(web_link)
            soup = bs4.BeautifulSoup(res.text,'html.parser')
            p=soup.get_text()
            p= p.replace("\""," ")
            p= p.replace("\n"," ")
            whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            p = ''.join(filter(whitelist.__contains__, p))

            text_file.write("\t\"add\" : {\n\t\t\"doc\" : {\n\t\t\t\"id\" : "+str(i)+",\n\t\t\t\"body\" : \""+p+"\",\n\t\t\t\"title\" : \""+t+"\"\n\t\t\t\t}\n\t\t\t}")
            text_file.write(",")
            text_file.write("\n")
            i=i+1
        except:
            pass


    text_file.write("\"commit\" : { } \n }")

        #div=soup.find_all("div", class_="views-field views-field-body answer")
        #for d in div:
        #    print(d.get_text())
        # para=soup.find_all("p")
        # for p in para:
        #     text_file.write(p.get_text())
        # text_file.close()