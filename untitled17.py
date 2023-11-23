# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:55:13 2023

@author: yoann
"""

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
config = AutoConfig.from_pretrained('ProsusAI/finbert')
tokenizer = AutoTokenizer.from_pretrained('C:/Users/yoann/Desktop/cpr/bert')

