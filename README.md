# Housing and Labor Market Project

This project analyzes the relationship between employment growth and housing price growth across U.S. metropolitan areas.

## Research Question
Do changes in local labor market conditions predict housing price appreciation?

## Data Sources
- FHFA House Price Index (metro-level)
- FRED Total Nonfarm Employment (PAYEMS)

The FHFA data is converted into a quarterly panel dataset for U.S. CBSAs from 1975 onward.

## Methodology
1. Construct a metro-level panel dataset
2. Compute log growth rates:
   - Δlog(HPI)
   - Δlog(Employment)
3. Estimate the following model using OLS with heteroskedasticity-robust standard errors:

Δlog(HPI) = α + β Δlog(Employment) + ε

## Main Finding
Employment growth has a positive and statistically significant effect on housing price growth.

## Repository Structure
- `code/` : data cleaning, panel construction, regression, and plotting
- `output/` : regression results and figures

Yifu Yang  
University of California, Berkeley  
Economics & Data Science
