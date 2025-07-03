# ehr_interoperability_hospital_analysis


--- 

**Objective**: Analyze the relationship between Electronic Health Record (EHR) interoperability adoption and hospital performance metrics to determine if hospitals with better EHR compliance demonstrate superior quality outcomes.

---

## Dataset 1: 🏥 Hospital General Information
***(hospital_general_info.csv)***


## 📘 Data Dictionary

| Column Name                         | Description                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| `facility_id`                       | CMS Certification Number (CCN) uniquely identifying the hospital or facility.              |
| `facility_name`                     | Official name of the hospital or healthcare facility.                                      |
| `city_town`                         | City or town where the hospital is located.                                                |
| `state`                             | Two-letter state abbreviation where the hospital is located.                               |
| `zip_code`                          | 5-digit ZIP code of the hospital’s address.                                                |
| `county_parish`                     | County or parish where the hospital is located.                                            |
| `hospital_type`                     | Category of hospital (e.g., Acute Care, Critical Access, Psychiatric).                     |
| `hospital_ownership`                | Entity that owns the hospital (e.g., Government - Federal, Proprietary, Voluntary Non-Profit). |
| `emergency_services`                | Indicates whether the hospital provides emergency department services (`Yes`/`No`).        |
| `hospital_overall_rating`           | Overall hospital quality star rating (1 to 5 stars) as assessed by CMS.                    |
| `count_of_mort_measures_better`     | Number of mortality measures where the hospital performed better than the national average.|
| `count_of_safety_measures_better`   | Count of safety measures where performance was better than the national average.           |
| `count_of_readm_measures_better`    | Count of readmission measures where the hospital performed better than the national average.|
| `count_of_readm_measures_better`    | Count of readmission measures where the hospital performed better than the national average.|
| 'total_improved_measures'           | sum of count_of_mort_measures_better', 'count_of_safety_measures_better', 'count_of_readm_measures_better.|

### 📊 Data Summary

This dataset contains a comprehensive list of hospitals registered with Medicare. It includes facility details such as name, address, phone number, hospital type, ownership, emergency service availability, and overall CMS quality ratings. The data provides a foundational view of hospital characteristics and performance across the U.S.

- **Data Types**: Mix of categorical (hospital type, ownership, state) and numerical (ratings, performance counts, dates)
- **Missing Data**: Several columns contain a high volume of missing values. However, many of these are labeled as "Not Available" and have been consistently standardized during cleaning. Others are considered non-essential for analysis and have been removed to streamline the dataset.
+ **Total Rows:** 5384
+ **Total Columns:** 38

  
### 🌐 Data Source
Hospital General Information - Centers for Medicare & Medicaid Services (CMS) :

[https://data.cms.gov/provider-data/dataset/xubh-q36u](https://data.cms.gov/provider-data/dataset/xubh-q36u)


___


## Dataset 2: 🔗 Promoting Interoperability - Hospital
***(hospital_interoperability_data.csv)***


## 📘 Data Dictionary

| Column Name                                                   | Description                                                                                           |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `facility_id`                                                 | Unique CMS Certification Number (CCN) identifying the hospital or facility.                           |
| `facility_name`                                               | Official name of the hospital or healthcare facility.                                                 |
| `city_town`                                                   | City or town where the facility is located.                                                           |
| `state`                                                       | Two-letter abbreviation of the state where the facility operates.                                     |
| `zip_code`                                                    | ZIP code for the facility’s address.                                                                  |
| `county_parish`                                               | County or parish in which the facility is located.                                                    |
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
