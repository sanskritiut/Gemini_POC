# GeminiPOC

Gemini LLM Quickstart
This is a simple Python proof-of-concept (POC) that demonstrates how to authenticate with the Gemini API using environment variables and make synchronous calls to a LLM model (gemini-2.0-flash)

Features
Secure API Key Loading: Loads the GOOGLE_API_KEY from a .env file using the python-dotenv library.

Simple Function Call: Executes a synchronous API call to the OpenAI Chat Completion endpoint.

Two-Model Example: Demonstrates chaining two prompts using different models for different tasks:


An IQ question generation (gemini-2.0-flash).

Setup and Installation
Follow these steps to set up the project locally.

1. Clone the Repositori

git clone https://github.com/sanskritiut/agenticAI.git
cd agenticAI

2. Create a Virtual Environment 

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install the required Python packages:
pip install openai python-dotenv

4. Configure Environment Variables
Create a file named .env in the root directory of your project and paste your Google API key into it:
.env

# Replace GOOGLE_API_KEY with your actual key
GOOGLE_API_KEY="YOUR_GOOGLE_API__KEY_HERE"

▶️ How to Run the Code
Execute the main Python script:

python3 main.py

Expected Output
The script will first confirm your API key status and then print the result of the two chained LLM calls:

OpenAI API Key exists
45600
In a system where 'N' represents the number of unique prime factors of an integer 'x', and 'P' represents the set of all divisors of 'x', determine the maximum number of consecutive composite integers that can be generated if the only constraint on 'x' is that 2^N must equal the cardinality of P (i.e., |P|).

