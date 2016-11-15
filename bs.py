import requests,bs4


i=1  #UNIQUE ID OF THE DOC ADDED
text_file = open("cranfield-data.json", "w")
text_file.write("{")
text_file.write("\n")
#ADD ALL LINKS IN THIS STRING
web_link_all=['http://facilities.columbia.edu/housing/faqs-4','http://welcomeday.gradengineering.columbia.edu/international-students.html','http://welcomeday.gradengineering.columbia.edu/housing.html','http://www.cuf.columbia.edu/arbor/','http://facilities.columbia.edu/housing/faqs-4#waitlist','http://cuit.columbia.edu/cuit/manage-my-uni','http://cuit.columbia.edu/email-aliases','http://welcomeday.gradengineering.columbia.edu/welcome-day-schedule.html','http://welcomeday.gradengineering.columbia.edu/contact.html','http://welcomeday.gradengineering.columbia.edu/new-student-check-list.html','http://health.columbia.edu/students/immunization-compliance-requirements/immunization-compliance-requirements','http://welcomeday.gradengineering.columbia.edu/international-students.html','https://cc-seas.financialaid.columbia.edu/grad-seas','http://www.cumc.columbia.edu/id/']


for web_link in web_link_all:

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


text_file.write("\"commit\" : { } \n }")

    #div=soup.find_all("div", class_="views-field views-field-body answer")
    #for d in div:
    #    print(d.get_text())
    # para=soup.find_all("p")
    # for p in para:
    #     text_file.write(p.get_text())
    # text_file.close()