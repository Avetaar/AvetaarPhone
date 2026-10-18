AVETAAR_BUILTIN_BOT_TOKEN = "T000000000"
AVETAAR_NAME = "Avetaar"
AVETAAR_DEV = "@Avetaar"
AVETAAR_CHANNEL = "https://t.me/RivalStudio"
AVETAAR_VERSION = "1.0.0"

AVETAAR_PACKAGES = ["phonenumbers", "requests", "colorama"]

def avetaar_ensure_deps():
    import subprocess, sys
    for pkg in AVETAAR_PACKAGES:
        try:
            __import__(pkg)
        except ImportError:
            print(f"\033[36m[Avetaar] تثبيت {pkg}...\033[0m")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", pkg])
            print(f"\033[32m[Avetaar] تم تثبيت {pkg}\033[0m")
    avetaar_ensure_deps = None

avetaar_ensure_deps()

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

AVETAAR_FLAGS = {
    "AF": "🇦🇫", "AL": "🇦🇱", "DZ": "🇩🇿",
    "AS": "🇦🇸", "AD": "🇦🇩", "AO": "🇦🇴",
    "AI": "🇦🇮", "AG": "🇦🇬", "AR": "🇦🇷",
    "AM": "🇦🇲", "AT": "🇦🇹", "AU": "🇦🇺",
    "AZ": "🇦🇿", "BS": "🇧🇸", "BH": "🇧🇭",
    "BD": "🇧🇩", "BB": "🇧🇧", "BY": "🇧🇾",
    "BE": "🇧🇪", "BZ": "🇧🇿", "BT": "🇧🇹",
    "BO": "🇧🇴", "BA": "🇧🇦", "BW": "🇧🇼",
    "BV": "🇧🇻", "BR": "🇧🇷", "BN": "🇧🇳",
    "BG": "🇧🇬", "BF": "🇧🇩", "BI": "🇧🇮",
    "KH": "🇭🇭", "CM": "🇨🇲", "CA": "🇨🇦",
    "CV": "🇨🇻", "KY": "🇰🇾", "CF": "🇨🇫",
    "TD": "🇹🇩", "CL": "🇨🇱", "CN": "🇨🇳",
    "CY": "🇨🇾", "CZ": "🇨🇿", "DE": "🇩🇪",
    "DK": "🇩🇰", "DO": "🇩🇴", "EC": "🇪🇨",
    "EG": "🇪🇬", "SV": "🇪🇻", "EE": "🇪🇪",
    "ET": "🇪🇹", "FI": "🇫🇮", "FR": "🇫🇷",
    "GE": "🇬🇪", "GR": "🇬🇷", "GD": "🇬🇩",
    "GT": "🇬🇹", "GU": "🇬🇺", "GQ": "🇬🇶",
    "IN": "🇮🇳", "ID": "🇮🇩", "IR": "🇮🇷",
    "IQ": "🇮🇶", "IE": "🇮🇪", "IL": "🇮🇱",
    "IT": "🇮🇹", "JP": "🇯🇵", "JO": "🇯🇴",
    "KZ": "🇰🇿", "KE": "🇰🇪", "KI": "🇰🇮",
    "KR": "🇰🇵", "KW": "🇰🇼", "KG": "🇰🇬",
    "LA": "🇱🇦", "LB": "🇱🇧", "LS": "🇱🇸",
    "LV": "🇱🇻", "LR": "🇱🇷", "LY": "🇱🇾",
    "LT": "🇱🇹", "LU": "🇱🇺", "MO": "🇲🇴",
    "MK": "🇲🇰", "MG": "🇲🇬", "MY": "🇲🇾",
    "MV": "🇲🇻", "MW": "🇲🇼", "MX": "🇲🇽",
    "FM": "🇫🇲", "MD": "🇲🇩", "MA": "🇲🇦",
    "MN": "🇲🇳", "ME": "🇲🇪", "MS": "🇲🇸",
    "MZ": "🇲🇿", "MM": "🇲🇲", "NA": "🇳🇦",
    "NR": "🇳🇷", "NP": "🇳🇵", "NL": "🇳🇱",
    "NZ": "🇳🇿", "NI": "🇳🇮", "NE": "🇳🇪",
    "NG": "🇳🇬", "MP": "🇲🇵", "NO": "🇳🇴",
    "OM": "🇴🇲", "PK": "🇵🇰", "PA": "🇵🇦",
    "PG": "🇵🇬", "PY": "🇵🇾", "PE": "🇵🇪",
    "PH": "🇵🇭", "PN": "🇵🇳", "PL": "🇵🇱",
    "PT": "🇵🇹", "PR": "🇵🇷", "QA": "🇶🇦",
    "RO": "🇷🇴", "RU": "🇷🇺", "RW": "🇷🇼",
    "SA": "🇸🇦", "SN": "🇸🇳", "SG": "🇸🇬",
    "SK": "🇸🇰", "SI": "🇸🇮", "SS": "🇸🇸",
    "SZ": "🇸🇿", "SE": "🇸🇪", "CH": "🇨🇭",
    "TN": "🇹🇳", "TR": "🇹🇷", "TT": "🇹🇹",
    "TW": "🇹🇼", "TZ": "🇹🇿", "TH": "🇹🇭",
    "TL": "🇹🇱", "TG": "🇹🇪", "HK": "🇭🇰",
    "UM": "🇺🇲", "US": "🇺🇸", "UY": "🇺🇾",
    "UZ": "🇺🇿", "VA": "🇻🇦", "VU": "🇻🇺",
    "VN": "🇻🇳", "WF": "🇼🇫", "EH": "🇪🇭",
    "YE": "🇾🇪", "ZM": "🇿🇲", "ZW": "🇿🇼",
}

