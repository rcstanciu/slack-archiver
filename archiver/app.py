import os

from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


def main():
    print("Starting app...")
    app.start(port=3000)


# Start your app
if __name__ == "__main__":
    main()
