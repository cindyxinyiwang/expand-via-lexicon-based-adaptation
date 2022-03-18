# Expanding Pretrained Models to Thousands More Languages via Lexicon-based Adaptation [(ACL 2022 paper)](https://arxiv.org/abs/2203.09435)


# download prepared data
We prepared the extracted lexicons and other data used in the expriments and you can get it [here](https://drive.google.com/file/d/1PTzpZYdQNG-DgZtObmv8ljcUCziVJBnd/view?usp=sharing).
To extract new lexicons from PanLex database directly, you can first download the sql database from [here](https://panlex.org/snapshot/), and run
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


