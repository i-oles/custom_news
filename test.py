my_dict = {
    'link_1' : 'subject_1',
    'link_2' : 'subject_2',
    'link_3' : 'subject_3',
}

for link, subject in my_dict.items():
    print(link)
    print(subject)


"""
articles_links_and_subjects_dict = {}

main_article_link = soup.find('div', class_='home-page').a.attrs['href']
main_article_subject = soup.find('span', class_='subcategory-title').text
articles_links_and_subjects_dict[main_article_link] = main_article_subject

for div_tag in soup.find_all('div', class_='large-collapse'):
    try:
        next_article_link = div_tag.find('h4').a.attrs['href']
        next_article_subject = div_tag.find('div', class_='sub-category-name').text
        articles_links_and_subjects_dict[next_article_link] = next_article_subject
    except:
        pass
"""
