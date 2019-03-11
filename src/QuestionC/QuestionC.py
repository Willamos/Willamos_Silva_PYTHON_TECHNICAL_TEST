import requests
import string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


class Scrapper():

    headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    session = None

    def query_from_google(self, user_query):
        self.session = requests.Session()
        query = '+'.join(user_query.split(' '))
        url = 'https://www.google.com/search?q=' + user_query + '&ie=utf-8&oe=utf-8&num=5&lr=lang_en'
        response = self.session.get(url, headers=self.headers_Get)
        infos = {}

        if(response.status_code == 200):
            soup = BeautifulSoup(response.content, 'html.parser')

            # findings = soup.find_all('div', {'class': g}).find_
            search = soup.find_all('div', {'class': 'r'})
            for item in search:
                current_link = item.a['href']
                most_relevant_paragraph = self.get_info_from_site(current_link, user_query)
                infos[current_link] = most_relevant_paragraph

        else:
            return {'status': 'the API wasn\'t able to get '}

        return infos


    def get_info_from_site(self, link, query):
        response = self.session.get(link, headers=self.headers_Get)
        query = query.translate(str.maketrans('', '', string.punctuation)).lower()
        if (response.status_code == 200):
            soup = BeautifulSoup(response.content, 'html.parser')

            texts = soup.find_all('p')
            texts = list(map(lambda x: x.getText().lower(), texts))
            # for i in range(len(texts)):
            #     texts[i] = texts[i].getText().lower()
            # text = soup.text.lower().split('\n')

            max_occurencies = 0
            best_paragraph = ''
            for paragraph in texts:
                paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
                ocurrencies = self.count_occurences(paragraph, query)
                if max_occurencies < ocurrencies:
                    max_occurencies = ocurrencies
                    best_paragraph = '\n'.join([best_paragraph, paragraph])
            return best_paragraph

        return ''


    def remove_stop_words(self, text):
        stop = stopwords.words('english')
        text = text.split()
        text = list(filter(lambda x: x not in stop, text))
        return ' '.join(text)

    def count_occurences(self, paragraph, query):
        query = self.remove_stop_words(query).split()
        total_count = 0
        for word in query:
            total_count += paragraph.count(word)
        return total_count

# my idea was to return the paragraphs with the most terms from the query
# with that said, I've tried to make both query and text form requested sites
# to lower case, so the words would match. I've tried an approach based on counting how many
# times each term would appear in each one of the paragraphs. If the paragraph seems to be more
# relevant than a previous relevant one,  I'd just concatenate what I previously have to the
# new relevant paragraph. I've also worried about removing the punctuation and stop words
# from the paragraphs to make the search more precise. with a bit more time to improve the
# solution I'd try to use TF-IDF algorithm as a way to decide which paragraphs
# are more relevant based on the query.
