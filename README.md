# University Progression Outcome Predictor

## Overview

The University Progression Outcome Predictor is a Python-based application designed to evaluate the progression status of university students at the end of each academic year. Analyzing student credit data determines whether a student can progress to the next academic year, must repeat certain modules, or faces exclusion based on their academic performance.

## Description

This application helps university administrators efficiently process student results using a structured method of input and calculation. It categorizes student outcomes into four primary statuses:

- **Progress**: The student advances to the next academic year.
- **Progress (module trailer)**: The student progresses but needs to retake specific modules.
- **Do not Progress – module retriever**: The student must repeat some modules before advancing.
- **Exclude**: The student is excluded due to poor academic performance.

## Key Features

1. **Interactive User Input**: The program provides a user-friendly interface for entering student credit data, ensuring inputs are valid and total credits sum to 120.

2. **Multiple Student Processing**: Users can input data for multiple students in one session, facilitating efficient handling of large datasets.

3. **Data Validation**: Ensures accuracy by validating all inputs and providing feedback and error messages for corrections.

4. **Graphical Representation**: Generates a histogram using the "graphics.py" module, offering a visual summary of student outcomes for easy interpretation.

5. **Data Storage and Retrieval**: Maintains records in a list and exports results to a text file for documentation and further analysis.

## Project Structure

Here's how the project is organized:
- **UniversityProgressionOutcomePredictor.py**: The main script containing the logic for processing student progression outcomes.
- **graphics.py**: A module responsible for generating visual representations, such as histograms, to display progression results.

## How to Run

**Clone the Repository**: 
   ```bash
   git clone https://github.com/sakith71/UniversityProgressionOutcomePredictor.git
   cd UniversityProgressionOutcomePredictor
   ```
<hr><br>
This "README.md" file provides a comprehensive guide to your project, from installation and usage to contributing and licensing. Adjust the placeholders with specific details related to your project, such as the GitHub repository URL and any special acknowledgements. Let me know if you need further customization or additional sections!
