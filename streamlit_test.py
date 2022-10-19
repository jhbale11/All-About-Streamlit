#import libs
from tokenize import group
import pandas as pd
import numpy as np
# import plotly.graph_objects as go
# import plotly.express as px
import streamlit as st
from datetime import datetime

import matplotlib.pyplot as plt
import time

####################################
# 1_ Define Functions
# - Load data
# - Clean data
####################################




####################################
# 2_ Engineer Data
# - prepare data for output
####################################




####################################
# 3_ Build Dashboard
####################################


DIVIDER = '--------------------------------------------------------------------------------'


####################################
# - Sidebar
####################################
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/16810004?v=4", width=300)
    st.title("Hi. This is jhbale11's Streamlit Study Repo")
    st.title("This is available page list!")
    st.markdown("**- Welcome :** Introduction & References")
    st.markdown("**- Text :** Text elements & st.write method")
    st.markdown("**- Data :** Data Display & Elements Display")
    st.markdown("**- Chart :** Chart Elements")
    st.markdown("**- Widget :** Display Interactive Widgets")
    st.markdown("**- Sample :** Toy project for uber pickup in NYC")

VIEW_WELCOME = 'Welcome '

VIEW_API_TEXT = 'Text'
VIEW_API_DATA = 'Data'
VIEW_API_CHART = 'Chart'
VIEW_UBER_NYC = 'Sample: Uber picksup in NYC'
VIEW_API_WIDGET = 'Widget'


sidebar = [VIEW_WELCOME, 
        VIEW_API_TEXT,
        VIEW_API_DATA,
        VIEW_API_CHART,
        VIEW_API_WIDGET,
        VIEW_UBER_NYC]
add_sidebar = st.sidebar.selectbox('Choose Page You Want to See', sidebar) #('Aggregate Metrics','Individual Video Analysis'))


with st.sidebar:
    add_radio = st.radio(
        "Choose a language (not working)",
        ("English", "Korean")
    )



####################################
# - VIEW_WELCOME
####################################
if add_sidebar == VIEW_WELCOME:
    st.title(add_sidebar)
    st.header('Let\'s learn Streamlit library')
    st.write(DIVIDER)
    st.subheader('Github Repo Available!')
    url1 = 'https://github.com/jhbale11/All-About-Streamlit'
    url1 

    st.write(DIVIDER)
    st.subheader('Install & Import')

    st.markdown('#### Pre-release Features')
    code = '''
        pip uninstall streamlit
        pip install streamlit-nightly --upgrade
        '''
    st.code(code, language='bash')


    st.markdown('#### Run streamlit server')
    code = '''
            streamlit run streamlit_test.py'''
    st.code(code, language='bash')

    st.markdown('#### Command Line')
    code = '''
        streamlit --help
        streamlit run your_script.py
        streamlit hello
        streamlit config show
        streamlit cache clear
        streamlit docs
        streamlit --version
        '''
    st.code(code, language='bash')

    st.markdown('#### Import Convention')
    code = '''
            # Import Convention
            import streamlit as st'''
    st.code(code, language='python')

    st.write(DIVIDER)
    
    st.subheader('Template')    

    code = '''
        #<Sample code for the template>
        
        import streamlit as st
        import pandas as pd
        
        ####################################
        # 1_ Define Functions
        # - Load data
        # - Clean data
        ####################################
        @st.cache
        def load_data():
            #filepath = 'some_filepath.csv'
            #df = pd.read_csv(filepath)
            df = pd.DataFrame({
                'first column': [1, 2, 3, 4],
                'second column': [10, 20, 30, 50],
            })
            return df
        df = load_data()
        ####################################
        # 2_ Engineer Data
        # - prepare data for output
        ####################################
        df.column = ['Number', 'Scores']
        df['Level'] = ['C', 'B', 'B', 'A']
        ####################################
        # 3_Build Dashboard using Streamlit
        ####################################
        st.title('You can build Streamlit Webapp')
        add_sidebar = st.sidebar.selectbox('Select Method', 'First','Second')
        if add_sidebar == 'First':
            # View for s'First'- show matrix, graph etc.
        else :
            # View for 'Second' - show matrix, graph etc.
        '''
    st.code(code, language='python')


    st.write(DIVIDER)
    st.subheader('References')
    url1 = 'https://docs.streamlit.io/'
    url2 = 'https://bittersweet-match-49f.notion.site/Streamlit-5ca73e87f96a443a902eefc5c721e3d0'

    url1
    url2



