import random 

Questions=[]
with open("myfiled.txt","r") as file:
    Content=file.read().strip().split("\n\n")
    
    for block in Content:
        line=block.strip().split("\n")
        # print(len(line))
        if len(line)==3:
            que=line[0]
            # print(que)
            Opetion=line[1].split(",")
            Answer=line[2]
            
            
        Questions.append(
            {
                "question":que,
                "Opetions":Opetion,
                "Answer":Answer
            }
        )

random.shuffle(Questions)
score=0
for index,q in enumerate(Questions,1):
    # print(q["question"])
    print(f"\n Q{index}: {q["question"].replace("\\n", "\n").replace("\\t", "\t")}")
    Opetions=q["Opetions"]
    random.shuffle(Opetions)
    
    
    for i ,opt in enumerate(Opetions):
        print(f"{i}.{opt}")
    try:
        ans=int(input("Enter your choice answer(0-3)"))
        if Opetions[ans]==q["Answer"]:
            print("Correct Answer")
            score+=1
        else:
            print("wrong answer!"f"correct answer is {q["Answer"]}")
    except (ValueError,IndexError):
        print(f"Invalid Input correct answer is {q["Answer"]}")
print(f"Your Score is {score},out of {12}")