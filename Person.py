import re

class Person:  
    def __init__(self, age, name, gender):
        self.name = name
        self.gender = gender
        self.age = int(age)

    def display(self): # 최종 출력
        print(f"\n이름 : {self.name}, 성별: {self.gender}")
        print(f"나이 : {self.age}")
        self.greet()
        
    def greet(self): # 인사 메시지
        if(self.age > 40):
            print(f"안녕하시렵니까, {self.name}! 어른이시군요!")
        elif(self.age > 20):
            print(f"안녕하세요, {self.name}! 성인이시군요!")
        else:
            print(f"안녕, {self.name}! 응애군요!") 
            
def get_age(): # 나이 입력 1이상
    while True:
        try:
            age = int(input("나이 : "))
            if(age > 0): 
                return age
            else :
                print("잘못된 나이를 입력하셨습니다.")
        except ValueError:
            print("잘못된 나이를 입력하셨습니다.")
    
def get_name(): # 이름 입력 한글 or 영어
    name = input("이름 : ").strip()
    pattern_en = r'^[a-zA-Z\s]+$'   # 영어 및 공백만 허용
    pattern_kr = r'^[가-힣\s]+$'     # 한글 및 공백만 허용
    if len(name) and (re.match(pattern_en, name) or re.match(pattern_kr, name)):
        return name
    else :
        print("잘못된 이름을 입력하셨습니다.")
        return get_name()
    
def get_gender(): # 성별 입력 male or female
    gender = input("성별 : ").strip().lower()
    
    if gender in ['male', 'female']:
        return gender
    else :
        print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")
        return get_gender()
    
age = get_age()
name = get_name()
gender = get_gender()

me = Person(age, name, gender)
me.display()