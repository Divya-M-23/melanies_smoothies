# Import python packages
import streamlit as st
# import requests
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


# Write directly to the ap
st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie"""
  # """Replace this example with your own code!
  # **And if you're new to Streamlit,** check
  # out our easy-to-follow guides at
  # [docs.streamlit.io](https://docs.streamlit.io).
  # """
)

# ADD A NAME BOX FOR SMOOTHIE ORDERS

name_on_order=st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:',name_on_order)

#ADDING INTERACTIVE ELEMENTS
# import streamlit as st

# option=st.selectbox(
#     'What is your favorite fruit?',
#     ('Banana','Strawberries','Peaches'))

# st.write('You favorite fruit is:',option)


# import requests  
# smoothiefroot_response = requests.get("[https://my.smoothiefroot.com/api/fruit/watermelon](https://my.smoothiefroot.com/api/fruit/watermelon)")  
# st.text(smoothiefroot_response)

#DISPLAY THE FRUIT OPTIONS LIST IN YOUR STREAMLIT IN SNOWFLAKE (SiS) APP
# session = get_active_session()

cnx=st.connection("snowflake")
session=cnx.session()


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
                                                                      # ,col('SEARCH_ON'))
st.dataframe(data=my_dataframe, use_container_width=True)
# st.stop()


# smoothiefroot_response = requests.get(f"https://my.smoothiefroot.com/api/fruit/{search_on}")
# CONVERT THE SNOWPARK DATAFRAME TO A PANDAS DATAFRAME SO WE CAN USE THE LOC FUNCTION

# pd_df=my_dataframe.to_pandas()
# st.dataframe(pd_df)
# st.stop()



ingredients_list=st.multiselect(
    'Choose up to 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
)


# NEW SECTION TO DISPLAY SMOOTHIEFRUIT NUTRITION INFORMATION
import requests  
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
# (https://my.smoothiefroot.com/api/fruit/watermelon)")  
# st.text(smoothiefroot_response.json())
sf_df=st.dataframe(data=smoothiefroot.response.json(), use_container_width=True)

# IF BLOCK

if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)
    
#CREATE THE INGREDIENTS_STRING VARIABLE
    ingredients_string=''

# FOR BLOCK

    for fruit_chosen in ingredients_list:
        ingredients_string+=fruit_chosen+' '

        # search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        # st.write('The search value for ', fruit_chosen,' is ', search_on, '.')

        # st.subheader(fruit_chosen+'Nutrition Information')
        # fruityvice_response= requests.get("https://fruityvice.com/api/fruit"+fruit_chosen)
        # # import requests
        # smoothiefroot_response = requests.get(f"https://my.smoothiefroot.com/api/fruit/{search_on}")
        # sf_df=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)
    # st.write(ingredients_string)

# BUILD A SQL INSERT STATEMENT AND TEST IT

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
                    values ('""" + ingredients_string +"""','"""+name_on_order+"""')"""

    # st.write(my_insert_stmt)
    # st.stop()

    
    time_to_insert=st.button('Submit Order')

# INSERT THE ORDER INTO SNOWFLAKE
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success(f'Your Smoothie is ordered, {name_on_order}!', icon="✅")

        
        # st.write('Your smoothie is ordered',name_on_order)
# # Get the current credentials
# session = get_active_session()

# # Use an interactive slider to get user input
# hifives_val = st.slider(
#   "Number of high-fives in Q3",
#   min_value=0,
#   max_value=90,
#   value=60,
#   help="Use this to enter the number of high-fives you gave in Q3",
# )

# #  Create an example dataframe
# #  Note: this is just some dummy data, but you can easily connect to your Snowflake data
# #  It is also possible to query data using raw SQL using session.sql() e.g. session.sql("select * from table")
# created_dataframe = session.create_dataframe(
#   [[50, 25, "Q1"], [20, 35, "Q2"], [hifives_val, 30, "Q3"]],
#   schema=["HIGH_FIVES", "FIST_BUMPS", "QUARTER"],
# )

# # Execute the query and convert it into a Pandas dataframe
# queried_data = created_dataframe.to_pandas()

# # Create a simple bar chart
# # See docs.streamlit.io for more types of charts
# st.subheader("Number of high-fives")
# st.bar_chart(data=queried_data, x="QUARTER", y="HIGH_FIVES")

# st.subheader("Underlying data")
# st.dataframe(queried_data, use_container_width=True)
