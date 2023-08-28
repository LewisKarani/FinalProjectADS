import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

@st.cache_data
def load_data():
    data = pd.read_csv(r'C:\Users\HP\Documents\my-data/amazon_cleaned.csv')
    return data
data = load_data()


st.title("Amazon sales data analysis")
st.write("This app shows the  amazon sales data and the respective visualizations.")


with st.sidebar:
    selected = option_menu(
        menu_title = "Options Menu",
        options= [ 'Number of products by Main & Sub category', 'Most products by Main & Sub category', 'Rating and rating count', 'Actual price, discounted price and discount percentage', 'Summary']
    )

# category analysis

#cat = data[['Main category', 'Sub category', 'product_id']]
#cat_piv = pd.pivot_table(cat, index=['Main category', 'Sub category'], aggfunc='count')

if selected == 'Number of products by Main & Sub category':
    st.subheader('Number of products by Main & Sub category')
    cat = data[['Main category', 'Sub category', 'product_id']]
    cat_piv = pd.pivot_table(cat, index=['Main category', 'Sub category'], aggfunc='count')

    st.dataframe(cat_piv)

if selected == 'Most products by Main & Sub category':
    st.subheader('Most products by Main & Sub category')
    main_cat_pro = data['Main category'].value_counts().head(5).rename_axis('Main category').reset_index(name = 'count')
    sub_cat_pro = data['Sub category'].value_counts().head(10).rename_axis('Sub category').reset_index(name = 'count')

    fig, ax = plt.subplots(2,1, figsize = (8,10))

    sns.barplot(ax=ax[0], data = main_cat_pro, x='count', y='Main category')
    sns.barplot(ax=ax[1], data = sub_cat_pro, x='count', y='Sub category')

    plt.subplots_adjust(hspace = 0.3)

    ax[0].set_xlabel('Number of Products', fontweight='bold')
    ax[0].set_ylabel('Product Main Category', fontweight='bold')

    ax[1].set_xlabel('Number of Products', fontweight='bold')
    ax[1].set_ylabel('Product Sub Category', fontweight='bold')

    ax[0].set_title('Most Products by Main Category', fontweight='bold')
    ax[1].set_title('Most Products by Sub Category', fontweight='bold')


    ax[0].bar_label(ax[0].containers[0])
    ax[1].bar_label(ax[1].containers[0])

    st.pyplot(fig)

    st.write('Electronis, Computer & Accessories and Home & Kitchen account for most of the products in this dataset. In general, most products are related to technology and eletronic devices.')
    fig2, ax = plt.subplots(figsize = (12,10))
    sns.boxplot(data = data, x='rating', y='Main category')
    plt.title('Rating range by Main Category', fontweight = 'bold')
    plt.xlabel('Rating', fontweight = 'bold')
    plt.ylabel('Main Category', fontweight = 'bold')
    st.pyplot(fig2)

if selected == 'Rating and rating count':
    st.subheader('Rating and rating count')
    fig, ax = plt.subplots(1,2, figsize = (15,7))
    sns.histplot(ax=ax[0],data=data, x='rating', bins=10, kde=True, color='blue')
    sns.histplot(ax=ax[1],data=data, x='rating_count', bins=10, kde=True, color='red')

    ax[0].set_title('Distribution of rating', fontweight='bold')
    ax[1].set_title('Distribution of rating count', fontweight='bold')

    ax[0].set_xlabel('Rating', fontweight='bold')
    ax[1].set_xlabel('Rating Count', fontweight='bold')

    ax[0].set_ylabel('Count', fontweight='bold')
    ax[1].set_ylabel('Count', fontweight='bold')
    st.pyplot(fig)

    # Create new category column `rating_score`
    st.write('Rating score by amount and percentage discount')
    rating_score = []
    for i in data['rating']:
       if i < 2.0: rating_score.append('Very unsatified')
       elif i < 3.0: rating_score.append('Unsatified')
       elif i < 4.0: rating_score.append('Neutral')
       elif i < 5.0: rating_score.append('Satified')
       elif i == 5.0: rating_score.append('Very satified')
    data['rating_score'] = rating_score
    data['rating_score'] = data['rating_score'].astype('category')
    # Reorder cateories
    data['rating_score'] = data['rating_score'].cat.reorder_categories(['Unsatified', 'Neutral', 'Satified','Very satified'], ordered=True)
    rating_score_pct = data['rating_score'].value_counts(normalize=True).rename_axis('score').reset_index(name='score_pct')
    rating_score_pct['score_pct'] = rating_score_pct['score_pct'].round(3)
    fig2, ax = plt.subplots(1,2, figsize = (15,7))
    sns.countplot(ax=ax[0], data=data, x='rating_score')
    sns.barplot(ax=ax[1],data = rating_score_pct, x='score', y='score_pct')

    ax[0].set_title('Amount of products by Rating Score', fontweight = 'bold')
    ax[1].set_title('Percentage of product by Rating Score', fontweight = 'bold')

    ax[0].set_xlabel('Rating Score', fontweight = 'bold')
    ax[1].set_xlabel('Rating Score', fontweight = 'bold')

    ax[0].set_ylabel('Amount', fontweight = 'bold')
    ax[1].set_ylabel('Percentage', fontweight = 'bold')

    ax[0].bar_label(ax[0].containers[0])
    ax[1].bar_label(ax[1].containers[0])
    st.pyplot(fig2)
    st.write("Over 75% of products listed in the marketplace are rated as 'Satified' by customers. Whereas, only 6 products as well as 0.4% receive 'Unsatified' score.")

