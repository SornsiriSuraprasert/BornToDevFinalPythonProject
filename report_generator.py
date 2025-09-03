import matplotlib.pyplot as plt

def generate_summary(df, output_file="summary.csv"):
    summary = df.groupby('หมวดหมู่')['จำนวนเงิน'].sum().reset_index()
    total = df['จำนวนเงิน'].sum()
    summary.to_csv(output_file, index=False)

    return summary, total

def plot_pie_chart(summary):
    plt.figure(figsize=(6, 6))
    plt.pie(summary['จำนวนเงิน'], labels=summary['หมวดหมู่'], autopct='%1.1f%%')
    plt.title('สัดส่วนค่าใช้จ่าย')
    plt.show()
