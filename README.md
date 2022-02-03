# text-analytics-blueprints
These are blueprints from the book by Albrecht, Ramachandran, and Winkler, published by O'Reilly in 2020. 

## Repo structure 
- `src`: contains code files 
- `.pre-commit-config.yaml`: config for use with `pre-commit`. It specifies what hooks to use. 
  Once this file is created, if you run `pre-commit install`, the pre-commit tool will populate the 
  `pre-commit` file in the `./.git/hooks` directory. Helpful references: 
    - [Automate Python workflow using pre-commits: black and flake8](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/)
    - [Keep your code clean using Black & Pylint & Git Hooks & Pre-commit](https://towardsdatascience.com/keep-your-code-clean-using-black-pylint-git-hooks-pre-commit-baf6991f7376)
    - [pre-commit docs](https://pre-commit.com/#)
  
- `config-sample.yaml`: sample config file. Update the values and save as `config.yaml`
- `requirements.txt`: python packages used 

### Other notes 
- I use `streambook` to convert python files to jupyter notebooks. 
This is why in many cases you will see several similar files, like below. 
  The `.ipynb` file is easiest to view in GitHub. 
  For more on streambook, see [this repo](https://github.com/nayefahmad/streambook/blob/main/README.md). 
  - example.py 
  - example.ipynb  
  - example.notebook.py 
  - example.streambook.py 
  

## Contents
1. [Exploratory data analysis of text data](https://github.com/nayefahmad/text-analytics-blueprints/blob/main/src/exploratory-analysis-of-text-data.ipynb) 
1. [Extracting twitter data using Tweepy](https://github.com/nayefahmad/text-analytics-blueprints/blob/main/src/extracting-twitter-data.py)