if selected == 'Actual price, discounted price and discount percentage':
    st.subheader('Actual price, discounted price and discount percentage')
    fig, ax = plt.subplots(2,2, figsize = (15,10))
    plt.subplots_adjust(hspace = 0.3)

    sns.histplot(ax=ax[0,0], data = data, x='actual_price', bins = 10, kde = True, color = 'blue')
    sns.histplot(ax=ax[0,1], data = data, x='discounted_price', bins = 10, kde = True, color = 'green')
    sns.histplot(ax=ax[1,0], data = data, x='discount_percentage', bins = 10, kde = True, color = 'purple')

    ax[0,0].set_title('Distribution of Actual Price', fontweight = 'bold')
    ax[0,1].set_title('Distribution of Discounted Price', fontweight = 'bold')
    ax[1,0].set_title('Distribution of Discount Percentage', fontweight = 'bold')

    ax[0,0].set_xlabel('Actual Price', fontweight = 'bold')
    ax[0,1].set_xlabel('Discounted Price', fontweight = 'bold')
    ax[1,0].set_xlabel('Discount Percentage', fontweight = 'bold')

    ax[0,0].set_ylabel('Amount', fontweight = 'bold')
    ax[0,1].set_ylabel('Amount', fontweight = 'bold')
    ax[1,0].set_ylabel('Amount', fontweight = 'bold')

    ax.flat[-1].set_visible(False)
    st.pyplot(fig)
    st.write("The scale of discount percentage is much more balanced with most of the products having discounts at around 50%-60%.")

    st.subheader('Box plots for the discount range for main category and sub category')
    
    fig3, ax = plt.subplots(2,1, figsize = (8,13))
    sns.boxplot(ax=ax[0], data = data, x='discount_percentage', y='Main category')
    sns.boxplot(ax=ax[1], data = data, x='discount_percentage', y='Sub category')

    ax[0].set_title('Discount Percentage Range by Main Category', fontweight = 'bold')
    ax[1].set_title('Discount Percentage Range by Sub Category', fontweight = 'bold')

    ax[0].set_xlabel('Discount Percentage', fontweight = 'bold')
    ax[1].set_xlabel('Discount Percentage', fontweight = 'bold')

    ax[0].set_ylabel('Main Category', fontweight = 'bold')
    ax[1].set_ylabel('Sub Category', fontweight = 'bold')
    st.pyplot(fig3)
if selected == 'Summary':
    st.subheader('Summary for the Amazon sales data')
    st.write('i. Electronis, Computer & Accessories and Home & Kitchen account for most of the products in this dataset. In general, most products are related to technology and eletronic devices.')
    st.write('ii. The majority of products receive the overall rating at the range around 3.8 and 4.0.')
    st.write('iii. The highest rating is 5.0 coming from Computer & Accessories.')
    st.write('iv. The lowest rating for a product is 2.0 from Home & Kitchen category.')
    st.write('v. The rating range of most products is around 3.75 and 4.38. The distribution of rating is left_skewed with no products rated lower than 2.0.')
    st.write('vi. Both Actual price and Discounted price have a widespread range of distribution, specifically 0-140000 and 0-78000 respectively and both of the 2 graphs are highly right-skewed.')
