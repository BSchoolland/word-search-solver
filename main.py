#SAVISEQBHOQVMAZEYHRSTHCAROLLWOJGDUQCJBBZAEXUKHJGEOFWNSLADJDAUXSREGAPLLAFMGSTPOYCSTHPANDXUNKPJEEMQCQAWKRELLIFXWPBDJOOQSRISUPGHOJCDWDLOXHLAQFSVCNFWPQHHZOEJEHOJSAESGIVMXLBQPAVPAVDOTDOIXYGMAQQEQFJSQTRXMNNSSUNWIBUYYECNKOYVHEDEUGBUMIMYTDJSLIANLBLLKJCSUXWFFECWERCSHILOLYWFFAUERNUFIRZHJSWVPSYPSYCJCZXCEZGINWTCUSHLCYGIARJKKHKNPPSLCPHROBACATYKQVSGMJFAAQXENREENNULMIHQWHREWFAHPKTSEREOEWDATTWWWBBSAWGSDHVNAQFSILXMWKKZREKLMLVUNJVUWTPEBBTOGUZECOTUNAMRAQQKRIKQQKMCYNMJLDHSSYHBSSNRAFYWVAZAFMPENUBSCOUONLLYYZTMIRBEATTBCNLCEUPCZDDAUJIWNXUHSMDJGJVMDTMGMOXOBXSHLCEWFHCXNCULERNNHVJBQEAUYAKOFRIFMJX

#WCAECCFZIRPICCSBBGYGNKLMOPXIESWMVHJNUWPURPLETITLEDYXAUNUCXGELYXXJFOUNTOHZGLXLLFCOIQAEQCFAAFJIGTICKLELFUEYSGEVCGXIIEYDMSALLPKBLKINBHUNFLZDSFBBMPKGYUJUVQPBELOUAYSMNDBBWLVHIRDCGZZUBOABPNCUSSUYALAFOTMILERNTPCOIZECYIMJPELULOAPYDRESLXGCAEQJBURMAYANYNRKEZPVCZVKVELPPAOUMKWADCABLEZPBZLSYETBOXOCREK


from colorama import Fore, Style 
import math

def Menu():
    print("\n\nMENU:")
    print("Press N to enter a new word search")
    print("Press V to view you current words")
    print("Press W to add words to your search list")
    print("Press D to delete words from your list")
    print("Press S to automatically solve the word search")
    return input()


def New():
    long_string = input('Input all characters in the word search')
    
    columns = math.sqrt(len(long_string))
    rows = math.sqrt(len(long_string))
    print(rows)
    long_string=Edit(long_string)
    Organize(long_string, columns,rows)
    return (long_string,columns,rows)

def Edit(long_string):
  long_string = long_string.replace('3','s')
  long_string = long_string.replace('0','o')
  long_string = long_string.replace(' ','')
  long_string = long_string.replace('.','')
  long_string = long_string.replace('/','I')
  #long_string = long_string.replace('\\','')
  long_string = long_string.replace('!','I')
  return(long_string)


def Organize(long_string, columns,rows):
    long_string = "".join(long_string.split())
    all_rows = []
    c = 1
    n = 0
    while c<=rows:
        x = ''
        while n<(columns*c):
            x = x + (long_string[n]+" ").lower()
            n = n + 1
        all_rows.append(x)
        c = c+1
    c = 0
    n = 0
    x = ''
    print('\nyour word search is:')
    while n<rows:
        print(all_rows[n])
        n = n + 1

    return (all_rows)


def Add_Words(List):
    print('The words you are currently searching for are:', (Words))
    string = input('Type the words you would like to add to your search\n')+ " "
    List = List + string.split()
    print("You are now searching for:",List)
    return (List)
    
def Solve(words,all_rows):
  print('Searching for',len(words),'words')
  n = 0
  while n<len(all_rows):
    all_rows[n] = "".join(all_rows[n].split())
    
    n = n +1
  for x in range(len(words)):
    Find_Word(words[x],all_rows)
  
def Highlight(distance,directionX,directionY,posX,posY,All_rows):
  
  for n in range(distance):
    All_rows[posY] = (All_rows[posY][0:posX])+All_rows[posY][posX].upper()+All_rows[posY][posX+1:]
    posX = posX+directionX
    posY = posY+directionY
  return(All_rows)

