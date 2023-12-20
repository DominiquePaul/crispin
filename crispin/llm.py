import openai

client = openai.OpenAI()

def get_all_gpts():
    client.models.list().model_dump()
    names = [entry["id"] for entry in client.models.list().model_dump()["data"] if "gpt" in entry["id"]]
    for x in names:
        print(x)
