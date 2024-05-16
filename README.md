# VoxMeteo Sahel: Harnessing Voice Technology for Timely Rain Data and Predictions to Support Agricultural Decision-Making in the Sahel
## Overview
METEO Service is a VoiceXML&Flask application that provides agricultural-related weather information and suggestions. 
## VoiceXML Prototype Access
| Number Type                       | Number                                      |
|-----------------------------------|---------------------------------------------|
| USA Toll Free PIN Access (Voice Only) | (800) 289-5570 then PIN: 9996145787     |
| USA Domestic PIN Access (Voice Only)  | (407) 386-2174 then PIN: 9996145787     |
| Skype VoIP                           | +990009369996145787                      |
| SIP VoIP                             | sip:9996145787@sip.voxeo.net            |

## Flask Server Running and Test Guide
### 1. Clone the repository

```sh
git clone https://github.com/yourusername/meteo-service.git
cd meteo-service
```
### 2. Create and activate a virtual environment
For windows: 
```
python -m venv venv
venv\Scripts\activate
```
For Unix or MacOS:
```
python -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run the application
```
python app.py
```
### 5. Run tests
```
python -m unittest discover -s tests
```
## Cloud Platform Implementation
Our VoiceXML is already implemented on https://evolution.voxeo.com/. To deploy the METEO Service to a cloud provider (e.g., AWS, Heroku, Azure), follow the provider's specific instructions for deploying a Flask application. Ensure that your deployment includes the following configurations:
1. Environment Variables: Set up any necessary environment variables.
2. Port Configuration: Make sure the application is configured to run on the appropriate port (e.g., 80 for HTTP, 443 for HTTPS).
3. Domain Configuration: Point your domain to the cloud service's IP address or use their domain management tools.
4. After updating the voice_local.xml file and deploying it, test the integration by accessing the Voxeo Evolution platform. 