def Organize2(all_rows):
  
    long_string ="".join(all_rows)
    columns = math.sqrt(len(long_string))
    rows = math.sqrt(len(long_string))
    all_rows=[]
    c = 1
    n = 0
    print('\n\n')
    while c<=rows:
        x = ''
        
        while n<(columns*c):
          if long_string[n].isupper():
            print(Fore.GREEN+long_string[n]+Style.RESET_ALL+" ",end='')
          else:
            print(long_string[n]+" ",end='')
          n = n + 1
          if n/rows==n//rows:
            print()
          
        c = c+1
    c = 0
    n = 0
    x = ''


    

def Find_Word(word,all_rows):
  first_letter=word[0]
  word_length = len(word)
  n = 0
  r = 0
  while r<rows:
    if first_letter == all_rows[r][n]:
        x = 0
        U = 1
        UL = 1
        L = 1
        DL = 1
        D = 1
        DR = 1
        R = 1
        UR = 1
        #find next letter
        while x<word_length:
            letter = word[x]
            #right to left
            if L ==1:
                 if not n+x>=columns and letter == all_rows[r][n+x]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going left')
                         all_rows=Highlight(word_length,1,0,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     L = 0
                     x = -1
            #down and left
            elif DL == 1:
                 if not r+x>=rows and not n+x>=columns and letter == all_rows[r+x][n+x]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going left and down')
                         all_rows=Highlight(word_length,1,1,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     DL = 0
                     x = -1
            #down
            elif D == 1:
                 if not r+x>=rows and letter == all_rows[r+x][n]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going down')
                         all_rows=Highlight(word_length,0,1,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     D = 0
                     x = -1
            #right
            elif R == 1:
                 if not n-x<=-1 and letter == all_rows[r][n-x]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going right')
                         all_rows=Highlight(word_length,-1,0,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     R = 0
                     x = -1
            # down right
            elif DR == 1:
                 if not r+n>=rows and not n-x<=-1 and letter == all_rows[r+x][n-x]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going down and right')
                         all_rows=Highlight(word_length,-1,1,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     DR = 0
                     x = -1
            #up right
            elif UR == 1:
                 if not r+n<=-1 and not n-x<=-1 and letter == all_rows[r-x][n-x]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going up and right')
                         all_rows=Highlight(word_length,-1,-1,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     UR = 0
                     x = -1
            #up
            elif U == 1:
                 if not r+n<=-1 and  letter == all_rows[r-x][n]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going up')
                         all_rows=Highlight(word_length,0,-1,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     U = 0
                     x = -1
            #up left
            elif UL == 1:
                 if not r+n<=-1 and not n+x>=columns and letter == all_rows[r-x][n+x]:
                     if x == word_length-1:
                         print('word',word,'found at column',n+1,'row',r+1,'going up and left')
                         all_rows=Highlight(word_length,1,-1,n,r,all_rows)
                         Organize2(all_rows)
                 else:
                     UL = 0
                     x = -1
            x = x + 1
    n = n +1
    if n>=columns:
        n = 0
        r = r +1
  


#  
        #down and left



def View(word_search,columns,rows,Words):
    Organize(word_search,columns,rows)
    print()
    print('you are searching for:')
    print(Words)
    print('\n\n')

def Delete(List):
    print('The words you are currently searching for are:', (Words))
    string = input('Type the words you would like to remove from this list\n')
    wordsToDelete = string.split()
    for n in range(len(wordsToDelete)):
      try:
        while True:
          List.remove(wordsToDelete[n])
      except ValueError:
        pass
    print("You are now searching for:",List)
    return (List)


word_search,columns,rows = New()
Words = []
while True:
    key = Menu()
    print('\n\n')
    if key == 'N' or key == 'n':
        word_search,columns,rows = New()
    elif key == 'V' or key == 'v':
        View(word_search,columns,rows,Words)
    elif key == 'W' or key == 'w':
        Words = Add_Words(Words)
    elif key == 'D' or key == 'd':
        Delete(Words)
    elif key == 'S'or key == 's':
      x = Organize(word_search,columns,rows)
      print(Solve(Words,x))
    else:
        print('\nError, enter a valid selection')