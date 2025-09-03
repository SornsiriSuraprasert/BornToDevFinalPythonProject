import pandas as pd

def load_and_validate_csv(file_path):
    df = pd.read_csv(file_path)
    required_cols = ['วันที่', 'หมวดหมู่', 'รายการ', 'จำนวนเงิน']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"CSV ต้องมีคอลัมน์: {', '.join(required_cols)}")
    df['จำนวนเงิน'] = pd.to_numeric(df['จำนวนเงิน'], errors='coerce')
    df = df.dropna(subset=['จำนวนเงิน'])
    df['จำนวนเงิน'] = df['จำนวนเงิน'].astype(float)

    return df
