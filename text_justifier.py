def justify(text, width):
    '''A function that takes a string of text as an input and an
    integer (width) returns a text block (separated by newlines)
    justified to the desired width
    '''

    # initialization
    words = [i for i in text.split(' ')]
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

    if string[-1] in [' ', '\n']:
        return string[:-1]
    else:
        return string 

# example input
text = 'Four score and seven years ago, our fathers brought forth upon this continent a new Nation, conceived in Liberty, and with the proposition that all men are created Equal.'

# example function call
print (justify(text, 20))