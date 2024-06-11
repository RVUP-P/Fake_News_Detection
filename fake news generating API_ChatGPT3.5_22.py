import random
from openai import OpenAI
import pickle
from datetime import datetime

client = OpenAI(api_key='Key는 비밀~')


def generate_political_news_article(topic):
    # Generate a catchy title based on the topic
    title_prompt = f"Generate a catchy news article title about {topic}."
    title_response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=title_prompt,
        max_tokens=100,  # 적절하게 조정
        temperature=0.7
    )
    title = title_response.choices[0].text.strip()

    # Use the title to generate the full article
    article_prompt = f"""
    Title: {title}
    Write a detailed news article on the topic of "{topic}". The article should cover recent developments, the background of the issue, key figures involved, and potential future implications. Include expert opinions and possible scenarios.

    Note: This article is generated for simulation purposes and does not reflect real events.
    """
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=article_prompt,
        max_tokens=2900,  # 충분한 길이로 조정
        temperature=0.7
    )
    content = response.choices[0].text.strip()

    return {"title": title, "text": content, "subject": topic}

# 파일에서 제목 목록 불러오기
with open("titles_list_all_4.pkl", "rb") as f:
    article_head_list = pickle.load(f)
    # article_head_list = article_head_list[550:]

# 각 배치의 제목을 사용하여 기사 생성
batch_size = 5
num_batches = len(article_head_list) // batch_size

for i in range(num_batches):
    start_index = i * batch_size
    end_index = start_index + batch_size
    titles_batch = article_head_list[start_index:end_index]
    
    articles_list = [generate_political_news_article(title) for title in titles_batch]

    # 파일 저장
    file_name = f"us_political_news_articles_3_{i+1}.pkl"
    with open(file_name, "wb") as f:
        pickle.dump(articles_list, f)
    
    print(f"Batch {i+1}: {len(articles_list)} articles have been successfully saved to {file_name}.")