# COL759 Assignment 1

Kartikeya Gupta - 2018CS10349  
Mayank Yadav - 2018CS10356

## Requirements

Python: 3.6+,
numpy,
sympy

## How to run

Encryption (encrypt<span></span>.py)

```eval
python encrypt.py --message <message_filename> --key <key_filename> --output <output_filename> 
```

Decryption (decrypt<span></span>.py)

```eval
python decrypt.py --encrypted <encrpyted_text_filename> --key <key_filename> --output <output_filename> 
```

Analysis (analysis<span></span>.py)

```eval
python analysis.py --message <message_filename> --encrpyted <encrypted_text_filename>
```
Some sample invertible keys and a test message of 1000+ characters have been provided for testing.

## Assumption

- <message_filename> : txt file containing message to be encrypted 
- <key_filename> : txt file where first line is key size(n). Then n lines each containing n integers separeted by space
- <encrpyted_text_filename> : txt file containing encrypted text

## Working

- encrypt<span></span>.py: First processes the message file (removing punctuations and capitalizing everything), appends 'X' to the processed text until it is a multiple of key size, and then encrypts it using the given key.

- decrypt<span></span>.py: Calculates inverse of the provided key and decrypts provided cyphertext with it. Indicates on the terminal if provided key is not invertible.

- analysis<span></span>.py: Iterates key size n over 2 to 10, takes n\*n segments of plaintext (if plaintext segment taken is not invertible then indicates on the terminal and takes next n\*n segment), calculates key K using K = CP<sup>-1</sup>, decrypts the whole cyphertext using calculated key, calculates index of coincidence for the decrypted text and terminates if the calculated IOC is within 10<sup>-2</sup> of 0.0686 (IOC for English)

## Extra

- tester<span></span>.py: Randomly generates invertible keys and test encryptor, decryptor and analysis on them