#Trong Tkinter, Frame là một widget được sử dụng để nhóm và quản lý các widget khác trong một container.
# Dưới đây là một số thuộc tính quan trọng của widget Frame:
import tkinter as tk

# Tạo cửa sổ
window = tk.Tk()
window.title("Frame")  # Đặt tiêu đề cửa sổ

#1. master: Xác định widget cha của Frame, tức là widget chứa Frame.
#frame = tk.Frame(window)

#2. relief: Xác định kiểu hiển thị của khung xung quanh Frame.
# Một số giá trị phổ biến bao gồm "flat", "raised", "sunken", "ridge", và "solid".
#frame = tk.Frame(window, relief="solid")

#3. borderwidth hoặc bd: Xác định độ rộng của khung nếu relief được thiết lập.
#frame = tk.Frame(window, relief="solid", borderwidth=2)

#4. background hoặc bg: Màu nền của Frame.
#frame = tk.Frame(window, bg="lightblue")

#5. width và height: Kích thước của Frame (đơn vị là pixel).
#frame = tk.Frame(window, width=200, height=150)

#6. padx và pady: Xác định khoảng cách ngang và dọc giữa nội dung của Frame và khung xung quanh nó.
#frame = tk.Frame(window, padx=10, pady=10)

#7.highlightbackground và highlightcolor: Xác định màu sắc của phần nền khi Frame nhận được sự chú ý.
#frame = tk.Frame(window, highlightbackground="black", highlightcolor="red")

#8. highlightthickness: Độ dày của đường viền chú ý khi Frame nhận được sự chú ý.
#frame = tk.Frame(window, highlightthickness=2)


# Chạy vòng lặp cửa sổ
window.mainloop()