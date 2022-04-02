# Expanding Pretrained Models to Thousands More Languages via Lexicon-based Adaptation 

# Intro
This repository contains the code for our [(ACL 2022 paper)](https://arxiv.org/abs/2203.09435) that synthesizes monolingual and labeled data for languages with limited or not textural data. We use these synthetic data to adapt pretrained multilingual models to languages with constraint textural data, which leads to significant improvements for these languages.  

# Download prepared data
We prepared the extracted lexicons and other data used in the expriments and you can get it [here](https://drive.google.com/file/d/1PTzpZYdQNG-DgZtObmv8ljcUCziVJBnd/view?usp=sharing).
To extract new lexicons from PanLex database directly, you can first download the sql database from [here](https://panlex.org/snapshot/)(in case the website doesn't work, [here](https://drive.google.com/file/d/1PRW7s1W2Q62nqAFVLY9SJG4d9hR0kWgB/view?usp=sharing) is the older version of the database we used), and run
```
python src/panlex_extract_lexicon.py --source_language=eng --target_language=$LAN --output_directory=data/lexicons
```
The lexicon extraction code is adapted from [this repository](https://github.com/dylandilu/Panlex-Lexicon-Extractor).

# Pseudo mono data
To generate synthetic data from the preprocessed Wikipedia sentences in English to another language, run the script
```
python src/make_pseudo_mono.py $LAN
```
where $LAN is a language code with a corresponding lexicon file under the folder data/lexicons/

 
# Pseudo labeled data
For finetuning, please first download and prepare the task specific data following the [XTREME repo]()
To generate synthetic data for a language and a task, use
```
python src/make_pseudo_label.py $LAN $TASK
```
where $TASK is could be [pos|panx] for [POS tagging|Wiki NER].

## Citation
Please cite our paper as:

```
@inproceedings{wang2022expand,
    title={Expanding Pretrained Models to Thousands More Languages via Lexicon-based Adaptation},
    author={Wang, Xinyi and
            Ruder, Sebastian and
            Neubig, Graham},
    booktitle={ACL},
    year={2022}
}
```

