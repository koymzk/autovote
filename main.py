import json
from playwright.sync_api import sync_playwright

# サイトURLとボタンのセレクタを適宜書き換えてください
TARGET_URL = "https://vote.miscolle.com/vote/keio2025/F/3"
BUTTON_SELECTOR = "button.flex.flex-auto.items-center.justify-center.rounded-lg.py-2.px-3.text-sm"


# localStorageの値をここに入力してください
LOCALSTORAGE_ITEMS = [
    {
        "key": "LIFF_STORE:1656040756-GwmBkdPY:accessToken",
        "value": "eyJhbGciOiJIUzI1NiJ9.LzTAY2tcHVWdIqD6D88QP8YlQpv_io-uC5HGNTIYGUMFGVclJvJFJhXp9NbDfilluQ3SMFFQYJojXocFdn_G0pwWvhwXdVBHdun3jxvvFeWQP8G6mzw8k-fOY3H4-VpJR60cM_wmMMlvXaBzh-oRmK2wXeLYOF64VxxB9K5TyHI.oyfupiMPFrcwE5oppLprDhkJMkTGiPhxETagFURbtYs"
    },
    {
        "key": "LIFF_STORE:1656040756-GwmBkdPY:clientId",
        "value": "1656040756"
    },
    {
        "key": "LIFF_STORE:1656040756-GwmBkdPY:context",
        "value": "{\"type\":\"external\",\"userId\":\"U5e1eeaa782bb564995708584b4074cb9\",\"liffId\":\"1656040756-GwmBkdPY\",\"endpointUrl\":\"https://vote.miscolle.com\",\"accessTokenHash\":\"Ila9wmuUL38Lz49LG1TtCQ\",\"availability\":{\"shareTargetPicker\":{\"permission\":false,\"minVer\":\"10.3.0\"},\"multipleLiffTransition\":{\"permission\":true,\"minVer\":\"10.18.0\"},\"subwindowOpen\":{\"permission\":true,\"minVer\":\"11.7.0\"},\"scanCode\":{\"permission\":false,\"minVer\":\"9.4.0\",\"unsupportedFromVer\":\"9.19.0\"},\"scanCodeV2\":{\"permission\":false,\"minVer\":\"11.7.0\",\"minOsVer\":\"14.3.0\"},\"getAdvertisingId\":{\"permission\":false,\"minVer\":\"7.14.0\"},\"addToHomeScreen\":{\"permission\":false,\"minVer\":\"9.16.0\"},\"bluetoothLeFunction\":{\"permission\":false,\"minVer\":\"9.14.0\",\"unsupportedFromVer\":\"9.19.0\"},\"skipChannelVerificationScreen\":{\"permission\":false,\"minVer\":\"11.14.0\"},\"addToHomeV2\":{\"permission\":false,\"minVer\":\"13.20.0\"},\"addToHomeHideDomain\":{\"permission\":false,\"minVer\":\"13.20.0\"},\"addToHomeLineScheme\":{\"permission\":false,\"minVer\":\"13.20.0\"},\"iap\":{\"permission\":false,\"minVer\":\"15.6.0\"}},\"scope\":[\"profile\"],\"menuColorSetting\":{\"adaptableColorSchemes\":[\"light\"],\"lightModeColor\":{\"iconColor\":\"#111111\",\"statusBarColor\":\"black\",\"titleTextColor\":\"#111111\",\"titleSubtextColor\":\"#B7B7B7\",\"titleButtonColor\":\"#111111\",\"titleBackgroundColor\":\"#FFFFFF\",\"progressBarColor\":\"#06C755\",\"progressBackgroundColor\":\"#FFFFFF\"},\"darkModeColor\":{\"iconColor\":\"#FFFFFF\",\"statusBarColor\":\"white\",\"titleTextColor\":\"#FFFFFF\",\"titleSubtextColor\":\"#949494\",\"titleButtonColor\":\"#FFFFFF\",\"titleBackgroundColor\":\"#111111\",\"progressBarColor\":\"#06C755\",\"progressBackgroundColor\":\"#111111\"}},\"utsTracking\":{\"mode\":\"none\",\"sendRatio\":1},\"miniDomainAllowed\":false,\"permanentLinkPattern\":\"concat\"}"
    }
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    # まず同一オリジンのトップページへ遷移
    page.goto("https://vote.miscolle.com")
    # localStorageの全キーをセット
    for item in LOCALSTORAGE_ITEMS:
        page.evaluate(f"""() => {{
            localStorage.setItem('{item['key']}', '{item['value']}');
        }}""")
    page.goto(TARGET_URL)
    print("Current URL after navigation:", page.url)
    page.click(BUTTON_SELECTOR)
    print("Button clicked!")
    browser.close()
