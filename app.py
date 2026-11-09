from pathlib import Path
import tomllib

import streamlit as st


DEFAULT_SETTINGS = {
    "store_name": "AOI CAFE",
    "tagline": "香りとくつろぎを、毎日の一杯に。",
}

MENU_ITEMS = [
    {"name": "ドリップコーヒー", "price": 400, "icon": "☕"},
    {"name": "カフェラテ", "price": 500, "icon": "🥛"},
    {"name": "チーズケーキ", "price": 450, "icon": "🍰"},
]


def load_store_settings() -> dict[str, str]:
    settings_path = Path(__file__).with_name("store_settings.toml")
    if not settings_path.exists():
        return DEFAULT_SETTINGS.copy()

    with settings_path.open("rb") as f:
        settings = tomllib.load(f)

    return {
        "store_name": settings.get("store_name", DEFAULT_SETTINGS["store_name"]),
        "tagline": settings.get("tagline", DEFAULT_SETTINGS["tagline"]),
    }


settings = load_store_settings()
menu = {item["name"]: item["price"] for item in MENU_ITEMS}
menu_icon = {item["name"]: item["icon"] for item in MENU_ITEMS}

st.set_page_config(page_title=f"{settings['store_name']} | カフェ注文", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f3eb;
    }

    .hero {
        background: linear-gradient(135deg, #5d3a1a, #8b5e34);
        color: #fff8ef;
        border-radius: 16px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
        box-shadow: 0 8px 20px rgba(61, 35, 17, 0.25);
    }

    .hero h1 {
        margin: 0;
        font-size: clamp(1.5rem, 2vw, 2.2rem);
    }

    .hero p {
        margin-top: 0.4rem;
        margin-bottom: 0;
        opacity: 0.95;
        font-size: 0.98rem;
    }

    .menu-card {
        background: #fffaf5;
        border: 1px solid #e4d3bf;
        border-radius: 14px;
        padding: 1rem;
        box-shadow: 0 4px 10px rgba(93, 58, 26, 0.08);
        min-height: 132px;
        margin-bottom: 0.5rem;
    }

    .menu-card .icon {
        font-size: 1.8rem;
        margin-bottom: 0.3rem;
    }

    .menu-card .name {
        font-weight: 700;
        color: #4f3319;
        margin-bottom: 0.2rem;
    }

    .menu-card .price {
        color: #6d4c2f;
        font-weight: 600;
    }

    .cart-box {
        background: #fffaf5;
        border: 1px solid #e4d3bf;
        border-radius: 14px;
        padding: 1rem;
    }

    @media (max-width: 768px) {
        div[data-testid="column"] {
            min-width: 100% !important;
            flex: 1 1 100% !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="hero">
      <h1>{settings['store_name']}</h1>
      <p>{settings['tagline']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if "cart" not in st.session_state:
    st.session_state.cart = {}

st.subheader("メニュー")
cols = st.columns(3, gap="medium")

for index, item in enumerate(MENU_ITEMS):
    with cols[index % 3]:
        st.markdown(
            f"""
            <div class="menu-card">
              <div class="icon">{item['icon']}</div>
              <div class="name">{item['name']}</div>
              <div class="price">{item['price']}円</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        quantity = st.number_input(
            f"{item['name']}の数量",
            min_value=1,
            value=1,
            step=1,
            key=f"qty_{item['name']}",
        )
        if st.button(f"{item['icon']} {item['name']}を追加", key=f"add_{item['name']}", use_container_width=True):
            st.session_state.cart[item["name"]] = (
                st.session_state.cart.get(item["name"], 0) + quantity
            )
            st.success(f"{item['name']}をカートに追加しました。")

st.subheader("カート")

if st.session_state.cart:
    total = 0
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)
    for name, count in st.session_state.cart.items():
        subtotal = menu[name] * count
        total += subtotal
        st.write(f"{menu_icon.get(name, '🧺')} {name} × {count}：{subtotal}円")
    st.write(f"### 合計金額：{total}円")
    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("カート操作")
    removable_item = st.selectbox(
        "削除する商品",
        list(st.session_state.cart.keys()),
        format_func=lambda name: f"{menu_icon.get(name, '🧺')} {name}",
    )

    action_col1, action_col2 = st.columns(2, gap="small")
    with action_col1:
        if st.button("選択商品を削除", use_container_width=True):
            del st.session_state.cart[removable_item]
            st.success(f"{removable_item}をカートから削除しました。")
    with action_col2:
        if st.button("カートを空にする", use_container_width=True):
            st.session_state.cart = {}
            st.success("カートを空にしました。")
else:
    st.info("カートは空です。")
