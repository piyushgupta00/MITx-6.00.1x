import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        
        alphabet_lower='abcdefghijklmnopqrstuvwxyz'
        alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shifted_lower_dict={}
        shifted_upper_dict={}
        for char in alphabet_lower:
          char_index=alphabet_lower.index(char)
          shifted_index=char_index+shift
          if shifted_index>25:
             shifted_index=shifted_index-26
          shifted_lower_dict[char]=alphabet_lower[shifted_index]

        for char in alphabet_upper:
          char_index=alphabet_upper.index(char)
          shifted_index=char_index+shift
          if shifted_index>25:
             shifted_index=shifted_index-26
          shifted_upper_dict[char]=alphabet_upper[shifted_index]
    
        shifted_lower_dict.update(shifted_upper_dict)
#    print(shifted_lower_dict)
#    print(shifted_upper_dict)

        return shifted_lower_dict

    def apply_shift(self, shift):
        
        alphabet_lower='abcdefghijklmnopqrstuvwxyz'
        alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        plaintext=self.get_message_text()
        #plaintextlist=list(self.get_message_text()), list() method not being
        #recognized in spyder, fuck spyder!!!
        ciphertextlist=[]
        shift_dict=self.build_shift_dict(shift)
        for char in plaintext:
          if str(char) in alphabet_lower or str(char) in alphabet_upper:
             ciphertextlist.append(shift_dict[char])
          else:
             ciphertextlist.append(str(char))

        return ''.join(ciphertextlist)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
              
        
        self.message_text = text
        self.shift=shift
        #self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict= self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)
        
        

    def get_shift(self):
        
        return self.shift
        
    def get_encrypting_dict(self):
        
        return self.encrypting_dict.copy()
        

    def get_message_text_encrypted(self):
        
        return self.message_text_encrypted

    def change_shift(self, shift):
        
        self.shift=shift
        self.encrypting_dict= self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        
        self.message_text=text
        self.valid_words = load_words(WORDLIST_FILENAME)
        #self.valid_words=self.get_valid_words()

    def decrypt_message(self):
       
        shift_wordcount_map={}
        word_list=self.get_valid_words()
        possible_shift_list=[x for x in range(0,26)]
        for shift in possible_shift_list:
            back_shift=26-shift
            count=0
            possible_decrypt_message=self.apply_shift(back_shift)
            possible_decrypt_list=possible_decrypt_message.split(' ')
            for word in possible_decrypt_list:
                
                if is_word(word_list, word):
                    count+=1
                else:
                    continue
            shift_wordcount_map[shift]=count
        
        word_count_values=list(shift_wordcount_map.values())
        word_count_values.sort(reverse=True)
        reverse_dict={v: k for k, v in shift_wordcount_map.items()}
        original_shift=reverse_dict.get(word_count_values[0])
        decrypted_message=self.apply_shift(26-original_shift)
        return(original_shift,decrypted_message)
                
            
        


#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())

cipher3=CiphertextMessage(get_story_string())

print(cipher3.decrypt_message())

input_story_encrypted=PlaintextMessage(cipher3.decrypt_message()[1],10)
print()
print(input_story_encrypted.get_message_text_encrypted())





