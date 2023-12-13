#Trong thư viện Tkinter của Python, "Label" là một widget được sử dụng để hiển thị văn bản
#hoặc hình ảnh trên giao diện người dùng. Dưới đây là một số thuộc tính quan trọng của widget Label:
import tkinter as tk

# Tạo cửa sổ
window = tk.Tk()
window.title("Lable")  # Đặt tiêu đề cửa sổ

#1. text: Đặc điểm này xác định nội dung văn bản của nhãn.
#label = tk.Label(window, text="Hello, Tkinter!")

#2. font: Xác định font của văn bản trong nhãn.
#label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 12))

#3.bg (background): Màu nền của nhãn.
#label = tk.Label(window, text="Hello, Tkinter!", bg="lightblue")

#4.fg (foreground): Màu văn bản của nhãn.
#label = tk.Label(window, text="Hello, Tkinter!", fg="darkred")

#5. width và height: Độ rộng và chiều cao của nhãn (đơn vị là ký tự).
#label = tk.Label(window, text="Hello, Tkinter!", width=20, height=3)

#6. anchor: Xác định vị trí của văn bản trong nhãn.
#Giá trị có thể là "n", "s", "e", "w", "ne", "nw", "se", "sw", hoặc "center".
#label = tk.Label(wiwndow, text="Hello, Tkinter!", anchor="w")

#7. justify: Căn chỉnh văn bản bên trong nhãn. Giá trị có thể là "left", "center", hoặc "right".
# label = tk.Label(window, text="Hello, Tkinter!", justify="center")

#8. relief: Xác định kiểu hiển thị của khung xung quanh nhãn.
# Một số giá trị phổ biến bao gồm "flat", "raised", "sunken", "ridge", và "solid".
#label = tk.Label(window, text="Hello, Tkinter!", relief="solid")


# Chạy vòng lặp cửa sổ
window.mainloop()