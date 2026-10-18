AVETAAR_BUILTIN_BOT_TOKEN = "T000000000"
AVETAAR_NAME = "Avetaar"
AVETAAR_DEV = "@Avetaar"
AVETAAR_CHANNEL = "https://t.me/RivalStudio"
AVETAAR_VERSION = "1.0.0"

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "RIVAL_requirements.txt"])
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone

try:
    import requests
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "RIVAL_requirements.txt"])
    import requests

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    def C(name):
        return getattr(Fore, name, "")
    def RST():
        return Style.RESET_ALL
except Exception:
    def C(name):
        return ""
    def RST():
        return ""

AVETAAR_NUMBER_TYPES = {
    0: "خط ثابت",
    1: "موبايل",
    2: "موبايل أو خط ثابت",
    3: "مكالمات مجانية",
    4: "أرقام مميزة",
    5: "تكلفة مشتركة",
    6: "VOIP",
    7: "رقم شخصي",
    8: "PAGER",
    9: "UAN",
    10: "بريد صوتي",
    99: "مجهول",
}

def avetaar_parse_number(raw: str):
    raw = (raw or "").strip()
    if not raw:
        return None
    if not raw.startswith("+"):
        raw = "+" + raw
    try:
        return phonenumbers.parse(raw, None)
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

def avetaar_number_type_name(number) -> str:
    t = phonenumbers.number_type(number)
    return AVETAAR_NUMBER_TYPES.get(t, "مجهول")

def avetaar_number_details(number) -> dict:
    region = phonenumbers.region_code_for_number(number) or "؟"
    country_name = geocoder.country_name_for_number(number, "en") or "مجهولة"
    location = geocoder.description_for_number(number, "en")
    carrier_name = carrier.name_for_number(number, "en") or "غير معروف"
    tzs = timezone.time_zones_for_number(number)
    tz_name = ", ".join(tzs) if tzs else "غير متاح"
    national_sig = phonenumbers.national_significant_number(number)
    e164 = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
    rfc3966 = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.RFC3966)
    natl = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
    valid = phonenumbers.is_valid_number(number)
    valid_region = phonenumbers.is_valid_number_for_region(number, region)
    possible = phonenumbers.is_possible_number(number)
    possible_mobile = phonenumbers.is_possible_number_for_type(number, phonenumbers.PhoneNumberType.MOBILE)
    possible_short = phonenumbers.is_possible_short_number(number)
    possible_emergency = "لا يوجد رقم طوارئ معروف لهذا الرقم"
    ext = number.extension if number.extension else "لا يوجد"
    return {
        "رقم الهاتف": str(e164),
        "رمز الدولة": region,
        "اسم الدولة": country_name,
        "الموقع": location,
        "المشغل (SIM)": carrier_name,
        "نوع الرقم": avetaar_number_type_name(number),
        "صالح": valid,
        "صالح في المنطقة": valid_region,
        "ممكن": possible,
        "ممكن موبايل": possible_mobile,
        "ممكن رقم قصير": possible_short,
        "ممكن طوارئ": possible_emergency,
        "المنطقة الزمنية": tz_name,
        "الرقم المحلي": natl,
        "الرقم الوطني الدال": national_sig,
        "تنسيق E164": e164,
        "تنسيق RFC3966": rfc3966,
        "الإضافة (Extension)": ext,
    }

def avetaar_format_terminal(details: dict) -> str:
    L = []
    L.append(f"{C('CYAN')}═" * 54 + RST())
    L.append(f"{C('MAGENTA')}  📞 Avetaar Phone Details  📞{RST()}")
    L.append(f"{C('CYAN')}═" * 54 + RST())
    L.append(f"  {C('GREEN')}رقم الهاتف{RST()}     : {details['رقم الهاتف']}")
    L.append(f"  {C('YELLOW')}رمز الدولة{RST()}    : {details['رمز الدولة']}")
    L.append(f"  {C('YELLOW')}اسم الدولة{RST()}    : {details['اسم الدولة']}")
    L.append(f"  {C('YELLOW')}الموقع{RST()}        : {details['الموقع']}")
    L.append(f"  {C('BLUE')}المشغل (SIM){RST()}  : {details['المشغل (SIM)']}")
    L.append(f"  {C('BLUE')}نوع الرقم{RST()}     : {details['نوع الرقم']}")
    L.append(f"  {C('BLUE')}صالح{RST()}          : {details['صالح']}")
    L.append(f"  {C('BLUE')}صالح في المنطقة{RST()} : {details['صالح في المنطقة']}")
    L.append(f"  {C('BLUE')}ممكن{RST()}         : {details['ممكن']}")
    L.append(f"  {C('BLUE')}ممكن موبايل{RST()}   : {details['ممكن موبايل']}")
    L.append(f"  {C('CYAN')}─" * 54 + RST())
    L.append(f"  {C('BLUE')}المنطقة الزمنية{RST()}  : {details['المنطقة الزمنية']}")
    L.append(f"  {C('BLUE')}الرقم المحلي{RST()}     : {details['الرقم المحلي']}")
    L.append(f"  {C('BLUE')}E164{RST()}            : {details['تنسيق E164']}")
    L.append(f"  {C('BLUE')}RFC3966{RST()}        : {details['تنسيق RFC3966']}")
    L.append(f"{C('CYAN')}═" * 54 + RST())
    L.append(f"  {C('LIGHTBLACK_EX')}{AVETAAR_NAME} {AVETAAR_DEV} — {AVETAAR_CHANNEL}{RST()}")
    return "\n".join(L)

