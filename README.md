# Teams-CS-Notifier

This Cobalt Strike CNA (Cobalt Strike Aggressor) script allows you to get notified in Teams when a new beacon is established. The notification includes details such as the external IP, internal IP, hostname, and username of the machine that established the beacon.

## Usage

To use this script, you need to perform the following steps:

1. Update the `notify.py` script with your Teams webhook URL. You can follow this [guide](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-an-incoming-webhook-1) to learn how to create a Teams incoming webhook.

2. Load the `teamsnotify.cna` script into Cobalt Strike.

3. Execute the `teamsnotify` command to start the script.

The script will now send a notification to the specified Teams channel every time a new beacon is established.

## Script Details

The `teamsnotify.cna` script hooks the `beacon_initial` event and passes the necessary parameters to the Python script. These parameters are the external IP, internal IP, hostname, and username of the machine that established the beacon.

The Python script, `notify.py`, takes these parameters and sends a notification to Teams using the webhook URL. The notification is in the form of a message card, which includes the details of the new beacon.

## Requirements

- Cobalt Strike
- Python 3
- Requests module (pip install requests)

## References

- [NVISO Blog Post: Tap Tap, Is This Thing On? Creating a Notification Service for Cobalt Strike](https://blog.nviso.eu/2021/03/05/tap-tap-is-this-thing-on-creating-a-notification-service-for-cobalt-strike/)
- [NVISO GitHub Repository: Cobalt Strike Notifier](https://github.com/NVISOsecurity/blogposts/tree/master/cobalt-strike-notifier)
- [ScriptIdiot GitHub Repository: BeaconNotifier-Discord](https://github.com/ScriptIdiot/BeaconNotifier-Discord/tree/main)