import wikipedia
wikipedia.set_lang("ru")
# result = wikipedia.search("2024")
result_2024_war = wikipedia.page("Бои в Курской области (2024)")
result_2024_Summer_Olympics = wikipedia.page("Летние Олимпийские игры 2024")
result_2024SO_medal_table = wikipedia.page("Медальный зачёт на летних Олимпийских играх 2024")

wiki_info = [
    result_2024_war,
    result_2024_Summer_Olympics,
    result_2024SO_medal_table,
]
