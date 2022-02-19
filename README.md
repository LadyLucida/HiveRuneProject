# Hive Rune Project #

This repo is divided into 3 sub-categories: Part Maker, Rune Maker and Phrase Searcher. Each category is explained below:


## Part Maker
The Part Maker generates the vertically flipped and bottom parts of runes from the top parts (as all tops can be bottoms). This has already been done for you, but if you want to know the process, you can read the readme in the Part_Maker Folder.

## Rune Maker
This is the bread and butter of the Hive Rune Project. Using the parts generated from the Part Maker and the Hive Rune Database, we can generate Hive Runes. Why you may ask? Because currently (before the release of Witch Queen), there isn't enough runes for the Hive Language to be a full functioning language, as there are only 53 symbols. The database will be updated with new runes frequently, and the statistics will change as well as new runes show up. To run this script run the following:

```
cd Rune_Maker
python Rune_Maker.py
```

That will generate and color code each of the runes into 4 distinct categories. You can read more about that here.

## Phrase Searcher
This is a neat little tool that searches all of the phrases for particular runes. Using the Hive Rune Database of known runes, you can give it any number of runes and it will return the number of phrases the runes are in. To run the script, do the following:

```
cd Phrase_Searcher
python Phrase_Searcher.py <sigil_01, sigil_02>
```
This in particular, returns all the phrases that have both sigil_01 and sigil_02 in them.