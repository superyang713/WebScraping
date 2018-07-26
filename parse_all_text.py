from bs4 import BeautifulSoup

html = """
<div>bunch of words一堆文字<img src="" alt="[吃瓜]"/>another bunch of words
又是一堆文字最后一堆文字<div>
<img src="" alt="[喵喵]haha"/><img src="" alt="[狗狗dog]"/>sfa又是一堆文字</div></div>
"""


def main():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())

    main_div = bs.find('div')
    contents = parse_div(main_div)
    print(contents)


def parse_div(div_tag):
    contents = div_tag.contents
    result = []
    for content in contents:
        if isinstance(content, str):
            content = content.replace('\n', '').replace(' ', '')
            result.append(content)
        elif content.has_attr('alt'):
            result.append(content.get('alt', ''))
        else:
            new_contents = parse_div(content)
            result.extend(new_contents)
    return ''.join(result)


if __name__ == '__main__':
    main()
