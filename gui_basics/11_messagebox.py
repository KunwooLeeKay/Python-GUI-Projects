# 메시지 박스 : 팝업으로 뜨는 메시지

import tkinter.messagebox as msgbox # 메시지박스는 import 필요!
from tkinter import *

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") 
    # 앞의 문장은 창에 써지는 내용, 뒤의 내용은 알림 내용이다. showinfo는 알림창의 아이콘을 설정하는 것으로, 윈도우로치면 I 라고 뜬다.

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다!") # showwarning은 아이콘이 노란색 느낌표

def error():
    msgbox.showerror("에러", "결제 오류가 발생하였습니다!!") # 맥에서는 showinfo랑 똑같은데, 윈도우에서는 빨간색 엑스표

def okcancel(): # 확인 / 취소가 뜨는 팝업창
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response =  msgbox.askyesnocancel(title = None, message = "예매 내역이 저장되지 않았습니다. \n저장 후 종료하시겠습니까?")
    # response라는 변수를 만들어서 거기에 사용자의 응답을 저장. 예 = 1, 아니오 = 0, 취소 = 그 외의 값, None
    print("응답 :", response)
    if response == 1:
        print("저장 후 종료합니다.")
    elif response == 0:
        print("저장하지 않고 종료합니다.")
    else :
        print("전 화면으로 돌아갑니다.")


Button(root, command = info, text = "알림"). pack()
Button(root, command = warn, text = "경고"). pack()
Button(root, command = error, text = "에러"). pack()
Button(root, command = okcancel, text = "확인 취소"). pack()
Button(root, command = retrycancel, text = "재시도"). pack()
Button(root, command = yesno, text = "예/아니오"). pack()
Button(root, command = yesnocancel, text = "예/아니오/취소"). pack()


root. mainloop()