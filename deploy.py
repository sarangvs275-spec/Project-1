import streamlit as st
import pickle

model=pickle.load(open('model.save','rb'))
scaler=pickle.load(open('scaler.save','rb'))
gen=pickle.load(open('gender.save','rb'))
smoke=pickle.load(open('smoke.save','rb'))

def main():

    st.title(':red[Diabetes prediction App]')

    gender=st.selectbox('Gender',['Female','male'])
    age=st.text_input('Age','type here')
    hyper=st.selectbox('HYPERTENSION',['yes','no'])
    if hyper=='yes':
        hyper=1
    else:
        hyper=0    
    heartdisease = st.selectbox('HEART DISEASE', ['yes', 'no'])
    heartdisease = 1 if heartdisease == 'yes' else 0  
    smoki=st.selectbox('SMOKING HISTORY',['never', 'No Info','former', 'current','ever' ,'not current', 'No Info'])
    bmi=st.text_input('BMI','type here')
    hb=st.text_input('HbA1c_level','type here')
    bgl=st.text_input('blood_glucose_level','type here')   

    pred=st.button('predict')   

    gender1=gen.transform([gender])[0]    
    smoki=smoke.transform([smoki])[0]      

    f=[
        gender1,age,hyper,heartdisease,smoki,bmi,hb,bgl
    ]   

    if pred:
        s=scaler.transform([f])
        m=model.predict(s)    
        if m==1:
            st.success('diabetes')
        else:
            st.error('no diabetes')           

main()
