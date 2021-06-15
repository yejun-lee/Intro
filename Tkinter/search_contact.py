import re

class Contact:
    def __init__(self, name, num, email, address):
        self.name = name
        self.num = num
        self.email = email
        self.address = address

    def print_info(self):
        print('이름 :', self.name)
        print('전화번호 :', self.num)
        print('이메일 :', self.email)
        print('주소 :', self.address)


def print_menu():    # 초기 메뉴 부분
    print('1. 연락처 입력, 2. 연락처 출력, 3. 연락처 삭제, 4. 연락처 검색, 5. 종료')
    sel_num = int(input('선택(1, 2, 3, 4, 5) : '))

    return sel_num


def print_all(contact_all):    # 연락처의 정보를 깔끔하게 출력하는 부분
    try:
        if len(contact_all) >= 4:
            for i in range(len(contact_all) // 4):
                print(i+1, '번째 주소 ) ',
                      '이름 :', contact_all[i*4],
                      '연락처 :', contact_all[i*4 + 1],
                      '이메일 :', contact_all[i*4 + 2],
                      '주소 :', contact_all[i*4 + 3])
    except:
        print('종료!')


def set_contact():    # 값을 입력받고 정규 표현식으로 양식 확인하는 부분
    reg1 = re.compile('^[a-zA-Z]{,30}$')
    reg2 = re.compile('^[0-1]{3}-[0-9]{4}-[0-9]{4}$')
    reg3 = re.compile('^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9]+\.[a-z]{2,3}$')

    name = input('Name : ')
    num = input('Phone number : ')
    email = input('E-mail : ')
    address = input('Address : ')

    re1 = reg1.match(name)
    re2 = reg2.match(num)
    re3 = reg3.match(email)

    while not (re1 and re2 and re3):    # 양식과 맞지 않을 때
        if not re1:
            name = input('이름을 30자 이내 영어로 입력해주세요 : ')
            re1 = reg1.match(name)
        if not re2:
            num = input('전화번호를 양식에 맞게 다시 입력해주세요 : ')
            re2 = reg2.match(num)
        if not re3:
            address = input('이메일을 양식에 맞게 다시 입력해주세요 : ')
            re3 = reg3.match(email)

    return name, num, email, address


def run_2():    # 메인 실행 부분
    menu = 0
    contact_all = []

    while menu != 5:    # 종료 모드
        menu = print_menu()

        if menu == 1:   # 입력 모드
            name, num, email, address = set_contact()
            # man = Contact(name, num, email, address)
            contact_all += [name, num, email, address]
            print_all(contact_all)

        elif menu == 2:   # 출력 모드
            try:
                print_all(contact_all)
            except:
                print('데이터 없음')

        elif menu == 3:   # 삭제 모드
            try:
                del_name = input('삭제할 연락처를 선택해주세요 : ')

                if del_name in contact_all:
                    for i in range(0, len(contact_all), 4):
                        if contact_all[i] == del_name:
                            del contact_all[i:i+4]
                else:
                    print('연락처에 해당 이름이 없습니다!')

            except:
                print('데이터 없음')

        elif menu == 4:   # 찾기 모드
            contact_name = input('이름을 입력하세요 : ')
            if contact_name in contact_all:
                for i in range(0, len(contact_all), 4):
                    if contact_all[i] == contact_name:
                        print(contact_name, '님의 연락처 : ', contact_all[i+1])
            else:
                print('연락처에 없는 이름입니다.')

    return contact_all

C1 = run_2()    # 실행 부분

if __name__ == '__main__':
    print()
    print('실행 종료!')

## < 연락처 업그레이드 구현 한 부분 >
###   00  예외처리 - 전화번호에 ***-****-**** 전화번호 형식이 맞지 않아요.
###   00  예외처리 - 메일에 ****@***** 이 형식이 아닐때, 형식이 맞지 않아요.
###   00  예외처리 - 이름이 30자 이상일 때, 이름은 30자 이내로 입력해 주세요.
###   00  예외처리 - 출력이나 삭제하려고 하는데, 데이터가 없어요. '데이터가 없습니다'
###   00  예외처리 - 삭제할 이름을 넣었을 때, 이름이 없어요. '연락처에 해당 이름이 없습니다.'

###   01  검색 기능 추가 - 이름을 입력하면 해당 연락처가 보이도록

## < 연락처 업그레이드 구현하지 못한 부분 >
###      한글자, 두글자로도 해당되는 연락처가 보이도록
###   01  번호 검색 기능 추가 - 번호를 입력하면 해당 연락처가 보이도록
###      추가 번호 검색 기능

###   01  파일에서 읽고 쓰고       ###
###   02  DB 연동해서 읽고 쓰고,   ###
###