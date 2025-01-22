
# ChatBot Studio

ChatBot Studio is a versatile Python framework designed to simplify the process of designing, training, and deploying AI-powered chatbots. Whether you're a business, an NLP developer, or a chatbot enthusiast, ChatBot Studio provides all the tools you need to create robust conversational agents.

## Key Features

- **Prebuilt Conversational Flows:** Quickly build conversational flows with reusable templates for customer support, FAQs, and more.
- **Integration with Popular NLP Models:** Leverage Hugging Face Transformers and other popular NLP frameworks.
- **Multi-Platform Deployment:** Seamlessly deploy your chatbot to Telegram, Slack, WhatsApp, and other platforms.
- **Custom Dataset Training:** Easily train chatbots with your own datasets to suit specific use cases.
- **Extensive Documentation:** Clear and concise documentation with examples to help you get started quickly.

---

## Installation

Install ChatBot Studio via pip:

```bash
pip install ChatBot_Studio
```

---

## Quick Start

### 1. Creating a Conversational Flow

```python
from ChatBot_Studio.core.flow_builder import create_conversational_flow

steps = [
    {"question": "How can I assist you today?", "responses": ["Billing", "Technical Support"]},
    {"question": "Can you provide more details?", "responses": ["Yes", "No"]},
]

flow = create_conversational_flow("Customer Support", steps)
print(flow)
```

### 2. Integrating an NLP Model

```python
from ChatBot_Studio.core.model_integration import integrate_model

model = integrate_model("distilbert-base-uncased", task="text-classification")
print(model("I love this product!"))
```

### 3. Training the Bot

```python
from ChatBot_Studio.core.training import train_bot

trained_model = train_bot("path/to/dataset.json", "mock_model")
```

### 4. Deploying the Bot

```python
from ChatBot_Studio.core.deployment import deploy_bot

status = deploy_bot("Telegram", {"api_key": "your_api_key"}, "my_bot")
print(status)
```

---

## Directory Structure

```plaintext
ChatBot_Studio/
|-- __init__.py
|-- core/
    |-- __init__.py
    |-- flow_builder.py
    |-- model_integration.py
    |-- training.py
    |-- deployment.py
|-- examples/
    |-- customer_support_flow.py
|-- tests/
    |-- test_flow_builder.py
    |-- test_model_integration.py
    |-- test_training.py
    |-- test_deployment.py
setup.py
```

---

## Running Tests

Run the test suite to verify that everything is working as expected:

```bash
pytest tests/
```

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance ChatBot Studio.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Authors

Created by Gopalakrishnan Arjunan.
