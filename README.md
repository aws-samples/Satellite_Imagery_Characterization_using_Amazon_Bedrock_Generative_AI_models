## Satellite Imagery Characterization using Amazon Bedrock workshop
Amazon Bedrock is a fully managed service that provides access to FMs from third-party providers and Amazon; available via an API. With Bedrock, you can choose from a variety of models to find the one that’s best suited for your use case.This Python application allows you to characterize satellite imagery using the Anthropic Claude model on Amazon Bedrock Runtime.

## Steps to run the Satellite Imagery Characterization application
1. Set up your Python development environment
2. Install streamlit :  https://docs.streamlit.io/get-started/installation
3. Clone this Github repo 
4. Run the bedrock python application with ```streamlit run Satellite_Imagery_Characterization_assistant.py``` command
5. Here is a sample Satellite Imagery from noaa.gov to test the application : ``` https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/GEOCOLOR/1800x1080.jpg ```

![Screenshot 2024-08-03 at 3 02 32 PM](https://github.com/user-attachments/assets/8c2aa26c-f21e-4df2-9dbb-5cceb4982165)

Image Reference: https://www.nhc.noaa.gov/satellite.php

6. Here is the sample output from the Satellite_Imagery_Characterization_assistant app:
![Screenshot 2024-08-03 at 3 00 17 PM](https://github.com/user-attachments/assets/a433baff-5d1c-4385-8ee5-f7a51f83e4fb)

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

