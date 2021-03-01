from os import environ

from handlers.message import message_handler
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=environ.get("SLACK_BOT_TOKEN"),
    signing_secret=environ.get("SLACK_SIGNING_SECRET"),
)


@app.message("")
def message(message, say):
    message_handler(message, say)


def main():
    print("Starting app...")
    app.start(port=3000)


# Start your app
if __name__ == "__main__":
    main()
