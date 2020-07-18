from bs4 import BeautifulSoup
import requests

source = requests.get('https://oko.press').text
soup = BeautifulSoup(source, 'lxml')

all_articles_links = []

main_article_link = soup.find('div', class_='home-page').a.attrs['href']
all_articles_links.append(main_article_link)

for div_tag in soup.find_all('div', class_='large-collapse'):
    try:
        next_article_link = div_tag.find('h4').a.attrs['href']
    except:
        pass
    all_articles_links.append(next_article_link)


for article in all_articles_links:
    try:
        article_subject = soup.find('div', class_='sub-category-name').text
        print(f"Subject of article: {article_subject}")
        print('\n')
    except:
        article_subject = soup.find('span', class_='subcategory-title').text
        print(f"Subject of article: {article_subject}")
        print('\n')

    article_site = requests.get(article).text
    article_site = BeautifulSoup(article_site, 'lxml')

# correct it
"""
    article_author = ''
    article_date = ''

    article_headline = article.h4.a.text
    print(article_headline)
    print('')
"""

    try:
        image_link = article_site.find('div', class_='slider_home_page slider_in_post')
        image_link = image_link.picture.source['data-srcset']
        print(image_link)
    except AttributeError:
        print("There is no image added to this article.")

    try:
        video_link = article_site.find('div', class_='off-canvas-wrapper')
        video_link = video_link.find('iframe')['src']
        print("Link to video:")
        print(video_link)
    except AttributeError:
        video_link = None
    except TypeError:
        video_link = None
    except KeyError:
        video_link = None

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
        elif paragraph in other_paragraphs.find_all('img'):
            filtered_paragraphs_list.append(paragraph.get('src'))

    all_paragraphs = ('\n').join(filtered_paragraphs_list)
    print(all_paragraphs)

"""