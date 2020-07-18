from bs4 import BeautifulSoup
import requests

source = requests.get('https://oko.press').text
soup = BeautifulSoup(source, 'lxml')

def find_article_subject(tag, tag_class):
    article_subject = article.find(tag, class_=tag_class).text
    return article_subject


for article in soup.find_all('div', class_='large-collapse'):
    try:
        try:
            find_article_subject('div', 'sub-category-name')
        except:
            find_article_subject('span', 'subcategory-title')

        link_to_article_site = article.a['href']

        article_site = requests.get(link_to_article_site).text
        article_site = BeautifulSoup(article_site, 'lxml')

        article_headline = article.h4.a.text
        print(article_headline)
        print('')

        article_author = ''
        article_date = ''

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

    except AttributeError:
        print("\nThe End")