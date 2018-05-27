import MeCab
import gensim
from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.doc2vec import Doc2Vec, Doc2VecVocab, TaggedDocument

mecab = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

wiki = WikiCorpus('jawiki-latest-pages-articles.xml.bz2')

class TaggedWikiDocument(object):
    def __init__(self, wiki):
        self.wiki = wiki
        self.wiki.metadata = True
    def __iter__(self):
        for content, (title) in self.wiki.get_texts():
            yield TaggedDocument([c for c in content], [title])

document = TaggedWikiDocument(wiki)
model = Doc2Vec(documents=document, dm=1, vector_size=400, window=8, min_count=10, epochs=10, workers=6)
model.save('model/wikipedia.model')
