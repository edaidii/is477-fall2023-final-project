# Reproduction of: Retiring Adult - New Datasets for Fair Machine Learning (IS477)

## Overview

### 
The purpose of this repository is to essentially validate and expand of the dataset, the UCI Adult that’s derived from 1994 Census survey, that’s being used to determine the ethicality or fairness of machine learning. Furthermore, the authors hope that the observations made will drive the need to utilize additional datasets to ensure that empirical observations are somewhat standardized and consistent with one another. The overall assignment requirement is to achieve a certain set of numbers of accuracy (85% overall, 91.4% for Black instances, and 92.7% for Female instances) through a simple logistic regression based on the UCI Adult dataset. The objectives and additional requirements within the overall assignment is to understand the impact that data and metadata have as well as addressing any quality issues. Furthermore, additional objectives include learning and understanding the ethics surrounding data and software usage, the importance of reproducibility and how to achieve it, and how to store data and workflows for long term usage. 

## Analysis

###
a.	Each dataset’s origin was obtained from the US Census; however, one was found from IPUMS Adult and the other was from ACS.
b.	For IPUMS Adult, the researcher should appropriately cite the data as well as register to access the data. Furthermore, there is no redistribution of the data without permission. For ACS, users also cannot redistribute the data, change the data, identify any respondent using the data, and in general, must remain compliant with the Census Bureau’s policies, agreements, laws, and will not infringe upon any third party’s IP.
c.	I will not include the data in my own repository as it’s stated that I cannot redistribute both datasets. Instead, I will include a link in a License and Terms of Use section where potential users can find the dataset from the original source: the website’s respective URL.


## Workflow

![Alt text](graph.png)

### 
a.	The data license that I would use is the Creative Commons CCZero which is the most open data license. I selected this choice because I don’t need to copyright my dataset nor profit off of it in any means. By choosing a public domain license, I look forward to more collaboration instead and it does not matter to me who uses the data so long as it’s not for malicious purposes

## Reproducing

###
In order to reproduce this script, here are the following steps:

1. Environment
    
ProductName:    macOS

ProductVersion: 12.2.1

BuildVersion:   21D62

Python 2.7.18

2. Setting up to run the script

    2a. First, clone this repository 

    2b. Then, create a virtual environment which you can do by going into the command line and selecting Python: Create Environment. After that, select .venv and choose the appropriate Python interpreter and you will know that this is successful for when you have a .venv folder. 


    Check if the correct directories and subsequent folders are set up - data, scripts, and results. Within data, check if the correct files are downloaded within the adult folder and the folktables folder. 

    Check and correct the relative paths in the scripts folder to see if the files in reproduce_adult and files in reproduce_reconstroncuted are copied to the right directories and subdirectories. 

    2c. Install dependencies in the virtual environment through pip install -r requirements.txt

    2d. Reference environment.log to check if there are any dependencies that you may have missed in case your code does not work. 

3. Run the script
Use the following scripts "prepare_data.py", "reproduce_adult", and "reproduce_reconstruction" and run it. 

4. Check the file uploads
There should be text files in the results folder labeled as "adult_reconstructed.txt", "income_threshold.pdf", and "uci_adult_results.txt" with the accuracies labeled. 

## Licenses

### Software License
a.	The license that I choose to use is the MIT license because it allows the widest adoption, fewest restrictions, and allows for open and easy collaboration and transparency amongst everyone who access the source code. Given that none of the software involved will require any additional permission, the MIT license is preferred. 

### Data License
a. The license for this dataset is Creative Commons Attribution 4.0 International which means that it's freely able to be used for any purpose with no restrictions on distribution or modification.

## Analysis

###
In order to document our results from trying to replicate the results from the UCI Adult database, here are our observations and insights compared to the original paper.

a. The regression results from the original database for the UCI Adult are as follows: 0.849, 0.92, and 0.929. This appears to be similar to our accuracies of: 0.847, 0.915, 0.925 which indicates that our results are consistent with the original papers.

b. The regression results from the reconstructed database for the UCI Adult with the default threshold are as follows: 0.853, 0.906, and 0.93. This appears to be almost consistent with the results from the original database, however, it worth nothing that the first metric appears to be deflated for the reconstructed database and elevated for the second and third metric when comparing the reconstructed database to the original one.

c. Referring back to Section 1 of the paper, the income threshold has an effect on prediction accuracy as variations in the threshold lead to different results because of different categorizations. This was seen with our results as illustrated in parts a and b.

## Citations

###
Bureau, US Census. “Terms of Service.” Census.Gov, 8 Oct. 2021, www.census.gov/data/developers/about/terms-of-service.html. 

Ding, F., Hardt, M., Miller, J., & Schmidt, L. (2022). Retiring Adult: New
Datasets for Fair Machine Learning. arXiv.
https://doi.org/10.48550/arXiv.2108.04884

Morin, A., Urban, J., & Sliz, P. (2012). A Quick Guide to Software Licensing for the Scientist-ProgrammerLinks to an external site.. PLOS Computational Biology, 8(7), e1002598.

Team, MPC UX/UI. “About IPUMS CPS.” IPUMS CPS, cps.ipums.org/cps/about.shtml. Accessed 10 Sept. 2023. 
