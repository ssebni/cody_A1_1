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

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{i}. [{prompt["category"]}] {prompt["title"]}{star}')

    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    choice = input("선택: ")

    if not choice.isdigit() or not 1 <= int(choice) <= len(categories):
        print("잘못된 선택입니다.")
        return

    selected_category = categories[int(choice) - 1]

    results = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            results.append(prompt)

    if len(results) == 0:
        print(f"\n[{selected_category}] 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    for i, prompt in enumerate(results, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{i}. {prompt["title"]}{star}')

    print(f"\n총 {len(results)}개의 프롬프트")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ")

    if keyword == "":
        print("검색어를 입력해주세요.")
        return

    results = []

    for prompt in prompts:
        if keyword.lower() in prompt["title"].lower() or keyword.lower() in prompt["content"].lower():
            results.append(prompt)

    if len(results) == 0:
        print("검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for i, prompt in enumerate(results, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{i}. [{prompt["category"]}] {prompt["title"]}{star}')

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    number = input("프롬프트 번호 입력: ")

    if not number.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    number = int(number)

    if number < 1 or number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[number - 1]

    star = "⭐" if prompt["favorite"] else "아니오"

    print("\n────────────────────────────")
    print(f'제목: {prompt["title"]}')
    print(f'카테고리: {prompt["category"]}')
    print(f"즐겨찾기: {star}")
    print("────────────────────────────")
    print("내용:")
    print(prompt["content"])
    print("────────────────────────────")

def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    number = input("프롬프트 번호 입력: ")

    if not number.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    number = int(number)

    if number < 1 or number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[number - 1]

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(f'\'{prompt["title"]}\' 프롬프트를 즐겨찾기에 추가했습니다!')
    else:
        print(f'\'{prompt["title"]}\' 프롬프트를 즐겨찾기에서 해제했습니다!')

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorites = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorites.append(prompt)

    if len(favorites) == 0:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(favorites, 1):
        print(f'{i}. [{prompt["category"]}] {prompt["title"]} ⭐')

    print(f"\n총 {len(favorites)}개의 즐겨찾기")

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
    elif choice == "2":
        show_list()
    elif choice == "3":
        show_by_category()
    elif choice == "4":
        search_prompt()
    elif choice == "5":
        show_detail()
    elif choice == "6":
        toggle_favorite()
    elif choice == "7":
        show_favorites()
    elif choice == "0":
        print("Prompt Box를 종료합니다.")
        break
    else:
        print("아직 준비 중인 기능입니다.")