import streamlit as st
import pandas as pd

def load_data():
    st.sidebar.header("📁 Upload CSV / Excel File")
    uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=['csv', 'xlsx', 'xls'])

    if uploaded_file:
        try:
            df = None

            try:
                df = pd.read_csv(uploaded_file, encoding="utf-8")
            except:
                pass

            if df is None:
                uploaded_file.seek(0)
                try:
                    df = pd.read_csv(uploaded_file, encoding="latin1")
                except:
                    pass

            if df is None:
                uploaded_file.seek(0)
                try:
                    df = pd.read_csv(uploaded_file, sep="\t", encoding="latin1")
                except:
                    pass

            if df is None:
                uploaded_file.seek(0)
                try:
                    df = pd.read_excel(uploaded_file)
                except:
                    pass

            if df is None:
                st.sidebar.error("❌ Unable to read file. Please upload a valid CSV/Excel file.")
                return pd.DataFrame()

            df.columns = df.columns.str.strip()
            st.sidebar.success(f"✅ Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
            return df

        except Exception as e:
            st.sidebar.error(f"❌ Error loading file: {e}")
            return pd.DataFrame()

    st.sidebar.info("📤 Upload a CSV or Excel file to begin analysis")
    return pd.DataFrame()


def main():
    st.title("📊 Intelligent HR Analytics Dashboard")

    df = load_data()

    # -------- NO MORE BLANK SCREEN --------
    if df.empty:
        st.info("📤 Please upload a CSV or Excel file to begin.")
        return

    st.subheader("📄 Preview of Uploaded Data")
    st.dataframe(df)


if __name__ == "__main__":
    main()
