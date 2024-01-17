import requests
import streamlit as st

def fetch_news(query):
    api_key = '72772f9ef4824d49b5227dfbd9ea5a30'  
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("articles", [])
    except requests.exceptions.RequestException as err:
        st.error(f"Error fetching news: {err}")
        return []

def main():
    st.title("News Flash: Bringing You the Latest and Greatest Updates")

    query = st.text_input("What headlines are you searching for today ?")
    if st.button("Search"):
        news = fetch_news(query)
        for article in news:
            st.write(f"**Title:** {article['title']}")
            st.write(f"**Description:** {article['description']}")

            # Display image if available
            if article.get('urlToImage'):
                st.image(article['urlToImage'], caption='Image', use_column_width=True)
            
            st.write("---")

if __name__ == "__main__":
    main()


