# Healthcare Interoperablity 

**Analyzing Hospital Compliance with EHR Modernization Standards and the Risks to Patient Privacy**

---

## 📘 Introduction 

This project takes a closer look at how EHR adoption has transformed healthcare by making patient records more accessible and improving compliance. But digital systems also raise concerns about privacy and security. By analyzing breach reports and hospital interoperability data, this study aims to reveal how modern healthcare must balance innovation with protecting sensitive information.

--- 

## 🔍 Objective
This analysis investigates the relationship between hospital compliance with EHR modernization efforts and the potential risk to patient privacy. Specifically, it asks whether hospitals that meet interoperability criteria are more or less likely to report data breaches involving protected health information.

--- 

<details>
  <summary>🏥 Dataset 1: Hospital General Information</summary>

**File:** ***(general.csv)***


## 📘 Data Dictionary

| Column Name                         | Description                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| `facility_id`                       | CMS Certification Number (CCN) uniquely identifying the hospital or facility.              |
| `facility_name`                     | Official name of the hospital or healthcare facility.                                      |
| `city_town`                         | City or town where the hospital is located.                                                |
| `state`                             | Two-letter state abbreviation where the hospital is located.                               |
| `zip_code`                          | 5-digit ZIP code of the hospital’s address.                                                |
| `hospital_type`                     | Category of hospital (e.g., Acute Care, Critical Access, Psychiatric).                     |
| `hospital_ownership`                | Entity that owns the hospital (e.g., Government - Federal, Proprietary, Voluntary Non-Profit). |
| `hospital_overall_rating`           | Overall hospital quality star rating (1 to 5 stars) as assessed by CMS.                    |
| `count_of_mort_measures_better`     | Number of mortality measures where the hospital performed better than the national average.|
| `count_of_safety_measures_better`   | Count of safety measures where performance was better than the national average.           |
| `count_of_readm_measures_better`    | Count of readmission measures where the hospital performed better than the national average.|
| `total_improved_measures`           | Sum of count_of_mort_measures_better, count_of_safety_measures_better, and count_of_readm_measures_better |


### 📊 Data Summary

This dataset contains a comprehensive list of hospitals registered with Medicare. It includes facility details such as name, address, phone number, hospital type, ownership, emergency service availability, and overall CMS quality ratings. The data provides a foundational view of hospital characteristics and performance across the U.S.

- **Data Types**: Mix of categorical (hospital type, ownership, state) and numerical (ratings, performance counts, dates)
- **Missing Data**: Several columns contain a high volume of missing values. However, many of these are labeled as "Not Available" and have been consistently standardized during cleaning. Others are considered non-essential for analysis and have been removed to streamline the dataset.
+ **Total Rows:** 5384
+ **Total Columns:** 38

  
### 🌐 Data Source
Hospital General Information - Centers for Medicare & Medicaid Services (CMS) :

[https://data.cms.gov/provider-data/dataset/xubh-q36u](https://data.cms.gov/provider-data/dataset/xubh-q36u)


</details>

--- 


<details>
  <summary>🔗 Dataset 2: Promoting Interoperability </summary>

**File:** ***(interoperability.csv)*** 



## 📘 Data Dictionary

| Column Name                                                   | Description                                                                                           |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `facility_id`                                                 | Unique CMS Certification Number (CCN) identifying the hospital or facility.                           |
| `facility_name`                                               | Official name of the hospital or healthcare facility.                                                 |
| `city_town`                                                   | City or town where the facility is located.                                                           |
| `state`                                                       | Two-letter abbreviation of the state where the facility operates.                                     |
| `zip_code`                                                    | ZIP code for the facility’s address.                                                                  |
| `meets_criteria_for_promoting_interoperability_of_ehrs`       | Indicates whether the facility meets CMS-defined criteria for promoting EHR interoperability (`Yes`/`No`). |
| `start_date`                                                  | Beginning date of the reporting period during which the facility was evaluated for interoperability criteria. |
| `end_date`                                                    | End date of the reporting period for the facility’s interoperability participation.                   |


### 📊 Data Summary

The Medicare Promoting Interoperability Program was created to encourage the use and exchange of electronic health information. This dataset reflects how hospitals are implementing certified Electronic Health Record (EHR) technology and includes performance measures that align with national quality standards. It provides insight into hospitals' engagement with digital health tools that support data sharing, patient care coordination, and overall interoperability.

- **Data Types**: Mix of categorical (hospital name, geographics) and numerical (dates)
- **Missing Data**: No missing values
+ **Total Rows:** 4593
+ **Total Columns:** 12


### 🌐 Data Source

Promoting Interoperability - Hospital - Centers for Medicare & Medicaid Services (CMS) :

[https://data.cms.gov/provider-data/dataset/f4ga-b9gx](https://data.cms.gov/provider-data/dataset/f4ga-b9gx)


</details>

--- 


<details>
  <summary>🛡️ Dataset 3: Healthcare Breach Report</summary>

**File:** ***(breach.csv)***


## 📘 Data Dictionary

| Column Name                        | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| `name_of_covered_entity`           | Name of the hospital, organization, or healthcare provider that reported the breach. |
| `state`                            | U.S. state where the breach occurred or where the entity is located.       |
| `covered_entity_type`              | Type of healthcare organization involved (e.g., Hospital, Clinic, Health Plan). |
| `individuals_affected`             | Estimated number of individuals whose data was compromised in the breach.  |
| `breach_submission_date`           | Date the breach was officially submitted or reported to HHS.               |
| `type_of_breach`                   | Classification of the breach (e.g., Hacking/IT Incident, Unauthorized Access). |
| `location_of_breached_information` | Describes what type of data was affected and where the information resided (e.g., EMR, paper records, network servers). |


### 📊 Data Summary

Dataset Summary This dataset includes hospital-reported breaches of unsecured protected health information, each affecting 500 or more individuals. In accordance with section 13402(e)(4) of the HITECH Act, these cases are published by the Department of Health and Human Services and represent organizations currently under investigation by the Office for Civil Rights.

- **Data Types**: Contains mostly categorical and qualitative variables, with one quantitative field.
- **Missing Data**: Small number of missing values mostly in the state column.
+ **Total Rows:** 7
+ **Total Columns:** 7019


### 🌐 Data Source

Breach Portal: Notice to the Secretary of HHS Breach of Unsecured Protected Health Information
U.S. Department of Health and Human Services - Office for Civil Rights

[https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf))


</details>

--- 





















