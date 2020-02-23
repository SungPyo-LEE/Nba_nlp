
import pandas as pd
import sys
from nltk.corpus import stopwords
from gensim import corpora
import gensim
import time
import pyLDAvis.gensim

#import nltk
#nltk.download('stopwords')
#sys.exit(0)
raw_data = pd.read_csv('C:/Users/sunng/PycharmProjects/Nba_Playoff_predic/raw_data/raw_data.csv')
documents = list(raw_data['0'])
news_df = pd.DataFrame({'document':documents})


# 알파벳을 제외하고 모두 제거`
news_df['clean_doc'] = news_df['document'].str.replace("[^a-zA-Z#]", " ")

clean_doc=list(news_df['clean_doc'])


cl_doc=[]
for doc in clean_doc:
    try:
        w = doc.split()
        #print(doc)
        if len(w)>3:
            doc = ' '.join(w)
            cl_doc.append(doc)
    except:
        pass
news_df = pd.DataFrame({'clean_doc':cl_doc})
# 길이가 3이하인 단어는 제거 (길이가 짧은 단어 제거)
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

# 전체 단어에 대한 소문자 변환
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: x.lower())



#볼용어 처리
stop_words = stopwords.words('english') # NLTK로부터 불용어를 받아옵니다.
tokenized_doc = news_df['clean_doc'].apply(lambda x: x.split()) # 토큰화
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])
# 불용어를 제거합니다.

# 역토큰화 (토큰화 작업을 역으로 되돌림)
detokenized_doc = []
for i in range(len(news_df)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

news_df['clean_doc'] = detokenized_doc

#정수 인코딩과 단어 빈도수 집합 만들기 (gensim의 corpora.Dictionary 사용)
testdic = corpora.Dictionary([['a','b','c'],['a','b','z']])
#print(testdic)
#print(testdic.doc2bow(['a','b','z','z']))

dictionary = corpora.Dictionary(tokenized_doc)
corpus = [dictionary.doc2bow(text) for text in tokenized_doc]
#print(corpus[0:2]) # 수행된 결과에서 두번째 문서 출력. 첫번째 문서의 인덱스는 0

#print(dictionary)

#print(dictionary[66])

### MODEL TRAIN
NUM_TOPICS = 20 #20개의 토픽, k=20


ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)


#토픽 핵심 4단어 출력
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)

print(ldamodel.print_topics())


## LDA를 이용한 문서분류 체크
for i, topic_list in enumerate(ldamodel[corpus]):
    if i==5:
        break
    print(i,'번째 문서의 topic 비율은',topic_list)

def make_topictable_per_doc(ldamodel, corpus, texts):
    topic_table = pd.DataFrame()

    # 몇 번째 문서인지를 의미하는 문서 번호와 해당 문서의 토픽 비중을 한 줄씩 꺼내온다.
    for i, topic_list in enumerate(ldamodel[corpus]):
        doc = topic_list[0] if ldamodel.per_word_topics else topic_list
        doc = sorted(doc, key=lambda x: (x[1]), reverse=True)
        # 각 문서에 대해서 비중이 높은 토픽순으로 토픽을 정렬한다.
        # EX) 정렬 전 0번 문서 : (2번 토픽, 48.5%), (8번 토픽, 25%), (10번 토픽, 5%), (12번 토픽, 21.5%),
        # Ex) 정렬 후 0번 문서 : (2번 토픽, 48.5%), (8번 토픽, 25%), (12번 토픽, 21.5%), (10번 토픽, 5%)
        # 48 > 25 > 21 > 5 순으로 정렬이 된 것.

        # 모든 문서에 대해서 각각 아래를 수행
        for j, (topic_num, prop_topic) in enumerate(doc): #  몇 번 토픽인지와 비중을 나눠서 저장한다.
            if j == 0:  # 정렬을 한 상태이므로 가장 앞에 있는 것이 가장 비중이 높은 토픽
                topic_table = topic_table.append(pd.Series([int(topic_num), round(prop_topic,4), topic_list]), ignore_index=True)
                # 가장 비중이 높은 토픽과, 가장 비중이 높은 토픽의 비중과, 전체 토픽의 비중을 저장한다.
            else:
                break
    return(topic_table)

topictable = make_topictable_per_doc(ldamodel, corpus, tokenized_doc)
topictable = topictable.reset_index() # 문서 번호을 의미하는 열(column)로 사용하기 위해서 인덱스 열을 하나 더 만든다.
topictable.columns = ['문서 번호', '가장 비중이 높은 토픽', '가장 높은 토픽의 비중', '각 토픽의 비중']
print(topictable[:10])