import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# A. Useful functions
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 0. Load data
df = pd.read_excel("./Econometrics_Clean.xlsx")
# print(df['Country Code'].nunique())
df_panel = df.loc[(df['Year']== 2000) | (df['Year']== 2008)]
df_panel = pd.get_dummies(df_panel, columns=['Country Code']) # 256 country code
df_panel['Year'] = df_panel['Year'].apply(lambda x: '1' if x == 2008 else '0')
df_panel['Year'] = df_panel['Year'].astype('float64')
df_panel.fillna(0, inplace=True)
df_panel.to_excel("Execute data.xlsx")

# 1. Dummy variables regression
regr = linear_model.LinearRegression()
x = np.asanyarray(df_panel[['Country Code_ABW', 'Country Code_AFG', 'Country Code_AGO', 'Country Code_ALB', 'Country Code_AND', 'Country Code_ARB', 'Country Code_ARE', 'Country Code_ARG'
 ,'Country Code_ARM', 'Country Code_ATG', 'Country Code_AUS', 'Country Code_AUT', 'Country Code_AZE', 'Country Code_BDI', 'Country Code_BEL', 'Country Code_BEN', 'Country Code_BFA'
 ,'Country Code_BGD', 'Country Code_BGR', 'Country Code_BHR', 'Country Code_BHS', 'Country Code_BIH', 'Country Code_BLR', 'Country Code_BLZ', 'Country Code_BMU', 'Country Code_BOL'
 ,'Country Code_BRA', 'Country Code_BRB', 'Country Code_BRN', 'Country Code_BTN', 'Country Code_BWA', 'Country Code_CAF', 'Country Code_CAN', 'Country Code_CEB', 'Country Code_CHE'
 ,'Country Code_CHL', 'Country Code_CHN', 'Country Code_CIV', 'Country Code_CMR', 'Country Code_COD', 'Country Code_COG', 'Country Code_COL', 'Country Code_COM', 'Country Code_CPV'
 ,'Country Code_CRI', 'Country Code_CSS', 'Country Code_CUB', 'Country Code_CYP', 'Country Code_CZE', 'Country Code_DEU', 'Country Code_DJI', 'Country Code_DMA', 'Country Code_DNK'
 ,'Country Code_DOM', 'Country Code_DZA', 'Country Code_EAP', 'Country Code_EAR', 'Country Code_EAS', 'Country Code_ECA', 'Country Code_ECS', 'Country Code_ECU', 'Country Code_EGY'
 ,'Country Code_EMU', 'Country Code_ERI', 'Country Code_ESP', 'Country Code_EST', 'Country Code_ETH', 'Country Code_EUU', 'Country Code_FCS', 'Country Code_FIN', 'Country Code_FJI'
 ,'Country Code_FRA', 'Country Code_FRO', 'Country Code_FSM', 'Country Code_GAB', 'Country Code_GBR', 'Country Code_GEO', 'Country Code_GHA', 'Country Code_GIN', 'Country Code_GMB'
 ,'Country Code_GNB', 'Country Code_GNQ', 'Country Code_GRC', 'Country Code_GRD', 'Country Code_GRL', 'Country Code_GTM', 'Country Code_GUY', 'Country Code_HIC', 'Country Code_HKG'
 ,'Country Code_HND', 'Country Code_HPC', 'Country Code_HRV', 'Country Code_HTI', 'Country Code_HUN', 'Country Code_IBD', 'Country Code_IBT', 'Country Code_IDA', 'Country Code_IDB'
 ,'Country Code_IDN', 'Country Code_IDX', 'Country Code_IND', 'Country Code_IRL', 'Country Code_IRN', 'Country Code_IRQ', 'Country Code_ISL', 'Country Code_ISR', 'Country Code_ITA'
 ,'Country Code_JAM', 'Country Code_JOR', 'Country Code_JPN', 'Country Code_KAZ', 'Country Code_KEN', 'Country Code_KGZ', 'Country Code_KHM', 'Country Code_KIR', 'Country Code_KNA'
 ,'Country Code_KOR', 'Country Code_KWT', 'Country Code_LAC', 'Country Code_LAO', 'Country Code_LBN', 'Country Code_LBR', 'Country Code_LBY', 'Country Code_LCA', 'Country Code_LCN'
 ,'Country Code_LDC', 'Country Code_LIC', 'Country Code_LIE', 'Country Code_LKA', 'Country Code_LMC', 'Country Code_LMY', 'Country Code_LSO', 'Country Code_LTE', 'Country Code_LTU'
 ,'Country Code_LUX', 'Country Code_LVA', 'Country Code_MAC', 'Country Code_MAR', 'Country Code_MCO', 'Country Code_MDA', 'Country Code_MDG', 'Country Code_MDV', 'Country Code_MEA'
 ,'Country Code_MEX', 'Country Code_MHL', 'Country Code_MIC', 'Country Code_MKD', 'Country Code_MLI', 'Country Code_MLT', 'Country Code_MMR', 'Country Code_MNA', 'Country Code_MNE'
 ,'Country Code_MNG', 'Country Code_MOZ', 'Country Code_MRT', 'Country Code_MUS', 'Country Code_MWI', 'Country Code_MYS', 'Country Code_NAC', 'Country Code_NAM', 'Country Code_NCL'
 ,'Country Code_NER', 'Country Code_NGA', 'Country Code_NIC', 'Country Code_NLD', 'Country Code_NOR', 'Country Code_NPL', 'Country Code_NRU', 'Country Code_NZL', 'Country Code_OED'
 ,'Country Code_OMN', 'Country Code_OSS', 'Country Code_PAK', 'Country Code_PAN', 'Country Code_PER', 'Country Code_PHL', 'Country Code_PLW', 'Country Code_PNG', 'Country Code_POL'
 ,'Country Code_PRE', 'Country Code_PRI', 'Country Code_PRK', 'Country Code_PRT', 'Country Code_PRY', 'Country Code_PSE', 'Country Code_PSS', 'Country Code_PST', 'Country Code_PYF'
 ,'Country Code_QAT', 'Country Code_ROU', 'Country Code_RUS', 'Country Code_RWA', 'Country Code_SAS', 'Country Code_SAU', 'Country Code_SDN', 'Country Code_SEN', 'Country Code_SGP'
 ,'Country Code_SLB', 'Country Code_SLE', 'Country Code_SLV', 'Country Code_SMR', 'Country Code_SOM', 'Country Code_SRB', 'Country Code_SSA', 'Country Code_SSD', 'Country Code_SSF'
 ,'Country Code_SST', 'Country Code_STP', 'Country Code_SUR', 'Country Code_SVK', 'Country Code_SVN', 'Country Code_SWE', 'Country Code_SWZ', 'Country Code_SYC', 'Country Code_SYR'
 ,'Country Code_TCD', 'Country Code_TEA', 'Country Code_TEC', 'Country Code_TGO', 'Country Code_THA', 'Country Code_TJK', 'Country Code_TKM', 'Country Code_TLA', 'Country Code_TLS'
 ,'Country Code_TMN', 'Country Code_TON', 'Country Code_TSA', 'Country Code_TSS', 'Country Code_TTO', 'Country Code_TUN', 'Country Code_TUR', 'Country Code_TUV', 'Country Code_TZA'
 ,'Country Code_UGA', 'Country Code_UKR', 'Country Code_UMC', 'Country Code_URY', 'Country Code_USA', 'Country Code_UZB', 'Country Code_VCT', 'Country Code_VEN', 'Country Code_VNM'
 ,'Country Code_VUT', 'Country Code_WLD', 'Country Code_WSM', 'Country Code_XKX', 'Country Code_YEM', 'Country Code_ZAF', 'Country Code_ZMB', 'Country Code_ZWE'
 ,'High-technology exports (% of manufactured exports)'
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
y = np.asanyarray(df_panel[['GDP']])
regr.fit (x, y)
# using statsmodels to calculate
est = sm.OLS(y, x)
est2 = est.fit()

# The coefficients present
x_label = ['Country Code_ABW', 'Country Code_AFG', 'Country Code_AGO', 'Country Code_ALB', 'Country Code_AND', 'Country Code_ARB', 'Country Code_ARE', 'Country Code_ARG'
 ,'Country Code_ARM', 'Country Code_ATG', 'Country Code_AUS', 'Country Code_AUT', 'Country Code_AZE', 'Country Code_BDI', 'Country Code_BEL', 'Country Code_BEN', 'Country Code_BFA'
 ,'Country Code_BGD', 'Country Code_BGR', 'Country Code_BHR', 'Country Code_BHS', 'Country Code_BIH', 'Country Code_BLR', 'Country Code_BLZ', 'Country Code_BMU', 'Country Code_BOL'
 ,'Country Code_BRA', 'Country Code_BRB', 'Country Code_BRN', 'Country Code_BTN', 'Country Code_BWA', 'Country Code_CAF', 'Country Code_CAN', 'Country Code_CEB', 'Country Code_CHE'
 ,'Country Code_CHL', 'Country Code_CHN', 'Country Code_CIV', 'Country Code_CMR', 'Country Code_COD', 'Country Code_COG', 'Country Code_COL', 'Country Code_COM', 'Country Code_CPV'
 ,'Country Code_CRI', 'Country Code_CSS', 'Country Code_CUB', 'Country Code_CYP', 'Country Code_CZE', 'Country Code_DEU', 'Country Code_DJI', 'Country Code_DMA', 'Country Code_DNK'
 ,'Country Code_DOM', 'Country Code_DZA', 'Country Code_EAP', 'Country Code_EAR', 'Country Code_EAS', 'Country Code_ECA', 'Country Code_ECS', 'Country Code_ECU', 'Country Code_EGY'
 ,'Country Code_EMU', 'Country Code_ERI', 'Country Code_ESP', 'Country Code_EST', 'Country Code_ETH', 'Country Code_EUU', 'Country Code_FCS', 'Country Code_FIN', 'Country Code_FJI'
 ,'Country Code_FRA', 'Country Code_FRO', 'Country Code_FSM', 'Country Code_GAB', 'Country Code_GBR', 'Country Code_GEO', 'Country Code_GHA', 'Country Code_GIN', 'Country Code_GMB'
 ,'Country Code_GNB', 'Country Code_GNQ', 'Country Code_GRC', 'Country Code_GRD', 'Country Code_GRL', 'Country Code_GTM', 'Country Code_GUY', 'Country Code_HIC', 'Country Code_HKG'
 ,'Country Code_HND', 'Country Code_HPC', 'Country Code_HRV', 'Country Code_HTI', 'Country Code_HUN', 'Country Code_IBD', 'Country Code_IBT', 'Country Code_IDA', 'Country Code_IDB'
 ,'Country Code_IDN', 'Country Code_IDX', 'Country Code_IND', 'Country Code_IRL', 'Country Code_IRN', 'Country Code_IRQ', 'Country Code_ISL', 'Country Code_ISR', 'Country Code_ITA'
 ,'Country Code_JAM', 'Country Code_JOR', 'Country Code_JPN', 'Country Code_KAZ', 'Country Code_KEN', 'Country Code_KGZ', 'Country Code_KHM', 'Country Code_KIR', 'Country Code_KNA'
 ,'Country Code_KOR', 'Country Code_KWT', 'Country Code_LAC', 'Country Code_LAO', 'Country Code_LBN', 'Country Code_LBR', 'Country Code_LBY', 'Country Code_LCA', 'Country Code_LCN'
 ,'Country Code_LDC', 'Country Code_LIC', 'Country Code_LIE', 'Country Code_LKA', 'Country Code_LMC', 'Country Code_LMY', 'Country Code_LSO', 'Country Code_LTE', 'Country Code_LTU'
 ,'Country Code_LUX', 'Country Code_LVA', 'Country Code_MAC', 'Country Code_MAR', 'Country Code_MCO', 'Country Code_MDA', 'Country Code_MDG', 'Country Code_MDV', 'Country Code_MEA'
 ,'Country Code_MEX', 'Country Code_MHL', 'Country Code_MIC', 'Country Code_MKD', 'Country Code_MLI', 'Country Code_MLT', 'Country Code_MMR', 'Country Code_MNA', 'Country Code_MNE'
 ,'Country Code_MNG', 'Country Code_MOZ', 'Country Code_MRT', 'Country Code_MUS', 'Country Code_MWI', 'Country Code_MYS', 'Country Code_NAC', 'Country Code_NAM', 'Country Code_NCL'
 ,'Country Code_NER', 'Country Code_NGA', 'Country Code_NIC', 'Country Code_NLD', 'Country Code_NOR', 'Country Code_NPL', 'Country Code_NRU', 'Country Code_NZL', 'Country Code_OED'
 ,'Country Code_OMN', 'Country Code_OSS', 'Country Code_PAK', 'Country Code_PAN', 'Country Code_PER', 'Country Code_PHL', 'Country Code_PLW', 'Country Code_PNG', 'Country Code_POL'
 ,'Country Code_PRE', 'Country Code_PRI', 'Country Code_PRK', 'Country Code_PRT', 'Country Code_PRY', 'Country Code_PSE', 'Country Code_PSS', 'Country Code_PST', 'Country Code_PYF'
 ,'Country Code_QAT', 'Country Code_ROU', 'Country Code_RUS', 'Country Code_RWA', 'Country Code_SAS', 'Country Code_SAU', 'Country Code_SDN', 'Country Code_SEN', 'Country Code_SGP'
 ,'Country Code_SLB', 'Country Code_SLE', 'Country Code_SLV', 'Country Code_SMR', 'Country Code_SOM', 'Country Code_SRB', 'Country Code_SSA', 'Country Code_SSD', 'Country Code_SSF'
 ,'Country Code_SST', 'Country Code_STP', 'Country Code_SUR', 'Country Code_SVK', 'Country Code_SVN', 'Country Code_SWE', 'Country Code_SWZ', 'Country Code_SYC', 'Country Code_SYR'
 ,'Country Code_TCD', 'Country Code_TEA', 'Country Code_TEC', 'Country Code_TGO', 'Country Code_THA', 'Country Code_TJK', 'Country Code_TKM', 'Country Code_TLA', 'Country Code_TLS'
 ,'Country Code_TMN', 'Country Code_TON', 'Country Code_TSA', 'Country Code_TSS', 'Country Code_TTO', 'Country Code_TUN', 'Country Code_TUR', 'Country Code_TUV', 'Country Code_TZA'
 ,'Country Code_UGA', 'Country Code_UKR', 'Country Code_UMC', 'Country Code_URY', 'Country Code_USA', 'Country Code_UZB', 'Country Code_VCT', 'Country Code_VEN', 'Country Code_VNM'
 ,'Country Code_VUT', 'Country Code_WLD', 'Country Code_WSM', 'Country Code_XKX', 'Country Code_YEM', 'Country Code_ZAF', 'Country Code_ZMB', 'Country Code_ZWE'
 ,'High-technology exports (% of manufactured exports)'
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
x_did = np.asanyarray(df_panel[['Country Code_ABW', 'Country Code_AFG', 'Country Code_AGO', 'Country Code_ALB', 'Country Code_AND', 'Country Code_ARB', 'Country Code_ARE', 'Country Code_ARG'
 ,'Country Code_ARM', 'Country Code_ATG', 'Country Code_AUS', 'Country Code_AUT', 'Country Code_AZE', 'Country Code_BDI', 'Country Code_BEL', 'Country Code_BEN', 'Country Code_BFA'
 ,'Country Code_BGD', 'Country Code_BGR', 'Country Code_BHR', 'Country Code_BHS', 'Country Code_BIH', 'Country Code_BLR', 'Country Code_BLZ', 'Country Code_BMU', 'Country Code_BOL'
 ,'Country Code_BRA', 'Country Code_BRB', 'Country Code_BRN', 'Country Code_BTN', 'Country Code_BWA', 'Country Code_CAF', 'Country Code_CAN', 'Country Code_CEB', 'Country Code_CHE'
 ,'Country Code_CHL', 'Country Code_CHN', 'Country Code_CIV', 'Country Code_CMR', 'Country Code_COD', 'Country Code_COG', 'Country Code_COL', 'Country Code_COM', 'Country Code_CPV'
 ,'Country Code_CRI', 'Country Code_CSS', 'Country Code_CUB', 'Country Code_CYP', 'Country Code_CZE', 'Country Code_DEU', 'Country Code_DJI', 'Country Code_DMA', 'Country Code_DNK'
 ,'Country Code_DOM', 'Country Code_DZA', 'Country Code_EAP', 'Country Code_EAR', 'Country Code_EAS', 'Country Code_ECA', 'Country Code_ECS', 'Country Code_ECU', 'Country Code_EGY'
 ,'Country Code_EMU', 'Country Code_ERI', 'Country Code_ESP', 'Country Code_EST', 'Country Code_ETH', 'Country Code_EUU', 'Country Code_FCS', 'Country Code_FIN', 'Country Code_FJI'
 ,'Country Code_FRA', 'Country Code_FRO', 'Country Code_FSM', 'Country Code_GAB', 'Country Code_GBR', 'Country Code_GEO', 'Country Code_GHA', 'Country Code_GIN', 'Country Code_GMB'
 ,'Country Code_GNB', 'Country Code_GNQ', 'Country Code_GRC', 'Country Code_GRD', 'Country Code_GRL', 'Country Code_GTM', 'Country Code_GUY', 'Country Code_HIC', 'Country Code_HKG'
 ,'Country Code_HND', 'Country Code_HPC', 'Country Code_HRV', 'Country Code_HTI', 'Country Code_HUN', 'Country Code_IBD', 'Country Code_IBT', 'Country Code_IDA', 'Country Code_IDB'
 ,'Country Code_IDN', 'Country Code_IDX', 'Country Code_IND', 'Country Code_IRL', 'Country Code_IRN', 'Country Code_IRQ', 'Country Code_ISL', 'Country Code_ISR', 'Country Code_ITA'
 ,'Country Code_JAM', 'Country Code_JOR', 'Country Code_JPN', 'Country Code_KAZ', 'Country Code_KEN', 'Country Code_KGZ', 'Country Code_KHM', 'Country Code_KIR', 'Country Code_KNA'
 ,'Country Code_KOR', 'Country Code_KWT', 'Country Code_LAC', 'Country Code_LAO', 'Country Code_LBN', 'Country Code_LBR', 'Country Code_LBY', 'Country Code_LCA', 'Country Code_LCN'
 ,'Country Code_LDC', 'Country Code_LIC', 'Country Code_LIE', 'Country Code_LKA', 'Country Code_LMC', 'Country Code_LMY', 'Country Code_LSO', 'Country Code_LTE', 'Country Code_LTU'
 ,'Country Code_LUX', 'Country Code_LVA', 'Country Code_MAC', 'Country Code_MAR', 'Country Code_MCO', 'Country Code_MDA', 'Country Code_MDG', 'Country Code_MDV', 'Country Code_MEA'
 ,'Country Code_MEX', 'Country Code_MHL', 'Country Code_MIC', 'Country Code_MKD', 'Country Code_MLI', 'Country Code_MLT', 'Country Code_MMR', 'Country Code_MNA', 'Country Code_MNE'
 ,'Country Code_MNG', 'Country Code_MOZ', 'Country Code_MRT', 'Country Code_MUS', 'Country Code_MWI', 'Country Code_MYS', 'Country Code_NAC', 'Country Code_NAM', 'Country Code_NCL'
 ,'Country Code_NER', 'Country Code_NGA', 'Country Code_NIC', 'Country Code_NLD', 'Country Code_NOR', 'Country Code_NPL', 'Country Code_NRU', 'Country Code_NZL', 'Country Code_OED'
 ,'Country Code_OMN', 'Country Code_OSS', 'Country Code_PAK', 'Country Code_PAN', 'Country Code_PER', 'Country Code_PHL', 'Country Code_PLW', 'Country Code_PNG', 'Country Code_POL'
 ,'Country Code_PRE', 'Country Code_PRI', 'Country Code_PRK', 'Country Code_PRT', 'Country Code_PRY', 'Country Code_PSE', 'Country Code_PSS', 'Country Code_PST', 'Country Code_PYF'
 ,'Country Code_QAT', 'Country Code_ROU', 'Country Code_RUS', 'Country Code_RWA', 'Country Code_SAS', 'Country Code_SAU', 'Country Code_SDN', 'Country Code_SEN', 'Country Code_SGP'
 ,'Country Code_SLB', 'Country Code_SLE', 'Country Code_SLV', 'Country Code_SMR', 'Country Code_SOM', 'Country Code_SRB', 'Country Code_SSA', 'Country Code_SSD', 'Country Code_SSF'
 ,'Country Code_SST', 'Country Code_STP', 'Country Code_SUR', 'Country Code_SVK', 'Country Code_SVN', 'Country Code_SWE', 'Country Code_SWZ', 'Country Code_SYC', 'Country Code_SYR'
 ,'Country Code_TCD', 'Country Code_TEA', 'Country Code_TEC', 'Country Code_TGO', 'Country Code_THA', 'Country Code_TJK', 'Country Code_TKM', 'Country Code_TLA', 'Country Code_TLS'
 ,'Country Code_TMN', 'Country Code_TON', 'Country Code_TSA', 'Country Code_TSS', 'Country Code_TTO', 'Country Code_TUN', 'Country Code_TUR', 'Country Code_TUV', 'Country Code_TZA'
 ,'Country Code_UGA', 'Country Code_UKR', 'Country Code_UMC', 'Country Code_URY', 'Country Code_USA', 'Country Code_UZB', 'Country Code_VCT', 'Country Code_VEN', 'Country Code_VNM'
 ,'Country Code_VUT', 'Country Code_WLD', 'Country Code_WSM', 'Country Code_XKX', 'Country Code_YEM', 'Country Code_ZAF', 'Country Code_ZMB', 'Country Code_ZWE'
 ,'High-technology exports (% of manufactured exports)'
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
x_labeldid = ['Country Code_ABW', 'Country Code_AFG', 'Country Code_AGO', 'Country Code_ALB', 'Country Code_AND', 'Country Code_ARB', 'Country Code_ARE', 'Country Code_ARG'
 ,'Country Code_ARM', 'Country Code_ATG', 'Country Code_AUS', 'Country Code_AUT', 'Country Code_AZE', 'Country Code_BDI', 'Country Code_BEL', 'Country Code_BEN', 'Country Code_BFA'
 ,'Country Code_BGD', 'Country Code_BGR', 'Country Code_BHR', 'Country Code_BHS', 'Country Code_BIH', 'Country Code_BLR', 'Country Code_BLZ', 'Country Code_BMU', 'Country Code_BOL'
 ,'Country Code_BRA', 'Country Code_BRB', 'Country Code_BRN', 'Country Code_BTN', 'Country Code_BWA', 'Country Code_CAF', 'Country Code_CAN', 'Country Code_CEB', 'Country Code_CHE'
 ,'Country Code_CHL', 'Country Code_CHN', 'Country Code_CIV', 'Country Code_CMR', 'Country Code_COD', 'Country Code_COG', 'Country Code_COL', 'Country Code_COM', 'Country Code_CPV'
 ,'Country Code_CRI', 'Country Code_CSS', 'Country Code_CUB', 'Country Code_CYP', 'Country Code_CZE', 'Country Code_DEU', 'Country Code_DJI', 'Country Code_DMA', 'Country Code_DNK'
 ,'Country Code_DOM', 'Country Code_DZA', 'Country Code_EAP', 'Country Code_EAR', 'Country Code_EAS', 'Country Code_ECA', 'Country Code_ECS', 'Country Code_ECU', 'Country Code_EGY'
 ,'Country Code_EMU', 'Country Code_ERI', 'Country Code_ESP', 'Country Code_EST', 'Country Code_ETH', 'Country Code_EUU', 'Country Code_FCS', 'Country Code_FIN', 'Country Code_FJI'
 ,'Country Code_FRA', 'Country Code_FRO', 'Country Code_FSM', 'Country Code_GAB', 'Country Code_GBR', 'Country Code_GEO', 'Country Code_GHA', 'Country Code_GIN', 'Country Code_GMB'
 ,'Country Code_GNB', 'Country Code_GNQ', 'Country Code_GRC', 'Country Code_GRD', 'Country Code_GRL', 'Country Code_GTM', 'Country Code_GUY', 'Country Code_HIC', 'Country Code_HKG'
 ,'Country Code_HND', 'Country Code_HPC', 'Country Code_HRV', 'Country Code_HTI', 'Country Code_HUN', 'Country Code_IBD', 'Country Code_IBT', 'Country Code_IDA', 'Country Code_IDB'
 ,'Country Code_IDN', 'Country Code_IDX', 'Country Code_IND', 'Country Code_IRL', 'Country Code_IRN', 'Country Code_IRQ', 'Country Code_ISL', 'Country Code_ISR', 'Country Code_ITA'
 ,'Country Code_JAM', 'Country Code_JOR', 'Country Code_JPN', 'Country Code_KAZ', 'Country Code_KEN', 'Country Code_KGZ', 'Country Code_KHM', 'Country Code_KIR', 'Country Code_KNA'
 ,'Country Code_KOR', 'Country Code_KWT', 'Country Code_LAC', 'Country Code_LAO', 'Country Code_LBN', 'Country Code_LBR', 'Country Code_LBY', 'Country Code_LCA', 'Country Code_LCN'
 ,'Country Code_LDC', 'Country Code_LIC', 'Country Code_LIE', 'Country Code_LKA', 'Country Code_LMC', 'Country Code_LMY', 'Country Code_LSO', 'Country Code_LTE', 'Country Code_LTU'
 ,'Country Code_LUX', 'Country Code_LVA', 'Country Code_MAC', 'Country Code_MAR', 'Country Code_MCO', 'Country Code_MDA', 'Country Code_MDG', 'Country Code_MDV', 'Country Code_MEA'
 ,'Country Code_MEX', 'Country Code_MHL', 'Country Code_MIC', 'Country Code_MKD', 'Country Code_MLI', 'Country Code_MLT', 'Country Code_MMR', 'Country Code_MNA', 'Country Code_MNE'
 ,'Country Code_MNG', 'Country Code_MOZ', 'Country Code_MRT', 'Country Code_MUS', 'Country Code_MWI', 'Country Code_MYS', 'Country Code_NAC', 'Country Code_NAM', 'Country Code_NCL'
 ,'Country Code_NER', 'Country Code_NGA', 'Country Code_NIC', 'Country Code_NLD', 'Country Code_NOR', 'Country Code_NPL', 'Country Code_NRU', 'Country Code_NZL', 'Country Code_OED'
 ,'Country Code_OMN', 'Country Code_OSS', 'Country Code_PAK', 'Country Code_PAN', 'Country Code_PER', 'Country Code_PHL', 'Country Code_PLW', 'Country Code_PNG', 'Country Code_POL'
 ,'Country Code_PRE', 'Country Code_PRI', 'Country Code_PRK', 'Country Code_PRT', 'Country Code_PRY', 'Country Code_PSE', 'Country Code_PSS', 'Country Code_PST', 'Country Code_PYF'
 ,'Country Code_QAT', 'Country Code_ROU', 'Country Code_RUS', 'Country Code_RWA', 'Country Code_SAS', 'Country Code_SAU', 'Country Code_SDN', 'Country Code_SEN', 'Country Code_SGP'
 ,'Country Code_SLB', 'Country Code_SLE', 'Country Code_SLV', 'Country Code_SMR', 'Country Code_SOM', 'Country Code_SRB', 'Country Code_SSA', 'Country Code_SSD', 'Country Code_SSF'
 ,'Country Code_SST', 'Country Code_STP', 'Country Code_SUR', 'Country Code_SVK', 'Country Code_SVN', 'Country Code_SWE', 'Country Code_SWZ', 'Country Code_SYC', 'Country Code_SYR'
 ,'Country Code_TCD', 'Country Code_TEA', 'Country Code_TEC', 'Country Code_TGO', 'Country Code_THA', 'Country Code_TJK', 'Country Code_TKM', 'Country Code_TLA', 'Country Code_TLS'
 ,'Country Code_TMN', 'Country Code_TON', 'Country Code_TSA', 'Country Code_TSS', 'Country Code_TTO', 'Country Code_TUN', 'Country Code_TUR', 'Country Code_TUV', 'Country Code_TZA'
 ,'Country Code_UGA', 'Country Code_UKR', 'Country Code_UMC', 'Country Code_URY', 'Country Code_USA', 'Country Code_UZB', 'Country Code_VCT', 'Country Code_VEN', 'Country Code_VNM'
 ,'Country Code_VUT', 'Country Code_WLD', 'Country Code_WSM', 'Country Code_XKX', 'Country Code_YEM', 'Country Code_ZAF', 'Country Code_ZMB', 'Country Code_ZWE'
 ,'High-technology exports (% of manufactured exports)'
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
