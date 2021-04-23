
"""Import the required libraries"""
from binascii import hexlify, unhexlify
from random import *
from typing import List, Tuple
import tkinter as tk

"""
hw ---> halfwidth
hdp ---> hamming distance for plaintext
hdk ---> hamming distance for key
r ---> number of round

"""
"""The s-boxes to be used in the encryption process"""
"""The same s-boxes are circularly used if morethan 8 s-boxes are required"""
s_box = [
        [ 
          [ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ], 
        [ 
          [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ], 
        [ 
          [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]
        ],
        [ 
          [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]
        ], 
        [ 
          [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]
        ],
        [ 
          [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]
        ], 
        [ 
          [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]
        ],
        [ 
          [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] 
        ]
    ]

"""To convert the string from one format to another format"""
def ascii_to_hexadecimal(string: str) -> str:
  return hexlify(string.encode()).decode()

def hexadecimal_to_ascii(string: str) -> str:
  return unhexlify(string.encode()).decode()

def hexadecimal_to_binary(string: str) -> str:
  return bin(int(string,16))[2:]

def binary_to_hexadecimal(string: str) -> str:
  return hex(int(string,2))[2:]

def get_2hw_bit_plaintext(plaintext: str, hw: int =32, hd: int =0) -> List[str]:
  """Used to produce plaintext blocks of size 2*hw by left padding with '0' if needed and produce alternated plaintext with the hamming distance as specified"""
  length = 2*hw
  x = len(plaintext)%length
  if(x != 0):
    x = length - x
  plaintext = '0'*x + plaintext
  """Mutatting the plaintext as per the given hamming distance"""
  if(hd != 0):
    plaintext = mutate(plaintext,hd)

  # Dividing the plaintext into blocks of size 2*hw
  pt_arr = []
  i=0
  while(i+length <= len(plaintext)):
    pt_arr.append(plaintext[i:i+length])
    i += length
  return pt_arr


def get_2hw_bit_key(key: str, hw:int =32, hd:int =0) -> str:
  """Used to produce the key for size 2*hw by left padding with '0' if needed and produce alternated key with the hamming distance specified"""
  if(len(key) > 2*hw):
    key = key[:2*hw]
  """Padding the key with zeroes if the size is less than 2*hw"""
  key = key.zfill(2*hw)
  """Mutating the key as per the given hamming distance"""
  if(hd != 0):
    key = mutate(key,hd)

  return key


def mutate(txt: str, hd: int) -> str:
  """Used to modify the plaintext or key with the given hamming distance and hence helpful in demonstrating the avalanche effect"""
  length = len(txt)
  """Randomly selecting the position where we change the bits"""
  random_pos = sample(range(0,length),hd)
  random_pos.sort() 
  mutated_txt = ""
  i = 0
  """Changing the positions randomly selected"""
  for pos in random_pos:
    mutated_txt += txt[i:pos]
    i = pos+1
    if(txt[pos] == '1'):
      mutated_txt += '0'
    else:
      mutated_txt += '1'
  
  mutated_txt += txt[i:]
  return mutated_txt


def initial_permutation_creation(size: int) -> List[int]:
  """Used to created a shuffled 1-indexed array of given size used to shuffle the plaintext initially"""
  arr = [x for x in range(1,size+1)]
  seed(34)
  shuffle(arr)
  return arr

def expansion_table_creation(size: int, n: int) -> List[int]:
  """Used to create the expansion table for expanding the halfwidth block to match the size of round key generated, with length as 'size+n' """
  arr = [x for x in range(1,size+1)]
  pos = sample(range(1,size+1),n)
  for i in pos:
    arr.append(i)
  seed(34)
  shuffle(arr)
  return arr

def permutation_operation(s: str, arr: List[int], n: int) -> str:
  """ To reorder and/or resize the given string 's' based on the 1-indexed array 'arr' to size 'n' """
  string = ""
  for i in range(n):
    string += s[arr[i] - 1]
  return string

def xor_operation(string1: str, string2: str) -> str:
  """To perform bitwise XOR operation of the two strings in every round and after all the rounds"""
  res = ""
  for i in range(len(string1)):
    if (string1[i] == string2[i]):
      res += '0'
    else:
      res += '1'
  return res

def shift(string: str, k: int) -> str:
  """To left shift the string 'string' through 'k' units in every round"""
  s =  string[k:] + string[:k]
  return s  


def permutation_table_creation(size: int) -> List[int]:
  """Used to produce a 1-indexed array which is used in shuffling the string"""
  arr = [x for x in range(1,size+1)]
  seed(34)
  shuffle(arr)
  return arr

def PC_1_creation(size: int) -> List[int]:
  """Used to create the permuted_choice1 for dropping the parity bits in the key given, the permutated_choice1 is created by shuffling the 1-indexed array of given size excluding the parity"""
  arr = [x for x in range(1,size+1) if x%8 != 0]
  seed(34)
  shuffle(arr)
  return arr

def PC_2_creation(size: int, n: int) -> List[int]:
  """Used to create the permuted_choice2 for resizing(reducing) and hence producing the round keys"""
  seed(34)
  pos = sample(range(size),n)
  arr = []
  for i in range(size):
    if(i not in pos):
      arr.append(i+1)
  seed(34)
  shuffle(arr)
  return arr


def inverse_initial_permutation_creation(arr: List[int]) -> List[int]:
  """Used in producing the inverse_initial permutation array based on the initial_permutation array provided"""
  inv = [0 for i in range(len(arr))]
  for i,x in enumerate(arr):
    inv[x-1] = i+1 
  return inv


def produce_round_keys(key_block: str, rounds: int =16, hw: int =32) :
  """Used to produce the round keys in binary"""
  # If number of rounds are greater than 16 then the left shifts for the 17th round and above is 2 
  shift_table = [ 1, 1, 2, 2, 
                  2, 2, 2, 2, 
                  1, 2, 2, 2, 
                  2, 2, 2, 1 ]
  if(hw == 32):
    # Conventional DES used permuted_choice1 table used to drop parity bits and shuffling
    PC_1 = [ 57, 49, 41, 33, 25, 17, 9, 
            1, 58, 50, 42, 34, 26, 18, 
            10, 2, 59, 51, 43, 35, 27, 
            19, 11, 3, 60, 52, 44, 36, 
            63, 55, 47, 39, 31, 23, 15, 
            7, 62, 54, 46, 38, 30, 22, 
            14, 6, 61, 53, 45, 37, 29, 
            21, 13, 5, 28, 20, 12, 4 ]
    # Conventional DES used permuted_choice2 table used to reduce the keysize
    PC_2 = [ 14, 17, 11, 24, 1, 5, 
            3, 28, 15, 6, 21, 10, 
            23, 19, 12, 4, 26, 8, 
            16, 7, 27, 20, 13, 2, 
            41, 52, 31, 37, 47, 55, 
            30, 40, 51, 45, 33, 48, 
            44, 49, 39, 56, 34, 53, 
            46, 42, 50, 36, 29, 32 ]
  else:
    PC_1 = PC_1_creation(2*hw)
    PC_2 = PC_2_creation(len(PC_1), hw//4)
  # Passing the key through the permuted_choice1
  key_block = permutation_operation(key_block, PC_1, len(PC_1))
  # Dividing the key into two halves to do left shift and produce round keys
  half = len(key_block)//2
  left = key_block[0:half]
  right = key_block[half:] 
  rkb = [] # list to store RoundKeys
  for i in range(rounds): 
    if(i < 16): 
      left = shift(left, shift_table[i])
      right = shift(right, shift_table[i])
    else: 
      left = shift(left,2)
      right = shift(right,2)
    # combine both halves and then further the size to expanded right half plaintext 
    combine = left + right 
    # The round key is produced using the permuted_choice2  
    RoundKey = permutation_operation(combine, PC_2, len(PC_2))
    rkb.append(RoundKey)
  return rkb

def encryption(plaintext: str, key: str, r: int =16, hw: int =32, hdp: int =0,  hdk: int=0) :
  """Coverting the plaintext and key into the binary format"""
  plaintext = ascii_to_hexadecimal(plaintext)
  plaintext = hexadecimal_to_binary(plaintext)
  key = ascii_to_hexadecimal(key)
  key = hexadecimal_to_binary(key)
  """Dividing the plaintext into blocks of twice the halfwidth"""
  plaintext_blocks = get_2hw_bit_plaintext(plaintext, hw, hdp)
  key_block = get_2hw_bit_key(key, hw, hdk)
  """Producing the round keys"""
  rkb = produce_round_keys(key_block, r, hw)    
  #selecting the size of the s-box needed for the given halfwidth
  if(hw == 32):
    size_of_s_box = 8
  elif(hw == 16):
    size_of_s_box = 4
  else:
    size_of_s_box = 16
  
  if(hw == 32):
    initial_perm = [ 58, 50, 42, 34, 26, 18, 10, 2, 
                  60, 52, 44, 36, 28, 20, 12, 4, 
                  62, 54, 46, 38, 30, 22, 14, 6, 
                  64, 56, 48, 40, 32, 24, 16, 8, 
                  57, 49, 41, 33, 25, 17, 9, 1, 
                  59, 51, 43, 35, 27, 19, 11, 3, 
                  61, 53, 45, 37, 29, 21, 13, 5, 
                  63, 55, 47, 39, 31, 23, 15, 7 ]
    expansion = [ 32, 1, 2, 3, 4, 5,
                4, 5, 6, 7, 8, 9, 
                8, 9, 10, 11, 12, 13, 
                12, 13, 14, 15, 16, 17, 
                16, 17, 18, 19, 20, 21, 
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1 ] 
    permutation = [ 16, 7, 20, 21, 
                    29, 12, 28, 17, 
                    1, 15, 23, 26, 
                    5, 18, 31, 10, 
                    2, 8, 24, 14, 
                    32, 27, 3, 9, 
                    19, 13, 30, 6, 
                    22, 11, 4, 25 ]
    inv_initial_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
                39, 7, 47, 15, 55, 23, 63, 31, 
                38, 6, 46, 14, 54, 22, 62, 30, 
                37, 5, 45, 13, 53, 21, 61, 29, 
                36, 4, 44, 12, 52, 20, 60, 28, 
                35, 3, 43, 11, 51, 19, 59, 27, 
                34, 2, 42, 10, 50, 18, 58, 26, 
                33, 1, 41, 9, 49, 17, 57, 25 ]
  else:
    """Creating the initial_permutation array, expansion_table, permuation_table and inverse_initial_permutation_table"""
    initial_perm = initial_permutation_creation(2*hw)
    expansion = expansion_table_creation(hw,len(rkb[0]) - hw)
    permutation = permutation_table_creation(hw)
    inv_initial_perm = inverse_initial_permutation_creation(initial_perm)

  final = ""
  round_ciphertexts = []
  
  for plaintext in plaintext_blocks:
    plaintext = permutation_operation(plaintext, initial_perm, len(initial_perm))

  for plaintext in plaintext_blocks:
    left = plaintext[0:hw]
    right = plaintext[hw:]
    rct = []
    for i in range(r): 
      """Expansion performed in the every round"""
      right_expanded = permutation_operation(right, expansion, len(expansion))
      """XOR operation with the round key""" 
      x = xor_operation(rkb[i], right_expanded) 
      op = ""
      """Used the s-boxes to contract"""
      for i in range(size_of_s_box):
          part = x[i*6:(i+1)*6]
          row = part[0] + part[5]
          row = int(row,2)
          col = part[1:-1]
          col = int(col,2)
          val = s_box[i%8][row][col]
          op += bin(val)[2:].zfill(4)
      
      # Permuting
      op = permutation_operation(op, permutation, len(permutation))

      # XOR operation with the left half 
      x = xor_operation(op, left)
      left = x
      
      # Swapping both the halves after every round
      left, right = right, left
      
      #appending both the halves and store the round ciphertexts
      rct.append(str(left+right))

    round_ciphertexts.append(rct)
    #swapping both the halves after all the rounds
    left,right = right, left
    # Appending both the halves and then appying the inverse_initial_permutation
    combine = left + right
    ciphertext = permutation_operation(combine, inv_initial_perm, len(inv_initial_perm))
    #appending the round ciphertext to final ciphertext
    final += ciphertext

  return rkb,round_ciphertexts,final


def calc_diff(arr1: List[List[str]], arr2: List[List[str]]) -> List[int]:
  """To calculate the sum of different positions in roundwise ciphertext for demonstrating the avalanche effect"""
  diff = []
  for i in range(len(arr1[0])):
    cnt = 0
    for j in range(len(arr1)):
      for (c,d) in zip(arr1[j][i], arr2[j][i]):
        if(c != d):
          cnt += 1
    diff.append(cnt)
  return diff




