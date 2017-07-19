from workflow_config import REPO_CONFIG, base_uri
from subprocess import call
from os.path import join

for repo in REPO_CONFIG:
    name = repo['name']
    input_file_type = repo['input_file_type']
    input_file = repo['input_file']
    model_file = repo['model_file']


    call(['java','-cp','karma-spark-0.0.1-SNAPSHOT-shaded.jar','edu.isi.karma.rdf.OfflineRdfGenerator',
        '--baseuri',base_uri,
        '--sourcetype',input_file_type,
        '--filepath',join(name,input_file),
        '--modelfilepath',join(name,model_file),
        '--sourcename','ccma',
        '--outputfile','test.rdf']
        )
    # FIXME: make this n3 generation 

# Concetenate all data
# Zip it
