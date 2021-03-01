# slack-archiver
Slack bot for archiving channel messages and files, and make it possible to quickly search beyond the free limit of 10k messages.

## Development setup
1. Create a Slack App

    https://api.slack.com/apps/new
2. Create a `.env` file and fill in the Slack Signing Secret and OAuth Token

    `cp .env.example .env`
3. For local development, use `ngrok` to listen for incoming requests.

    `ngrok http 3000`

    You should have access now to a public facing URL, similar to `https://973b0acaf77c.ngrok.io` which will redirect all requests to `http://localhost:3000`.
4. Fill in the Slack App configuration page the **Request URL** under the **Event Subscriptions** menu, with your public facing URL provided by `ngrok`, and append **/slack/events**. Your final **Request URL** should become:

    **`https://973b0acaf77c.ngrok.io/slack/events`**
5. Spin up development containers using docker-compose

    `docker-compose up`
