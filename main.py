import sys
from stats import get_word_count , character_count, sort_on



def main():
    
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count= get_word_count(sys.argv[1])
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books")
    print ("----------- Word Count ----------")
    print ("Found", word_count ,"total words")
    letter_count=character_count(sys.argv[1])
    print ("--------- Character Count -------")
    for final_letter in letter_count:
        print(f'{final_letter["char"]}: {final_letter["num"]}')
    print ("============= END ===============")
main()