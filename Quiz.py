def kiosk():
    menu = ["1. 냉면", "2. 볶음밥", "3. 피자", "4. 짜장면"]

    print(f"메뉴를 선택하세요: {menu}")

    try:
        choice = int(input("번호를 입력하세요: "))

        if choice < 1 or choice > 4:
            raise IndexError

        print(f"선택한 메뉴: {menu[choice - 1]}")

    except ValueError:
        print("숫자를 입력하세요.")
        kiosk()

    except IndexError:
        print("1에서 4 사이의 숫자를 입력하세요.")
        kiosk()

kiosk()