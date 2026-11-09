import streamlit as st


menu = {
    "ドリップコーヒー": 400,
    "カフェラテ": 500,
    "チーズケーキ": 450,
}

st.set_page_config(page_title="カフェ注文シミュレーター")
st.title("カフェ注文シミュレーター")
st.write("メニューから商品を選び、カートに追加してください。")

st.subheader("メニュー")
for name, price in menu.items():
    st.write(f"{name}：{price}円")

if "cart" not in st.session_state:
    st.session_state.cart = {}

st.subheader("注文")
selected_item = st.selectbox("商品", list(menu.keys()))
quantity = st.number_input("数量", min_value=1, value=1, step=1)

if st.button("カートに追加"):
    st.session_state.cart[selected_item] = (
        st.session_state.cart.get(selected_item, 0) + quantity
    )
    st.success(f"{selected_item}をカートに追加しました。")

st.subheader("カート")
if st.session_state.cart:
    total = 0
    for name, count in st.session_state.cart.items():
        subtotal = menu[name] * count
        total += subtotal
        st.write(f"{name} × {count}：{subtotal}円")
    st.write(f"### 合計金額：{total}円")
else:
    st.write("カートは空です。")