def avetaar_flag(region_code: str) -> str:
    return AVETAAR_FLAGS.get(region_code or "", "")

def avetaar_country_time(region_code: str, tz_names: list) -> str:
    import datetime
    import zoneinfo
    tz_name = tz_names[0] if tz_names else None
    try:
        if tz_name:
            tz = zoneinfo.ZoneInfo(tz_name)
            return datetime.datetime.now(tz).strftime("%H:%M %Z")
    except Exception:
        pass
    try:
        tz = zoneinfo.ZoneInfo(f"Etc/GMT0")
        return datetime.datetime.now(tz).strftime("%H:%M UTC")
    except Exception:
        return "?"

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
    country_name = geocoder.country_name_for_number(number, "en") or "غير معروفة"
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
        "رابط واتساب": "https://wa.me/" + e164.lstrip("+"),
        "رابط مكالمه": f"tel:{e164.lstrip('+')}",
        "رابط خريطة": (f"https://www.google.com/maps?q={region}" if region not in ("؟", "") else "غير متاح"),
        "رقم موبايل صالح": bool(phonenumbers.is_valid_number(number) and phonenumbers.is_possible_number_for_type(number, phonenumbers.PhoneNumberType.MOBILE)),
        "متوفر للمقارنة": True,
        "رابط تلكرام": ("https://t.me/" + national_sig if not national_sig.startswith("0") else "غير متاح"),
        "طول الرقم": len(str(number.national_number)),
        "رمز الدولة فقط": str(number.country_code),
        "صيغة الهاتف": phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        "صيغة وطنية": phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL),
        "علم الدولة": avetaar_flag(region),
        "الساعة المحلية": avetaar_country_time(region, tzs),
        "وصف الدولة": f"https://en.wikipedia.org/wiki/{country_name.replace(' ', '_').lower()}" if country_name not in ("غير معروفة", "مجهولة") else "غير متاح",
        "الرقم الوطني": national_sig,
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

def avetaar_record(number_raw: str, details: dict):
    entry = {"رقم": details['رقم الهاتف'], "دولة": details['اسم الدولة'], "مشغل": details['المشغل (SIM)'], "نوع": details['نوع الرقم']}
    AVETAAR_RECENT.append(entry)
    if len(AVETAAR_RECENT) > 5:
        AVETAAR_RECENT.pop(0)

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
    flag = details.get('علم الدولة', '')
    clock = details.get('الساعة المحلية', '')
    L.append(f"{flag} 🌍 الدولة: <b>{avetaar_esc(details['اسم الدولة'])}</b> ({avetaar_esc(details['رمز الدولة'])})")
    L.append(f"📍 الموقع: {avetaar_esc(details['الموقع'])}")
    L.append(f"📶 المشغل (SIM): <b>{avetaar_esc(details['المشغل (SIM)'])}</b>")
    L.append(f"⏰ الساعة هناك: <b>{avetaar_esc(clock)}</b> — 📏 طول الرقم: {avetaar_esc(details['طول الرقم'])} رقم")
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
    L.append("⬇️ استخدم الأزرار بالأسفل:")
    L.append("")
    L.append(f"⚙️ {AVETAAR_NAME} {AVETAAR_DEV} — {AVETAAR_CHANNEL}")
    return "\n".join(L)

