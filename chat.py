def send(user: str, channel: str, msg: str) -> None:
    """
    Sends a message from the inputted user to the inputted channel containing the inputted msg.

    Args:
        user (str): The user to send the message from.
        channel (str): The channel to send the message to.
        msg (str): The message to send.
    """
    import requests
    import json
    from sys import path

    with open(f"{path[0]}/config.json") as f:
        config: dict = json.load(f)

    token: str = config["chat_token"]
    header: dict = config["header"]

    payload = {
        "chat_token": token,
        "username": user,
        "channel": channel,
        "msg": msg,
    }

    requests.post(
        url="https://www.hackmud.com/mobile/create_chat.json",
        headers=header,
        json=payload,
    )


def read(
    users: list[str], before: int | float = None, after: int | float = None
) -> dict:
    """
    Returns the messages recieved by the inputted users within the given before and after parameters.

    Args:
        users (list[str]): A list of the users who you want to read the recieved messages of.
        before (int | float, optional): A UNIX timestamp in seconds with a fractional component. Defaults to "now".
        after (int | float, optional): A UNIX timestamp in seconds with a fractional component. Defaults to 60 seconds before "now".

    Returns:
        dict: The "chats" component of the request return content.
    """
    import requests
    import json
    from sys import path
    import time

    now = time.time()

    if not before:
        before = now

    if not after:
        after = now - 60

    with open(f"{path[0]}/config.json") as f:
        config: dict = json.load(f)

    token = config["chat_token"]
    header = config["header"]

    payload = {
        "chat_token": token,
        "usernames": users,
        "before": before,
        "after": after,
    }

    chats: dict = json.loads(
        requests.post(
            url="https://www.hackmud.com/mobile/chats.json",
            headers=header,
            json=payload,
        ).content
    )["chats"]

    return chats
