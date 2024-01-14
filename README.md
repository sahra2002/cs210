# Sabancı University Email Analysis Project 📧
## About the Project 🚀

The Sabancı University Email Analysis Project is a comprehensive exploration of personal email communication patterns. This initiative seeks to gain insights into various aspects of email interactions.
## Motivation 💡

The motivation behind this project stems from the curiosity about daily email communication patterns. The desire to understand key aspects such as the most frequent communication partners, commonly used keywords, and the sentiment of emails—whether they are positive, negative, or neutral—prompted the initiation of this analysis.

## Data Source 🗃️

The data for this project was obtained through Google Takeout, allowing the import of email content in mbox format. To facilitate the usability of the mbox data, a custom Python script was developed. This script efficiently converts mbox-formatted data into a more user-friendly JSON format. The script addresses the intricacies of the mbox structure, extracting relevant information such as subject, from, to, date, and content fields for each email, and organizes it into a structured JSON representation.


## Data Analysis Techniques 📊

The data analysis involved several stages, starting with a comprehensive exploration of the data to identify any missing values or formatting issues. Various exploratory data analysis (EDA) techniques were applied, and different graphs were created to visualize patterns and trends. For instance, a graph illustrating email traffic over time was generated to provide a broader understanding of general data analysis trends.

## Findings 🕵️‍♂️

The analysis revealed several insightful findings about email communication habits:

- During certain periods, such as exam periods or assignments, the number of sent and received emails increased significantly.
- Emails from official Sabancı University accounts were predominant in the received emails, while teaching assistants emerged as the primary recipients of sent emails.
- The majority of emails were short in length.
- Sentiment analysis indicated that the vast majority of received emails were either neutral or positive, with a minimal number of negative emails.

## Limitations and Future Work 🚧

**Limitations:**
- The analysis is based on a sample of the first 200 emails, which may not represent the entirety of the email dataset.
- The data may be subject to bias, as the focus is on a specific time frame.
- The sentiment analysis, while informative, has inherent limitations in accurately capturing nuanced emotions.

**Future Work:**
- Expand the analysis to include a larger sample size for more comprehensive insights.
- Address biases by considering a more extended timeframe for a holistic view of email communication patterns.
- Explore advanced natural language processing (NLP) techniques to enhance sentiment analysis accuracy.
- Implement machine learning models for predictive analysis of email trends and behaviors.

This project provides valuable insights into personal email communication habits, and future iterations aim to address limitations and enhance the depth of analysis.
