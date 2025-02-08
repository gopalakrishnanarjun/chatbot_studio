from chatbot_studio.core.flow_builder import create_conversational_flow

if __name__ == "__main__":
    steps = [
        {"question": "How can I assist you today?", "responses": ["Billing", "Technical Support"]},
        {"question": "Can you provide more details?", "responses": ["Yes", "No"]},
    ]

    flow = create_conversational_flow("Customer Support", steps)
    print(flow)