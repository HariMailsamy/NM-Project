import streamlitasst 
from transformers import pipeline
#Loadapre-trainedemotionclassificationmodelfromHuggingFaceclassifier
=pipeline("text-classification",
model="bhadresh-savani/bert-base-go-emotion", 
return_all_scores=True)
#StreamlitUI 
st.set_page_config(page_title="EmotionAnalyzer",layout="centered") 
st.title("◻ SocialMedia EmotionAnalyzer")
st.markdown("Enteratweet,message,orsocialmediaposttodetectemotionsin the 
text.")
#Userinput 
text_input=st.text_area("YourText",placeholder="e.g.Ican'tbelievehow
amazingthisdayhasbeen!",height=150)
ifst.button("Analyze"):
if not text_input.strip(): 
st.warning("Pleaseentersometext.")
else:
with st.spinner("Analyzing..."): 
results=classifier(text_input)[0]#
Sort results by score 
results=sorted(results,key=lambdax:x['score'],reverse=True)
st.subheader("◻EmotionScores")
for itemin results[:5]:# show top5 emotions 
st.write(f"**{item['label'].capitalize()}**:{item['score']:.2f}")
st.success("Analysiscomplete!")
