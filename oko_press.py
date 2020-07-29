from bs4 import BeautifulSoup
import requests

source = requests.get('https://oko.press').text
soup = BeautifulSoup(source, 'lxml')

# correct it \n thing
articles_links_and_subjects_dict = {}

main_article_link = soup.find('div', class_='home-page').a.attrs['href']
main_article_subject = soup.find('span', class_='subcategory-title').text
articles_links_and_subjects_dict[main_article_link] = main_article_subject

for div_tag in soup.find_all('div', class_='large-collapse'):
    try:
        next_article_link = div_tag.find('h4').a.attrs['href']
        next_article_subject = div_tag.find('div', class_='sub-category-name').text
    except:
        pass
    articles_links_and_subjects_dict[next_article_link] = next_article_subject

#NUM_OF_SELECTED_ARTICLES = 6
#for article_link in all_articles_links[:NUM_OF_SELECTED_ARTICLES]:
for article_link in all_articles_links:

# correct it: print(f"Subject of article: {article_subject}")

    article_site = requests.get(article_link).text
    article_site = BeautifulSoup(article_site, 'lxml')

# correct it: different tag then time

    article_date = article_site.find('time', class_='updated').text
    print(f'article date: {article_date}')

    article_author = article_site.find('span', class_='meta-section__autor').a.text
    print(f'article author: {article_author}')

    article_headline = article_site.find('h1', class_='title smaller-post-title').span.text
    print(article_headline)

    try:
        image_link = article_site.find('div', class_='slider_home_page slider_in_post')
        image_link = image_link.picture.source['data-srcset']
        print(image_link)
        # add image author
    except AttributeError:
        print("There is no image added to this article.")
    
    try:
        video_link = article_site.find('div', class_='off-canvas-wrapper')
        video_link = video_link.find('iframe')['src']
        print("Link to video:")
        print(video_link)
    # AttributeError, TypeError, KeyError
    except:
        video_link = None
    print('\n')

    all_paragraphs_list = []

    try:
        first_paragraph = article_site.find('div', class_="excerpt").p.text
    except:
        first_paragraph = ''

    all_paragraphs_list.append(first_paragraph)

    other_paragraphs = article_site.find('div', class_="entry-content")
    for paragraph in other_paragraphs:
        if paragraph in other_paragraphs.find_all('p'):
            all_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('h2'):
            all_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('blockquote'):
            all_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('ul'):
            all_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('tr'):
            all_paragraphs_list.append(paragraph.text)
        elif paragraph in other_paragraphs.find_all('img'):
            all_paragraphs_list.append(paragraph.get('src'))

    all_paragraphs = ('\n').join(all_paragraphs_list)
    print(all_paragraphs)

