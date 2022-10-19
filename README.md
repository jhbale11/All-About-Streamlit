# All-About-Streamlit [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/streamlit/demo-face-gan)

#### **The fastest way to build and share data apps!**
#### **Streamlit은 데이터 사이언티스드가 데이터로 app을 만드는 가장 쉬운 방법입니다!**

본 repo는 강력한 시각화 툴인 Streamlit에 대한 스터디 정리입니다.

Streamlit lets you turn data scripts into shareable web apps in minutes, not weeks. It’s all Python, open-source, and free! And once you’ve created an app you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app!

![Example of live coding an app in Streamlit|635x380](https://raw.githubusercontent.com/streamlit/docs/main/public/images/Streamlit_overview.gif)

## Installation

```bash
pip install streamlit
streamlit hello
```

Streamlit can also be installed in a virtual environment on
- [Windows](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-windows)
- [Mac](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux)
- [Linux](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux)

## Simple Usage

```python
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
```

<img src="https://raw.githubusercontent.com/streamlit/docs/main/public/images/simple_example.png"/>

## Streamlit Study App

[jhbale11's Streamlit Study App](https://jhbale11-all-about-streamlit-streamlit-test-h7bpp9.streamlitapp.com/)

![app-gif](https://github.com/jhbale11/All-About-Streamlit/blob/main/img/streamlit-streamlit_test-2022-10-19-11-10-33.gif)

#### Side Bar List
- Welcome : Introduction & References
- Text : Text elements & st.write method
- Data : Data Display & Elements Display
- Chart : Chart Elements
- Widget : Display Interactive Widgets
- Sample : Toy project for uber pickup in NYC

I made a sample app, make a simple cheat-sheet for all elements in Streamlit
Use app to easily understand all features of powerfull streamlit!

## License
[MIT](https://choosealicense.com/licenses/mit/)



