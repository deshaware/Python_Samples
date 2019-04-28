import sharepy

s = sharepy.connect("lti3.sharepoint.com")

r = s.get("https://lti3.sharepoint.com/_api/web/lists/GetByTitle('Documents')");
s.save()
sharepy.load()