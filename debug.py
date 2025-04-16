
def test_llm():
    from src.agents.llm import (
        reasoning_llm, 
        basic_llm,
        vl_llm
    )
    stream = reasoning_llm.stream("what is mcp?")
    full_response = ""
    for chunk in stream:
        full_response += chunk.content
    print("=== output:", full_response)

    print(basic_llm.invoke("Hello"))
    print(vl_llm.invoke("Hello"))



def test_crawler():
    # markdown格式
    from src.crawler import Crawler
    url = "https://fintel.io/zh-hant/s/br/nvdc34"
    crawler = Crawler()
    article = crawler.crawl(url)
    print(article.to_markdown())

def test_crawler_msg():
    # 消息格式
    from src.crawler import Crawler
    url = "https://news.qq.com/rain/a/20250415A09JQ200"
    crawler = Crawler()
    article = crawler.crawl(url)
    print(article.to_message())

if __name__ == "__main__":
    print("=== start")
    test_crawler_msg()
    print("=== end")
