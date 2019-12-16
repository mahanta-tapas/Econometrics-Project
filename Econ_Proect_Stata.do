clear
use "Z:\Group_proj\income_category.dta"
keep if year == 2006 | year == 2014
gen lpatent_nresid = log(patentapplicationsnonresidents)
gen year14 = cond(year==2014, 1, 0)
xtset code year, delta(8)
xtreg lpatent_nresid year14 internet_users, fe robust

clear
use "Z:\Group_proj\income_category.dta"
keep if year == 2006 | year == 2014
gen lpatent_resid = log(patent_applications_residents)
gen year14 = cond(year==2014, 1, 0)
xtset code year, delta(8)
xtreg lpatent_resid year14 internet_users, fe robust

clear
use "Z:\Group_proj\income_category.dta"
keep if year == 2006 | year == 2014
gen patent_total = patentapplicationsnonresidents + patent_applications_residents
gen lpatent_total = log(patent_total)
gen year14 = cond(year==2014, 1, 0)
xtset code year, delta(8)
xtreg lpatent_total year14 internet_users, fe robust


use "Z:\Group_proj\income_category.dta"
keep if year == 2006 | year == 2014
gen science = scientific_and_technical_journal + trademark_applications_total + patent_total
gen lsci = log(science)
gen year14 = cond(year==2014, 1, 0)
xtset code year, delta(8)
xtreg lsci year14 internet_users, fe robust

clear
use "Z:\Group_proj\income_category.dta"
keep if year == 2006 | year == 2014
gen ltrade_resid = log(trademarkapplicationsdirectresid)
gen year14 = cond(year==2014, 1, 0)
xtset code year, delta(8)
xtreg ltrade_resid year14 internet_users, fe robust

clear
use "Z:\Group_proj\income_category.dta"
keep if year == 2006 | year == 2014
gen ltrade_nresid = log(trademarkapplicationsdirectnonre)
gen year14 = cond(year==2014, 1, 0)
xtset code year, delta(8)
xtreg ltrade_nresid year14 internet_users, fe robust

clear
use "Z:\Group_proj\income_category.dta"
keep if year == 2006 | year == 2014
gen ltrade_total = log(trademark_applications_total)
gen year14 = cond(year==2014, 1, 0)
xtset code year, delta(8)
xtreg ltrade_total year14 internet_users, fe robust

use "Z:\Group_proj\group_project_data_v3.dta"
keep if year == 2006 | year == 2015
gen ltrade_nresid = log(trademarkapplicationsdirectnonre)
gen year06 = cond(year==2006, 1, 0)
xtset code year, delta(9)
xtreg ltrade_nresid year06 internet_users, fe robust

use "Z:\Group_proj\group_project_data_v3.dta"
keep if year == 2006 | year == 2015
gen ltrade_resid = log(trademarkapplicationsdirectresid)
gen year15 = cond(year==2015, 1, 0)
xtset code year, delta(9)
xtreg ltrade_resid year15 internet_users, fe robust


*Regrssion of scientific_and_technical_journal on internet users
use "Z:\Group_proj\group_project_data_v3.dta"
keep if year == 2007 | year == 2017
gen lstj = log(scientific_and_technical_journal)
gen year07 = cond(year==2007, 1, 0)
xtset code year, delta(10)
xtreg lstj year07 internet_users, fe robust

*Regrssion of patent applications residents on internet users (without log)
*Using income groups - high income/middle income/lower middle, etc*
use "Z:\Group_proj\Anushka_Econ.dta"
keep if year == 2006 | year == 2015
gen year06 = cond(year==2006, 1, 0)
xtset code year, delta(9)
xtreg patent_applications_residents year06 internet_users, fe robusts

*Regrssion of scientific and technical journals on internet users (without log)
*Using income groups - high income/middle income/lower middle, etc*
use "Z:\Group_proj\Anushka_Econ.dta"
keep if year == 2006 | year == 2015
gen year06 = cond(year==2006, 1, 0)
xtset code year, delta(9)
xtreg scientific_and_technical_journal internet_users, fe robusts

*Regrssion of patent applications non residents on internet users (without log)
*Using income groups - high income/middle income/lower middle, etc*
use "Z:\Group_proj\Anushka_Econ.dta"
keep if year == 2006 | year == 2015
gen year06 = cond(year==2006, 1, 0)
xtset code year, delta(9)
xtreg patentapplicationsnonresidents internet_users, fe robusts