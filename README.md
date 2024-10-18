# Renting Research Bot

## Overview
The **Renting Research Bot** is a Python automation tool designed to streamline the process of collecting rental property data from [Housing.com](https://housing.com). It scrapes details such as property location, price, and links, and automatically fills a Google Form with the gathered data. Built using Selenium for automation and BeautifulSoup for web scraping, this bot offers an efficient solution for real estate research, enabling users to quickly collect and manage rental property information.

## Problem Statement
Finding rental properties in a bustling city like **Jaipur** can be overwhelming due to the sheer volume of listings and the time-consuming process of gathering information. The **Renting Research Bot** aims to simplify this task by automating the data collection process, allowing users to quickly find suitable rental options without the hassle of manual searches.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Data Files](#data-files)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Automated Web Scraping**: Uses BeautifulSoup to extract property details such as location, price, and links from Housing.com.
- **Form Automation**: Employs Selenium to fill out and submit a Google Form with the collected data.
- **Scalable and Extendable**: Easily customizable to work with other real estate websites and data fields.

## Requirements
- Python 3.x
- Google Chrome installed
- ChromeDriver (Ensure the version matches your installed Google Chrome)
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-github-username>/renting-research-bot.git
   cd renting-research-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up ChromeDriver**:
   - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Make sure the version matches your installed Google Chrome.
   - Add ChromeDriver to your system PATH or specify its location in the script.

## Usage

1. **Configure the script**:
   - Update the `url` variable with the desired Housing.com search URL.
   - Update the `form_url` with the target Google Form URL.

2. **Run the script**:
   ```bash
   python renting_research_bot.py
   ```

3. **Output**:
   - The bot will scrape data from Housing.com and fill out the specified Google Form automatically.

## Customization

- **Adding More Fields**:
   Modify the BeautifulSoup selectors to scrape additional details from the Housing.com page if needed.
   
- **Changing the Form Structure**:
   If the Google Form layout changes, update the XPath expressions in the Selenium section of the script to match the new form structure.

## Data Files
This repository includes:
- **Excel File**: `Renting_Research_Data.xlsx` - Contains the collected rental data from the Google Form.
- **Screenshot**: `form_screenshot.png` - A screenshot of the Google Form used for data collection.

## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or support, please contact [Aditya Agarwal](mailto:aditya.agarwal1066@gmail.com).
