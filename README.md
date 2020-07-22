# AnagramsCheat
Python program to give the longest possible words for the iOS GamePidgeon game <b>Anagrams</b>

## How to Use:
> Note: You must have python3 installed

### Install DLIB
> The following is an excellent guide: https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/

In the command line enter the following:

```bash
git clone https://github.com/josephdiniso/AnagramsCheat.git
cd AnagramsCheat/Docker
```
### Install requirements.txt
Then enter the following in the command line:

```bash
pip install -r requirements.txt
```
### Running the program
To run the program, then type in the command line:

```bash
python main.py --letters <letters given in game>
```

> For example

```bash
python main.py --letters aencaq
```

## How it works:
The program takes in letters as an argument and calculates all possible combinations of letters, showing the highest awarding letters first. Using dlib's facial landmark detector, the user's eyes are tracked. When the aspect ratio average of the eyes drops below a certain threshold (meaning the eyes are closed), then the program displays the next best word to use in Anagrams.

### TODO:
- [ ] Containerize program into a docker image
