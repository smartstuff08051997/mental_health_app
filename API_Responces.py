import dwani
import os

dwani.api_key = "bhavyalahoti2906@gmail.com_dwani"

dwani.api_base = "https://dwani-dwani-api.hf.space"

prompt1 = "what is the normal age of cat?"

resp = dwani.Chat.create(prompt=f"{prompt1} - Note you are a psychologist whose job to enhance mental health of human beings not matter what questions people are asking you have to answer it and then two things you must have to add 1)how it can impact there mental health and 2) Give prescriptions to improve there mental health in that situation. - don't finish your response without prescription manage tokens accordingly. -long responses only", src_lang="eng_L", tgt_lang="english")
print(resp["response"])

api_response = dwani.Chat.create(
    prompt=f"{prompt1} - Note you are a psychologist whose job to enhance mental health of human beings not matter what questions people are asking you have to answer it and then two things you must have to add 1)how it can impact there mental health and 2) Give prescriptions to improve there mental health in that situation. - don't finish your response without prescription manage tokens accordingly. -long responses only",
    src_lang="eng_Latn",
    tgt_lang="english"
)

response_text = api_response["response"]

response = dwani.Audio.speech(input=response_text, response_format="mp3")
with open("output.mp3", "wb") as f:
    f.write(response)