AVETAAR_BTN_COLORS = {
    "action": "primary",
    "test": "primary",
    "validate": "success",
    "exit": "danger",
    "back": "success",
}

def avetaar_btn(text: str, callback_data: str, color_key: str) -> dict:
    style = AVETAAR_BTN_COLORS.get(color_key, "primary")
    b = {"text": text, "callback_data": callback_data}
    if style:
        b["style"] = style
    return b

def avetaar_buttons_menu() -> dict:
    return {
        "inline_keyboard": [
            [
                avetaar_btn("📞 أدخل رقم", "phone_input", "action"),
                avetaar_btn("✅ فحص موبايل", "validate_mobile", "validate"),
            ],
            [
                avetaar_btn("⚡ فحص سريع", "batch_input", "action"),
                avetaar_btn("🔀 مقارنة رقمين", "compare_input", "action"),
            ],
            [
                avetaar_btn("🎲 رقم عشوائي", "random_number", "test"),
                avetaar_btn("🔍 رقم تجريبي", "test_number", "test"),
            ],
            [
                avetaar_btn("📊 آخر 5 فحص", "recent_history", "back"),
                avetaar_btn("❌ خروج", "exit", "exit"),
            ],
        ]
    }

def avetaar_prompt_buttons() -> dict:
    return {
        "inline_keyboard": [
            [avetaar_btn("❌ خروج", "exit", "exit")],
        ]
    }

_pending_action = {}
AVETAAR_RECENT = []

def avetaar_handle_callback(token: str, update: dict):
    cb = update["callback_query"]
    chat_id = cb["message"]["chat"]["id"]
    data = cb["data"]
    try:
        avetaar_tg_call(token, "answerCallbackQuery", {"callback_query_id": cb["id"]})
    except Exception:
        pass
    if data == "menu":
        avetaar_tg_call(token, "editMessageText", {
            "chat_id": chat_id,
            "message_id": cb["message"]["message_id"],
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
            "reply_markup": avetaar_prompt_buttons(),
        })
    elif data == "test_number":
        avetaar_send_number_result(token, chat_id, "9647701234567")
    elif data == "validate_mobile":
        _pending_action[chat_id] = "validate_mobile"
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "✅ اكتب رقم لتفحص إذا كان موبايل صالح:\nمثال: <code>9647701234567</code>",
            "parse_mode": "HTML",
            "reply_markup": avetaar_prompt_buttons(),
        })
    elif data == "batch_input":
        _pending_action[chat_id] = "batch"
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "⚡ الصق 2-5 أرقام (سطر لكل رقم):\n9647701234567\n9647509876543\n12025551234",
            "parse_mode": "HTML",
            "reply_markup": avetaar_prompt_buttons(),
        })
    elif data == "compare_input":
        _pending_action[chat_id] = "compare"
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "🔀 اكتب رقمين بمسافة واحدة بينهما للمقارنة:\n9647701234567 9647509876543",
            "parse_mode": "HTML",
            "reply_markup": avetaar_prompt_buttons(),
        })
    elif data == "random_number":
        import random
        region = random.choice(["964", "966", "971", "974", "20", "90", "234", "34", "44"])
        num = random.randint(10000000, 99999999)
        raw = f"{region}{num}"
        avetaar_send_number_result(token, chat_id, raw)
    elif data == "recent_history":
        if AVETAAR_RECENT:
            L = ["📊 آخر الفحوصات:"]
            for i, e in enumerate(AVETAAR_RECENT, 1):
                L.append(f"{i}. <b>{avetaar_esc(e['رقم'])}</b> — {avetaar_esc(e['دولة'])} / {avetaar_esc(e['مشغل'])} / {avetaar_esc(e['نوع'])}")
            avetaar_tg_call(token, "sendMessage", {
                "chat_id": chat_id,
                "text": "\n".join(L),
                "parse_mode": "HTML",
                "reply_markup": avetaar_buttons_menu(),
            })
        else:
            avetaar_tg_call(token, "sendMessage", {
                "chat_id": chat_id,
                "text": "ماكو فحص بعد — جرّب زر '📞 أدخل رقم' أو '🎲 رقم عشوائي'.",
                "reply_markup": avetaar_buttons_menu(),
            })
    elif data.startswith("call_"):
        num = data.replace("call_", "")
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "📞 رابط الاتصال:\n<code>tel:" + avetaar_esc(num) + "</code>",
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })
    elif data.startswith("copy_e164_"):
        e164 = data.replace("copy_e164_", "")
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": f"📋 الرقم ب صيغة E164:\n<code>{avetaar_esc(e164)}</code>",
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })
    elif data.startswith("copy_nat_"):
        nat = data.replace("copy_nat_", "")
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": f"📋 نسخت الرقم الوطني <code>{avetaar_esc(nat)}</code> — انسخه من الرسالة.",
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })
    elif data == "copy_e164":
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "📋 أولّد رقم تجريبيًا ونسخ E164:\n<code>+9647701234567</code>\n\nشوف تفاصيل الرقم من زر '🔍 رقم تجريبي'.",
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
            action = _pending_action.get(chat_id)
            if action == "phone":
                _pending_action.pop(chat_id)
                avetaar_send_number_result(token, chat_id, text)
            elif action == "validate_mobile":
                _pending_action.pop(chat_id)
                avetaar_validate_mobile(token, chat_id, text)
            elif action == "batch":
                _pending_action.pop(chat_id)
                avetaar_batch_check(token, chat_id, text)
            elif action == "compare":
                _pending_action.pop(chat_id)
                avetaar_compare_two(token, chat_id, text)
            else:
                avetaar_send_number_result(token, chat_id, text)
    cb = u.get("callback_query")
    if cb:
        avetaar_handle_callback(token, u)

