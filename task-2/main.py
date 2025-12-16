#Саплицкий
import json
with open("dump.json", "r", encoding="utf-8") as f:
    data = json.load(f)

skills = []
for item in data:
    if item.get("model") == "data.skill":
        code = item["fields"]["code"]
        title = item["fields"]["title"]
        skills.append({"code": code, "title": title})
        
print("start code ...")

user_code = input("Введите номер квалификации: ").strip()

chain = []
for skill in skills:
    skill_code = skill["code"]
    if user_code == skill_code or user_code.startswith(skill_code + "-"):
        chain.append(skill)

chain.sort(key=lambda x: len(x["code"]))

seen = set()
unique_chain = []
for skill in chain:
    if skill["code"] not in seen:
        unique_chain.append(skill)
        seen.add(skill["code"])

if unique_chain:
    print("============== Найдено ==============")
    for skill in unique_chain:
        print(f"{skill['code']} >> {skill['title']}")
else:
    print("============== Не найдено ==============")
    
print("... end code")
