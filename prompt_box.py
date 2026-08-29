prompts = [
    {
        "title": "데이터 분석 보고서 생성",
        "content": "데이터 분석 결과를 바탕으로 보고서 개요를 작성해줘. 보고서 제목, 한 줄 요약, 핵심 인사이트, 목차, 리스크 및 한계, 후속 분석 과제를 포함하고 데이터에 없는 원인이나 수치는 임의로 만들지 말아줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "리포트 코치",
        "content": "너는 리포트 코치라는 이름의 AI 업무 보고서 설계 어시스턴트다. 사용자가 제공한 데이터 분석 결과를 바탕으로 경영진 또는 실무자가 이해하기 쉬운 보고서 개요를 작성해줘. 불확실한 내용은 단정하지 말고 확인 필요로 표시해줘.",
        "category": "페르소나",
        "favorite": False
    },
    {
        "title": "글로벌 여행 이슈 분석",
        "content": "수집된 여행 뉴스를 분석하여 국가, 지역, 여행 이슈 카테고리, 핵심 내용, 여행자 영향을 정리하고 영향도, 관심도, 시급성을 평가해줘. 여행 블로그에 활용할 수 있는 추천 제목도 생성해줘.",
        "category": "자동화",
        "favorite": False
    }
]

def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ")
    while title == "":
        print("제목을 입력해주세요.")
        title = input("제목: ")

    content = input("내용: ")
    while content == "":
        print("내용을 입력해주세요.")
        content = input("내용: ")

    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

    print("\n카테고리를 선택해주세요.")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    category_choice = input("선택: ")

    if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
        category = categories[int(category_choice) - 1]
    else:
        category = input("직접 카테고리를 입력해주세요: ")
        while category == "":
            print("카테고리를 입력해주세요.")
            category = input("카테고리: ")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)
    print("프롬프트가 추가되었습니다!")

def show_menu():
    print("\n=== Prompt Box ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

while True:
    show_menu()
    choice = input("선택: ")

    if choice == "1":
        add_prompt()
    elif choice == "0":
        print("Prompt Box를 종료합니다.")
        break
    else:
        print("아직 준비 중인 기능입니다.")