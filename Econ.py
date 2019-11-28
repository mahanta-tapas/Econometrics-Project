import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from linearmodels import PanelOLS
from linearmodels import RandomEffects

# A. Useful functions
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 0. Load data
df = pd.read_excel("/Users/tapas/Downloads/Oil/Econometrics_Clean.xlsx")
# print(df['Country Code'].nunique())
df1 = df[['Country_Name','Trademark_applications_total','Patent_applications_residents','Scientific_and_technical_journal_articles','Year','Internet_Users']]

df_panel = df.loc[(df['Year']== 2000) | (df['Year']== 2008)]
df_panel['Y2008'] = df_panel['Year'].apply(lambda x: '1' if x == 2008 else '0')
df_panel['Y2008'] = df_panel['Y2008'].astype('float64')
df_panel.fillna(0, inplace=True)
df_panel['total_research'] = df_panel['Trademark_applications_total'] + df_panel['Patent_applications_residents'] + df_panel['Scientific_and_technical_journal_articles']
#df_panel['Internet_Usage_Interaction'] = df_panel['Internet_Users'] * df_panel['Y2008']
#df_panel.to_excel("Execute data.xlsx")

# 1. Dummy variables regression
regr = linear_model.LinearRegression()
x = np.asanyarray(df_panel[[
'Y2008',
'Internet_Users',
'Internet_Usage_Interaction']])
y = np.asanyarray(df_panel[['total_research']])
regr.fit (x, y)
regr.coef_
#array([[30100.44305406,  4454.7342977 , -1373.52001246]])
regr.intercept_
#array([92084.43616858])
# using statsmodels to calculate
est = sm.OLS(y, x)
est2 = est.fit()

# The coefficients present
x_label = ['High-technology exports (% of manufactured exports)'
 ,'High-technology exports (current US$)'
 ,'Technicians in R&D (per million people)'
 ,'Researchers in R&D (per million people)'
 ,'Trademark applications (total)'
 ,'Trademark applications (direct resident)'
 ,'Trademark applications (direct nonresident)'
 ,'Patent applications (residents)'
 ,'Patent applications (nonresidents)'
 ,'Scientific and technical journal articles'
 ,'Research and development expenditure (% of GDP)'
 ,'Charges for the use of intellectual property receipts (Bop current US$)'
 ,'Charges for the use of intellectual property payments (BoP current US$)'
 ,'Year'
 ,'Internet Users %']
y_coef  = regr.coef_.tolist()    # extract coefficients from linear regression
y_coef = str(y_coef).strip('[]') # remove the outside []
y_coef = list(y_coef.split(',')) # list the coefficent seperate by ','
intercept = regr.intercept_ # the intercept of the regression

# Put p value and std.err inside the summary dataframe
coeff_df = pd.DataFrame({'Variables': x_label, 'Coefficients': y_coef})
coeff_df.set_index('Variables', inplace=True, drop=True)
# print(coeff_df)

# Output Result
results = est2.summary(xname=x_label)
with open('DummyRegression_Summary.csv', 'w') as fh:
    fh.write(results.as_csv())

# 1. DID
# Use columns 'Internet Users %' to interact with 'Year' and see the differece
# -> 2000=0, 2008=1
df_panel['Irate&Year'] = df_panel['Year']*df_panel['Internet Users %']
# 1. Build a regression
x_did = np.asanyarray(df_panel[['High-technology exports (% of manufactured exports)'
 ,'High-technology exports (current US$)'
 ,'Technicians in R&D (per million people)'
 ,'Researchers in R&D (per million people)'
 ,'Trademark applications, total'
 ,'Trademark applications, direct resident'
 ,'Trademark applications, direct nonresident'
 ,'Patent applications, residents'
 ,'Patent applications, nonresidents'
 ,'Scientific and technical journal articles'
 ,'Research and development expenditure (% of GDP)'
 ,'Charges for the use of intellectual property, receipts (BoP, current US$)'
 ,'Charges for the use of intellectual property, payments (BoP, current US$)'
 ,'Year'
 ,'Internet Users %'
 ,'Irate&Year']]) # add 'Irate&Year'
y_did = np.asanyarray(df_panel[['GDP']])
# using statsmodels to calculate
est_did = sm.OLS(y_did, x_did)
est2_did = est_did.fit()
# Show the report
x_labeldid = ['High-technology exports (% of manufactured exports)'
 ,'High-technology exports (current US$)'
 ,'Technicians in R&D (per million people)'
 ,'Researchers in R&D (per million people)'
 ,'Trademark applications (total)'
 ,'Trademark applications (direct resident)'
 ,'Trademark applications (direct nonresident)'
 ,'Patent applications (residents)'
 ,'Patent applications (nonresidents)'
 ,'Scientific and technical journal articles'
 ,'Research and development expenditure (% of GDP)'
 ,'Charges for the use of intellectual property - receipts (BoP current US$)'
 ,'Charges for the use of intellectual property - payments (BoPlll current US$)'
 ,'Year'
 ,'Internet Users %'
 ,'Irate&Year']
results_did = est2_did.summary(xname=x_labeldid)
with open('DID_summary.csv', 'w') as fh:
     fh.write(results_did.as_csv())

# 2. First differencesre

# 3. Fixed effect

# 4. Simple regression
regr_simple = linear_model.LinearRegression()
x_simp = np.asanyarray(df_panel[['High-technology exports (% of manufactured exports)'
 ,'High-technology exports (current US$)'
 ,'Technicians in R&D (per million people)'
 ,'Researchers in R&D (per million people)'
 ,'Trademark applications, total'
 ,'Trademark applications, direct resident'
 ,'Trademark applications, direct nonresident'
 ,'Patent applications, residents'
 ,'Patent applications, nonresidents'
 ,'Scientific and technical journal articles'
 ,'Research and development expenditure (% of GDP)'
 ,'Charges for the use of intellectual property, receipts (BoP, current US$)'
 ,'Charges for the use of intellectual property, payments (BoP, current US$)'
 ,'Year'
 ,'Internet Users %']])
y_simp = np.asanyarray(df_panel[['GDP']])
regr_simple.fit (x_simp, y_simp)
# using statsmodels to calculate
est_simp = sm.OLS(y_simp, x_simp)
est2_simp = est_simp.fit()

# The coefficients present
x_label_simp = ['High-technology exports (% of manufactured exports)'
 ,'High-technology exports (current US$)'
 ,'Technicians in R&D (per million people)'
 ,'Researchers in R&D (per million people)'
 ,'Trademark applications (total)'
 ,'Trademark applications (direct resident)'
 ,'Trademark applications (direct nonresident)'
 ,'Patent applications (residents)'
 ,'Patent applications (nonresidents)'
 ,'Scientific and technical journal articles'
 ,'Research and development expenditure (% of GDP)'
 ,'Charges for the use of intellectual property receipts (Bop current US$)'
 ,'Charges for the use of intellectual property payments (BoP current US$)'
 ,'Year'
 ,'Internet Users %']

# Output Result
results_simp = est2_simp.summary(xname=x_label_simp)
with open('LinearRegression_Summary.csv', 'w') as fh:
    fh.write(results_simp.as_csv())
