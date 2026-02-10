# Github Auto Block Account

## Why auto block account ? 

Someone use spam anime profile bot for follow to your account in Github profile. that it's make your profile follow list like dirty and disturbing. That's big problem GitHub can't resolve for a long time. which is why I developed this tool.

<div align="center">
   <img style="margin: 0 auto; padding-bottom: 15px; padding-top: 30px" width=70%" src="https://github.com/KravitzMC/github-auto-block-account/blob/main/dirtyfollow.png">
</div>

## Usage

### 1. First clone repository:

```bash
git clone https://github.com/KravitzMC/github-auto-block-account.git && cd github-auto-block-account.git
```

### 2. Setup Virtual Enviroment

```bash
# Install uv if you don't have it
pip install uv

# create an venv with python 3.11
uv venv --python 3.11

# Activate the virtual environment (and need to activate it each time you return to use it again.)

# For macOS/Linux:
source .venv/bin/activate

# For Windows (CMD):
.venv\Scripts\activate.bat
```





### 2. Create access tokens at : [https://github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens/new)

Follow this step:
* Token name : <your_token_name>
* Expiration : No Expiration
* Repository access : Public repositories
* Permissions : Block another user (Read-only)

and click generate token

### 3. Update configuration access token and save

```bash
config.json5
```
### 4. Update configuration access token and save

### 🏃 Run the script
 
  




