import webbrowser



try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = input("Please Input You want to search: ")
  
for j in search(query, tld="co.in", num=1, stop=1, pause=2):
    url=j

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)

     