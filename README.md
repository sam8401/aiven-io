# aiven-io

# Tested with Python 3.8.6

$python -m venv <python-envs-root-folder>/aiv_env

(optional) $echo alias aiv=\'source <python-envs-root-folder>/aiv_env/bin/activate\' > ~/.bashrc (or .zshrc)

  
$aiv (or  $source <python-envs-root-folder>/aiv_env/bin/activate)


$pip install -r requirements.txt


# Test website_check metric being pushed to Postgres
$python test_script.py 

# Test website_check metrics pushed to Kafka
$python main_script.py 


Pending - Integration of all three
