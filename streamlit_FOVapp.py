import streamlit as st
import math


def FOV(wl_min, wl_max,ng,theta_d_max):
    
    theta_d_max = math.radians(theta_d_max)
    theta_d_min = math.radians(critical_angle(ng)) 
    FOV = 2*math.asin((ng*math.sin(theta_d_max) - (ng*wl_max/(wl_min+wl_max)*(math.sin(theta_d_max) + math.sin(theta_d_min)))))
    FOV = round(math.degrees(FOV),3)
    return FOV 

def critical_angle(ng):
    
    theta_d_min = math.asin(1/ng)
    theta_d_min = math.degrees(theta_d_min)
    print(f"critical angle, aka. theta_d_min : {theta_d_min: .2f} deg") 
    return theta_d_min

def main():
    st.title("光波导FOV 系统")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">视场角快速计算 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    ng = st.text_input("材料折射率","1")
    wl_max = st.text_input("最长波长（nm）","700")
    wl_min = st.text_input("最短波长（nm）","400")
    theta_d_max = st.text_input("最大衍射角（度）","90")
    ng,wl_max,wl_min,theta_d_max = float(wl_min), float(wl_max),float(ng),float(theta_d_max)
    result=""
    if st.button("预测"):
        result=FOV(ng,wl_max,wl_min,theta_d_max) 
    st.success('视场角FOV： {}'.format(result))
    if st.button("关于About"):
        
        st.text("Built from Jerry W")

if __name__=='__main__':
    main()
