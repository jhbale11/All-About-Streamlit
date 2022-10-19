# All-About-Streamlit

**The fastest way to build and share data apps.**

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

## Streamlit Test App

Streamlit's simple and focused API lets you build incredibly rich and powerful tools.  [This demo project](https://github.com/streamlit/demo-self-driving) lets you browse the entire [Udacity self-driving-car dataset](https://github.com/udacity/self-driving-car) and run inference in real-time using the [YOLO object detection net](https://pjreddie.com/darknet/yolo).

![Final App Animation](https://raw.githubusercontent.com/streamlit/docs/main/public/images/complex_app_example.gif)

The complete demo is implemented in less than 300 lines of Python. In fact, the app contains [only 23 Streamlit calls](https://github.com/streamlit/demo-self-driving/blob/master/streamlit_app.py) which illustrates all the major building blocks of Streamlit. You can try it right now at [share.streamlit.io/streamlit/demo-self-driving](https://share.streamlit.io/streamlit/demo-self-driving).

## The Streamlit GitHub badge

Streamlit's GitHub badge helps others find and play with your Streamlit app.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/streamlit/demo-face-gan)

Once you deploy your app, you can embed this badge right into your GitHub readme.md as follows:

```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourGitHubName/yourRepo/yourApp/)
```


