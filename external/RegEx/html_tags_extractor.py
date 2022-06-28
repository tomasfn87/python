import re


class Html:
    def __init__(self, html_string):
        self.html_string = html_string
        self.innerHtml = self.extractTagInnerHtml()
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
        if not self.doesStringContainTags():
            return False
        return self.checkForMultipleTags()

    def extractTagInnerHtml(self):
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
        # else:
        #     return { 'content': self.html_string }

    def isHtmlTag(self):
        self.html_string = Html.cleanHtml(self.html_string)
        match = re.match(Html.reHtml, self.html_string)
        if match:
            if Html.cleanHtml(match[0]) == self.html_string:
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
        content = self.extractTagInnerHtml()
        if content:
            if re.match(Html.reHtml, content) or re.match(Html.reSimpleHtml, content):
                return True
        return False
    
    def doesStringContainTags(self):
        if self.isHtmlTag() or self.isSimpleHtmlTag():
            return True
        else:
            html = re.match(Html.reHtml, self.html_string)
            simpleHtml = re.findall(Html.reSimpleHtml, self.html_string)
            if html or simpleHtml:
                return True
        return False

    def checkForMultipleTags(self):
        if self.isSimpleHtmlTag():
            return self.extractHtmlTagAsDict()
        if not self.doesStringContainTags():
            return self.html_string
        tags = []
        if self.isHtmlTag():
            tags.append(self.extractHtmlTagAsDict())
            if self.doesTagContainOtherTags():
                tags.append(Html(self.extractTagInnerHtml()).extractHtmlTagAsDict())
        elif self.doesStringContainTags():
            while self.html_string:
                html = re.match(Html.reHtml, self.html_string)
                simpleHtml = re.match(Html.reSimpleHtml, self.html_string)
                if html or simpleHtml:
                    if html:
                        tags.append(Html(html[0]).extractHtmlTagAsDict())
                        self.html_string = self.html_string[len(html[0]):]
                    else:
                        tags.append(Html(simpleHtml[0]).extractHtmlTagAsDict())
                        self.html_string = self.html_string[len(simpleHtml[0]):]
                else:
                    break
        return tags

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
t1 = Html(test1)
t2 = Html(test2)
t3 = Html('<img src="test.gif">')
t4 = Html('<head><title>Test</title></head>')
t5 = Html('<div><p>Just</p>a<span><br>test</span></div>')
t6 = Html('<span><img src="test.gif"></span>')
t7 = Html('<footer></footer><p></p>')
t8 = Html('<br>')
t9 = Html('Text and tag: <br>')
t10 = Html('Only text')
t11 = Html('<body onload="myFunction"><div><h1>*** Hello</h1><p>World! ***</p></div><footer><p></p></footer></body>')

print(t11.extractTagInnerHtml())

print()
print(' * Get HTML Tags')
print('1', t1.getHtmlTags())
print('2', t2.getHtmlTags())
print('3', t3.getHtmlTags())
print('4', t4.getHtmlTags())
print('5', t5.getHtmlTags())
print('6', t6.getHtmlTags())
print('7', t7.getHtmlTags())
print('8', t8.getHtmlTags())
print('9', t9.getHtmlTags())
print('10', t10.getHtmlTags())

# print()
# print(' * Extract HTML Tags As Dict')
# print('1', t1.extractHtmlTagAsDict())
# print('2', t2.extractHtmlTagAsDict())
# print('3', t3.extractHtmlTagAsDict())
# print('4', t4.extractHtmlTagAsDict())
# print('5', t5.extractHtmlTagAsDict())
# print('6', t6.extractHtmlTagAsDict())
# print('7', t7.extractHtmlTagAsDict())
# print('8', t8.extractHtmlTagAsDict())
# print('9', t9.extractHtmlTagAsDict())
# print('10', t10.extractHtmlTagAsDict())

# print()
# print(' * Extract Tag Inner HTML')
# print('1', t1.extractTagInnerHtml())
# print('2', t2.extractTagInnerHtml())
# print('3', t3.extractTagInnerHtml())
# print('4', t4.extractTagInnerHtml())
# print('5', t5.extractTagInnerHtml())
# print('6', t6.extractTagInnerHtml())
# print('7', t7.extractTagInnerHtml())
# print('8', t8.extractTagInnerHtml())
# print('9', t9.extractTagInnerHtml())
# print('10', t10.extractTagInnerHtml())

# print()
# print(' * Is HTML Tag')
# print('1', t1.isHtmlTag())
# print('2', t2.isHtmlTag())
# print('3', t3.isHtmlTag())
# print('4', t4.isHtmlTag())
# print('5', t5.isHtmlTag())
# print('6', t6.isHtmlTag())
# print('7', t7.isHtmlTag())
# print('8', t8.isHtmlTag())
# print('9', t9.isHtmlTag())
# print('10', t10.isHtmlTag())

# print()
# print(' * Is Simple HTML Tag')
# print('1', t1.isSimpleHtmlTag())
# print('2', t2.isSimpleHtmlTag())
# print('3', t3.isSimpleHtmlTag())
# print('4', t4.isSimpleHtmlTag())
# print('5', t5.isSimpleHtmlTag())
# print('6', t6.isSimpleHtmlTag())
# print('7', t7.isSimpleHtmlTag())
# print('8', t8.isSimpleHtmlTag())
# print('9', t9.isSimpleHtmlTag())
# print('10', t10.isSimpleHtmlTag())

# print()
# print(' * Does tag contain other tags')
# print('1', t1.doesTagContainOtherTags())
# print('2', t2.doesTagContainOtherTags())
# print('3', t3.doesTagContainOtherTags())
# print('4', t4.doesTagContainOtherTags())
# print('5', t5.doesTagContainOtherTags())
# print('6', t6.doesTagContainOtherTags())
# print('7', t7.doesTagContainOtherTags())
# print('8', t8.doesTagContainOtherTags())
# print('9', t9.doesTagContainOtherTags())
# print('10', t10.doesTagContainOtherTags())

# print()
# print(' * Does string contain other tags')
# print('1', t1.doesStringContainTags())
# print('2', t2.doesStringContainTags())
# print('3', t3.doesStringContainTags())
# print('4', t4.doesStringContainTags())
# print('5', t5.doesStringContainTags())
# print('6', t6.doesStringContainTags())
# print('7', t7.doesStringContainTags())
# print('8', t8.doesStringContainTags())
# print('9', t9.doesStringContainTags())
# print('10', t10.doesStringContainTags())