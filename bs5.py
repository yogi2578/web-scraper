def GenerateLinks(levels):
    import requests, bs4
    import difflib

    j=0

    def get_overlap(s1, s2):
        s = difflib.SequenceMatcher(None, s1, s2)
        pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2))
        return s1[0:pos_a]+s2[0:]

    f = open('linksinput.txt', 'r')
    web_link_all = []
    for line in f:
        line = line.rstrip()
        web_link_all.append(line)
    final=web_link_all

    for i in range(1,levels):
        final_links=[]
        for wl in web_link_all:
            try:
                res = requests.get(wl)
                if(str(res) == "<Response [200]>"):
                    soup = bs4.BeautifulSoup(res.text,'html.parser')
                    aa=soup.find_all("a",href=True)
                    for a in aa:
                        if len(a['href'])!=0:
                            if (a['href'][0]=="h") or (a['href'][0]=="/"):
                                if a['href'][0]=="/":
                                    a['href']=get_overlap(wl,a['href'])
                                if a['href'][0:4]=="http":
                                    print j
                                    j=j+1
                                    final_links.append(a['href'])
            except:
                pass

        final_links=list(set(final_links))
        final.extend(final_links)
        final = list(set(final))
        web_link_all=final_links
    thefile = open('linksoutput.txt', 'w')
    for item in final:
      thefile.write("%s\n" % item)