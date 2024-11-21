import streamlit as st # pip install streamlit==0.82.0
import gtts # pip install gtts
import os
lines = open('./双语语料库.txt','r').readlines()
   
def translator(lines,text):
    language_dict = {}
    for line in lines:
        line = line.strip()
        if line:    
            cantonese, english = line.split('=')
            language_dict[cantonese] = english
    if text in list(language_dict.keys()):
        return language_dict[text]
    else:
        return '对不起，我不会'

st.set_page_config(page_title='Simply! Translate', page_icon='translator-icon.png', layout='wide', initial_sidebar_state='expanded')


Languages = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','odia':'or','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr','turkmen':'tk','ukrainian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}


text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")

option1 = st.selectbox('Input language',
                      ('中文','English'))

option2 = st.selectbox('Output language',
                       ('English','中文'))

#value1 = Languages[option1]
#value2 = Languages[option2]

if st.button('Translate Sentence'):
    if text == "":
        st.warning('Please **enter text** for translation')

    else:
        translate = translator(lines,text)
        st.info(str(translate))

        converted_audio = gtts.gTTS(translate, lang='en')
        converted_audio.save("translated.mp3")
        audio_file = open('translated.mp3','rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio')
        st.write("To **download the audio file**, click the kebab menu on the audio bar.")
        st.success("Translation is **successfully** completed!")
        st.balloons()
else:
    pass

 
 





