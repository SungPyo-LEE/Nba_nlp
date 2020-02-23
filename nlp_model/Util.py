from sklearn.metrics.pairwise import linear_kernel #, cosine_similarity
import pandas as pd
from numpy import dot
from numpy.linalg import norm
import numpy as np

class Util:
    def cos_sim(A, B):
        return dot(A, B) / (norm(A) * norm(B))

    def get_recommendations(title, cosine_sim=cosine_sim):
        # 선택한 영화의 타이틀로부터 해당되는 인덱스를 받아옵니다. 이제 선택한 영화를 가지고 연산할 수 있습니다.
        idx = indices[title]

        # 모든 영화에 대해서 해당 영화와의 유사도를 구합니다.
        sim_scores = list(enumerate(cosine_sim[idx]))

        # 유사도에 따라 영화들을 정렬합니다.
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # 가장 유사한 10개의 영화를 받아옵니다.
        sim_scores = sim_scores[1:11]

        # 가장 유사한 10개의 영화의 인덱스를 받아옵니다.
        movie_indices = [i[0] for i in sim_scores]

        # 가장 유사한 10개의 영화의 제목을 리턴합니다.
        return data['title'].iloc[movie_indices]