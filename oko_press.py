from bs4 import BeautifulSoup
import requests

source = requests.get('https://oko.press').text
soup = BeautifulSoup(source, 'lxml')

num_of_articles = 6

for article in soup.find_all('div', class_='large-collapse'):

    subject = article.find('div', class_='sub-category-name').text
    print(subject)
    print('')

    headline = article.h4.a.text
    print(headline)
    print('')

    link_to_article_site = article.h4.a['href']

    article_site = requests.get(link_to_article_site).text
    article_site = BeautifulSoup(article_site, 'lxml')

    try:
        image_link = article_site.find('picture').img['src']
    except:
        image_link = None
        video_link = article_site.find('iframe')['src']
        print(video_link)

    print(image_link)
    print('')
    try:
        first_paragraph = article_site.find('div', class_="excerpt").p.text
    except:
        first_paragraph = ''
        
    other_paragraphs = article_site.find('div', class_="entry-content")
    filtered_paragraphs_list = [first_paragraph]
    for paragraph in other_paragraphs:
        if paragraph in other_paragraphs.find_all('p'):
            filtered_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('h2'):
            filtered_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('blockquote'):
            filtered_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('ul'):
            filtered_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('tr'):
            filtered_paragraphs_list.append(paragraph.text)


    all_paragraphs = ('\n').join(filtered_paragraphs_list)
    print(all_paragraphs)


"""
elif paragraph in other_paragraphs.find_all('img'):
filtered_paragraphs_list.append(paragraph.get('src'))
"""
