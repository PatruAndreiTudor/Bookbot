def get_word_count(filepath):
    with open(filepath) as f:
        read_data= f.read()
    split_words=read_data.split()
    word_count=len(split_words)
    return word_count

def sort_on(ch_list):
    return ch_list["num"]

def character_count(filepath):
    letters= {}
    with open(filepath) as f:
        read_data= f.read()
    all_lower_case=read_data.lower()
    split_words=all_lower_case.split()

    for words in split_words:
        for ch in words:
            if not ch.isalpha():
                continue
            if ch in letters:
                letters[ch]+=1
            else:
                letters[ch]=1

    
    ch_list=[]
    for letter in letters:
        new_dict= {"char":letter , "num":letters[letter]}
        ch_list.append(new_dict)
    ch_list.sort(reverse=True, key=sort_on)
    return ch_list


