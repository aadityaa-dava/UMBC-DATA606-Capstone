
## 1. Title and Author

- Project Title -  **Analysis of Consumer Complaint Root Causes Using Large Language Models**
- Author - Aadityaa Dava
- Semester - Spring'26
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Link to the author's GitHub repo of the project: https://github.com/aadityaa-dava/UMBC-DATA606-Capstone
- Link to the author's LinkedIn profile: www.linkedin.com/in/aadityaa-dava-688908308
    
## 2. Background

Provide the background information about the chosen topic. 

- **What is it about?**

Each year financial institutions get a lot of customer complaints. These usually are a representation of actual issues by the customers, including billing mistakes, poor credit reporting, slow customer service or slow response. Although the complaints are addressed one at a time, it is hard to see the bigger picture when considering complaints one at a time and it is hard to see how the recurring issues or patterns in the system.

This project aims at studying the customer complaint stories in establishing the causal factors that led to customer dissatisfaction. The project analyses the actual text used by the consumers instead of simple dependence on preset categories like product type or labels of issues to understand what went wrong and why.

This project is based on the complaint data provided by the Consumer Financial Protection Bureau (CFPB), which has been filtered to cover the state of Washington between 2016 and 2026 and uses modern text analysis methods to cluster similar issues and determine typical underlying causes. The aim is to transform unstructured texts of complaints to insights that may be analyzed using visualizations and an interactive application.

- **Why does it matter?**

Direct feedback on consumers provided by customers is referred to as customer complaints, which is not sufficiently used. Most times, organizations pay attention to individual case closures without even knowing to the fullest, whether the cases are recurring. Consequently, systemic issues might end up years in duration term without their correct resolution.

This is a relevant project since it assists in shifting toward reactive complaint management to initiation of proactive insights. Through the determination of root causes that have been recurring in thousands of complaints, organizations can focus on the improvements that can have the most significant impact on customer experience. To illustrate, when there are a number of complaints claiming similarities in billing or reporting, this is the indication that changes in processes or systems need to take place instead of the individual fixes.

On the data science side, this project also shows how text data on a large-scale level can be analyzed in a systematic manner. It demonstrates how unstructured data which is usually deemed hard to manipulate can be converted into enactable information that can be used to make decisions.

**What are your research questions?**

1. What are the leading underlying root causes of customer complaints in Washington state?
    
2. What are the root causes of complaints in the various financial product lines (credit reporting, loans and banking services)?

3. Has the patterns of customer complaint themes and root causes changed over years since 2016 to 2026?
	
4. How far can complaint stories be clustered into consistent and meaningful root-cause categories on the basis of their contents?
	
5. What can be the best way of presenting insights made by complaint analysis in the form of visualization and interactive tools?

## 3. Data 

**Data sources**

- The dataset is obtained from **Consumer Complaint Database** maintained by the Consumer Financial Protection Bureau(CFPB). This dataset contains complaints from the customers against financial institutions in Washington(WA).
- https://www.consumerfinance.gov/data-research/consumer-complaints/#get-the-data

**Data size**
- 85.6 MB (combined CSV files)

**Data shape**
- Number of rows: 110,879
- Number of columns: 18

**Time period:** 
- 02/02/2016 - 02/02/2026
 
**What does each row represent?**
- Each row in the dataset represents **one individual consumer complaint**
 
**Data dictionary**

| Column Name | Data Type | Definition | Potential Values |
|------------|----------|------------|------------------|
| Date received | Date | Date the complaint was received by the CFPB | YYYY-MM-DD |
| Product | Categorical | Financial product involved in the complaint | Credit reporting, Mortgage, Student loan, Bank account, etc. |
| Sub-product | Categorical | More specific category of the financial product | Varies by product |
| Issue | Categorical | Primary issue reported by the consumer | Billing disputes, Incorrect information, Payment issues |
| Sub-issue | Categorical | More detailed description of the issue | Varies |
| Consumer complaint narrative | Text | Free-text description of the complaint submitted by the consumer | Unstructured text |
| Company | Categorical | Name of the company named in the complaint | Financial institution names |
| State | Categorical | State where the consumer resides | WA |
| ZIP code | Categorical | Partial ZIP code of the consumer | 981XX, 983XX |
| Submitted via | Categorical | Channel through which the complaint was submitted | Web, Phone |
| Company response to consumer | Categorical | Outcome of the company’s response | Closed, In progress |
| Timely response? | Categorical | Indicates whether the company responded on time | Yes, No |
| Consumer disputed? | Categorical | Indicates whether the consumer disputed the company’s response | Yes, No |
| Complaint ID | Numeric | Unique identifier for each complaint | Integer |

**Which variable/column will be your target/label in your ML model?**
- This project does not have any target variable provided in the dataset, the target variable is derived during the analysis.
- **Complaint root cause** will be the target variable for the modeling.
  
**Which variables/columns may be selected as features/predictors for your ML models?**
- The primary column used will be **Consumer complaint narrative**.
- **Supporting features:** Product, Sun-Product, Issue, Company and Date received.