def avetaar_validate_mobile(token: str, chat_id: int, raw_number: str):
    number = avetaar_parse_number(raw_number)
    if not number:
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": f"⛔ رقم غير صالح: <b>{avetaar_esc(raw_number)}</b>",
            "parse_mode": "HTML",
            "reply_markup": avetaar_buttons_menu(),
        })
        return
    is_valid = phonenumbers.is_valid_number(number)
    is_mobile = phonenumbers.is_possible_number_for_type(number, phonenumbers.PhoneNumberType.MOBILE)
    if is_valid and is_mobile:
        L = [f"✅ <b>{avetaar_esc(raw_number)}</b> — رقم موبايل صالح!"]
    else:
        L = [f"❌ <b>{avetaar_esc(raw_number)}</b> — "]
        L.append("رقم غير صالح" if not is_valid else "رقم صالح بس مو موبايل")
    avetaar_tg_call(token, "sendMessage", {
        "chat_id": chat_id,
        "text": "\n".join(L),
        "parse_mode": "HTML",
        "reply_markup": avetaar_buttons_menu(),
    })

def avetaar_batch_check(token: str, chat_id: int, raw_text: str):
    nums = [n.strip() for n in raw_text.splitlines() if n.strip()]
    L = ["⚡ نتائج الفحص السريع:"]
    valid_count = 0
    mobile_count = 0
    total = min(len(nums), 5)
    for raw in nums[:5]:
        number = avetaar_parse_number(raw)
        if not number:
            L.append(f"⛔ <b>{avetaar_esc(raw)}</b> — رقم غير صالح")
            continue
        details = avetaar_number_details(number)
        avetaar_record(raw, details)
        ok = "✅" if details['صالح'] else "❌"
        if details['صالح']:
            valid_count += 1
        if details['ممكن موبايل']:
            mobile_count += 1
        flag = details.get('علم الدولة', '')
        L.append(f"{ok} {flag} <b>{avetaar_esc(details['رقم الهاتف'])}</b> — {avetaar_esc(details['اسم الدولة'])} / {avetaar_esc(details['المشغل (SIM)'])} / {avetaar_esc(details['نوع الرقم'])}")
    L.append("")
    L.append(f"📊 الإحصائيات: {valid_count}/{total} صالحة · {mobile_count}/{total} موبايلات")
    avetaar_tg_call(token, "sendMessage", {
        "chat_id": chat_id,
        "text": "\n".join(L),
        "parse_mode": "HTML",
        "reply_markup": avetaar_buttons_menu(),
    })

