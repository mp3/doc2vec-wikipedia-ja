## Preparation

Download dump file of japanese wikipedia from [here](https://dumps.wikimedia.org/jawiki/latest/) (filename is `jawiki-latest-pages-articles.xml.bz2`)

Install MeCab and NEologd dictionary
- https://github.com/neologd/mecab-ipadic-neologd

Install packages
```
pip install requirements.txt
```

## Training

```
python train.py
```

## Inference

example
```
import gensim
from pprint import pprint
model = gensim.models.Doc2Vec.load(''wikipedia.model)
pprint(model.docvecs.most_similar(['バラク・オバマ']))
```

result
```
[('ジョージ・W・ブッシュ', 0.6693710684776306),
('ビル・クリントン', 0.6429920196533203),
('ジョー・バイデン', 0.6411311030387878),
('ヒラリー・クリントン', 0.6324282884597778),
('リチャード・ホルブルック', 0.6311899423599243),
('ドナルド・トランプ', 0.6021257638931274),
('アメリカ合衆国の歴史', 0.5982885360717773),
('ロナルド・レーガン', 0.5905283689498901),
('胡錦濤', 0.5833597183227539),
('ティーパーティー運動', 0.5821385383605957)]
```

