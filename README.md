# text-analytics-blueprints
These are blueprints from book by Albrecht, Ramachandran, and Winkler, published by O'Reilly in the year 2020. 

# Repo structure 
- `src`: contains code files 
- `.pre-commit-config.yaml`: config for use with `pre-commit`. It specifies what hooks to use. 
  Once this file is created, if you run `pre-commit install`, the pre-commit tool will populate the 
  `pre-commit` file in the `./.git/hooks` directory. Helpful references: 
    - [Automate Python workflow using pre-commits: black and flake8](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/)
    - [Keep your code clean using Black & Pylint & Git Hooks & Pre-commit](https://towardsdatascience.com/keep-your-code-clean-using-black-pylint-git-hooks-pre-commit-baf6991f7376)
    - [pre-commit docs](https://pre-commit.com/#)
  
- `config-sample.yaml`: sample config file. Update the values and save as `config.yaml`
- `requirements.txt`: python packages used 

## Contents
1. Extracting twitter data:
    1. See file `src/extracting-twitter-data.py`
    2. Uses package tweepy. 