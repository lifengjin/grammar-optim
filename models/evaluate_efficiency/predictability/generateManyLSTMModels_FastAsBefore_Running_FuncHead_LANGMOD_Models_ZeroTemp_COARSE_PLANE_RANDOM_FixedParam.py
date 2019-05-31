import os
import sys

BASE_DIR = sys.argv[1]
assert BASE_DIR in ["RANDOM", "RANDOM2", "RANDOM3", "RANDOM4", "RANDOM5"]

languages = ["Hindi", "Swedish", "German", "Urdu", "English", "Spanish", "Chinese", "Slovenian", "Estonian", "Norwegian", "Serbian", "Croatian", "Finnish", "Portuguese", "Catalan", "Russian", "Arabic", "Czech", "Japanese", "French", "Latvian", "Basque", "Danish", "Dutch", "Ukrainian", "Gothic", "Hebrew", "Hungarian", "Latin", "Persian", "Bulgarian", "Romanian", "Indonesian", "Greek", "Turkish", "Slovak", "Belarusian", "Galician", "Italian", "Lithuanian", "Polish", "Vietnamese", "Korean", "Tamil", "Irish", "Marathi", "Afrikaans", "Telugu", "Coptic", "Ancient_Greek", "Old_Church_Slavonic"]
assert len(languages) == 51, len(languages)
#languages = ["Ancient_Greek", "Old_Church_Slavonic"]

import os

import subprocess
import random

from math import exp, sqrt
import sys

modelNumbers = None

modelsProcessed = []
for language in languages:
   modelsProcessed.append((language, BASE_DIR))
models = modelsProcessed
assert len(models) > 0
print(models)
print(modelNumbers)
models = [model for model in models if len(model) == 2]

import os


scripts = ["readDataDistCrossGPUFreeMomentumEarlyStopEntropyPersevereAnneal_OrderBugfix_Fixed_NoPunct_AllCorpPerLang_NEWPYTORCH_Corrected_FastAsBefore_Zero_Running_FuncHead_LANGMOD_ZeroTemp_COARSE_PLANE_FixedParam.py"]



failures = 0

while failures < 200:
  existingFiles = os.listdir("../../../raw-results/language_modeling_coarse_plane_fixed")
  script = random.choice(scripts) #scripts[0] if random.random() < 0.8 else scripts[1]
  language, model = random.choice(models)
  if languages is not None and language not in languages:
      continue
  existing = [x for x in existingFiles if x.startswith(language) and "_"+model+"_" in x]
#  assert ((1.0/(1+len(existing)))) > 0
  if len(existing) > 10: #random.random() > ((1.0/(1+len(existing)))):
     print("Language models for this model exists "+str(((1.0/(1+len(existing))))))
     failures += 1
     continue
  failures = 0
#  existing = [x for x in existingFiles if x.startswith(language)]
#  if len(existing) > 5:
#    if random.random() > 0.3:
#        print("Skipping "+language)
#        continue
  entropy_weight = random.choice([0.001, 0.001,0.001, 0.001,  0.01, 0.1, 1.0])
  lr_policy = random.choice([0.0002, 0.0002, 0.0005, 0.0005, 0.001, 0.001, 0.001, 0.001, 0.002, 0.01])
  momentum = random.choice([0.8, 0.9])
  lr_baseline = random.choice([1.0])
  dropout_prob = random.choice([0.3])
  lr_lm = random.choice([0.1])
  batchSize = random.choice([1])
  command = map(str,["/u/nlp/anaconda/ubuntu_16/envs/py27-mhahn/bin/python2.7", script, language, "L", entropy_weight, lr_policy, momentum, lr_baseline, dropout_prob, lr_lm, batchSize, model, BASE_DIR])
  #print " ".join(command)
  #quit()
  subprocess.call(command)
 
