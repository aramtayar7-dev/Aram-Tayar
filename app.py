import streamlit as st

# ئەم بەشە بۆ ئەوەیە ماڵپەڕەکە ژمارەی ڕۆژەکان لەبیر نەکات
if 'days_clean' not in st.session_state:
    st.session_state.days_clean = 0

def recovery_guide_bot(user_input):
    text = user_input.lower()
    
    zianekan = ["زیان", "خراپە", "بۆچی خراپە", "کێشە", "مەترسی"]
    charasar = ["چارەسەر", "چۆن واز بهێنم", "وازهێنان", "یارمەتی", "ڕێگا", "سروشتی"]
    arezakan = ["ئارەزوو", "خەریکە", "بێزارم", "بێهێزم", "تێکچووم"]
    ziadkrdn = ["سەرکەوتم", "ڕۆژێکی تر", "تێپەڕاند"]
    shkandin = ["شکاندم", "گەڕامەوە", "سفر", "هەڵەم کرد"]
    prsiari_roj = ["چەند ڕۆژە", "ڕۆژەکانم", "چەندم"]

    if any(word in text for word in ziadkrdn):
        st.session_state.days_clean += 1
        return f"🎉 پیرۆزە! تۆ زۆر بەهێزیت. ئەمڕۆش بە سەرکەوتوویی تێپەڕی.\nئێستا ژمارەی ڕۆژە پاکەکانت بوو بە: {st.session_state.days_clean} ڕۆژ."
        
    elif any(word in text for word in shkandin):
        st.session_state.days_clean = 0
        return "هیچ کێشە نییە، هەموومان هەڵە دەکەین. گرنگ ئەوەیە کۆڵ نەدەیت و لێوەی فێربیت. ژمێرەرەکە سفر کرایەوە، با بەیەکەوە سەرلەنوێ دەست پێبکەینەوە!"
        
    elif any(word in text for word in prsiari_roj):
        if st.session_state.days_clean == 0:
            return "ئێستا لە ڕۆژی سفرداین. با هەر ئەمڕۆ بکەینە یەکەم ڕۆژی دەستپێکردنێکی نوێ!"
        else:
            return f"تۆ تا ئێستا {st.session_state.days_clean} ڕۆژە سەرکەوتوو بوویت. بەردەوام بە!"

    elif any(word in text for word in zianekan):
        return "سەیرکردنی ئەم جۆرە ڤیدیۆیانە چەندین زیانی هەیە:\n١. تێکدانی سیستەمی دۆپامین.\n٢. کەمبوونەوەی سەرنج.\n٣. دروستبوونی دڵەڕاوکێ و خەمۆکی."

    elif any(word in text for word in charasar):
        return "بۆ وازهێنان، ئەم هەنگاوانە پەیڕەو بکە:\n١. کاتە بەتاڵەکانت پڕ بکەرەوە.\n٢. مۆبایل مەبە بۆ ناو جێگەی خەو.\n٣. تێکەڵی خێزان و هاوڕێکانت ببە."

    elif any(word in text for word in arezakan):
        return "ئێستا مۆبایلەکەت دابنێ! هەستە بڕۆ دەرەوە پیاسەیەک بکە یان ئاوێکی سارد بە ڕووخسارتدا بکە. ئەم هەستە کاتییە و تێدەپەڕێت."

    elif "سڵاو" in text:
        return "سڵاو! من ڕێبەری تەندروستیی تۆم. دەتوانیت پرسیارم لێ بکەیت یان پێم بڵێیت (سەرکەوتم)."
    
    else:
        return "تێناگەم مەبەستت چییە. دەتوانیت بڵێیت (سەرکەوتم)، (چەند ڕۆژە)، یان پرسیار دەربارەی (چارەسەر) بکەیت."

# دیزاینی ماڵپەڕەکە
st.title("🌿 ڕێبەری تەندروستی")
st.write("ئەمە یەکەمین ژیریی دەستکردی کوردییە بۆ یارمەتیدانت لە وازهێنان لە ئالوودەبوون و دەستپێکردنی ژیانێکی نوێ.")

# وەرگرتنی پرسیار لە بەکارهێنەر
user_input = st.text_input("پرسیارەکەت یان قسەکەت لێرە بنووسە:")

if st.button("ناردن"):
    if user_input:
        response = recovery_guide_bot(user_input)
        st.info(response)