####################################
# - VIEW_API_TEXT
####################################
elif add_sidebar == VIEW_API_TEXT:
    st.title(add_sidebar)
    st.subheader('Streamlit supports various types of text elements')

    
    with st.container():
        #st.write(f'(1) Text Elements')
        st.write(DIVIDER)
        st.header('st.header | (1) Text Elements')
        st.write(DIVIDER)
        st.subheader('st.subheader | texts for formatted texts')
        st.write(DIVIDER)
        st.markdown('st.markdown | Streamlit is **_really_ cool**.')
        st.write(DIVIDER)
        st.caption('st.caption | caption: This is a string that explains something above.')
        st.write(DIVIDER)

        st.markdown('This is how to write code')
        code = '''
            def hello():
            print("This is code block for python")'''
        st.code(code, language='python')

        code = '''
            <script type="text/javascript">
            alert("Hello Javatpoint");
            </script>'''
        st.code(code, language='javascript')
        st.write(DIVIDER)
        st.markdown('**This is how st.echo() works :** Write & Show Instantly')
        with st.echo():
            st.write("with st.echo(): ")
            st.write("This is another way to show code.")
        st.write(DIVIDER)

        st.text('st.text | This is some text.')
        st.write(DIVIDER)
        st.markdown('This is how to write latex : ')
        st.latex(r'''
            st.latex = a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
            \sum_{k=0}^{n-1} ar^k =
            a \left(\frac{1-r^{n}}{1-r}\right)
            ''')
        


    st.write(DIVIDER)


    with st.container():
        #st.write(f'(2) st.write and Magic function')
        st.header('(2) st.write and Magic')
        st.subheader('(2-1) st.write can write many things')

        st.write(1234)
        st.write('1000+ 4, ' , (1000+4))
        st.write('Below is a pandas dataframe')
        st.write(pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 50],
        }))

        st.subheader('(2-2) Magic write without command')
        tab_names = ['Valuable','Pandas Dataframe', 'Matplotlib']
        tab1, tab2, tab3 = st.tabs(tab_names)

        with tab1:
            st.header(tab_names[0])
            x = 10
            y = 20
            'x', x  #  Draw the string 'x' and then the value of x
            'y', y
            'x+y', x+y


        with tab2:
            st.header(tab_names[1])
            test_df = pd.DataFrame({'col1': [1,2,3]})
            test_df  #  Draw the dataframe            

        with tab3:
            st.header(tab_names[2])
            # Also works with most supported chart types
            arr = np.random.normal(1, 1, size=100)
            fig, ax = plt.subplots()
            ax.hist(arr, bins=20)
            fig  #  Draw a Matplotlib chart


####################################
# - VIEW_API_DATA
####################################
elif add_sidebar == VIEW_API_DATA:
    st.title(add_sidebar)
    st.subheader('Stream supports various types of data showing methods')

    with st.echo():
        df = pd.DataFrame(
        np.random.randn(20, 20),
        columns=('col %d' % i for i in range(20)))


    with st.container():
        st.subheader('(1) st.dataframe(pd.dataframe)')
        st.markdown('Can show pandas dataframe with `st.dataframe(df)`')
        st.dataframe(df)  # Same as st.write(df)
    
    with st.container():
        st.subheader('(2) st.table(pd.dataframe)')
        st.markdown('Can show pandas dataframe with `st.table(df)`')
        st.table(df)    

    with st.container():
        st.subheader('(3) st.metric')
        st.markdown('Can show metric with `st.metric`')
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "70 °F", "1.2 °F")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")
        st.markdown('Automatic visualization like dashboard form')

    with st.container():
        st.subheader('(4) st.json')
        st.markdown('Can show json data type with `st.json`')
        st.json({
            'foo': 'bar',
            'baz': 'boz',
            'stuff': [
                'stuff 1',
                'stuff 2',
                'stuff 3',
                'stuff 5',
            ],
        })
        



