from tkinter import *
import tkinter.scrolledtext
import pandas as pd
from PIL import ImageTk
import os   # 폴더를 만들고 삭제, 현재 폴더 위치

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(os.getcwd())  # 현재 디렉토리 이름 표시

## 파일 불러오기
dat = pd.read_csv("./의료용어.csv")
subset = dat.head(n=621)[['용어']]

## 기능 추가
## 제출 버튼을 클릭했을 때, 동작 기능.
def click():
    word = entry.get()  # 아래 엔트리 상자의 내용을 text로 넣는다.
    # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 쓴다.
    output.delete(0.0, END)   # 텍스트 박스 내용을 지운다.

    try:
        def_word = dat.loc[dat['용어']==word, '정의'].values[0]  # values = 0인 이유 : pandas
        # word 안의 단어를 찾고 그 단어의 def 값을 반환함
    except:
        def_word = '단어의 뜻을 찾을 수 없음'

    output.insert(END, def_word)

window = Tk()
window.title('의료시험용어사전')

# 01 입력 상자 설명 레이블
label = Label(window, text='원하는 단어 입력 후, 엔터 키 누르기')
label.grid(row=0, column=0, sticky=W, pady=10, padx=5)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg='light blue')
entry.grid(row=1, column=0, sticky=W, pady=10, padx=10)

# 03 제출 버튼 만들기
button = Button(window, text='제출', width=5, command=click)   # command에 함수 전달, 클릭했을 때 함수 실행
button.grid(row=2, column=0, sticky=W, pady=10, padx=10)

# 04 설명 레이블 - 의미
label_1 = Label(window, text='\n의미')
label_1.grid(row=3, column=0, sticky=W, pady=10, padx=5)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0) ~ (4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background='light blue')
output.grid(row=4, column=0, columnspan=2, sticky=W, pady=10, padx=10)

# 06 용어를 출력하기 위한 스크롤 바 생성
label_2 = Label(window, text='\n용어 목록')
label_2.grid(row=5, column=0, sticky=W, pady=10, padx=5)

scrollbar = tkinter.scrolledtext.ScrolledText(window, background='light blue')
scrollbar.grid(row=6, column=0, sticky=W, pady=10, padx=10)
scrollbar.insert(INSERT, subset)
scrollbar.configure(state='disabled')

# 07 이미지 삽입
Image_1 = ImageTk.PhotoImage(file='dog_e.png')
label_3 = Label(window, background='white', relief='sunken', image=Image_1)
label_3.place(x=365, y=15, width=230, height=200)

print(dat.shape)
print(dat.columns)
print(dat.head())

window.mainloop()

## 목록 출력기능 만들어보기
## 외관 깔끔하게 만들기