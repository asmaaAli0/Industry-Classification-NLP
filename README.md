# Industry-Classification-NLP
You can think of the job industry as the category or general field in which you work. On a job application, "industry" refers to a broad category under which a number of job titles can fall. For example, sales is an industry; job titles under this category can include sales associate, sales manager, manufacturing sales rep, pharmaceutical sales and so on.

# Solution  :star_struck:	
The problem is supervised text classification problem, and our goal is to investigate which 
supervised machine learning methods are best suited to solve it. Given a new job title that comes in, 
we want to assign it to one of 4 industry categories.
The classifier makes the assumption that each new complaint is assigned to one and only one 
category. This is multi-class text classification problem.

# DataSet 
https://drive.google.com/file/d/1W_MO19MlDDUn0qCfxEaVxGKKlKHsFFly/view

# DataSet Details 
You are given a dataset that has two variables (Job title & Industry) in a csv format of more than 8,500 samples. This dataset is imbalanced (Imbalance means that the number of data points available for different classes is different) as follows: IT 4746 Marketing 2031 Education 1435 Accountancy 374

# Cleaning the data and preparing for model.

- Firstly, I noticed that there are a lot of duplicates in the data instances (job titles). The unique job titles in data were 3000+ while the entire data was 8000+.
- ## Text preprocessing techniques 

1. removing stop words (by adding some to default library and exclude “it”) 2- neglect words less than 2 letters 
2. remove text noise 
3. remove words that has digits in it 
4. lemmatization and stemming
5. convert all to lowercase letters

# Dealing with Data Imbalance
## tried several approaches  :exploding_head:	
1. Over Sampling
2. SMOTE
3. Weighted cost 
4. Tried different evaluation metrics
And finally I choose to combine oversampling with weighted cost :ok_hand:	

# Flask API
### I used Flask API to create a RESTful API for my model. The Model is not recompiled or trained each request, it just predicts upon the given data in request.

**Flask** is a web framework for Python, meaning that it provides functionality for building web applications, including managing HTTP requests and rendering templates. 





