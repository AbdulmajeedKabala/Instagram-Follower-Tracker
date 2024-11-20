# Instagram Follower Tracker

This project uses **Instaloader** to track Instagram profiles, retrieve profile data, and analyze follower trends. The goal is to automate Instagram profile tracking while overcoming challenges such as authentication and API limitations.

## Features

- Fetch and analyze Instagram profile data.
- Track followers, posts, and metadata for specified profiles.
- Support for logging in with Instagram credentials.
- Option to handle private profiles (requires following the profile).
- Utilizes session cookies for seamless repeated usage.

## Prerequisites

Before using this project, ensure you have the following installed on your system:

- Python 3.7 or later
- Pip (Python's package manager)

### Installing Instaloader

To install `instaloader`, use the following command:

```bash
pip install instaloader
```

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/instagram-follower-tracker.git
    cd instagram-follower-tracker
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Log in to Instagram using Instaloader (required for private profiles and certain features):

    ```bash
    instaloader --login=your_instagram_username
    ```

4. Start using the tool to track profiles:

    ```bash
    instaloader profile instagram_username
    ```

## Troubleshooting

### Common Errors

1. **401 Unauthorized**
   - Ensure you're logged in to Instagram through Instaloader.
   - Run the command `instaloader --login=your_instagram_username` and retry.

2. **Too Many Requests**
   - If Instagram temporarily blocks your requests, wait a few hours before trying again.
   - Use session cookies to minimize repeated logins.

3. **Profile Not Found**
   - Check if the profile name is correct and public.
   - For private profiles, make sure your logged-in account follows them.

### Debugging Tips

- Use the `--verbose` flag for more detailed logs:

    ```bash
    instaloader --login=your_instagram_username --verbose profile instagram_username
    ```

## Acknowledgments

- Thanks to the developers of [Instaloader](https://github.com/instaloader/instaloader) for their excellent tool.
- Inspired by the need for efficient Instagram profile tracking and analysis.

