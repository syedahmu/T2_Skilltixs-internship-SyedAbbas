# T2_Skilltixs-internship-SyedAbbas
🧹 Data Cleaning & 🧠 Exploratory Data Analysis (EDA)
This project refines and analyzes a supermarket sales dataset using Python, showcasing best practices in data preparation, visualization, and insight generation with Pandas, Matplotlib, and Seaborn.

🚀 1. Data Cleaning & Preparation
Performed in clean_data.py:

Load dataset: Imported supermarket_sales.csv into a Pandas DataFrame.

Missing values: Checked for nulls (df.isnull().sum()). Although none were found, handling strategies like mean/median/mode imputation are outlined {CITATION_START}cite{CITATION_DELIMITER}turn0search1{CITATION_DELIMITER}turn0search3{CITATION_STOP}.

Duplicates: Removed duplicate entries (df.drop_duplicates()) to ensure data integrity {CITATION_START}cite{CITATION_DELIMITER}turn0search3{CITATION_DELIMITER}turn0search1{CITATION_STOP}.

Text standardization: Cleaned categorical fields—gender (to ‘M’/‘F’), trimmed and capitalized customer_type, product_line, payment {CITATION_START}cite{CITATION_DELIMITER}turn0search3{CITATION_DELIMITER}turn0search13{CITATION_STOP}.

Datetime handling: Converted Date and Time into datetime objects and combined into a DateTime column for seamless analysis {CITATION_START}cite{CITATION_DELIMITER}turn0search1{CITATION_DELIMITER}turn0search21{CITATION_STOP}.

Rename columns: Renamed verbose headers to clean snake_case (e.g., Invoice ID → invoice_id, Tax 5% → tax_5pc) for readability.

Data type enforcement: Ensured numeric fields were numeric and categorical fields were strings.

Export: Saved cleaned data as supermarket_sales_cleaned.csv for downstream analysis.

📊 2. Exploratory Data Analysis
Performed in eda_analysis.py:

Initial Exploration

Used .info() and .describe() to inspect data structure and summary statistics.

Checked value counts of categorical features to assess distribution.

Missing Data Check

Heatmap visualization confirmed no missing values post-cleaning {CITATION_START}cite{CITATION_DELIMITER}turn0search24{CITATION_STOP}.

Distribution Analysis

Numerical features: plotted histograms (with KDE) and boxplots to examine shape and outliers.

Categorical features: bar plots to understand category frequencies.

Analyzed total sales across product_line categories.

Correlation Analysis

Correlation heatmap highlighted relationships among numerical variables.

Scatterplot of total vs gross_income confirmed positive correlation.

Aggregation & Group Analysis

Calculated summary statistics (sum, mean, count, std) of total by product_line, payment, and gender, with barplots.

Extracted month & day_of_week for time-based trend analysis.

Outlier & Skewness Handling

Calculated skewness for numeric features.

Applied log-transformations to skewed features (quantity, gross_income, tax_5pc) to improve normality.

Combined boxplots offered a view of outliers across all numeric fields.

Bonus - Time of Day Trends

Extracted hour from time and plotted hourly sales to uncover peak shopping times.



