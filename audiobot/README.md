# Hyperbolic Labs Chatbot
This repository contains a simple automated chatbot built using the [Hyperbolic Labs API](https://app.hyperbolic.xyz). The chatbot asks 100 unique, pre-defined questions and retrieves answers from the API, simulating a conversational AI experience. It’s a fun demonstration of how to integrate Hyperbolic Labs' AI models into a Python application.

## About Hyperbolic
[Hyperbolic Labs](https://hyperbolic.xyz) provides an accessible and affordable platform for AI development, offering open-access AI models and scalable computing resources via their API.
* Check out their [official documentation](https://docs.hyperbolic.xyz) for more details.

## Features
- Contains a list of 100 unique  on diverse topics.
- Randomly selects and asks audio questions without repetition.
- Integrates with the Hyperbolic Labs API to fetch answers.
- Adds random delays (1-2 minutes) between questions to simulate natural pacing.
- Built with Python and the `requests` library.

## Prerequisites
- Python 3.6+
- A [Hyperbolic API key](https://app.hyperbolic.xyz/settings) (replace the placeholder in the code with your own key)

## Setup
1. **Install Packages**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install git screen python3 python3-pip python3-venv -y
   ```
2. **Clone the Repository**
   ```bash
   git clone https://github.com/Hasanmallick07/audiobot.git
   cd audiobot
   ```
3. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install requests
   ```
4. **Configure the API Key**

Replace the `YOUR_API_KEY_HERE` in `audiobot.py` with your own [Hyperbolic API Key](https://app.hyperbolic.xyz/settings):
   ```bash
nano audiobot.py
   ```
5. **Run the Chatbot**

Execute the script to start the chatbot:
   ```bash
   python3 audiobot.py
   ```
* You can enter `screen -S audio` before running it to run the script on a minimizable screen in background.
* To minimize screen: `CTRL+A+D`
* To kill screen: `Ctrl+C` or command: `screen -XS audio quit`

## Usage
Once running, the chatbot will:
* Print each of the 100 audio questions one by one.
* Fetch and display answers from the Hyperbolic Labs API.
* Pause for a random interval (60-120 seconds) between audio questions.
* Stop after completing all 100 audio questions.

Example output:
```
Fetching audio 6 with text: Did you know that Los Angeles is home to some of t...
Audio 6 generated successfully.
Audio saved as output_audio_6.mp3
Pausing for 65 seconds...
```

## Notes
* The API key in the code is a placeholder. You’ll need to sign up at [Hyperbolic Labs](https://app.hyperbolic.xyz/) to get your own.
* Be mindful of API usage limits and costs depending on your Hyperbolic Labs plan.
* Feel free to modify the `questions` list in `audiobot.py` to suit your interests!