def avetaar_terminal_loop():
    while True:
        raw = input("\n[Avetaar] أدخل رقم الهاتف (مثال: 9647701234567 أو +964...): ").strip()
        if raw.lower() in ("q", "0", "خروج"):
            break
        number = avetaar_parse_number(raw)
        if number is None:
            print(f"{C('RED')}[Avetaar] رقم غير صالح — تأكد من صيغة الرقم (بداية + أو رمز الدولة).{RST()}")
            continue
        details = avetaar_number_details(number)
        print(avetaar_format_terminal(details))
    print(f"{C('CYAN')}\nإلى اللقاء! 📞{RST()}")
    import sys
    sys.exit(0)

def avetaar_load_bot_token() -> str:
    import os
    return os.environ.get("AVETAAR_BOT_TOKEN", AVETAAR_BUILTIN_BOT_TOKEN)

def avetaar_tg_call(token: str, method: str, params: dict):
    r = requests.post(f"https://api.telegram.org/bot{token}/{method}", json=params, timeout=30)
    d = r.json()
    if not d.get("ok"):
        raise RuntimeError(d.get("description", str(r.status_code)))
    return d.get("result")

def avetaar_esc(s) -> str:
    import html
    return html.escape(str(s), quote=False)

def avetaar_bool(v) -> str:
    if isinstance(v, bool):
        return f"{C('GREEN')}✅ نعم{RST()}" if v else f"{C('RED')}❌ لا{RST()}"
    return str(v)

def avetaar_bot_message(details: dict) -> str:
    L = []
    L.append(f"📞 <b>{avetaar_esc(details['رقم الهاتف'])}</b>")
    L.append("")
    L.append(f"🌍 الدولة: <b>{avetaar_esc(details['اسم الدولة'])}</b> ({avetaar_esc(details['رمز الدولة'])})")
    L.append(f"📍 الموقع: {avetaar_esc(details['الموقع'])}")
    L.append(f"📶 المشغل (SIM): <b>{avetaar_esc(details['المشغل (SIM)'])}</b>")
    L.append(f"🧩 النوع: {avetaar_esc(details['نوع الرقم'])}")
    valid_str = "✅ صالح" if details['صالح'] else "⛔ غير صالح"
    mobile_str = "✅ ممكن موبايل" if details['ممكن موبايل'] else "⛔ غير ممكن موبايل"
    L.append(f"{valid_str} · {mobile_str}")
    L.append("")
    L.append("🌐 المنطقة الزمنية: " + avetaar_esc(details["المنطقة الزمنية"]))
    L.append(f"🏠 الرقم المحلي: {avetaar_esc(details['الرقم المحلي'])}")
    L.append(f"🔢 E164: <code>{avetaar_esc(details['تنسيق E164'])}</code>")
    L.append(f"🔗 RFC3966: <code>{avetaar_esc(details['تنسيق RFC3966'])}</code>")
    L.append("")
    L.append(f"⚙️ {AVETAAR_NAME} {AVETAAR_DEV} — {AVETAAR_CHANNEL}")
    return "\n".join(L)

def avetaar_btn(text: str, callback_data: str, color_key: str) -> dict:
    BTN_STYLE = {
        "search": ("primary", ""),
        "players": ("success", ""),
        "positive": ("success", ""),
        "negative": ("danger", ""),
        "info": ("primary", ""),
    }
    style, _ = BTN_STYLE.get(color_key, ("", ""))
    b = {"text": text, "callback_data": callback_data}
    if style:
        b["style"] = style
    return b

def avetaar_buttons_menu() -> dict:
    return {
        "inline_keyboard": [
            [
                avetaar_btn("📞 أدخل رقم", "phone_input", "search"),
                avetaar_btn("📋 نسخ E164", "copy_e164", "positive"),
            ],
            [
                avetaar_btn("🔍 رقم تجريبي", "test_number", "info"),
                avetaar_btn("❌ خروج", "exit", "negative"),
            ],
        ]
    }

_pending_action = {}

def avetaar_handle_callback(token: str, update: dict):
    cb = update["callback_query"]
    chat_id = cb["message"]["chat"]["id"]
    data = cb["data"]
    avetaar_tg_call(token, "answerCallbackQuery", {"callback_query_id": cb["id"]})
    if data == "menu":
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "اختر:",
            "reply_markup": avetaar_buttons_menu(),
        })
    elif data == "exit":
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": f" 👋 إلى اللقاء! اضغط /start للعودة.\n\n{AVETAAR_NAME} {AVETAAR_DEV}",
        })
    elif data == "phone_input":
        _pending_action[chat_id] = "phone"
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "📞 اكتب رقم الهاتف:\nمثال: <code>+9647701234567</code> أو <code>9647701234567</code>",
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })
    elif data == "test_number":
        avetaar_send_number_result(token, chat_id, "9647701234567")
    elif data == "copy_e164":
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "📋 أولّد رقم تجريبيًا ونسخ E164:\n<code>+964 770 123 4567</code>\n\nشوف تفاصيل الرقم من زر '🔍 رقم تجريبي'.",
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })

