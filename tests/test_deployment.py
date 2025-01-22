from ChatBot_Studio.core.deployment import deploy_bot

def test_deploy_bot():
    platform = "Telegram"
    credentials = {"api_key": "mock_api_key"}
    bot = "mock_bot"

    status = deploy_bot(platform, credentials, bot)
    assert status == "Deployment successful"