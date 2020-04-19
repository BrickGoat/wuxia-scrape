# Introduction 
This page covers the installation of Wuxia Scrape and its current capabillities. 

# Installation
### Requirements
* A linux terminal
* Python3 
  * Check your version of python with:
```
$ python -V
```
  * Install latest version with: 
```
$ sudo apt-get install python3.6
```
* Beautiful Soup4
  * Python library that enables script to parse HTML files.
  * Install library with 
```
$ sudo apt-get install python3-bs4
```
* [Wuxia Scrape](https://github.com/BrickGoat/wuxia_scrape)
  * Download directly from link above or use: 
```
$ git clone https://github.com/BrickGoat/wuxia_scrape
```

# Command-line arguments
Here's a list of command-line arguments to Wuxia Scrape and what they do.

### [-h] / [--help] : get help
This flag will print out help information for Wuxia Scrape.

### [-s] / [--start=] : start writing from this chapter
This flag **must be** followed by a number specifying the **first chapter** to write from.

### [-e] / [--end=] : write up to and including this chapter
This flag allows you to specify the **last chapter** to write into a text document. Only the chapter specified by -s will be used if -e is not used.

### [-l] / [--link=] : link of novel homepage
This flag is followed by a link coming from a novel on the [NovelFull](https:NovelFull.com) website. The link **must** be the **index page** of the web novel.

### [-i] / [--individual] : separate chapters
This flag caused the chapters to be put in its own individual text documents. If not used all chapters are written to a single file.

# Examples
 
### Getting chapters 1 through chapter 23 and storing them in individual files.
1. Change into the directory of Wuxia Scrape
2. Then change into scrape directory
3. Run the command below:
```
 $ python3 scrape.py --link=https://novelfull.com/library-of-heavens-path.html --start=1 --end=23 -i
```

![Long option example](/assets/images/long-opt.png)

### Getting chapters 66 through chapter 84 and storing them in one file.
- Run in Wuxia Scrape sub directory scrape:
```
$ python3 scrape.py -lhttps://novelfull.com/library-of-heavens-path.html -s66 -e84
```

![Short option example](/assets/images/short-opt.png)

# Troubleshooting

- No such file or directory
    - Make sure you are in the folder /wuxia-scrape when running the script.
    
```
$ python3 scrape.py --link=https://novelfull.com/library-of-heavens-path.html -s1 -e23 -i
python3: can't open file 'scrape.py': [Errno 2] No such file or directory
```
  
- "I downloaded all the chapters to one file and there's a chapter missing!"
    - Sometimes the title of a chapter isn't parsed when retrieving all the chapters. The chapter should still be in the file and in the correct order. 
  
- IndexError
    - Make sure you are using Python3 and not Python2.
    - Double check that the start and or end flags are followed by valid chapter numbers.
  
```
Traceback (most recent call last):
  File "scrape.py", line 38, in <module>
    chapterLinks = nf.getChapterLinks(contentPages)
  File "/home/UserName/DownloadLocation/scrape/search.py", line 26, in getChapterLinks
    chapterLinks.append('http://novelfull.com' + linkTables[x])
IndexError: list index out of range
```

 - "The novel text file is blank!"
    - Make sure the ending parameter comes after the start parameter.
  
 - "I got chapter 49 instead of 1!"
    - Check if your start or end number is negative or if a dash was mistyped.
  
# Support
  1. Create an [Issue](https://github.com/BrickGoat/wuxia_scrape/issues).
  2. Provide an in-depth explanation of your problem.
     - Refer to the GitHub Issue [guide](https://guides.github.com/features/issues/) if needed.
