import re


test1 = '''<html>
  <body onload="myFunction">
    <div>
      <h1>*** Hello</h1>
      <p>World! ***</p>
    </div>
    <footer><p></p></footer>
  </body>
</html>'''
test2 = '''<head>
  <title>Test</title>
</head>
<body onload="myFunction">
  <div>
    <h1>*** Hello</h1>
    <p>World! ***</p>
  </div>
  <footer><p></p></footer>
</body>'''
test3 = '<img src="test.gif">'


class Html:
    def __init__(self, html_string):
        self.html_string = html_string
        self.innerHtml = self.extractHtmlTagContent()
        self.content = self.extractHtmlTagAsDict()
    
    reHtml = r"(?si)(\<)([a-z][a-z0-9]*\b)(\s*[^>]*)(\>)(.*?)(<\/)\2(\>)"
    reSimpleHtml = r"\<\/?([a-z][a-z0-9]*\b)\s*[^>]*\s*\>"
    reEmptySpacesBetweenTags = r"\>\s*\<"
    
    def cleanHtml(html_string):
        clean = True
        cleanHtml = ''

        for i in range(0, len(html_string)):
            if html_string[i] in ['<', '"', "'"]:
                clean = False
            if html_string[i] in ['>', '"', "'"] and not clean:
                clean = True
            if not clean:
                cleanHtml += html_string[i]
            else:
                if html_string[i] not in ['\n', '\t', '\r']:
                    cleanHtml += html_string[i]

        return re.sub(Html.reEmptySpacesBetweenTags, '><', cleanHtml)

    def getHtmlTags(self):
        if not self.isHtmlTag() and not self.isSimpleHtmlTag():
            return False
        return self.checkForMultipleTags()

    def extractHtmlTagContent(self):
        if self.isHtmlTag():
            tag = re.match(Html.reHtml, self.html_string)
            innerTag = Html.cleanHtml(tag[5]).strip()
            if innerTag:
                innerTag = innerTag.strip()
            return innerTag
        return ''

    def extractHtmlTagAsDict(self):
        if self.isHtmlTag():
            tag = re.match(Html.reHtml, self.html_string)
            tagName = tag[2]
            cleanTag = Html.cleanHtml(tag[0])
            return { 'name': tagName, 'content': cleanTag, 'innerHtml': Html(self.innerHtml).checkForMultipleTags() }
        elif self.isSimpleHtmlTag():
            tag = re.match(Html.reSimpleHtml, self.html_string)
            tagName = tag[1]
            cleanTag = Html.cleanHtml((tag[0]))
            return { 'name': tagName, 'content':  cleanTag }
        else:
            return ''

    def isHtmlTag(self):
        self.html_string = Html.cleanHtml(self.html_string)
        match = re.match(Html.reHtml, self.html_string)
        if match:
            if re.match(Html.reHtml, self.html_string):
                return True
        return False

    def isSimpleHtmlTag(self):
        self.html_string = Html.cleanHtml(self.html_string)
        match = re.match(Html.reSimpleHtml, self.html_string)
        if match:
            if match[0] == self.html_string:
                return True
        return False

    def doesTagContainOtherTags(self):
        if self.isHtmlTag():
            content = self.extractHtmlTagContent()
            if content:
                if re.match(Html.reHtml, content) or re.match(Html.reSimpleHtml, content):
                    return True
        return False

    def checkForMultipleTags(self):
        tags = []
        if self.isHtmlTag():
            while self.doesTagContainOtherTags():
                match = re.match(Html.reHtml, self.html_string)
                if match:
                    tags.append(self.extractHtmlTagAsDict())
                else:
                    match = re.match(Html.reSimpleHtml, self.html_string)
                    if match:
                        tags.append(self.extractHtmlTagAsDict())
                self.html_string = Html.cleanHtml(self.html_string[len(match[0]):]).strip()
            if len(tags) != 0:
                if len(tags) == 1:
                    return tags[0]
                else:
                    return tags
        elif self.isSimpleHtmlTag():
            return self.extractHtmlTagAsDict()

t1 = Html(test1)
t2 = Html(test2)
t3 = Html(test3)
t4 = Html('<head><title>Test</title></head>')
t5 = Html('<div><p></p><span></span></div>')

#print(t4.extractHtmlTagContent())

# print(t1.content)
# print(t2.content)
# print(t3.content)
# print()
# print(t1.innerHtml)
# print(t2.innerHtml)
# print(t3.innerHtml)
# print()
print(t1.getHtmlTags())
print()
print(t2.getHtmlTags())
print()
print(t3.getHtmlTags())
# print(t5.checkForMultipleTags())
# print()
# print(t5.checkForMultipleTags())