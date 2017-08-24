# BadDayBot

## Every One Deserves Some Morning Unpleasantries


### Prerequisite:

* Twitter Account/App with OAuth Token
* Python3
* Virtualenv
  * Create/Activate python3 Virtualenv
    * `virtualenv -p python3 <venv_name>`
  * Install Python Module Dependencies
    * `pip install -r requirements.txt`

### Usage:

* Create file in repo base dir named: `credentials.yaml` with Twitter App OAuth contents:

```yaml
---
consumer_key: '<consumer_key>'
consumer_secret: '<consumer_secret>'
access_token: '<access_token>'
access_token_secret: '<access_token_secret>'
```

* Create file in repo base dir named `people.yaml` with contents:

```yaml
---

bad_people:
  - '<twitter_handle_of_bad_person#1>'
  - '<twitter_handle_of_bad_person#2>'
  - '<etc, etc.>'

```

* Execute Script to Wish people wonderful unpleasantries for the day to come:

  * `python bad_day_bot.py`


* Feel Free to Add Your Own Unpleasantries to [unpleasantries.yaml](unpleasantries.yaml):

  * Each line will be built out as:
    * `Morning @<twitter_handle>, <unpleasantry>.`
  * For Example:
    * `Morning @<Some_Person>, Hope you step in a scat pile of unknown origin today.`

