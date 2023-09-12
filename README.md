# DATA ANALYSIS AND MACHINE LEARNING IMPLEMENTATION FOR AMAZON DATA
## DATA ANALYSIS
### PURPOSE FOR THE PROJECT
The purpose of this project was to analyse the amazon sales data by cleaning it accordingly and doing the necessary feature engineering to make the dataset easier to use after which the necessary data visualizations were to be made for the data. After the data visualisations, a machine learning model was created with the necessary columns in order to make a ML model that accepts inputs from the user and makes the appropriate price predictuions.
### DATA ANALYSIS
- First was to check the information on the data to know:
  1. Find out the number of rows and columns that we will be dealing with
  2. Check for the null values
  3. Check the data types that the data contains to see if the data is in its correct data type
- Then I proceeded to now clean the data according to the information that was obtained and deal with it accordingly.
  1. First, the Yen symbol was removed from the prices columns because its prescence caused the columns to appear as strings instead of intagers.
  2. The commas indicating the prices were in thousands was removed so as the columns to be converted from strings to integer.
  3. Since there was a column that appeared abnormal(strings) yet contains ints, it had to be checked individualy and identify the root of the problem which was done and solved.
  4. A dummy dataframe was created and columns I deemed unnecessary were dropped so as to affect the original dataframe for future purposes if need be.
- Feature engineering
  1. First was to split the 'category' column to a 'Main category' amd a Sub category due to the prescence of the separator '|' which would pose a problem in the future.
  2. After the splitting of the main category column, the original category column was dropped as itbwas no longer needed.
  3. The names in the sub and main category were joined hence needed to be separated and were separated with the str.replace method for each value.
- The data info was checked again and was concluded that the data was good for saving.
### DATA VISUALIZATION
- A .py file was created using the VS-Code app so as to create the streamlit app which would display the data visualizations.
- Streamlit was imported first which would be used in the whole process.
- Seaborn and matplotlib.pyplot were imported which would be used to make the plots.
- The cleaned data was loaded to the .py file with the @st.cache_data function
- A title of the app was set and a brief description of the app and its purpose.
- an option menu was created for a more neat and organized work for each of the visualizations.
#### CREATING THE PLOTS
- The first plot was to deal with the number of products in the main and sub category
  -This was done with two axes and the data loaded was used as data and the plots were made using the count as the y-value and the categories respectively as the x-axis.
- The products and their ratings were displayed in the following ways:
  1. The direct relationship between the products and their respective ratings.
  2. A new 'table' was created by called rating score that showed the various ratings on the satisfaction scale, which was then reordered to show from the least satisfactory to the most satisfactory rating.
  3. The visualizations of the rating score were done against the products using seaborn with x-axis as the score and the y-axix as the score scale.
- The relationship between actual price, discounted price and discount percentage was shpwn with the appropriate seaborn plots and the conclusions drawn from the plots.
### TRAINING THE MACHINE LEARNING MODEL
-A model needed to be trained in order to make the actual price predictions.
1. The cleaned data was first imported to the ipynb file and null values were checked and corrected with the mode.
2. The necessary Science Kit tools were imported and the necessary python libraries as well.
3. The X and y values were created from the dataframe columns and were split using the train_test_split method.
4. Regression models were used since the data was continous so regression models were imported.
5. The models were trained wih the split data and the best parameters were required to be determined using the best_params_ method to produce a model with the best accuracy.
6. The models were fitted with the data and evaluated to determine the best model to use with the best parameters determined.
7. the best model was then trained with the data and a prediction was made.
8. The model was evaluated and a score was deemed acceptable and the data was saved using joblib.
### STREAMLIT APP FOR THE TRAINED MODEL
- The streamlit, scikit-learn and joblib tools were imported for usage.
- The model was imported using joblib.
- A feature for the data input was created with number_input function to accept the user inputs for predictions.
- A dict was created to complement the feature vakues created by the number inputs which will feed the model the said values.
- The input data was scaled with the StandardScaler.
- THe dat was then fitted to the model.
- Predictions were then made with the model.
- A prediction button was created unto which apon clicking would prompt the st.success to give the output.
- An st.success function was created which would display the predicted values on the streamlit app.
- The streamlit app was the created.