def avetaar_compare_two(token: str, chat_id: int, raw_text: str):
    parts = raw_text.split()
    if len(parts) != 2:
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "⛔ لازم تكتب رقمين بمسافة واحدة بينهما.",
            "reply_markup": avetaar_buttons_menu(),
        })
        return
    n1, n2 = avetaar_parse_number(parts[0]), avetaar_parse_number(parts[1])
    if not n1 or not n2:
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": "⛔ رقم واحد أو الاثنين غير صالح.",
            "reply_markup": avetaar_buttons_menu(),
        })
        return
    d1, d2 = avetaar_number_details(n1), avetaar_number_details(n2)
    avetaar_record(parts[0], d1)
    avetaar_record(parts[1], d2)
    L = [f"🔀 مقارنة: <b>{avetaar_esc(d1['رقم الهاتف'])}</b> vs <b>{avetaar_esc(d2['رقم الهاتف'])}</b>", ""]
    L.append(f"الدولة: {avetaar_esc(d1['اسم الدولة'])} vs {avetaar_esc(d2['اسم الدولة'])} {'✅ نفس الدولة' if d1['اسم الدولة'] == d2['اسم الدولة'] else '⛔ دولتين مختلفين'}")
    L.append(f"المشغل: {avetaar_esc(d1['المشغل (SIM)'])} vs {avetaar_esc(d2['المشغل (SIM)'])} {'✅ نفس المشغل' if d1['المشغل (SIM)'] == d2['المشغل (SIM)'] else '⛔ مشغلين مختلفين'}")
    L.append(f"النوع: {avetaar_esc(d1['نوع الرقم'])} vs {avetaar_esc(d2['نوع الرقم'])}")
    L.append(f"صالح: {'✅' if d1['صالح'] else '❌'} vs {'✅' if d2['صالح'] else '❌'}")
    avetaar_tg_call(token, "sendMessage", {
        "chat_id": chat_id,
        "text": "\n".join(L),
        "parse_mode": "HTML",
        "reply_markup": avetaar_buttons_menu(),
    })

def avetaar_result_buttons(details: dict) -> dict:
    wa = details['رابط واتساب']
    tel = details['رابط مكالمه']
    maps = details['رابط خريطة']
    flag = details.get('علم الدولة', '')
    return {
        "inline_keyboard": [
            [
                {"text": "💬 واتساب", "url": wa, "style": "success"},
                {"text": "📞 مكالمة", "callback_data": "call_" + details['رقم الهاتف'].lstrip('+'), "style": "primary"},
            ],
            [
                {"text": "🗺️ خريطة الدولة", "url": maps, "style": "primary"},
                {"text": "🌐 ويكيبيديا", "url": details.get('وصف الدولة', "https://en.wikipedia.org"), "style": "primary"},
            ],
            [
                {"text": "📋 نسخ E164", "callback_data": "copy_e164_" + details['تنسيق E164'], "style": "success"},
                {"text": "📋 نسخ الوطنية", "callback_data": "copy_nat_" + details['الرقم الوطني'], "style": "primary"},
            ],
            [
                {"text": f"{flag} 📞 رقم جديد", "callback_data": "phone_input", "style": "success"},
                {"text": "🔙 رجوع للقائمة", "callback_data": "menu", "style": "danger"},
            ],
        ]
    }

def avetaar_send_number_result(token: str, chat_id: int, raw_number: str):
    number = avetaar_parse_number(raw_number)
    if number:
        details = avetaar_number_details(number)
        avetaar_record(raw_number, details)
        avetaar_tg_call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": avetaar_bot_message(details),
            "parse_mode": "HTML",
            "reply_markup": avetaar_result_buttons(details),
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
    conflict_count = 0
    while True:
        try:
            d = avetaar_tg_call(token, "getUpdates", {
                "limit": 100,
                "offset": last_update_id + 1,
                "timeout": 10,
            })
            error_count = 0
            conflict_count = 0
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
            if "Conflict" in str(e):
                conflict_count += 1
                if conflict_count >= 5:
                    print(f"{C('RED')}⛔ نسخة ثانية من البوت شغّالة بنفس التوكن — أغلها أولًا.{RST()}")
                    print(f"   أغلق البرنامج الثاني ثم أعد تشغيل هذا البوت.")
                    time.sleep(15)
                    conflict_count = 0
                else:
                    print(f"{C('YELLOW')}⚠️ Conflict (نسخة ثانية) — إعادة بعد 5 ثوانٍ...{RST()}")
                    time.sleep(5)
            else:
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
