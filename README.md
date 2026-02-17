# 🛡️ Github Auto Block Spam Follow

##  Why auto block account ❔

When you see this bio → <b>"GIVE ME STARS TO MY REPOSITORIES AND BACK TO YOUR REPOSITORIES"</b>
because someone use spam anime profile bot follow to your account in Github public mode profile. that it's make your profile follow list look dirty and disturbing. That's major problem GitHub can't resolve for a long time. which is why I developed this tool.

<div align="center">
   <img style="margin: 0 auto; padding-bottom: 15px; padding-top: 30px" width=70%" src="https://github.com/KravitzMC/github-auto-block-account/blob/main/followdirty2.png">
</div>

## 👇 Usage

### 1. First clone repository:

```bash
git clone https://github.com/KravitzMC/github-auto-block-account.git
cd github-auto-block-account
```

### 2. Setup Virtual Enviroment

```bash
# Install uv if you don't have it
pip install uv

#install python 3.11 inside enviroment
uv python install 3.11

# create venv with python 3.11
uv venv --python 3.11

# Activate the virtual environment (and need to activate it each time you return to use it again.)

# For macOS/Linux:
source .venv/bin/activate

# For Windows (CMD):
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 2. Create access tokens at : [https://github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens/new)

Follow this step:
* <b>Token name :</b> <your_token_name>
* <b>Expiration :</b> No Expiration
* <b>Repository access :</b> Public repositories
* <b>Permissions :</b> Add → Block another user (Read-only)

.. And click generate token

### 3. Update configuration access token and save

```bash
nano config.json5
```

###  5. Run the script 🏃

 ```bash
uv run main.py
```

### Note 

* For running on Server/VPS hosting you can use ```sudo crontab -e``` in Linux Shell and set up the Cron Jobs on your required time. Cron Job will execute automatically like task scheduler app. 

### Contributing

If you would like to support the project, pull requests are welcome.
  




