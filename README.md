# Meme Tuning Generator

## About
This is a simple python script meant to generate meme tuning for string instruments

## How it works
The scripts uses PyEnchant to check if the word is in the English Dictionary

## How to Use
Run the meme_tuning.py file you will be prompted on how many strings you will be using

It selects from a hard coded array of natural notes in a twelve tone equal tempermant scale
    [A, B, C, D, E, F, G]


Advanced Letters (S and M):
In addition some other letter to increase the possible tunings
    M: typically for major or minor interval (CM would be translated to C and E or C and Eb) 
    S: Either Seventh, Sixth, Added Second, or Suspended
    MM: Minor Major (Minor 3rd and Major 7th interval)
    SS: Suspended Seconds (No fifth and a Major 2nd interval)

    Temperant interval

    Minor 2nd, Major 2nd, Minor 3rd, Major 3rd, Perfect 4th, Diminished 5th, Perfect 5th, minor 6th, major 6th, minor 7th, and major 7th

    Sharp Notation:
    C -> C# -> D -> D# -> E -> F -> F# -> G -> G# -> A -> A# -> B -> C
    ^                     ^
    |_____________________|
               ^
               |
        Major 3rd Interval

    Flat Notation:
    C <- Db <- D <- Eb <- E <- F <- Gb <- G <- Ab <- A <- Bb <- B <- C
    ^               ^
    |_______________|
            ^          
            |
     Minor 3rd Interval

## Note:
    If you wish to modify the notes array be aware that the more letter add the exponentially longer it will take to complete    