def avetaar_handle_update(token: str, u: dict):
    msg = u.get("message")
    if msg:
        text = (msg.get("text") or "").strip()
        chat_id = msg["chat"]["id"]
        tl = text.lower()
        if tl in ("/start", "start", "ابدأ", "/help", "help", "/"):
            avetaar_tg_call(token, "sendMessage", {
                "chat_id": chat_id,
                "text": f" 👋 أهلاً! أنا {AVETAAR_NAME} — أحلل أرقام الهاتف وأعرض كل التفاصيل.\nاضغط زرًا من القائمة:",
                "reply_markup": avetaar_buttons_menu(),
            })
        elif not text.startswith("/"):
            if chat_id in _pending_action:
                action = _pending_action.pop(chat_id)
                if action == "phone":
                    avetaar_send_number_result(token, chat_id, text)
            else:
                avetaar_send_number_result(token, chat_id, text)
    cb = u.get("callback_query")
    if cb:
        avetaar_handle_callback(token, u)

def avetaar_send_number_result(token: str, chat_id: int, raw_number: str):
    number = avetaar_parse_number(raw_number)
    if number:
        details = avetaar_number_details(number)
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": avetaar_bot_message(details),
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })
    else:
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": f" ⛔ رقم غير صالح: <b>{avetaar_esc(raw_number)}</b>\nجرّب صيغة مثل <code>+9647701234567</code> أو <code>9647701234567</code>.",
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })

def avetaar_single_instance_lock() -> bool:
    import os
    lock_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".bot_lock")
    if os.path.exists(lock_path):
        with open(lock_path) as f:
            old_pid = f.read().strip()
        alive = False
        try:
            os.kill(int(old_pid), 0)
            alive = True
        except (ProcessLookupError, ValueError, OSError):
            alive = False
        if alive:
            return False
        os.remove(lock_path)
    with open(lock_path, "w") as f:
        f.write(str(os.getpid()))
    return True

def avetaar_bot_run_long_poll():
    import time, os, sys
    token = avetaar_load_bot_token()
    if not token or token == "T000000000":
        print(f"{C('YELLOW')}⚠️ ما فيه توكن — أنشئ بوت مع @BotFather واستلم التوكن.{RST()}")
        print(f"   الخيارات: [1] توكن جديد | [2] تخطي (توكن مدمج غير صالح)")
        choice = input(f"{C('YELLOW')}  الاختيار (1/2): ").strip()
        if choice == "1":
            token = input(f"{C('YELLOW')}  التوكن: ").strip()
            if not token:
                print(f"{C('RED')}التوكن فاضي — ما تقدر تشغل البوت.{RST()}")
                sys.exit(1)
            os.environ["AVETAAR_BOT_TOKEN"] = token
        else:
            token = AVETAAR_BUILTIN_BOT_TOKEN
    if not avetaar_single_instance_lock():
        sys.exit(f"{C('YELLOW')}⚠️ نسخة بوت أخرى شغالة — أغلها أولًا.{RST()}")
    print(f"{C('GREEN')}🚀 {AVETAAR_NAME} بوت شغّال... (Ctrl+C للإيقاف){RST()}")
    last_update_id = 0
    error_count = 0
    while True:
        try:
            d = avetaar_tg_call(token, "getUpdates", {
                "limit": 100,
                "offset": last_update_id + 1,
                "timeout": 10,
            })
            error_count = 0
            for u in d:
                last_update_id = u["update_id"]
                try:
                    avetaar_handle_update(token, u)
                except Exception as e:
                    print(f"{C('RED')}⛔ خطأ: {e} — تم تخطي.{RST()}")
        except requests.RequestException as e:
            error_count += 1
            wait = min(5 * error_count, 30)
            print(f"{C('YELLOW')}⚠️ اتصال مفقود — إعادة بعد {wait} ثوانٍ...{RST()}")
            time.sleep(wait)
        except RuntimeError as e:
            error_count += 1
            wait = min(5 * error_count, 30)
            print(f"{C('YELLOW')}⚠️ خطأ تلكرام: {e} — إعادة بعد {wait} ثوانٍ...{RST()}")
            time.sleep(wait)

def avetaar_main():
    import argparse
    parser = argparse.ArgumentParser(description=f"{AVETAAR_NAME} Phone Details")
    parser.add_argument("--bot", action="store_true", help="شغل وضع البوت")
    args, _ = parser.parse_known_args()
    if args.bot:
        avetaar_bot_run_long_poll()
    else:
        avetaar_terminal_loop()

if __name__ == "__main__":
    try:
        avetaar_main()
    finally:
        import os
        lock_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".bot_lock")
        if os.path.exists(lock_path):
            os.remove(lock_path)
