# text_justifier.py

def justify(words, width):
    '''A function that takes a string of text as an input and an
    integer (width) returns a text block (separated by newlines)
    justified to the desired width.  Greedy algorithm implementation.
    '''

    # initialization
    string = ''
    i, l,  count = 0, 0, 0

    # greedy algorithm to add the maximum amount of words
    # per line, separated by spaces
    while i in range(len(words)):
        if count <= width+1:
            count += len(words[i]) + 1
            i += 1
            
        if count > width + 1:
            i -= 1

            # computes spaces to be added
            count = 0
            for r in range(len(words[l:i])):
                count += len(words[l+r])
            spaces = width - count

            # add spaces to words not at the end of the line
            while spaces > 0:
                if len(words[l:i-1]) == 1:
                    words[l] += ' ' * (spaces)
                    spaces = 0
                if len(words[l:i-1]) == 0:
                    spaces = 0
                else:
                    for j in range(len(words[l:i-1])):
                        if spaces > 0:
                            words[l+j] += ' '
                            spaces -= 1
                            
            string += ''.join(words[l:i])
            string += '\n'
            l = i 
            count = 0
    
        if i == len(words):
            for k in range(len(words[l:])):
                string += words[l+k] + ' ' 
            break

    ls = [i for i in string.split("\n")]
    return ls


# example input
words = ["This", "is", "an", "example", "of", "text", "justification."]
width = 16
# example function call
print (justify(words, width))