####################################
# - VIEW_API_CHART
####################################
elif add_sidebar == VIEW_API_CHART:
    st.title(add_sidebar)
    st.subheader('Stream supports various types of data showing methods')
    st.header('(1) Dataframe to streamlit chart')
    with st.echo():
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])


    with st.container():
        st.subheader('(1-1) st.line_chart(chart_data)')
        st.line_chart(chart_data)

    with st.container():
        st.subheader('(1-2) st.area_chart(chart_data)')
        st.area_chart(chart_data)

    with st.container():
        st.subheader('(1-3) st.bar_chart(chart_data)')
        st.bar_chart(chart_data)

    st.write(DIVIDER)
    with st.container():
        st.subheader('(1-4) st.map(df)')
        with st.echo():
            df = pd.DataFrame(
                np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                columns=['lat', 'lon'])
        st.map(df)


    st.write(DIVIDER)

    st.header('(2) Python library chart')
    st.markdown('Visualizations with `df` dataframe')
    with st.echo():
        
        df = pd.DataFrame(
            np.random.randn(100, 3),
            columns= ['a', 'b', 'c'])


    with st.container():
        st.subheader('(2-1) matplotlib.pyplot --> `st.pyplot`')


        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.hist(df, bins=10)
        
        st.pyplot(fig)

    st.write(DIVIDER)

    with st.container():
        st.subheader('(2-2) Plotly.Chart --> `st.plotly_chart()`')
        
        import plotly.figure_factory as ff

        fig1 = ff.create_distplot([df[c] for c in df.columns], df.columns, bin_size=.25)
        st.plotly_chart(fig1, user_container_width=True)


    st.write(DIVIDER)
    


####################################
# - \VIEW_API_WIDGET
####################################
elif add_sidebar == VIEW_API_WIDGET:
    st.title(add_sidebar)

    st.subheader('This is button with `st.button()`')
    st.button('Click me')

    st.subheader('This is checkbox with `st.checkbox()`')
    st.checkbox('I agree')

    st.subheader('This is radio with `st.radio()`')
    st.radio('Pick one', ['cats', 'dogs'])

    st.subheader('This is selectbox with `st.selectbox()`')
    st.selectbox('Pick one', ['cats', 'dogs'])

    st.subheader('This is multiselect with `st.multiselect()`')
    st.multiselect('Buy', ['milk', 'apples', 'potatoes', 'carrots', 'bananas'])
    
    st.subheader('This is slider with `st.slider()`')
    st.slider('Pick a number between `0 - 100`', 0, 100)

    st.subheader('This is categorical slider with `st.select_slider()`')
    st.select_slider('Pick a size', ['XS','S', 'M', 'L', 'XL', 'XXL'])
    
    st.subheader('This is text input with `st.text_input()`')
    text = st.text_input('What is your First name')
    st.write('My first name is : ', text)

    st.subheader('This is number input with `st.number_input()`')
    st.number_input('Pick a number', 0, 10)

    st.subheader('This is text area with `st.text_area()`')
    long_text = st.text_area('Text to translate')
    st.write('output : ', long_text)

    st.subheader('This is date type input with `st.date_input()`')
    date = st.date_input('Your birthday')
    st.write('output : ',date)

    st.subheader('This is  with `st.()`')
    st.time_input('Meeting time')

    st.subheader('This is  with file uploader `st.file_uploader()`')
    uploaded_df = st.file_uploader('Upload a CSV')
    st.write(uploaded_df)

    st.subheader('This is color picker with `st.color_picker()`')
    color = st.color_picker('Pick a color')
    st.write(color)

####################################
# - \VIEW_UBER_NYC
####################################
elif add_sidebar == VIEW_UBER_NYC:
    st.title(VIEW_UBER_NYC)
	
    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
        
    @st.cache
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
        
    data_load_state = st.text('Loading data...')
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache)")
        
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
        
    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
        
    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
        
    st.subheader('Map of all pickups at %s:00' % hour_to_filter)
    st.map(filtered_data)

