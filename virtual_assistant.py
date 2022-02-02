import wolframalpha
import wikipedia
import wikipediaapi

while True:
    try:
            # wolframalpha API
            app_id = "[Unique App ID]"
            client = wolframalpha.Client(app_id)
            question = input("What would you like to know? ")
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
    except:
            # wikipedia-API
            wiki = wikipediaapi.Wikipedia('en')
            wiki_page = wiki.page(question)
            if print(wiki_page.summary) is None:
                print("No results returned, please search for something else.")
            else:
                print(wiki_page.summary)
