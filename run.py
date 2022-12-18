from bot import Bot

with Bot() as bot:
    bot.open_page()
    print("Enter job type")
    job = input()
    print("Enter location")
    location = input()
    bot.search(job, location)



