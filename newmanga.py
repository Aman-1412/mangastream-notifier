# to search:
# refresh the page in flask
# ajax. to "update" the updated manga in the same page(effectively rendering the first "to search" pointless)
#Check out : http://flask.pocoo.org/docs/0.11/patterns/jquery/#the-html

# setInterval(                               //Periodically 
  # function()
  # {
     # $.getJSON(                            //Get some values from the server
        # $SCRIPT_ROOT + '/get_values',      // At this URL
        # {},                                // With no extra parameters
        # function(data)                     // And when you get a response
        # {
          # $("#result").text(data.result);  // Write the results into the 
                                           # // #result element
        # });
  # },
  # 500);                                    // And do it every 500ms
  
  
 # for x in a:
     # print x.link[-6:-2]
	 
# s =set(ch_name)	 
# for i in s:
    # names[i] = names.get(i)

def checker(count=0):
	if latest == ch_name[0] and count==0:
		pass
	elif latest == ch_name[0] and count!=0:
		while(count):
			ch_name.insert(0," ".join((feed.entries[count].title).split()[:-1]))
			ch_num.insert(0,(feed.entries[count].title).split()[-1])
			ch_name.pop()
			ch_num.pop()
			count-=1
			
	else:
		count+=1
		checker(count)


import feedparser
from time import sleep
from flask import Flask, render_template, request

app=Flask(__name__)


# feed = feedparser.parse("http://mangastream.com/rss")

# feed.keys()

 # for x in feed.entries:
     # ch_name = " ".join((x.title).split()[:-1])
     # ch_num = (x.title).split()[-1]
	 
@app.route("/")
def initial_scan():
	feed = feedparser.parse("http://mangastream.com/rss")
	ch_name=[]
	ch_link=[]
	ch_num=[]
	for x in feed.entries:
		ch_name.append(" ".join((x.title).split()[:-1]))
		ch_num.append((x.title).split()[-1])
		ch_link.append(x.link)
	combo = zip(ch_name,ch_num)
	return render_template("index.html",ch_name=ch_name,ch_link=ch_link,ch_num=ch_num,lenva=len(ch_name))

# @app.route("/subscribe")
def scan():
	feed = feedparser.parse("http://mangastream.com/rss")
	latest_ch_name = " ".join((feed.entries[1].title).split()[:-1])
	latest_ch_num = (feed.entries[1].title).split()[-1]

	
# sleep(60)
# scan()
	
	 
if __name__=="__main__":
    app.run(debug=True)	 
	 
# feed.entries[1]
# {'summary_detail': {'base': u'http://mangastream.com/rss', 'type': u'text/html',
 # 'value': u'Sudden Death', 'language': None}, 'links': [{'href': u'http://mangas
# tream.com/read/tokyo_ghoulre/104/3858/1', 'type': u'text/html', 'rel': u'alterna
# te'}], 'published_parsed': time.struct_time(tm_year=2016, tm_mon=12, tm_mday=3,
# tm_hour=14, tm_min=43, tm_sec=32, tm_wday=5, tm_yday=338, tm_isdst=0), 'title':
# u'Tokyo Ghoul:re 104', 'summary': u'Sudden Death', 'guidislink': False, 'title_d
# etail': {'base': u'http://mangastream.com/rss', 'type': u'text/plain', 'value':
# u'Tokyo Ghoul:re 104', 'language': None}, 'link': u'http://mangastream.com/read/
# tokyo_ghoulre/104/3858/1', 'published': u'Sat, 03 Dec 2016 6:43:32 -0800', 'id':
 # u'http://mangastream.com/r/tokyo_ghoulre/104/3858/1'}