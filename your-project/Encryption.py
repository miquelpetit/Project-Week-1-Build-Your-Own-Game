{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Choosing whether to encrypt or decrypt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type 0 to encrypt or 1 to decrypt: 7\n",
      "Your input is numeric but not '0' or '1'.\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "choicestring = ''\n",
    "choice = input('Type 0 to encrypt or 1 to decrypt: ')\n",
    "\n",
    "def enc_or_dec(choice):\n",
    "    options = [0,1]\n",
    "    if choice.isnumeric():\n",
    "        choice = int(choice)\n",
    "        if choice not in options:\n",
    "            print(\"Your input is numeric but not '0' or '1'.\")\n",
    "            sys.exit()\n",
    "        else:\n",
    "            if choice == 0:\n",
    "                choicestring = 'encrypt'\n",
    "            else:\n",
    "                choicestring = 'decrypt'\n",
    "    else:\n",
    "        print('ERROR! Your input is not numeric.')\n",
    "        sys.exit()\n",
    "    return (choicestring)\n",
    "\n",
    "enc_or_dec(choice)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Inserting the message to encrypt/decrypt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You chose to decrypt.\n",
      "Insert the text you want to decrypt: vQSiNHiu*Qq\n"
     ]
    }
   ],
   "source": [
    "print(f'You chose to {enc_or_dec(choice)}.')\n",
    "text = input(inserttext)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating the encryption dictionary "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "import random\n",
    "\n",
    "ALLCHARACTERS = []\n",
    "ALLCHARACTERS += list(string.printable)\n",
    "\n",
    "RANDCHARACTERS = ['\\n', ':', 'W', '.', '`', '>', '<', 'E', '}', '5', 'i', 'n', 'u', 'X', 'a', '2', ';', '*', '!', 'K', 'U', 'S', '+', 'V', 'Q', 'p', '9', 'P', ',', '?', '7', 'o', '(', 'Z', '#', 'A', '\\\\', '^', 'I', '=', '$', '4', 'm', 'v', '-', '3', '1', '\\x0b', '8', 'H', 'O', '\"', 'r', 'T', 'F', 'b', '6', 'z', 'l', 'D', ']', '_', 'q', 'j', '%', \"'\", 'L', 'R', 'C', '[', 'e', '&', '~', 't', 'k', '@', 'x', 'h', '|', 'G', 's', 'M', 'g', '\\t', 'Y', '\\r', 'd', '/', ')', 'c', ' ', '\\x0c', 'w', 'y', 'N', 'B', '{', 'J', 'f', '0']\n",
    "\n",
    "DICTENCRYPTED = {}\n",
    "\n",
    "for i in range(len(ALLCHARACTERS)):\n",
    "    DICTENCRYPTED[ALLCHARACTERS[i]] = RANDCHARACTERS[i]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating the decryption dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "DECRYPTEDDICT = {}\n",
    "\n",
    "for i in range(len(ALLCHARACTERS)):\n",
    "    DECRYPTEDDICT[RANDCHARACTERS[i]] = ALLCHARACTERS[i]\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Setting the function to encrypt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "enctext = ''\n",
    "\n",
    "def encrypt():\n",
    "    lstenc = []\n",
    "    for i in range(len(text)):\n",
    "        lstenc.append(DICTENCRYPTED[text[i]])\n",
    "        \n",
    "    enctext = ''.join(lstenc)\n",
    "    return print('Your encrypted text: ', enctext)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Setting the function to decrypt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "dec = ''\n",
    "\n",
    "def decrypt():\n",
    "    lstdec = []\n",
    "    for i in range(len(text)):\n",
    "        lstdec.append(DECRYPTEDDICT[text[i]])\n",
    "        \n",
    "    dectext = ''.join(lstdec)\n",
    "    return print('Your encrypted text: ', dectext)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Giving the output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your encrypted text:  Hola Nacho!\n"
     ]
    }
   ],
   "source": [
    "if choice == '0':\n",
    "    encrypt()\n",
    "else:\n",
    "    decrypt()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

