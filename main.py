import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib import rcParams
from data_loader import load_and_validate_csv
from report_generator import generate_summary, plot_pie_chart
from utils import setup_logger

rcParams['font.family'] = 'Arial Unicode MS'
rcParams['axes.unicode_minus'] = False

logger = setup_logger()
file_path = ""

def load_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        label_file.config(text=file_path)

def generate_report():
    global file_path
    if not file_path:
        messagebox.showerror("เกิดข้อผิดพลาด", "กรุณาเลือกไฟล์ CSV ก่อน")
        return

    try:
        df = load_and_validate_csv(file_path)
        summary, total = generate_summary(df)

        messagebox.showinfo("สำเร็จ", f"สร้างรายงานเสร็จแล้ว!\nรวมยอดทั้งหมด: {total} บาท")
        plot_pie_chart(summary)

    except Exception as e:
        logger.error(f"เกิดข้อผิดพลาด: {e}")
        messagebox.showerror("เกิดข้อผิดพลาด", str(e))

root = tk.Tk()
root.title("รายจ่ายรายเดือน")

label_file = tk.Label(root, text="ยังไม่ได้เลือกไฟล์ CSV")
label_file.pack(pady=10)

btn_load = tk.Button(root, text="เลือกไฟล์ CSV ของฉัน", command=load_file)
btn_load.pack(pady=5)

btn_generate = tk.Button(root, text="สร้างรายงาน", command=generate_report)
btn_generate.pack(pady=5)

root.mainloop()
