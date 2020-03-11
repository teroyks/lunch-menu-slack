# Slack Configuration

TL;DW (too long; didn’t write) version:

[Create an app](https://api.slack.com/apps "Apps list") in your Slack workspace, and add an [incoming webhook](https://api.slack.com/messaging/webhooks "Instructions for sending messages using webhooks") to it.
You can add different webhooks for posting to different targets (ie. a QA webhook to post private messages only to yourself and a production webhook for posting to a public channel).

Create .env files for the environments you want (`.qa.env` and `.prod.env` are automatically ignored by the version control so your API URLs won’t be added to the repository) and add the webhook URLs to them as `SLACK_URL` (see `.env` for a template).
